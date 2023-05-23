from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://genesis-staging.hq.unity3d.com"
    input_userName_locator = (By.ID, "conversations_create_session_form_email")
    input_password_locator = (By.ID, "conversations_create_session_form_password")
    btn_sign_in_locator = (By.NAME, "commit")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_userName = self.input_userName_locator
        self.input_password = self.input_password_locator
        self.btn_sign_in = self.btn_sign_in_locator
        self.present_locator = self.btn_sign_in_locator

    def init_elements(self):
        super().init_elements()
        self.input_userName = super().get_element(self.input_userName_locator)
        self.input_password = super().get_element(self.input_password_locator)
        self.btn_sign_in = super().get_element(self.btn_sign_in_locator)
