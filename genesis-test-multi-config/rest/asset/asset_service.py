import os
import re

import core.utility as ut

from rest.http_base import HttpClient
import requests
import json


class Service(HttpClient):
    def __init__(self, var, param, index, config_name):
        super().__init__(var, param, index, config_name)
        self.vars = var
        self.params = param
        self.index = index
        self.npm_url = self.parser.get_setting("endpoint", "npm.url")
        self.kharma_url = self.parser.get_setting("endpoint", "kharma.url")
        self.base_url = self.default_url

    def rename_by_index(self, name):
        return name + "_step_" + self.index

    def get_access_token_with_email(self):
        user_email = self.params.get("email")
        rest_url = self.base_url + "/oauth2/token"
        service_client_key = "serviceClient"
        service_secret_key = "serviceSecret"
        request_body = {
            "username": user_email,
            "password": "Test1234",
            "grant_type": "PASSWORD",
            "client_id": self.properties.get(service_client_key),
            "client_secret": self.properties.get(service_secret_key)
        }
        res = requests.post(rest_url, data=json.dumps(request_body), headers=self.headers)
        if res.status_code == 200:
            response_json = json.loads(res.text)
            self.logger.info("get user access token success! " + response_json["access_token"])
            return response_json["access_token"]

    def get_oauth_code(self):
        rest_url = self.base_url + "/oauth2/authorize"
        payload = "client_id=packman&response_type=code&format=json&" + "access_token=" + str(
            self.get_access_token_with_email()) + "&grant_type=AUTHORIZATION_CODE"
        self.headers["Content-Type"] = "application/x-www-form-urlencoded"
        res = requests.request("POST", rest_url, headers=self.headers, data=payload)
        if res.status_code == 200:
            response_json = res.json()
            self.logger.info("get user code success! " + response_json["code"])
            return response_json["code"]

    def get_access_token_with_code(self):
        rest_url = self.base_url + "/oauth2/token"
        vetting_client_key = "vettingClient"
        vetting_secret_key = "vettingSecret"
        payload = "grant_type=AUTHORIZATION_CODE&client_id=" + str(
            self.properties.get(vetting_client_key)) + "&client_secret=" + str(
            self.properties.get(vetting_secret_key)) + "&code=" + str(
            self.get_oauth_code()) + "&redirect_uri=packman%3A//unity"
        self.headers["Content-Type"] = "application/x-www-form-urlencoded"
        res = requests.request("POST", rest_url, headers=self.headers, data=payload)
        if res.status_code == 200:
            response_json = res.json()
            self.logger.info("get access token success! " + response_json["access_token"])
            return response_json["access_token"]

    def upload_pacman(self):
        files = [
            ('file', open('./testcase/vettingTestImage/helloworld.zip', 'rb'))
        ]
        payload = {'publisherId': '311',
                   'name': 'com.unity.' + ut.random_str(4),
                   'version': '0.0.1',
                   'packageVersion': ''.join(self.get_package_version()),
                   'packmanVersion': '2019.1',
                   'displayName': 'Test name',
                   'minUnityVersion': '2018.2.2'}
        rest_url = self.npm_url + "/api/upload"
        user_token = "Bearer " + self.get_access_token_with_code()
        headers = {
            'Authorization': user_token
        }
        res = requests.request("POST", rest_url, headers=headers, data=payload, files=files)
        if res.status_code == 200:
            self.logger.info("upload success!")

    def get_param_value(self, name):
        value = self.params.get(name)
        if value.startswith("${"):
            return self.vars.get(value[2:-1])
        return name

    def get_package_version(self):
        now_url = self.vars.get("current_url")
        pattern = re.compile('id=([0-9]*)')
        id_value = pattern.findall(now_url)
        self.logger.info("package version is :" + str(id_value))
        return id_value

    def create_value(self):
        Digits = self.params.get("Digits")
        name = ut.random_str(int(Digits)) + "_package"
        self.vars.put(self.rename_by_index("value"), name)
        self.logger.info("package name is :" + name)

    def login_with_AccessToken(self):
        license_hash_key = "license_hash"
        hardware_hash_key = "hardware_hash"
        rest_url = self.kharma_url + "/login"
        payload = "user_access_token=" + self.get_access_token_with_code() + "&unityversion=2018.2.2f1" + "&toolversion=V5.0.2" + "&license_hash=" + self.properties.get(
            license_hash_key) + "&hardware_hash=" + self.properties.get(hardware_hash_key)
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        res = requests.request("POST", rest_url, headers=headers, data=payload)
        if res.status_code == 200:
            response_json = res.json()
            self.logger.info(
                "login with accessToken successfully,the xunitysession is ! " + response_json["xunitysession"])
            return response_json["xunitysession"]

    def upload_asset_package(self):
        rest_url = self.kharma_url + "/api" + "/asset-store-tools" + "/package/" + ''.join(
            self.get_package_version()) + "/unitypackage.json?"
        param = {
            "unityversion": "2018.2.2f1",
            "toolversion": "V5.0.2"
        }
        files = [
            ('file', open('./testcase/vettingTestImage/Scenes.gzip', 'rb'))
        ]
        headers = {
            'X-Unity-Session': self.login_with_AccessToken(),
            'Keep-Alive':'false',
            'Content-Length':str(os.path.getsize('./testcase/vettingTestImage/Scenes.gzip'))
        }
        res = requests.request("PUT", rest_url, params=param, headers=headers, files=files)
        if res.status_code == 200:
            self.logger.info("upload success!")
