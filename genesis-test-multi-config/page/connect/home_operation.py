from typing import Tuple

from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-internal.unity.com/"
    div_user_locator = (By.XPATH,"//*[@id=\"feed-top\"]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div[1]")
    icon_report_adt_locator = (By.XPATH, "//*[@id=\"feed-top\"]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div/div")
    btn_report_locator = (By.XPATH, "//*[@id=\"feed-top\"]/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div[3]/div/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.div_user = None
        self.icon_report_adt = None
        self.btn_report = None
        self.present_locator = self.icon_report_adt_locator

    def init_elements(self):
        super().init_elements()
        self.div_user = super().get_element(self.div_user_locator)
        self.icon_report_adt = super().get_element(self.icon_report_adt_locator)
        self.btn_report = super().get_element(self.btn_report_locator)