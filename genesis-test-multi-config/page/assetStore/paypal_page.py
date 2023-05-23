from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    input_pw_locator = (By.ID, "password")
    btn_agree_continue_locator = (By.ID, "payment-submit-btn")
    login_paypal_locator = (By.ID, "btnLogin")
    title_locator = (By.ID,"headerText")
    iframe_name_locator = (By.XPATH, '//*[@id="pwdIframe"]')
    accept_cookies_locator = (By.XPATH, '//*[@id="pwdIframe"]')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_agree_continue = None
        self.input_pw = self.input_pw_locator
        self.login_paypal = self.login_paypal_locator
        self.input_account = None
        self.title = self.title_locator
        self.iframe_name = None
        self.accept_cookies = None
        self.present_locator = self.title_locator

    def init_elements(self):
        super().init_elements()
        self.btn_agree_continue = super().get_element(self.btn_agree_continue_locator)
        self.input_pw = super().get_element(self.input_pw_locator)
        self.login_paypal = super().get_element(self.login_paypal_locator)
        self.title = super().get_element(self.title_locator)
        self.iframe_name = super().get_element(self.iframe_name_locator)
        self.accept_cookies = super().get_element(self.accept_cookies_locator)