from page.base_page import BasePage
from selenium.webdriver.common.by import By

class Page(BasePage):
            base_url = "https://connect-dev.unity.com/livehelp/"
            input_search_locator = (By.CLASS_NAME, "input_1nJ-ppVU")
            input_search2_locator = (By.CLASS_NAME, "input_1nJ-ppVU")
            verify_search_name_locator = (By.XPATH, "//div[@class=\"name_3lUKClEi dashboard_3TGRH7Bo\"]")
            verify_search_category_locator = (By.XPATH, "//div/div[@class=\"name_3lUKClEi dashboard_3TGRH7Bo\"]")

            def __init__(self, driver, wait):
                super().__int__(driver, wait)
                self.url = self.base_url
                self.input_search = None
                self.input_search2 = None
                self.verify_search_name = None
                self.verify_search_category = None
                self.present_locator = self.input_search_locator

            def init_elements(self):
                super().init_elements()
                self.input_search = super().get_element(self.input_search_locator)
                self.input_search2 = super().get_element(self.input_search2_locator)
                self.verify_search_name = super().get_element(self.verify_search_name_locator)
                self.verify_search_category = super().get_element(self.verify_search_category_locator)