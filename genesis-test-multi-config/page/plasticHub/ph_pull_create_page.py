from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    # info_commend_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[1]/div/div/div/div[3]/div[1]/div/div[2]/div[
    # 6]/div[1]/div/div/div/div[5]/pre/span")
    btn_merge_into_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]")
    btn_merge_into_element_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]")
    btn_apply_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/button")
    btn_create_locator = (By.XPATH, "//*[@id=\"new-issue\"]/div[1]/div/div/div/div[5]/button")
    info_pr_verify_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/p")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        # self.info_commend = None
        self.btn_merge_into = None
        self.btn_merge_into_element = None
        self.btn_apply = None
        self.btn_create = None
        self.info_pr_verify = None
        self.present_locator = self.btn_user_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        # self.info_commend = super().get_element(self.info_commend_locator)
        self.btn_merge_into = super().get_element(self.btn_merge_into_locator)
        self.btn_merge_into_element = super().get_element(self.btn_merge_into_element_locator)
        self.btn_apply = super().get_element(self.btn_apply_locator)
        self.btn_create = super().get_element(self.btn_create_locator)
        self.info_pr_verify = super().get_element(self.info_pr_verify_locator)
