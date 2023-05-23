from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/groups"
    btn_picture_locator = (By.XPATH, "//div[@class='buttons_16lIDcK0']/button[@class='raised-btn_2vTjL538 raised-btn-primary_MYOE9bp7 add_1LW0yga-']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_picture = None
        self.present_locator = self. btn_picture_locator

    def init_elements(self):
        super().init_elements()
        self.btn_picture_locator = super().get_element(self.btn_picture_locator)
