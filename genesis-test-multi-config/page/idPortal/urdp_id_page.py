from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Page(BasePage):
    base_url = "https://urdp-int.unity.cn/balance"
    decline_btn_locator = (By.XPATH, '//*[@id="content-wrapper"]/div/div/div/div/ul/li[2]/a')
    login_btn_locator = (By.XPATH, '//*[@id="new_conversations_create_session_form"]/div[4]/input')
    input_email_locator = (By.ID, "conversations_create_session_form_email")
    input_password_locator = (By.ID, "conversations_create_session_form_password")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_email = None
        self.input_password = None
        self.login_btn = None
        self.decline_btn = self.decline_btn_locator
        self.present_locator = self.decline_btn_locator

    def init_elements(self):
        super().init_elements()
        self.decline_btn = super().get_element(self.decline_btn_locator)
        self.input_email = super().get_element(self.input_email_locator)
        self.input_password = super().get_element(self.input_password_locator)
        self.login_btn = super().get_element(self.login_btn_locator)
