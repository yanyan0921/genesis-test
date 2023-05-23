from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    saveForLater_list_locator = (By.CSS_SELECTOR, "[class='row za-BQ']")
    favorites_list_locator = (By.CSS_SELECTOR, "[class = 'row za-BQ _2vpRP']")
    test_list_locator = (
    By.CLASS_NAME, "[class = 'row za-BQ']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.saveForLater_list = None
        self.favorites_list = self.favorites_list_locator
        self.test_list = None
        self.present_locator = self.favorites_list_locator

    def init_elements(self):
        super().init_elements()
        self.saveForLater_list = super().get_element(self.saveForLater_list_locator)
        self.favorites_list = super().get_element(self.favorites_list_locator)
        self.test_list = super().get_element(self.test_list_locator)
