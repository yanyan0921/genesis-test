from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_commit_locator = (By.XPATH, "//*[@id=\"repo-files-table\"]/thead/tr/th[1]/span/span/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_commit = None
        self.present_locator = self.btn_commit_locator

    def init_elements(self):
        super().init_elements()
        self.btn_commit = super().get_element(self.btn_commit_locator)
