from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    response_checkbox_locator = (By.NAME, "paResMagicValues")
    submit_btn_locator = (By.CLASS_NAME, "lefty")
    payment_cancelled_locator = (By.XPATH,"/html/body/div/form/ul/li[6]/span/select/option[3]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.response_checkbox = None
        self.submit_btn = None
        self.payment_cancelled = None
        self.present_locator = self.submit_btn_locator

    def init_elements(self):
        super().init_elements()
        self.response_checkbox = super().get_element(self.response_checkbox_locator)
        self.submit_btn = super().get_element(self.submit_btn_locator)
        self.payment_cancelled = super().get_element(self.payment_cancelled_locator)
