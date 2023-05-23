from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    btn_releases_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/a[3]")
    btn_create_releases_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/a")
    btn_branch_page_locator = (By.XPATH, "//*[@id=\"release-list\"]/li/div[1]/span[3]/a")
    info_tag_name_locator = (By.ID, "tag-name")
    info_title_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[2]/div[1]/input")
    btn_pre_publish_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[1]/div")
    btn_publish_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[2]/button")
    info_pr_verify_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/p")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        self.btn_releases_page = None
        self.btn_create_releases_page = None
        self.btn_branch_page = None
        self.info_tag_name = None
        self.info_title = None
        self.btn_pre_publish = None
        self.btn_publish = None
        self.info_pr_verify = None
        self.present_locator = self.btn_user_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.btn_releases_page = super().get_element(self.btn_releases_page_locator)
        self.btn_create_releases_page = super().get_element(self.btn_create_releases_page_locator)
        self.btn_branch_page = super().get_element(self.btn_branch_page_locator)
        self.info_tag_name = super().get_element(self.info_tag_name_locator)
        self.info_title = super().get_element(self.info_title_locator)
        self.btn_pre_publish = super().get_element(self.btn_pre_publish_locator)
        self.btn_publish = super().get_element(self.btn_publish_locator)
        self.info_pr_verify = super().get_element(self.info_pr_verify_locator)
