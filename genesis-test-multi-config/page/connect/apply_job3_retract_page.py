from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/jobs?t=applied"
    button_retract_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div/div/div[3]/div[3]/div/div/div/div[2]/div/button")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.button_retract = None
        self.present_locator = self.button_retract_locator


    def init_elements(self):
        super().init_elements()
        self.button_retract = super().get_element(self.button_retract_locator)