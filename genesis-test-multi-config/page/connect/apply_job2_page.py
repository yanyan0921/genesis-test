from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    button_search_another_locator = (By.CSS_SELECTOR,".keyword-input-border_14MSI51R > .input_3yaUP2ah")
    button_view_application_locator = (By.XPATH,"//button[@class=\"raised-btn_2vTjL538 raised-btn-thirdly_QAfXf1ST button_1iiKL6U9\"]")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.button_search_another = None
        self.button_view_application = None
        self.present_locator = self.button_view_application_locator


    def init_elements(self):
        super().init_elements()
        self.button_search_another = super().get_element(self.button_search_another_locator)
        self.button_view_application = super().get_element(self.button_view_application_locator)