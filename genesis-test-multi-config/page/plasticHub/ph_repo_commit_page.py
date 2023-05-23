from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_fork_page_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/a[1]")
    btn_issue_page_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/a[2]")
    btn_file_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/a")
    btn_source_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        self.btn_fork_page = None
        self.btn_issue_page = None
        self.btn_file = None
        self.btn_source = None
        self.present_locator = self.btn_fork_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_fork_page = super().get_element(self.btn_fork_page_locator)
        self.btn_issue_page = super().get_element(self.btn_issue_page_locator)
        self.btn_file = super().get_element(self.btn_file_locator)
        self.btn_source = super().get_element(self.btn_source_locator)
