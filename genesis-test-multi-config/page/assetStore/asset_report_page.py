import parser

from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    Input_box_locator = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]"
                                   "/div/div/div[2]/div[2]/div/div[1]/textarea")
    Submit_btn_locator = (By.CSS_SELECTOR, "[class='_3UE3J pDJt- auto _3er3j']")
    icon_locator = (By.CLASS_NAME, "_1uxJT")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.Input_box = None
        self.Submit_btn = None
        self.verify_txt = None
        self.present_locator = self.Submit_btn_locator

    def init_elements(self):
        super().init_elements()
        self.Input_box = super().get_element(self.Input_box_locator)
        self.Submit_btn = super().get_element(self.Submit_btn_locator)
