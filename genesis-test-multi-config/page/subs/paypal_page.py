from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    #input_email_locator = (By.ID, "paypal-email") #zwh@123.com
    input_password_locator = (By.ID, "password") #Bugsfor$
    btn_login_locator = (By.ID, "btnLogin")
    btn_pay_locator = (By.ID, "consentButton")
    btn_verified_locator = (By.ID, "J_signUp")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.input_password_locator
        self.input_password = None
        self.btn_login = None
        self.btn_pay = None
        self.icon_QR = None

    def init_elements(self):
        super().init_elements()
        self.input_password = super().get_element(self.input_password_locator)
        self.btn_login = super().get_element(self.btn_login_locator)
        self.btn_pay = super().get_element(self.btn_pay_locator)
        self.btn_verified = super().get_element(self.btn_verified_locator)