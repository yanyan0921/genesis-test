from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    submissionGuidelines_title_locator = (By.XPATH, '//*[@id="submission-guidelines-0"]')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.submissionGuidelines_title = None
        self.present_locator = self.submissionGuidelines_title_locator

    def init_elements(self):
        super().init_elements()
        self.submissionGuidelines_title = super().get_element(self.submissionGuidelines_title_locator)
