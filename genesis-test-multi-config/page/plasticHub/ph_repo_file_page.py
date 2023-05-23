from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_repo_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/a[2]")
    btn_fork_page_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/a[1]")
    btn_issue_page_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/a[2]")
    btn_raw_locator = (By.XPATH, "//*[@id=\"repo-files-table\"]/tbody/tr[1]/td[1]/span/a")
    btn_history_locator = (By.XPATH, "//*[@id=\"file-buttons\"]/div/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_repo = None
        self.btn_fork_page = None
        self.btn_issue_page = None
        self.btn_raw = None
        self.btn_history = None
        self.present_locator = self.btn_fork_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_repo = super().get_element(self.btn_repo_locator)
        self.btn_fork_page = super().get_element(self.btn_fork_page_locator)
        self.btn_issue_page = super().get_element(self.btn_issue_page_locator)
        self.btn_raw = super().get_element(self.btn_raw_locator)
        self.btn_history = super().get_element(self.btn_history_locator)
