from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    #btn_post_succeed_locator = (By.XPATH , "//button[contains(.,'现在发布')]")
    #article
    btn_post_succeed_locator = (By.XPATH, "//button[@class=\"raised-btn_2vTjL538 raised-btn-blue_37QDrHj0 post_3zXA0Q8b GA_btn_project_publish\"]")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_post_succeed = None
        self.present_locator = self.btn_post_succeed_locator

    def init_elements(self):
        super().init_elements()
        self.btn_post_succeed = super().get_element(self.btn_post_succeed_locator)
