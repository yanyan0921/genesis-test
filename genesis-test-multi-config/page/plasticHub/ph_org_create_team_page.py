from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    input_team_name_locator = (By.ID, "team_name")
    btn_create_team_locator = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/form/div/div[3]/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.input_team_name = self.input_team_name_locator
        self.btn_create_team = self.btn_create_team_locator
        self.present_locator = self.btn_create_team_locator

    def init_elements(self):
        super().init_elements()
        self.input_team_name = super().get_element(self.input_team_name_locator)
        self.btn_create_team = super().get_element(self.btn_create_team_locator)
