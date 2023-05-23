from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    button_yes_locator = (By.XPATH,"//button[@class=\"raised-btn_2vTjL538 raised-btn-red_2RcoM63p button-ok_t2XoE94U\"]")
    button_no_locator = (By.XPATH,"//button[class=\"raised-btn_2vTjL538 raised-btn-default_3M_uvHPG button-cancel_1V_1gtzJ\"]")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.button_yes = None
        self.button_no = None
        self.present_locator = self.button_yes_locator


    def init_elements(self):
        super().init_elements()
        self.button_yes = super().get_element(self.button_yes_locator)
        self.button_no = super().get_element(self.button_no_locator)