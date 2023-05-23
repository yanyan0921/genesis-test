from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Page(BasePage):
    btn_guide_update_locator = (By.CSS_SELECTOR,"[class ='btn next ']")
    guide_OK_btn_locator = (By.NAME, "conversations_accept_updated_tos_form[accept]")
    guide2_OK_btn_locator = (By.NAME, "conversations_connect_migration_review_form[next]")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.guide_OK_btn = None
        self.guide2_OK_btn = None
        self.btn_guide_update = self.btn_guide_update_locator
        self.present_locator = self.btn_guide_update_locator

    def init_elements(self):
        super().init_elements()
        self.guide_OK_btn = super().get_element(self.guide_OK_btn_locator)
        self.btn_guide_update = super().get_element(self.btn_guide_update_locator)
        self.guide2_OK_btn = super().get_element(self.guide2_OK_btn_locator)