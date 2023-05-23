from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    btn_fromemailaddress_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[7]/div/div[3]/div/div[2]/div[1]/div[2]/div")
    icon_language_dropdown_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[4]/div[3]/div/button/div/div[2]")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_fromemailaddress = None
        self.present_locator = self.icon_language_dropdown_locator

    def init_elements(self):
        super().init_elements()
        self.btn_fromemailaddress = super().get_element(self.btn_fromemailaddress_locator)
        self.icon_language_dropdown = super().get_element(self.icon_language_dropdown_locator)
