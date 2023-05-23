from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-int.unity.com/"
    input_email_locator = (By.ID, "conversations_create_session_form_email")
    input_password_locator = (By.ID, "conversations_create_session_form_password")
    #input_group_name_locator = (By.CSS_SELECTOR,".active_1tGpmPsf > .input_3yaUP2ah")
    btn_sign_in_locator = (By.NAME,"commit")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_email = None
        self.input_password = None
        self.btn_sign_in = None
        self.present_locator = self.btn_sign_in_locator

    def init_elements(self):
        super().init_elements()
        self.input_email = super().get_element(self.input_email_locator)
        self.input_password = super().get_element(self.input_password_locator)
        self.btn_sign_in = super().get_element(self.btn_sign_in_locator)