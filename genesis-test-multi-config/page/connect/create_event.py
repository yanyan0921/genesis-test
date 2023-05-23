from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/groups"
    button_event_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[1]/div/div[2]/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.button_event = None
        self.present_locator = self. button_event_locator

    def init_elements(self):
        super().init_elements()
        self.button_event = super().get_element(self.button_event_locator)