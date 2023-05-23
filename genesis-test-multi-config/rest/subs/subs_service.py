from rest.http_base import HttpClient
import requests
import json
import time
import string
import requests
import json


class Service(HttpClient):

    def __init__(self, var, param, index, config_name):
        super().__init__(var, param, index, config_name)
        self.vars = var
        self.params = param
        self.index = index
        self.base_url = self.default_url

    def get_param_value(self, name):
        value = self.params.get(name)
        if value.startswith("${"):
            return self.vars.get(value[2:-1])
        return name

    def rename_by_index(self, name):
        return name + "_step_" + self.index

    def cancel_subs(self):
        search_org_url = self.base_url + "/organizations?name=" + self.get_param_value("org_name")
        resone = requests.get(search_org_url, headers=self.headers)
        result_json = json.loads(resone.text)
        for org_info in result_json["results"]:
            org_id = org_info["id"]

        search_subs_url = self.base_url + "/subscriptions?ownerId=" + org_id
        subs_list = list()
        while (len(subs_list) == 0):
            time.sleep(10)
            res = requests.get(search_subs_url, headers=self.headers)
            self.logger.info(res)
            result_json = json.loads(res.text)
            self.logger.info(result_json)
            subs_list = result_json["results"]
        self.logger.info("get subs by org id :" + org_id)

        for subs in subs_list:
            subsId = subs["id"]
            cancel_subs_url = self.base_url + "/subscriptions/" + subsId + "/cancel"
            cancel_subs_request_body = {"immediateCancel": True}
            res = requests.post(cancel_subs_url, data=json.dumps(cancel_subs_request_body), headers=self.headers)
            self.logger.info("subs cancelled :" + subsId)

    def post_purchase_quote(self):
        search_org_url = self.base_url + "/organizations?name=" + self.get_param_value("org_name")
        response = requests.get(search_org_url, headers=self.headers)
        result_json = json.loads(response.text)
        for org_info in result_json["results"]:
            org_id = org_info["id"]
        self.logger.info(org_id)
        pi_type = self.params.get("pi_type")
        url = self.base_url + "/quotes"
        quote_action_type = "PURCHASE"
        email = self.get_param_value("email")
        res = requests.post(url, data=json.dumps(self.quote_body(email, pi_type, org_id, quote_action_type)), headers=self.headers)
        self.logger.info("post purchase quote ")
        self.logger.info(res)
        self.logger.info(res.text)

    def post_purchase_pro(self):
        search_org_url = self.base_url + "/organizations?name=" + self.get_param_value("org_name")
        response = requests.get(search_org_url, headers=self.headers)
        result_json = json.loads(response.text)
        for org_info in result_json["results"]:
            org_id = org_info["id"]
        self.logger.info(org_id)
        pi_type = self.params.get("pi_type")
        url = self.base_url + "/quotes"
        quote_action_type = "PURCHASE"
        email = self.get_param_value("email")
        moths = self.params.get("moths")
        res = requests.post(url, data=json.dumps(self.pro_body(email, pi_type, org_id, quote_action_type, moths)), headers=self.headers)
        self.logger.info("post purchase quote ")
        self.logger.info(res)
        self.logger.info(res.text)


    def post_purchase_quote_without_org_id(self):
        org_id = None
        pi_type = self.params.get("pi_type")
        url = self.base_url + "/quotes"
        quote_action_type = "PURCHASE"
        email = self.get_param_value("email")
        res = requests.post(url, data=json.dumps(self.quote_body(email, pi_type, org_id, quote_action_type)), headers=self.headers)
        self.logger.info("post purchase quote ")
        self.logger.info(res)
        self.logger.info(res.text)

    def post_change_seat_quote(self):
        search_org_url = self.base_url + "/organizations?name=" + self.get_param_value("org_name")
        resone = requests.get(search_org_url, headers=self.headers)
        result_json = json.loads(resone.text)
        for org_info in result_json["results"]:
            org_id = org_info["id"]
        self.logger.info(org_id)
        pi_type = self.params.get("pi_type")
        url = self.base_url + "/quotes"
        quote_action_type = "CHANGE_SEAT"
        email = self.get_param_value("email")
        res = requests.post(url, data=json.dumps(self.quote_body(email, pi_type, org_id, quote_action_type)), headers=self.headers)
        self.logger.info("post change seat quote ")
        self.logger.info(res)
        self.logger.info(res.text)

    def post_renew_quote(self):
        search_org_url = self.base_url + "/organizations?name=" + self.get_param_value("org_name")
        resone = requests.get(search_org_url, headers=self.headers)
        result_json = json.loads(resone.text)
        for org_info in result_json["results"]:
            org_id = org_info["id"]
        self.logger.info(org_id)
        pi_type = self.params.get("pi_type")
        email = self.get_param_value("email")
        url = self.base_url + "/quotes"
        res = requests.post(url, data=json.dumps(self.renew_quote_body(email, pi_type, org_id)), headers=self.headers)
        self.logger.info("post renew quote ")
        self.logger.info(res)
        self.logger.info(res.text)

    def quote_body(self, email, pi_type, org_id, quote_action_type):
        return {
            "quoteNum": "80025000004h6rtAAA",
            "expirationTime": "2024-04-28T08:00:00Z",
            "quoteActionType": quote_action_type,
            "contractStartDate": "2020-05-01T00:00:00Z",
            "contractEndDate": "2021-01-01T00:00:00Z",
            "sfAccountId": "0012500000nbUj1AAE",
            "contactEmail": email,
            "country": "DK",
            "currency": "USD",
            "paymentMethodType": pi_type,
            "supportedPITypes": [
                "CREDITCARD",
                "PAYPAL",
                "KCP",
                "BOACOMPRA",
                "CHINAPAYRECURRING",
                "CHINAPAYONETIME"
            ],
            "salespersonEmail": "leonlu@silkcloud.com",
            "salespersonName": "LeonLu",
            "blackBoxDeal": False,
            "allowSeatReduction": False,
            "taxExempt": False,
            "paymentTerm": "CM+1M",
            "offlineMigrate": False,
            "onlineToOffline": False,
            "skipNotification": False,
            "issueOffice": "DK",
            "orgId": org_id,
            "quoteLines": [
                {
                    "quoteLineId": "sf-pro",
                    "productFamily": "unity",
                    "productTier": "pro",
                    "productSize": "",
                    "contractTerm": "24",
                    "paymentFrequency": "prepaid",
                    "productClass": "subscription",
                    "quantity": 2,
                    "startDate": "2017-01-01T00:00:00Z",
                    "endDate": "2019-01-01T00:00:00Z",
                    "segments": {
                        "year1": {
                            "discounts": {
                                "commitmentDiscRatio": "0.2",
                                "volumeDiscRatio": "0.1",
                                "conversionDiscRatio": "0.1",
                                "otherDiscRatio": "0.1",
                                "upliftRatio": "0"
                            },
                            "originalAmount": "0",
                            "finalAmount": "0",
                            "totalDiscountAmount": "0",
                            "commitmentDiscAmount": "0",
                            "volumeDiscAmount": "0",
                            "conversionDiscAmount": "0",
                            "otherDiscAmount": "0",
                            "deductionAmount": "0",
                            "localLevisAmount": "0"
                        },
                        "year2": {
                            "discounts": {
                                "commitmentDiscRatio": "0.05",
                                "volumeDiscRatio": "0.1",
                                "conversionDiscRatio": "0.05",
                                "otherDiscRatio": "0.03",
                                "upliftRatio": "0"
                            },
                            "originalAmount": "0",
                            "finalAmount": "0",
                            "totalDiscountAmount": "0",
                            "commitmentDiscAmount": "0",
                            "volumeDiscAmount": "0",
                            "conversionDiscAmount": "0",
                            "otherDiscAmount": "0",
                            "deductionAmount": "0",
                            "localLevisAmount": "0"
                        }
                    }
                }
            ],
            "vatNumber": "FR92518837927",
            "sellToAddress": {
                "locality": "Richardson",
                "country": "FR",
                "postalCode": "75080",
                "streetAddress": "Sell To",
                "firstName": "Shipping",
                "lastName": "Address",
                "phoneNumber": "8116330493",
                "email": "silkcloudtest+rNfLOMfCSiq@gmail.com"
            },
            "billToAddress": {
                "locality": "Richardson123",
                "region": "12",
                "country": "CN",
                "postalCode": "75080",
                "streetAddress": "800 West Campbell Road",
                "firstName": "Billing",
                "lastName": "Address",
                "phoneNumber": "8116330493",
                "email": "silkcloudtest+mlASAroKvEX@gmail.com"
            }
        }

    def pro_body(self, email, pi_type, org_id, quote_action_type, moths):
        return {
            "quoteNum": "80025000004h6rtAAA",
            "expirationTime": "2024-04-28T08:00:00Z",
            "quoteActionType": quote_action_type,
            "contractStartDate": "2020-05-01T00:00:00Z",
            "contractEndDate": "2021-01-01T00:00:00Z",
            "sfAccountId": "0012500000nbUj1AAE",
            "contactEmail": email,
            "country": "DK",
            "currency": "USD",
            "paymentMethodType": pi_type,
            "supportedPITypes": [
                "CREDITCARD",
                "PAYPAL",
                "KCP",
                "BOACOMPRA",
                "CHINAPAYRECURRING",
                "CHINAPAYONETIME"
            ],
            "salespersonEmail": "leonlu@silkcloud.com",
            "salespersonName": "LeonLu",
            "blackBoxDeal": False,
            "allowSeatReduction": False,
            "taxExempt": False,
            "paymentTerm": "CM+1M",
            "offlineMigrate": False,
            "onlineToOffline": False,
            "skipNotification": False,
            "issueOffice": "DK",
            "orgId": org_id,
            "quoteLines": [
                {
                    "quoteLineId": "sf-pro",
                    "productFamily": "unity",
                    "productTier": "pro",
                    "productSize": "",
                    "contractTerm": moths,
                    "paymentFrequency": "prepaid",
                    "productClass": "subscription",
                    "quantity": 1,
                    "startDate": "2017-01-01T00:00:00Z",
                    "endDate": "2019-01-01T00:00:00Z",
                    "segments": {
                        "year1": {
                            "discounts": {
                                "commitmentDiscRatio": "0.2",
                                "volumeDiscRatio": "0.1",
                                "conversionDiscRatio": "0.1",
                                "otherDiscRatio": "0.1",
                                "upliftRatio": "0"
                            },
                            "originalAmount": "0",
                            "finalAmount": "0",
                            "totalDiscountAmount": "0",
                            "commitmentDiscAmount": "0",
                            "volumeDiscAmount": "0",
                            "conversionDiscAmount": "0",
                            "otherDiscAmount": "0",
                            "deductionAmount": "0",
                            "localLevisAmount": "0"
                        },
                        "year2": {
                            "discounts": {
                                "commitmentDiscRatio": "0.05",
                                "volumeDiscRatio": "0.1",
                                "conversionDiscRatio": "0.05",
                                "otherDiscRatio": "0.03",
                                "upliftRatio": "0"
                            },
                            "originalAmount": "0",
                            "finalAmount": "0",
                            "totalDiscountAmount": "0",
                            "commitmentDiscAmount": "0",
                            "volumeDiscAmount": "0",
                            "conversionDiscAmount": "0",
                            "otherDiscAmount": "0",
                            "deductionAmount": "0",
                            "localLevisAmount": "0"
                        }
                    }
                }
            ],
            "vatNumber": "FR92518837927",
            "sellToAddress": {
                "locality": "Richardson",
                "country": "FR",
                "postalCode": "75080",
                "streetAddress": "Sell To",
                "firstName": "Shipping",
                "lastName": "Address",
                "phoneNumber": "8116330493",
                "email": "silkcloudtest+rNfLOMfCSiq@gmail.com"
            },
            "billToAddress": {
                "locality": "Richardson123",
                "region": "12",
                "country": "CN",
                "postalCode": "75080",
                "streetAddress": "800 West Campbell Road",
                "firstName": "Billing",
                "lastName": "Address",
                "phoneNumber": "8116330493",
                "email": "silkcloudtest+mlASAroKvEX@gmail.com"
            }
        }

    def renew_quote_body(self, email, pi_type, org_id):
        return {
            "quoteNum": "80025000004h6rtAAA",
            "expirationTime": "2024-04-28T08:00:00Z",
            "quoteActionType": "PURCHASE_RENEW",
            "contractStartDate": "2021-08-28T00:00:00Z",
            "contractEndDate": "2022-08-28T00:00:00Z",
            "sfAccountId": "0012500000nbUj1AAE",
            "contactEmail": email,
            "country": "DK",
            "currency": "USD",
            "paymentMethodType": pi_type,
            "supportedPITypes": [
                "CREDITCARD",
                "PAYPAL",
                "KCP",
                "BOACOMPRA",
                "CHINAPAYRECURRING",
                "CHINAPAYONETIME"
            ],
            "salespersonEmail": "leonlu@silkcloud.com",
            "salespersonName": "LeonLu",
            "blackBoxDeal": False,
            "allowSeatReduction": False,
            "taxExempt": False,
            "paymentTerm": "CM+1M",
            "offlineMigrate": False,
            "onlineToOffline": False,
            "skipNotification": False,
            "issueOffice": "DK",
            "orgId": org_id,
            "quoteLines": [
                {
                    "quoteLineId": "sf-pro",
                    "productFamily": "unity",
                    "productTier": "pro",
                    "productSize": "",
                    "contractTerm": "24",
                    "paymentFrequency": "prepaid",
                    "productClass": "subscription",
                    "quantity": 2,
                    "startDate": "2017-01-01T00:00:00Z",
                    "endDate": "2019-01-01T00:00:00Z",
                    "segments": {
                        "year1": {
                            "discounts": {
                                "commitmentDiscRatio": "0.2",
                                "volumeDiscRatio": "0.1",
                                "conversionDiscRatio": "0.1",
                                "otherDiscRatio": "0.1",
                                "upliftRatio": "0"
                            },
                            "originalAmount": "0",
                            "finalAmount": "0",
                            "totalDiscountAmount": "0",
                            "commitmentDiscAmount": "0",
                            "volumeDiscAmount": "0",
                            "conversionDiscAmount": "0",
                            "otherDiscAmount": "0",
                            "deductionAmount": "0",
                            "localLevisAmount": "0"
                        },
                        "year2": {
                            "discounts": {
                                "commitmentDiscRatio": "0.05",
                                "volumeDiscRatio": "0.1",
                                "conversionDiscRatio": "0.05",
                                "otherDiscRatio": "0.03",
                                "upliftRatio": "0"
                            },
                            "originalAmount": "0",
                            "finalAmount": "0",
                            "totalDiscountAmount": "0",
                            "commitmentDiscAmount": "0",
                            "volumeDiscAmount": "0",
                            "conversionDiscAmount": "0",
                            "otherDiscAmount": "0",
                            "deductionAmount": "0",
                            "localLevisAmount": "0"
                        }
                    }
                }
            ],
            "vatNumber": "FR92518837927",
            "sellToAddress": {
                "locality": "Richardson",
                "country": "FR",
                "postalCode": "75080",
                "streetAddress": "Sell To",
                "firstName": "Shipping",
                "lastName": "Address",
                "phoneNumber": "8116330493",
                "email": "silkcloudtest+rNfLOMfCSiq@gmail.com"
            },
            "billToAddress": {
                "locality": "Richardson123",
                "region": "12",
                "country": "CN",
                "postalCode": "75080",
                "streetAddress": "800 West Campbell Road",
                "firstName": "Billing",
                "lastName": "Address",
                "phoneNumber": "8116330493",
                "email": "silkcloudtest+mlASAroKvEX@gmail.com"
            }
        }