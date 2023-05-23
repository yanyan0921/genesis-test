from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    input_embed_locator = (By.XPATH,"//div[@class=\"text-input_1zwaVtSr theme-dark_2f3h2N29\"]/div/input")
    btn_ok_locator = (By.XPATH, "//button[@class='raised-btn_2vTjL538 raised-btn-blue_37QDrHj0 size-xlarge_26YC-cEO width-full_2wWLBFy9']")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_embed = None
        self.btn_ok = None
        self.present_locator = self.input_embed_locator

    def init_elements(self):
        super().init_elements()
        self.input_embed = super().get_element(self.input_embed_locator)
        self.btn_ok = super().get_element(self.btn_ok_locator)
