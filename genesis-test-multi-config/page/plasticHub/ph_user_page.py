from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    icon_user_locator = (By.XPATH, "//*[@id=\"navbar\"]/div[2]/div[3]/span/img")
    btn_starred_locator = (By.ID, "menuitem_4")
    btn_log_out_locator = (By.ID, "menuitem_6")
    btn_repo_create_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div[1]/div[1]/button/a")
    btn_orgs_locator = (By.XPATH, "//*[@id=\"app\"]/div/div[1]/a[2]")
    btn_org_info_page_locator = (By.XPATH, "//*[@id=\"app\"]/div/div[3]/div/ul/li[1]")
    btn_explore_locator = (By.XPATH, "//*[@id=\"navbar\"]/a[2]")
    btn_events_element_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div[1]/div[3]/div[2]/div[1]/div/p[1]/a[2]")
    btn_notification_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div[2]/a[2]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.icon_user = None
        self.btn_starred = None
        self.btn_log_out = None
        self.btn_repo_create = None
        self.btn_orgs = None
        self.btn_org_info_page = None
        self.btn_explore = None
        self.btn_events_element_page = None
        self.btn_notification_page = None
        self.present_locator = self.icon_user_locator

    def init_elements(self):
        super().init_elements()
        self.icon_user = super().get_element(self.icon_user_locator)
        self.btn_starred = super().get_element(self.btn_starred_locator)
        self.btn_log_out = super().get_element(self.btn_log_out_locator)
        self.btn_repo_create = super().get_element(self.btn_repo_create_locator)
        self.btn_orgs = super().get_element(self.btn_orgs_locator)
        self.btn_org_info_page = super().get_element(self.btn_org_info_page_locator)
        self.btn_explore = super().get_element(self.btn_explore_locator)
        self.btn_events_element_page = super().get_element(self.btn_events_element_page_locator)
        self.btn_notification_page = super().get_element(self.btn_notification_page_locator)
