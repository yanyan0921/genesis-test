from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_visa_locator = (By.ID, "pmitem_0")
    input_card_no_locator = (By.ID, "cardNumber")
    input_cardholder_locator = (By.ID, "cardholderName")
    input_expiry_month_locator = (By.ID, "expiryMonth")
    input_expiry_year_locator = (By.ID, "expiryYear")
    input_security_code_locator = (By.ID, "securityCode")
    btn_pay_locator = (By.ID, "submitButton")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.input_card_no_locator
        self.btn_visa = None
        self.input_card_no = None
        self.input_cardholder = None
        self.input_expiry_month = None
        self.input_expiry_year = None
        self.input_security_code = None
        self.btn_pay = None

    def init_elements(self):
        super().init_elements()
        self.btn_visa = super().get_element(self.btn_visa_locator)
        self.input_card_no = super().get_element(self.input_card_no_locator)
        self.input_cardholder = super().get_element(self.input_cardholder_locator)
        self.input_expiry_month = super().get_element(self.input_expiry_month_locator)
        self.input_expiry_year = super().get_element(self.input_expiry_year_locator)
        self.input_security_code = super().get_element(self.input_security_code_locator)
        self.btn_pay = super().get_element(self.btn_pay_locator)
