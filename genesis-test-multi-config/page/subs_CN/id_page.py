from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_account_login_locator = (By.XPATH, "//*[@id=\"content-wrapper\"]/div/div/div/div[1]/ul/li[2]/a")
    btn_email_login_locator = (By.XPATH, "//*[@id=\"content-wrapper\"]/div/div/div/div/ul/li[2]/a")
    input_email_address_locator = (By.ID, "conversations_create_session_form_email")
    input_password_locator = (By.ID, "conversations_create_session_form_password")
    btn_login_locator = (By.XPATH, "//*[@id=\"new_conversations_create_session_form\"]/div[4]/input")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.btn_email_login_locator
        self.btn_account_login = None
        self.btn_email_login = None
        self.input_email_address = None
        self.input_password = None
        self.btn_login = None

    def init_elements(self):
        super().init_elements()
        self.btn_account_login = super().get_element(self.btn_account_login_locator)
        self.btn_email_login = super().get_element(self.btn_email_login_locator)
        self.input_email_address = super().get_element(self.input_email_address_locator)
        self.input_password = super().get_element(self.input_password_locator)
        self.btn_login = super().get_element(self.btn_login_locator)
