from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://api-int.unity.com/v1/oauth2/authorize/new-account?client_id=marketplace&display=popup&response_type=code&scope=identity&redirect_uri=https%3A%2F%2Fconnect-dev.unity.com%2Fpublic%2Fpages%2Fauth%2Fcbiframe.html%3Fredirect_to%3D%252F%26source%3Daccount_switch"
    input_email_locator = (By.ID, "conversations_create_session_form_email")
    input_password_locator = (By.ID, "conversations_create_session_form_password")
    btn_login_locator = (By.NAME, "commit")



    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_email = None
        self.input_password = None
        self.btn_login = None
        self.present_locator = self.input_email_locator

    def init_elements(self):
        super().init_elements()
        self.input_email = super().get_element(self.input_email_locator)
        self.input_password = super().get_element(self.input_password_locator)
        self.btn_login = super().get_element(self.btn_login_locator)
