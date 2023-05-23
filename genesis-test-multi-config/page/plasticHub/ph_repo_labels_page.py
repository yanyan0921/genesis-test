from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    btn_issue_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/a[2]")
    btn_milestones_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/a[2]")
    btn_default_label_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[4]/div/div[1]/div/div/form/button")
    btn_delete_label_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[4]/div/li[1]/div/div[4]/a[1]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        self.btn_milestones_page = None
        self.btn_milestone_create = None
        self.btn_close = None
        self.btn_close_page = None
        self.btn_open = None
        self.btn_open_page = None
        self.btn_default_label = None
        self.btn_delete_label = None
        self.present_locator = self.btn_user_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.btn_milestones_page = super().get_element(self.btn_milestones_page_locator)
        self.btn_default_label = super().get_element(self.btn_default_label_locator)
        self.btn_delete_label = super().get_element(self.btn_delete_label_locator)
