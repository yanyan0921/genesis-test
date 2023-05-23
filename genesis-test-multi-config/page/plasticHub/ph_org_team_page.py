from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_join_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div[1]/h4/div/form/button")
    btn_remove_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div[2]/div[3]/div/form/button")
    btn_setting_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div[1]/div[2]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_join = self.btn_join_locator
        self.btn_remove = self.btn_remove_locator
        self.btn_setting = self.btn_setting_locator
        self.present_locator = self.btn_remove_locator

    def init_elements(self):
        super().init_elements()
        self.btn_join = super().get_element(self.btn_join_locator)
        self.btn_remove = super().get_element(self.btn_remove_locator)
        self.btn_setting = super().get_element(self.btn_setting_locator)
