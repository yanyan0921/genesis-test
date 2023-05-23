from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_delete_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/form/div/div[3]/button[2]")
    btn_confirm_locator = (By.XPATH, "/html/body/div[4]/div/div[3]/div[2]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_delete = self.btn_delete_locator
        self.btn_confirm = self.btn_confirm_locator
        self.present_locator = self.btn_confirm_locator

    def init_elements(self):
        super().init_elements()
        self.btn_delete = super().get_element(self.btn_delete_locator)
        self.btn_confirm = super().get_element(self.btn_confirm_locator)
