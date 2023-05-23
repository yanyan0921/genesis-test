from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    icon_signin_locator = (By.XPATH, "//*[@id=\"avatar-menu-wrapper\"]/div/div/div/a")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.icon_signin = None
        self.present_locator = self.icon_signin_locator

    def init_elements(self):
        super().init_elements()
        self.icon_signin = super().get_element(self.icon_signin_locator)
