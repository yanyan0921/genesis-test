import requests
import json


class Transport:
    base_test_get_url = "/v1/testcases"

    def __init__(self, url, port):
        self.url = url

    def get_testcase(self, id):
        request_url = self.url + self.base_test_get_url + '/' + id
        res = requests.get(request_url)
        return json.loads(res.text)

    def post_test_result(self, result, run_id, suit_id):
        request_url = self.url + "/v1/testruns/" + run_id + "/testsuits/" + suit_id
        headers = {'Content-Type': 'application/json'}
        print("start post result")
        res = requests.put(request_url, data=json.dumps(result), headers=headers)
        print(request_url)
        print(json.dumps(result))
        print("done")

    def post_test_log(self, runner_id):
        request_url = self.url + "/v1/testruns/log/" + runner_id

        file = {'file': open(runner_id + '.txt', 'rb')}
        print("start post log")
        res = requests.post(request_url, files=file)
        print(request_url)
        print("done")
