from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    btn_issue_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/a[2]")
    btn_milestones_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/a[2]")
    btn_milestone_create_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/a")
    btn_close_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]/li/div[3]/a[2]")
    btn_close_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/a[2]")
    btn_open_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]/li[1]/div[3]/a[2]")
    btn_open_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/a[1]")
    btn_spec_milestone_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]/li[1]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        self.btn_milestones_page = None
        self.btn_milestone_create = None
        self.btn_close = None
        self.btn_close_page = None
        self.btn_open = None
        self.btn_open_page = None
        self.btn_spec_milestone_page = None
        self.present_locator = self.btn_user_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.btn_milestones_page = super().get_element(self.btn_milestones_page_locator)
        self.btn_milestone_create = super().get_element(self.btn_milestone_create_locator)
        self.btn_close = super().get_element(self.btn_close_locator)
        self.btn_close_page = super().get_element(self.btn_close_page_locator)
        self.btn_open = super().get_element(self.btn_open_locator)
        self.btn_open_page = super().get_element(self.btn_open_page_locator)
        self.btn_spec_milestone_page = super().get_element(self.btn_spec_milestone_page_locator)
