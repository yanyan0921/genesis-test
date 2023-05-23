from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    myFavorites_title_locator = (By.CLASS_NAME, '_1dKGw')


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.present_locator = self.myFavorites_title_locator

    def init_elements(self):
        super().init_elements()
        self.myFavorites_title = super().get_element(self.myFavorites_title_locator)
