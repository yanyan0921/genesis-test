from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_repo_locator = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_repo = self.btn_repo_locator
        self.present_locator = self.btn_repo_locator

    def init_elements(self):
        super().init_elements()
        self.btn_repo = super().get_element(self.btn_repo_locator)
