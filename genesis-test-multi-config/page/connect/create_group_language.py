from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/groups"
    #选择偏好语言
    icon_language_locator = (By.CSS_SELECTOR, ".input-wrapper_3Q82pEu2 .triangle_20fmw_FF")
    select_language_locator = (By.CSS_SELECTOR, ".selectItem_2K6fI4KB:nth-child(45)")
    btn_save_locator = (By.CSS_SELECTOR, ".blue_1N0NIlL6")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.icon_language = None
        self.select_language = None
        self.btn_save = None
        self.present_locator = self.btn_save_locator

    def init_elements(self):
        super().init_elements()
        self.icon_language = super().get_element(self.icon_language_locator)
        self.select_language = super().get_element(self.select_language_locator)
        self.btn_save = super().get_element(self.btn_save_locator)