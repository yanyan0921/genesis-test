from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    text_job_verify_locator = (By.XPATH, "//div[@class='job-title_S2AobEan']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.text_job_verify = None
        self.present_locator = self.text_job_verify_locator

    def init_elements(self):
        super().init_elements()
        self.text_job_verify = super().get_element(self.text_job_verify_locator)

