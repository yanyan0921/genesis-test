from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    btn_new_Team_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div[2]/div[4]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        self.btn_new_Team = self.btn_new_Team_locator
        self.present_locator = self.btn_new_Team_locator

    def init_elements(self):
        super().init_elements()
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.btn_new_Team = super().get_element(self.btn_new_Team_locator)
