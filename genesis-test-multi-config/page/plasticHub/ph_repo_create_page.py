from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://plastichub-int.unity.cn/repo/create"
    choose_owner_locator = (By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div/div[1]/div")
    btn_owner_locator = (By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div/div[1]/div/div/div")
    input_repo_name_locator = (By.ID, "repo_name")
    btn_repo_visibility_locator = (By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div/div[3]/div/label")
    btn_repo_create_locator = (By.XPATH, "/html/body/div[2]/div[2]/div/div/form/div/div[5]/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.choose_owner = None
        self.btn_owner = None
        self.input_repo_name = None
        self.btn_repo_visibility = None
        self.btn_repo_create = None
        self.present_locator = self.btn_repo_create_locator

    def init_elements(self):
        super().init_elements()
        self.choose_owner = super().get_element(self.choose_owner_locator)
        self.btn_owner = super().get_element(self.btn_owner_locator)
        self.input_repo_name = super().get_element(self.input_repo_name_locator)
        self.btn_repo_visibility = super().get_element(self.btn_repo_visibility_locator)
        self.btn_repo_create = super().get_element(self.btn_repo_create_locator)


