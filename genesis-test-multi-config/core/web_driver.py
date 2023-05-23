from selenium import webdriver
import core.config_parser as config_parser
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


class WebDriver:
    parser = config_parser.ConfigLoader("default")
    platform = parser.get_setting("selenium", "platform")

    def __init__(self, browser):
        if browser == "firefox":
            self.driver = webdriver.Firefox(executable_path='geckodriver')
        elif browser == "chrome":
            options = Options()
            options.page_load_strategy = 'eager'
            options.add_experimental_option("detach", True)
            if self.platform == "mac":
                self.driver = webdriver.Chrome(executable_path="./driver/chromedriver", options=options)
            else:
                self.driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe", options=options)
        elif browser == "edge":  # 88.0.705.81
            self.driver = webdriver.Edge(executable_path="./driver/msedgedriver.exe")

    def get_driver(self):
        return self.driver
