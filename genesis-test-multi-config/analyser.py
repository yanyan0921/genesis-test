import re

from selenium.webdriver.common.keys import Keys

import core.config_parser as config_parser
import core.web_driver as web_driver
import core.json_parser as json_parser
import importlib
import logging
import time
import selenium.common.exceptions
from threading import Thread
import core.variable as var
import json
import os
import rest.rest_core as rest
import core.summary_report as report_helper
import threading
import datetime
import sys
import action.chain as chain

if sys.version > '3':
    import queue as Queue
else:
    import Queue

lock = threading.Lock()
failure_reason_case_not_found = "Test case not found"
failure_reason_not_defined = "Web element not defined"
failure_reason_element_not_found = "Web element not found"
failure_reason_not_expected = "Target has not expected value"
failure_reason_timeout = "Page load time out"


class Analyser(Thread):
    def __init__(self, test_id_list, retry_count, skip_list, config_name):
        Thread.__init__(self)
        self.vars = var.Variable()
        self.test_id_list = test_id_list
        self.retry_count = retry_count
        self.rest = None
        self.chain = None
        self.queue = Queue.Queue()
        self.test_case_list = {}
        self.skip_list = skip_list

        self.config_name = config_name
        self.parser = config_parser.ConfigLoader(config_name)

    def switch_window(self, driver, i):
        handles = driver.window_handles
        size = len(handles)
        if handles[i] != driver.current_window_handle:
            driver.switch_to.window(handles[i])

    # you can set testcase priority here
    def set_test_priority_queue(self):
        for test_id in self.test_id_list:
            testcase = json_parser.JsonParser(test_id).load()
            if "retry_count" not in testcase["testcase"]:
                if self.retry_count > 0:
                    testcase["testcase"]["retry_count"] = self.retry_count
                else:
                    testcase["testcase"]["retry_count"] = 0
            self.queue.put(test_id)
            self.test_case_list[test_id] = testcase

    def convert_abspath(self, path):
        if os.path.isfile(path):
            return os.path.abspath(path)

    def rename_by_index(self, name, index):
        return name + "_step_" + index

    def get_page_base_url(self, page_path, env):
        page_name = page_path[page_path.rindex('.') + 1:]
        resources_folder_path = page_path[:page_path.rindex('.')].replace('.', '/')
        url_json_path = './' + resources_folder_path + '/resources/url.json'
        url_list = json_parser.JsonParser(url_json_path).load()
        for url in url_list[page_name]:
            if "base_url" in url:
                return url["base_url"][env]

    def run(self):
        try:
            logger = logging.getLogger("main.runner")
            result = {}
            duration = {}
            failure_reasons = {}
            self.set_test_priority_queue()

            while not self.queue.empty():
                test_id = self.queue.get()
                if test_id in self.test_case_list.keys():
                    res = self.test_case_list[test_id]
                    retry_count = res["testcase"]["retry_count"]
                else:
                    result[test_id] = False
                    failure_reasons[test_id] = failure_reason_case_not_found
                    retry_count = 0

                try:
                    logger.info("===========================================================================")
                    logger.info("Name: " + res["testcase"]["name"])
                    logger.info("Owner: " + res["testcase"]["owner"])
                    logger.info("Priority: " + res["testcase"]["priority"])
                    logger.info("Smoke: " + res["testcase"]["smoke"])
                    logger.info("Scenario: " + res["testcase"]["scenario"]["name"])
                    logger.info("---------------------------- START ---------------------------------------")

                    abort = False
                    current_case_start_time = time.time()
                    wait = self.parser.get_setting("selenium", "page.load.timeout")
                    browser = self.parser.get_setting("selenium", "browser.type")
                    env = self.parser.get_setting("test", "environment")
                    driver = web_driver.WebDriver(browser).get_driver()
                    driver.set_window_size(1980, 1080)
                    # driver.maximize_window()
                    logger.info("initialize web driver, and the driver is: " + browser)
                    logger.info("set max page load time to " + wait + "s")

                    for step in res["testcase"]["scenario"]["steps"]["step"]:
                        if abort is True:
                            continue
                        else:
                            logger.info("**************************************************************************")
                            logger.info("Step " + step["index"] + ": " + step["description"])
                            failure_reasons[test_id] = "STEP " + step["index"] + ": " + step[
                                "description"] + " | "
                            # 导入对应模块
                            if "resource" in step.keys():
                                try:
                                    self.rest = rest.Rest(self.vars, step["resource"], step["action"], step["index"],
                                                          self.config_name)
                                except Exception as e:
                                    result[test_id] = False
                                    failure_reasons[test_id] = failure_reasons[test_id] + str(e) + ""
                                    abort = True
                                    logger.error(e)
                            else:
                                class_name = "Page"
                                module_name = "page." + step.get("page")
                                try:
                                    module = importlib.import_module(module_name)
                                    obj_c = getattr(module, class_name)
                                    page = obj_c(driver, wait)
                                    if (step["need_redirect"]) == "true":
                                        url = self.get_page_base_url(module_name, env)
                                        page.navigate(url)

                                    if "switch_tab" in step.keys():
                                        self.switch_window(driver, int(step["switch_tab"]))

                                    try:

                                        getattr(page, "init_page")()
                                    except selenium.common.exceptions.TimeoutException as e:
                                        result[test_id] = False
                                        failure_reasons[test_id] = failure_reasons[
                                                                       test_id] + failure_reason_timeout + "  "
                                        logger.error(e)

                                    for action in step.get("action"):
                                        if action.get("present") == "false":
                                            page.init_elements()
                                        method_name = action.get("method")
                                        if method_name == "switch_default_content":
                                            driver.switch_to.default_content()
                                            break
                                        elif method_name == "switch_to_active_element":
                                            driver.switch_to.active_element()
                                            continue
                                        elif method_name == "action_chain":
                                            chain.Chain(driver, self.vars, page, action.get("chain"))
                                            if action.get("sleep"):
                                                logger.info("sleep" + action.get("sleep") + "s")
                                                time.sleep(int(action.get("sleep")))
                                            continue
                                        element_name = action.get("element")

                                        element = getattr(page, element_name)
                                        if method_name == "get_element_values":
                                            page_values = element.text
                                            self.vars.put(self.rename_by_index("value", step["index"]), page_values)

                                            logger.info("get page values success: " + str(page_values))
                                            continue

                                        if element is None and method_name == "null":
                                            logger.error("Unable to locate element " + element_name)
                                            break
                                        if element is None and method_name != "script":
                                            logger.error("Unable to locate element " + element_name)
                                            result[test_id] = False
                                            failure_reasons[test_id] = failure_reasons[
                                                                           test_id] + " ELEMENT: " + element_name + "|"
                                            failure_reasons[test_id] = failure_reasons[
                                                                           test_id] + failure_reason_element_not_found + "  "
                                            abort = True
                                            break
                                        if method_name == "get_current_url":
                                            current_url = driver.current_url
                                            self.vars.put("current_url", current_url)
                                            break
                                        elif method_name == "switch_frame":
                                            driver.switch_to.frame(element)
                                        elif method_name != "script":
                                            method = getattr(element, method_name)

                                        if action.get("value"):
                                            value = action["value"]
                                            if method_name == "send_keys":
                                                logger.info(
                                                    "execute " + method_name + " to element:[" + element_name + "] with value:[" + value + "]")
                                                if value.startswith("./"):
                                                    value = self.convert_abspath(value)
                                                elif value.startswith("${"):
                                                    value = self.vars.get(value[2:-1])
                                                elif value.startswith("Keys."):
                                                    value = getattr(Keys(), value[5:])
                                                method(value)
                                            elif method_name == "text":
                                                logger.info(
                                                    "execute verify " + method_name + " to element:[" + element_name + "]")
                                                text_value = element.text
                                                if value.startswith("${") and text_value != '':
                                                    if re.search("[+\-*/]", value):
                                                        vlist = re.split(r"(\+|-|\*|/)", value)
                                                        msg_text = str(
                                                            eval(self.vars.get(vlist[0][2:-1]) + vlist[1] + vlist[2]))
                                                    else:
                                                        msg_text = self.vars.get(value[2:-1])

                                                    if msg_text in element.text:
                                                        logger.info(
                                                            "verify success!" + element_name + " is contained by: " + element.text)
                                                        continue

                                                if text_value != value:
                                                    logger.error(element_name + " has not expected value:" + value)
                                                    result[test_id] = False
                                                    failure_reasons[test_id] = failure_reasons[
                                                                                   test_id] + " ELEMENT: " + element_name + " | "
                                                    failure_reasons[test_id] = failure_reasons[
                                                                                   test_id] + failure_reason_not_expected + "  "
                                                    abort = True
                                                    break
                                                else:
                                                    logger.info(
                                                        "verify success! " + element_name + " has expected value:" + value)
                                            elif method_name == "script":
                                                if element_name is not None and element_name != "":
                                                    logger.info(
                                                        "execute " + method_name + " to element:[" + element_name + "]"
                                                                                                                    " with value:[" + value + "]")
                                                    failure_reasons[test_id] = failure_reasons[
                                                                                   test_id] + " ELEMENT: " + element_name + " | "
                                                    driver.execute_script(value, element)
                                                else:
                                                    failure_reasons[test_id] = failure_reasons[
                                                                                   test_id] + " ELEMENT: " + element_name + " | "
                                                    logger.info(
                                                        "execute " + method_name + " with value:[" + value + "]")
                                                    driver.execute_script(value)
                                            if action.get("sleep"):
                                                logger.info("sleep" + action.get("sleep") + "s")
                                                time.sleep(int(action.get("sleep")))
                                        elif method_name != "switch_frame":
                                            method = getattr(element, method_name)
                                            logger.info("execute " + method_name + " to element:[" + element_name + "]")
                                            method()
                                            if action.get("sleep"):
                                                logger.info("sleep for " + action.get("sleep") + " s")
                                                time.sleep(int(action.get("sleep")))
                                except Exception as e:
                                    abort = True
                                    failure_reasons[test_id] = failure_reasons[test_id] + str(e) + ""
                                    logger.error(e)

                    if abort is True:
                        result[test_id] = False
                        if retry_count > 0:
                            self.test_case_list[test_id]["testcase"]["retry_count"] = retry_count - 1
                            self.queue.put(test_id)
                    else:
                        result[test_id] = True

                except (AttributeError, selenium.common.exceptions) as e:
                    logger.error(e)
                    result[test_id] = False
                    if retry_count > 0:
                        self.test_case_list[test_id]["testcase"]["retry_count"] = retry_count - 1
                        self.queue.put(test_id)

                    failure_reasons[test_id] = failure_reasons[test_id] + str(e) + ""
                finally:
                    logger.info("---------------------------- FINISH --------------------------------------")
                    duration_time = (time.time() - current_case_start_time)
                    duration[test_id[test_id.rfind("/") + 1:]] = str(datetime.timedelta(seconds=duration_time))[:-3]
                    logger.info("Elapsed: %dms" % (duration_time * 1000))
                    close = self.parser.get_setting("selenium", "close.browser.after.test")
                    if not result[test_id]:
                        driver.save_screenshot(test_id[test_id.rfind('/') + 1:test_id.rfind('.')] + ".png")
                    if close == "true":
                        driver.quit()
        finally:
            test_status = "PASSED"
            failure_count = 0
            failed_cases = []
            passed_cases = []
            skip_cases = []
            pass_count = 0

            if len(self.test_id_list) is 0:
                test_status = "SKIPPED"
            for skip_case in self.skip_list:
                skip_cases.append({"caseName": skip_case, "reason": failure_reason_case_not_found})
                duration[skip_case[skip_case.rfind("/") + 1:]] = str(datetime.timedelta(seconds=0))[:-3]

            for single_result in result.keys():
                if result[single_result] is False:
                    testcase_name = single_result[single_result.rfind("/") + 1:]
                    if single_result in failure_reasons:
                        failed_case = {"caseName": testcase_name, "reason": failure_reasons[single_result]}
                    else:
                        failed_case = {"caseName": testcase_name}
                    failed_cases.append(failed_case)
                    failure_count += 1
                    test_status = "FAILED"
                else:
                    testcase_name = single_result[single_result.rfind("/") + 1:]
                    passed_case = {"caseName": testcase_name}
                    pass_count += 1
                    passed_cases.append(passed_case)
            request_body = {
                "testSuitStatus": test_status,
                "results": {
                    "failedCases": failed_cases,
                    "failedCasesNumber": failure_count,
                    "passCaseNumber": len(result) - failure_count,
                    "passedCases": passed_cases,
                    "allCaseNumber": len(result)
                },
                "logFilePath": 'log.txt',
            }

            summary_report = report_helper.Report(failed_cases, passed_cases, skip_cases, test_status,
                                                  len(result) + len(self.skip_list), duration)
            summary_report.gen_report()
            logger.info(json.dumps(request_body))
            if test_status != "PASSED" or len(self.skip_list) > 0:
                raise Exception("Test failed!")
            elif pass_count + failure_count is 0:
                raise Exception("No testcase!")
