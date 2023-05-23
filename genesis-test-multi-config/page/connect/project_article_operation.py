from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    btn_report_locator = (By.CLASS_NAME, "report_1ROrVAqF")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_report = None
        self.present_locator = self.btn_report_locator


    def init_elements(self):
        super().init_elements()
        self.btn_report = super().get_element(self.btn_report_locator)
     