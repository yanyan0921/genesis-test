from rest.http_base import HttpClient
import core.utility as ut
import string
import requests
import json


class Service(HttpClient):
    def __init__(self, var, param, index, config_name):
        super().__init__(var, param, index, config_name)
        self.vars = var
        self.params = param
        self.gmail_user = "silkcloudtest" + "+"
        self.core_url = self.parser.get_setting("endpoint", "core.url")
        self.base_url = self.default_url

    def create_random_values(self):
        random_value = '' + ut.random_str(2) + ut.random_number(3) + ''
        self.vars.put("random_value", random_value)

    def rename_by_index(self, name):
        return name + "_step_" + self.index

    def create_login_user(self):
        country = self.params.get("country")
        user_rest_url = self.base_url + "/users"
        user_email = self.gmail_user + ut.random_str(1, string.ascii_lowercase) + ut.random_str(10) + '@gmail.com'
        tel = ut.create_phone(8)
        self.vars.put(self.rename_by_index("phone_number"), tel)
        user_request_body = self.user_body(user_email, country)
        super().get_service_token()
        self.vars.put(self.rename_by_index("email"), user_email)
        res = requests.post(user_rest_url, data=json.dumps(user_request_body), headers=self.headers)
        response_json = json.loads(res.text)
        self.logger.info(response_json)
        self.logger.info("User created, email :" + user_email)
        user_id = response_json["id"]
        self.vars.put(self.rename_by_index("user_id"), user_id)
        for email in response_json["emails"]:
            if email["primary"]:
                email_id = email["id"]
                break

        email_rest_url = user_rest_url + "/" + user_id + "/emails/" + email_id + "/verify"
        res = requests.put(email_rest_url, headers=self.headers)
        self.logger.info("User email verified")

        tfa_rest_url = self.base_url + "/user-skip-email-security"
        tfa_request_body = self.user_tfa(user_email)
        requests.post(tfa_rest_url, data=json.dumps(tfa_request_body), headers=self.headers)
        self.logger.info("Skip user email security")
        org_name = user_request_body.get("username")
        self.vars.put(self.rename_by_index("org_name"), org_name)
        self.logger.info("org name: " + org_name)

    def get_param_value(self, name):
        value = self.params.get(name)
        if value.startswith("${"):
            return self.vars.get(value[2:-1])
        return name

    def post_organization(self):
        user_email = self.get_param_value("email")
        request_body = self.organization_body()
        request_url = self.base_url + "/organizations"
        user_token = "Bearer " + self.get_user_access_token(user_email)
        self.headers["Authorization"] = user_token
        res = requests.post(request_url, data=json.dumps(request_body), headers=self.headers)
        if res.status_code == 200:
            response_body = json.loads(res.text)
            self.logger.info("create new org id: " + response_body["id"] + " success!")
            self.vars.put(self.rename_by_index("org_id"), response_body["id"])

    def add_user_to_org(self):
        org_id = self.get_param_value("org_id")
        user_id = self.get_param_value("user_id")
        org_rest_url = self.base_url + "/organizations/" + org_id + "/members"
        user_group_id = self.get_user_group_id(org_id)
        request_body = {
            "groupId": user_group_id,
            "userId": user_id
        }
        self.get_service_token()
        res = requests.post(org_rest_url, data=json.dumps(request_body), headers=self.headers)
        assert res.status_code == 200
        self.logger.info("Add user:" + user_id + "to org:" + org_id + " success!")

    def get_user_access_token(self, email):
        rest_url = self.core_url + "/api/login"
        request_body = {
            "username": email,
            "password": "Test1234",
            "grant_type": "password"
        }
        res = requests.post(rest_url, data=json.dumps(request_body), headers=self.headers)
        if res.status_code == 200:
            response_json = json.loads(res.text)
            self.logger.info("get user access token success! " + response_json["access_token"])
            return response_json["access_token"]
        return None

    def get_user_group_id(self, org_id):
        self.get_service_token()
        group_rest_url = self.base_url + "/groups?organizationId=" + org_id + "&&name=Users"
        res = requests.get(group_rest_url, headers=self.headers)
        result_json = json.loads(res.text)
        if result_json["total"] > 0:
            response_body = result_json["results"][0]
            self.logger.info("get user group id: " + response_body["id"])
            return response_body["id"]
        else:
            return None

    def get_org_id(self):
        search_org_url = self.base_url + "/organizations?name=" + self.get_param_value("org_name")
        response = requests.get(search_org_url, headers=self.headers)
        result_json = json.loads(response.text)
        for org_info in result_json["results"]:
            org_id = org_info["id"]
        self.vars.put(self.rename_by_index("org_id"), org_id)
        # New transfer parameters-》orgId
        self.logger.info("get orgId is :" + org_id)

    def get_default_org_id(self):
        user_id = self.get_param_value("user_id")
        search_org_url = self.base_url + "/users" + "/" + user_id
        response = requests.get(search_org_url, headers=self.headers)
        result_json = json.loads(response.text)
        default_org_id = result_json["extendedProperties"].get("UNITY_DEFAULT_ORGANIZATION")
        self.vars.put(self.rename_by_index("default_org_id"), default_org_id)
        self.logger.info("the " + user_id + " default orgId is :" + default_org_id)

    def set_org_online_invoice_pay(self):
        search_org_url = self.base_url + "/organizations?name=" + self.get_param_value("org_name")
        resone = requests.get(search_org_url, headers=self.headers)
        result_json = json.loads(resone.text)
        for org_info in result_json["results"]:
            org_id = org_info["id"]
        self.logger.info(org_id)
        change_org_url = self.base_url + "/organizations/" + org_id + "/set-online-invoice-pay"
        change_org_request_body = {"onlineInvoicePay": True}
        self.get_service_token()
        res = requests.post(change_org_url, data=json.dumps(change_org_request_body), headers=self.headers)
        assert res.status_code == 200
        self.logger.info("enable org online invoice pay successfully: " + org_id)

    def set_org_tax_exempt(self):
        search_org_url = self.base_url + "/organizations?name=" + self.get_param_value("org_name")
        resone = requests.get(search_org_url, headers=self.headers)
        result_json = json.loads(resone.text)
        for org_info in result_json["results"]:
            org_id = org_info["id"]
        self.logger.info(org_id)
        set_org_tax_url = self.base_url + "/organizations/" + org_id + "/set-tax-exempt"
        set_org_tax_request_body = {"taxExempt": {
            "US": "taxExempt"
        }}
        self.get_service_token()
        res = requests.put(set_org_tax_url, data=json.dumps(set_org_tax_request_body), headers=self.headers)
        assert res.status_code == 200
        self.logger.info("set org tax exempt successfully: " + org_id)

    def get_sms_code(self):
        area_code = self.params.get("area_code")
        phone_number = area_code + self.get_param_value("phone_number")
        search_sms_code_url = self.base_url + "/sms?phone_number=" + phone_number
        self.get_service_token()
        res_sms_one = requests.get(search_sms_code_url, headers=self.headers)
        result_json = json.loads(res_sms_one.text)
        for phoneNumbers in result_json["results"]:
            sms_code = phoneNumbers["replacements"].get("code")
        self.vars.put(self.rename_by_index("sms_code"), sms_code)
        self.logger.info("sms code :" + sms_code)

    def organization_body(self):
        return {
            "url": "org." + ut.random_str(10) + ".silkcloud.com",
            "name": "Org_" + ut.random_str(10),
            "description": "test organization" + ut.random_str(10),
            "company": "Silkcloud Gongz",
            "email": ut.random_mail(),
            "vat": {},
            "addressList": [
                {
                    "streetAddress": "800 West Campbell Road",
                    "locality": "Richardson",
                    "region": "27",
                    "postalCode": "90012",
                    "country": "US",
                    "fullName": ut.random_str(10),
                    "phoneNumber": "+8622288848614",
                    "email": ut.random_mail(),
                    "firstName": ut.random_str(5),
                    "lastName": ut.random_str(5),
                    "companyName": "Silkcloud" + ut.random_str(5),
                    "primary": True
                }
            ],
            "userRoles": [],
            "allowedUserTypes": [],
            "extendedProperties": {}
        }

    def user_tfa(self, email):
        return {
            'type': 'EMAIL',
            'value': email,
            'isRegex': False
        }

    def user_body(self, email, country):
        return {
            "username": ut.random_str(1, string.ascii_letters) + ut.random_str(10),
            "name": {
                "givenName": ut.random_str(10),
                "familyName": ut.random_str(10)
            },
            'password': "Test1234",
            "dob": "1980-05-01T00:00:00Z",
            "gender": "FEMALE",
            "changePasswordAtNextLogin": False,
            "suspended": False,
            "countryOfResidence": country,
            "preferredLocale": "en_US",
            "avatar": None,
            "emails": [
                {
                    "primary": True,
                    "type": "HOME",
                    "value": email
                },
                {
                    "primary": False,
                    "type": "HOME",
                    "value": self.gmail_user + ut.random_str(1, string.ascii_letters) + ut.random_str(10) + '@gmail.com'
                }
            ],
            "agreedTerms": [
                {
                    "tosId": "unity_privacy",
                    "tosVersion": 14,
                    "agreedTime": "2018-06-01T01:32:53Z"
                },
                {
                    "tosId": "unity_tos",
                    "tosVersion": 6,
                    "agreedTime": "2018-06-01T01:32:53Z"
                }
            ],
            "externalIds": [
                {
                    "type": "XIAOMI_SESSION_ID",
                    "value": ut.random_str(20)
                },
                {
                    "value": ut.random_str(20),
                    "type": "GITHUB_EXTERNAL_ID"
                }
            ],
            "addresses": [
                {
                    "primary": True,
                    "type": "HOME",
                    "isFormatted": False,
                    "poBox": "95544",
                    "extendedAddress": "Room 201",
                    "streetAddress": "115 Justin Street",
                    "region": "CA",
                    "postalCode": "95533",
                    "country": country,
                    "email": email,
                    "firstName": ut.random_str(10, string.ascii_letters),
                    "lastName": ut.random_str(10, string.ascii_letters),
                    "companyName": ut.random_str(10, string.ascii_letters),
                    "phoneNumber": "8116330493"
                },
                {
                    "primary": False,
                    "type": "HOME",
                    "isFormatted": False,
                    "poBox": "95544",
                    "extendedAddress": "Room 202",
                    "streetAddress": "116 Justin2 Street",
                    "region": "CA",
                    "postalCode": "95343",
                    "country": "US",
                    "email": self.gmail_user + ut.random_str(1, string.ascii_letters) + ut.random_str(
                        10) + '@gmail.com',
                    "firstName": ut.random_str(10, string.ascii_letters),
                    "lastName": ut.random_str(10, string.ascii_letters),
                    "companyName": ut.random_str(10, string.ascii_letters),
                    "phoneNumber": "8116330493"
                }
            ],
            "phones": [
                {
                    "value": '+86' + ut.random_number(20),
                    "type": "HOME",
                    "primary": True
                },
                {
                    "value": '+86' + ut.random_number(20),
                    "type": "HOME",
                    "primary": False
                }
            ],
            "extendedProperties": {
                'USER_STATE_CODE': {
                    'stateCode': 'FL'
                }
            }
        }
