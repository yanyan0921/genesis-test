from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    input_title_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[1]/div[1]/input")
    btn_create_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[2]/div[2]/button")
    btn_milestone_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[5]/li/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_user_page = None
        self.input_title = None
        self.btn_create = None
        self.btn_milestone_page = None
        self.present_locator = self.btn_user_page_locator

    def init_elements(self):
        super().init_elements()
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.input_title = super().get_element(self.input_title_locator)
        self.btn_create = super().get_element(self.btn_create_locator)
        self.btn_milestone_page = super().get_element(self.btn_milestone_page_locator)
