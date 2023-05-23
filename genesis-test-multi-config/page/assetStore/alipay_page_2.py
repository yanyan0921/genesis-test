from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    password_input_locator = (By.CSS_SELECTOR,".sixDigitPassword")
    pay_btn_locator = (By.CSS_SELECTOR,"#J_authSubmit")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.password_input = self.password_input_locator
        self.pay_btn = self.pay_btn_locator
        self.present_locator = self.pay_btn_locator

    def init_elements(self):
        super().init_elements()
        self.password_input = super().get_element(self.password_input_locator)
        self.pay_btn = super().get_element(self.pay_btn_locator)
