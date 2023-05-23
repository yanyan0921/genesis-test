from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    btn_issue_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/a[2]")
    btn_issue_create_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/a[2]")
    btn_issue_spec_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[6]/li/div[2]/div[1]/a")
    btn_milestone_setting_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[3]/a[1]")
    btn_closed_page_locator = (By.XPATH, "//*[@id=\"issue-filters\"]/div[1]/div/a[2]")
    btn_closed_milestones_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[6]/li/div[3]/a[2]")
    btn_closed_milestones2_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]/li/div[3]/a[2]")
    btn_spec_issue_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[6]/li/div[2]/div[1]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        self.btn_issue_page = None
        self.btn_issue_create = None
        self.btn_issue_spec_page = None
        self.btn_milestone_setting_page = None
        self.btn_closed_page = None
        self.btn_spec_issue = None
        self.btn_closed_milestones = None
        self.btn_closed_milestones2 = None
        self.present_locator = self.btn_user_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.btn_issue_page = super().get_element(self.btn_issue_page_locator)
        self.btn_issue_create = super().get_element(self.btn_issue_create_locator)
        self.btn_issue_spec_page = super().get_element(self.btn_issue_spec_page_locator)
        self.btn_milestone_setting_page = super().get_element(self.btn_milestone_setting_page_locator)
        self.btn_closed_page = super().get_element(self.btn_closed_page_locator)
        self.btn_spec_issue = super().get_element(self.btn_spec_issue_locator)
        self.btn_closed_milestones = super().get_element(self.btn_closed_milestones_locator)
        self.btn_closed_milestones2 = super().get_element(self.btn_closed_milestones2_locator)
