from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    div_confirm_purchase_locator = (By.XPATH, "//*[@id=\"new_prepay_subscription_form\"]/div/div[3]/div/input")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.div_confirm_purchase = None
        self.present_locator = self.div_confirm_purchase_locator


    def init_elements(self):
        super().init_elements()
        self.div_confirm_purchase = super().get_element(self.div_confirm_purchase_locator)

