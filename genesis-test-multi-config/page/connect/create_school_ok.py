from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    btn_ok_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div[7]/button")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_ok = None
        self.present_locator = self.btn_ok_locator


    def init_elements(self):
        super().init_elements()
        self.btn_ok = super().get_element(self.btn_ok_locator)