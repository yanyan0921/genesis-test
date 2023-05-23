import base64
import functools
import os
import re
import core.utility as ut
from rest.http_base import HttpClient
import requests
import json
import uuid
from datetime import datetime
from queue import Queue
from threading import Thread
import jwt


class Service(HttpClient):
    def __init__(self, var, param, index, config_name):
        super().__init__(var, param, index, config_name)
        self.vars = var
        self.params = param
        self.index = index
        self.npm_url = self.npm_url = self.parser.get_setting("endpoint", "npm.url")
        self.kharma_url = self.kharma_url = self.parser.get_setting("endpoint", "kharma.url")
        self.asv2_url = self.parser.get_setting("endpoint", "asv2_url")
        self.asv1_url = self.parser.get_setting("endpoint", "asv1_url")
        self.package_version_id = None
        self.api_key = None
        self.access_token = None
        self.base_url = self.default_url

    def rename_by_index(self, name):
        return name + "_step_" + self.index

    def auth(self):
        # Login
        user_email = self.params.get("email")
        token = requests.post(
            url=self.asv2_url + "/api/login",
            json={
                "username": user_email,
                "password": "Test1234"
            }
        ).json()
        user_id = token["userId"]
        self.access_token = token["accessToken"]
        self.logger.info("get user access token success! " + self.access_token)
        self.logger.info(f'Successfully login with user {user_id}, publisher {token["publisherId"]}.')

        # Check private key
        key_file = f'./testcase/publisherPortalV2/{user_id}.json'
        if not os.path.exists(key_file):
            key = requests.post(
                url=self.asv2_url + "/api/publishing-key",
                headers=self.auth_headers
            ).json()
            with open(key_file, 'w') as f:
                f.write(json.dumps(key, indent=4))
            self.logger.info(f'Successfully generated key and stored in {key_file}.')

        # Generate api key
        with open(key_file, 'r') as f:
            key = json.loads(f.read())
            private_key = f'-----BEGIN PRIVATE KEY-----\n{key["privateKey"]}\n-----END PRIVATE KEY-----'
            payload = {
                'sub': str(key['keyChainId']),
                'iss': str(key['keyChainId']),
                'iat': datetime.now().timestamp() - 60,
                'exp': datetime.now().timestamp() + 86400,  # expire in 1 day
                'aud': 'genesis',
                'scope': 'genesis.generateAccessToken'
            }
            self.api_key = jwt.encode(
                payload=payload,
                key=private_key,
                algorithm='RS256',
                headers={'kid': str(key['id']), 'uid': str(user_id)}
            )
        self.logger.info('Successfully encoded API key.')

    @property
    def auth_headers(self):
        return {
            'Authorization': f'Bearer {self.access_token}'
        }

    @property
    def publishing_headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}'
        }

    def get_param_value(self, name):
        value = self.params.get(name)
        if value.startswith("${"):
            return self.vars.get(value[2:-1])
        return name

    def get_package(self):
        now_url = self.vars.get("current_url")
        pattern = re.compile('([0-9]+)')
        id_value = ''.join(pattern.findall(now_url))
        self.package_id = id_value
        self.logger.info("package id is :" + str(id_value))
        return id_value

    def get_package_version(self):
        now_url = self.vars.get("current_url")
        pattern = re.compile('([0-9]+)')
        id_value = ''.join(pattern.findall(now_url))
        self.package_version_id = id_value
        self.logger.info("package version is :" + str(id_value))
        return id_value

    def create_value(self):
        Digits = self.params.get("Digits")
        name = ut.random_str(int(Digits)) + "_UIpackage"
        self.vars.put(self.rename_by_index("value"), name)
        self.logger.info("package name is :" + name)

    def create_launch_value(self):
        Digits = self.params.get("Digits")
        name = ut.random_str(int(Digits)) + "_launch_package"
        self.vars.put(self.rename_by_index("value"), name)
        self.logger.info("package name is :" + name)

    def upload_unitypackage(self, thread_nums=1, slices=None):
        self.auth()
        source = "./testcase/vettingTestImage/openapi.unitypackage"
        unity_version = self.params.get("unity_version")
        if self.params.get("unity_version") is None:
            unity_version = "2020.1.0f1"
        size = os.path.getsize(source)
        if slices is None:
            slices = (size - 1) // (500 * 1024 * 1024) + 1
        sizes = [size // slices] * (slices - 1) + [size // slices + size % slices]
        res = requests.post(
            url=self.asv2_url + "/store-publishing/package-version/" + self.get_package_version() + "/unitypackage/prepare",
            json={
                'unityVersion': unity_version,
                'sizes': sizes
            },
            headers=self.publishing_headers
        )
        if res.status_code == 200:
            self.logger.info(f'Successfully prepared to upload unitypackage in {slices} slices.')
            tasks = Queue()
            failures, context = [], {"index": 0}
            f = open(source, 'rb')
            for slice_size in sizes:
                tasks.put(
                    functools.partial(self.upload_unitypackage_slice, f, slice_size, unity_version, failures, context))
            threads = [Thread(target=self.upload_unitypackage_thread, args=(tasks,))
                       for _ in range(thread_nums)]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            if len(failures) > 0:
                raise failures[0]

    @staticmethod
    def upload_unitypackage_thread(tasks: Queue):
        while not tasks.empty():
            tasks.get()()

    def upload_unitypackage_slice(self, f, size, unity_version, failures, context):
        tempfile = f'{uuid.uuid4()}.partial'
        index = context["index"]
        context["index"] += 1
        with open(tempfile, 'wb') as g:
            g.write(f.read(size))
        try:
            res = requests.post(
                url=self.asv2_url + "/store-publishing/package-version/" + self.package_version_id + "/unitypackage",
                files={'file': open(tempfile, 'rb')},
                data={'unityVersion': unity_version, 'index': index},
                headers=self.publishing_headers
            )
            if res.status_code == 200:
                self.logger.info(f'Successfully uploaded slice {index} with {size / 1024:.2f} KB.')
        except Exception as e:
            failures.append(e)
        finally:
            os.remove(tempfile)

    def get_asv1_token(self):
        asv1_client_key = "asv1Client"
        asv1_secret_key = "asv1Secret"

        client = self.properties.get(asv1_client_key)
        secret = self.properties.get(asv1_secret_key)

        asv1_token = 'Basic ' + str(base64.b64encode((client + ":" + secret).encode('utf-8')),
                                    'utf-8')
        self.headers["Authorization"] = asv1_token
        return asv1_token


    def download_unitypackage(self):
        version_id = self.params.get("package_version_id")
        user_id = self.get_param_value("userid")
        self.get_asv1_token()
        res = requests.get(
            url=self.asv1_url + "/api/content/download/" + self.get_package() + "/" + version_id + "/unitypackage",
            params={'kharma_user_id': user_id},
            headers=self.headers)
        if res.status_code == 200:
            self.logger.info(f'Successfully download package: {self.package_id}')