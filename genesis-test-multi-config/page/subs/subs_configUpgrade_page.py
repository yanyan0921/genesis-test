from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_purchase_locator = (By.XPATH, "//*[@id=\"main-wrapper\"]/div/section/div[2]/div[2]/div[1]/div/div[3]/div[2]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.btn_purchase_locator
        self.btn_purchase = self.btn_purchase_locator

    def init_elements(self):
        super().init_elements()
        self.btn_purchase = super().get_element(self.btn_purchase_locator)
