from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    btn_fork_page_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/a[1]")
    btn_issue_page_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div/a[2]")
    btn_commits_page_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[1]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        self.btn_fork_page = None
        self.btn_issue_page = None
        self.btn_commits_page = None
        self.present_locator = self.btn_user_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.btn_fork_page = super().get_element(self.btn_fork_page_locator)
        self.btn_issue_page = super().get_element(self.btn_issue_page_locator)
        self.btn_commits_page = super().get_element(self.btn_commits_page_locator)
