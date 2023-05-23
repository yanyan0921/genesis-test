from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_repo_create_locator = (By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div/div[6]/button")
    btn_owner_locator = (By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div/div[1]/div")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_repo_create = None
        self.present_locator = self.btn_repo_create_locator
        self.btn_owner = self.btn_owner_locator

    def init_elements(self):
        super().init_elements()
        self.btn_repo_create = super().get_element(self.btn_repo_create_locator)
        self.btn_owner = super().get_element(self.btn_owner_locator)
