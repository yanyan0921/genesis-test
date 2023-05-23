from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-staging.unity.com"
    userAnotherAccount_locator = (By.CSS_SELECTOR, "[class='default-avatar']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.userAnotherAccount = None
        self.present_locator = self.userAnotherAccount_locator

    def init_elements(self):
        super().init_elements()
        self.userAnotherAccount = super().get_element(self.userAnotherAccount_locator)





