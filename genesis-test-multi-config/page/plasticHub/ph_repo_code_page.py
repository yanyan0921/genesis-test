from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_copy_url_locator = (By.ID, "clipboard-btn")
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a/img")
    btn_fork_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/a[1]")
    btn_starred_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/form[2]/div/button")
    btn_issue_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/a[2]")
    btn_releases_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/a[3]")
    btn_code_locator = (By.XPATH, "//*[@id=\"repo-files-table\"]/tbody/tr[4]/td[1]/span/a")
    btn_setting_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/div/a")
    btn_pull_request_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/a[2]")
    btn_tag_management_locator = (By.ID, "manage_topic")
    input_tag_locator = (By.XPATH, "//*[@id=\"topic_edit\"]/div[1]/div/div/input[2]")
    btn_tag_index_locator = (By.XPATH, "//*[@id=\"topic_edit\"]/div[1]/div/div/div[2]/div")
    btn_save_tag_locator = (By.ID, "save_topic")
    btn_tag_locator = (By.XPATH, "//*[@id=\"repo-topics\"]/a[1]")
    info_search_code_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/form/div/div/input")
    btn_search_code_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/form/div/div/button")
    btn_notification_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/div/a")
    info_tag_verify_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/p")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_copy_url = None
        self.btn_user_page = None
        self.btn_fork_page = None
        self.btn_starred = None
        self.btn_issue_page = None
        self.btn_releases_page = None
        self.btn_code = None
        self.btn_setting = None
        self.btn_pull_request_page = None
        self.btn_tag_management = None
        self.input_tag = None
        self.btn_save_tag = None
        self.btn_tag = None
        self.info_search_code = None
        self.btn_tag_index = None
        self.btn_search_code = None
        self.btn_notification = None
        self.info_tag_verify = None
        self.present_locator = self.btn_user_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_copy_url = super().get_element(self.btn_copy_url_locator)
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.btn_fork_page = super().get_element(self.btn_fork_page_locator)
        self.btn_starred = super().get_element(self.btn_starred_locator)
        self.btn_issue_page = super().get_element(self.btn_issue_page_locator)
        self.btn_releases_page = super().get_element(self.btn_releases_page_locator)
        self.btn_code = super().get_element(self.btn_code_locator)
        self.btn_setting = super().get_element(self.btn_setting_locator)
        self.btn_pull_request_page = super().get_element(self.btn_pull_request_page_locator)
        self.btn_tag_management = super().get_element(self.btn_tag_management_locator)
        self.input_tag = super().get_element(self.input_tag_locator)
        self.btn_tag_index = super().get_element(self.btn_tag_index_locator)
        self.btn_save_tag = super().get_element(self.btn_save_tag_locator)
        self.btn_tag = super().get_element(self.btn_tag_locator)
        self.info_search_code = super().get_element(self.info_search_code_locator)
        self.btn_search_code = super().get_element(self.btn_search_code_locator)
        self.btn_notification = super().get_element(self.btn_notification_locator)
        self.info_tag_verify = super().get_element(self.info_tag_verify_locator)
