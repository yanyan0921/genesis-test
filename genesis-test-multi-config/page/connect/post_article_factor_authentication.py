from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    btn_ok_locator = (By.XPATH,"//button[@class=\"raised-btn_2vTjL538 raised-btn-red_2RcoM63p button-ok_1g3l_Woz\"]")
    btn_skip_locator = (By.XPATH,"//button[@class=\"raised-btn_2vTjL538 raised-btn-default_3M_uvHPG button-cancel_1uHAq297\"]")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_ok = None
        self.btn_skip = None
        self.present_locator = self.btn_ok_locator


    def init_elements(self):
        super().init_elements()
        self.btn_ok = super().get_element(self.btn_ok_locator)
        self.btn_skip = super().get_element(self.btn_skip_locator)