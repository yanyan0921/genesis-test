from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_visa_locator = (By.ID, "pmitem_0")
    input_cc_number_locator = (By.ID, "cardNumber")
    input_cc_month_locator = (By.ID, "expiryMonth")
    input_cc_year_locator = (By.ID, "expiryYear")
    input_cc_name_locator = (By.ID, "cardholderName")
    btn_pay_now_locator = (By.ID, "submitButton")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.input_cc_number_locator
        self.btn_visa = None
        self.input_cc_number = None
        self.input_cc_month = None
        self.input_cc_year = None
        self.input_cc_name = None
        self.btn_pay_now = None

    def init_elements(self):
        super().init_elements()
        self.btn_visa = super().get_element(self.btn_visa_locator)
        self.input_cc_number = super().get_element(self.input_cc_number_locator)
        self.input_cc_month = super().get_element(self.input_cc_month_locator)
        self.input_cc_year = super().get_element(self.input_cc_year_locator)
        self.input_cc_name = super().get_element(self.input_cc_name_locator)
        self.btn_pay_now = super().get_element(self.btn_pay_now_locator)

