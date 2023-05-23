from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_visibility_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]/form/div[3]/div")
    btn_update_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[1]/form/div[5]/button")
    btn_update_self_locator = (By.XPATH, "/html/body/div/div[2]/div[3]/div[1]/form/div[6]/button")
    tag_success_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]")
    btn_delete_repo_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div/div[1]/button")
    btn_delete_repo2_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div/div[1]/button")
    info_delete_locator = (By.ID, "repo_name")
    btn_delete_confirm_locator = (By.XPATH, "//*[@id=\"delete-repo-modal\"]/div[2]/form/div[3]/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_visibility = None
        self.btn_update = None
        self.btn_update_self = None
        self.tag_success = None
        self.btn_delete_repo = None
        self.btn_delete_repo2 = None
        self.info_delete = None
        self.btn_delete_confirm = None
        self.present_locator = self.btn_visibility_locator

    def init_elements(self):
        super().init_elements()
        self.btn_visibility = super().get_element(self.btn_visibility_locator)
        self.btn_update = super().get_element(self.btn_update_locator)
        self.btn_update_self = super().get_element(self.btn_update_self_locator)
        self.tag_success = super().get_element(self.tag_success_locator)
        self.btn_delete_repo = super().get_element(self.btn_delete_repo_locator)
        self.btn_delete_repo2 = super().get_element(self.btn_delete_repo2_locator)
        self.info_delete = super().get_element(self.info_delete_locator)
        self.btn_delete_confirm = super().get_element(self.btn_delete_confirm_locator)
