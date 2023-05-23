from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    FAQ_title_locator = (By.XPATH, '//*[@id="main-content"]/header/h1')
    myActivities_locator = (By.CSS_SELECTOR,"[class = 'page-header']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.FAQ_title = None
        self.myActivities = None
        self.present_locator = self.FAQ_title_locator

    def init_elements(self):
        super().init_elements()
        self.FAQ_title = super().get_element(self.FAQ_title_locator)
        self.myActivities = super().get_element(self.myActivities_locator)
