from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    info_title_locator = (By.XPATH, "//*[@id=\"issue_title\"]")
    # info_commend_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[1]/div/div/div/div[3]/div[1]/div/div[2]/div[
    # 6]/div[1]/div/div/div/div[5]/pre/span")
    btn_create_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[1]/div/div/div/div[5]/button")
    info_issue_create_verify_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[1]/div")
    info_issue_comment_verify_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        self.info_title = None
        # self.info_commend = None
        self.btn_create = None
        self.info_issue_create_verify = None
        self.info_issue_comment_verify = None
        self.present_locator = self.btn_user_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.info_title = super().get_element(self.info_title_locator)
        # self.info_commend = super().get_element(self.info_commend_locator)
        self.btn_create = super().get_element(self.btn_create_locator)
        self.info_issue_create_verify = super().get_element(self.info_issue_create_verify_locator)
        self.info_issue_comment_verify = super().get_element(self.info_issue_comment_verify_locator)
