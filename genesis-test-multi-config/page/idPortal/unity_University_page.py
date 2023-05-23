from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-staging.unity.com/en/account"
    skip_btn_locator = (By.NAME, "commit")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.present_locator = self.skip_btn_locator

    def init_elements(self):
        super().init_elements()
        self.skip_btn = super().get_element(self.skip_btn_locator)

