from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_renewal_purchase_locator = (By.XPATH, "/html/body/div[1]/section/div[3]/div/div/form/div/div[3]/div/input")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_confirm_purchase = None
        self.present_locator = self.btn_renewal_purchase_locator


    def init_elements(self):
        super().init_elements()
        self.btn_renewal_purchase = super().get_element(self.btn_renewal_purchase_locator)

