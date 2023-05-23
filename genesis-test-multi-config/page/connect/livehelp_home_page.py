from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/livehelp/client/requests"
    btn_get_livehelp_locator = (By.XPATH,"//button[@class=\"raised-btn_2vTjL538 raised-btn-primary-blue_CwUp44WJ menu-button_YyixL-_9 live-help_3w9b1wHE GA_btn_global_get_help size-new-medium_1KbDqy0a\"]")
    btn_search_expert_locator = (By.CLASS_NAME,"search-experts_Emckt8A0")
    btn_become_expert_locator = (By.XPATH,"//button[@class=\"raised-btn_2vTjL538 raised-btn-violet_P77QoYei menu-button_YyixL-_9 guru_1sDCljQ5 GA_btn_global_become_expert size-new-medium_1KbDqy0a\"]")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_get_livehelp = None
        self.btn_search_expert = None
        self.btn_become_expert = None
        self.present_locator = self.btn_get_livehelp_locator


    def init_elements(self):
        super().init_elements()
        self.btn_get_livehelp = super().get_element(self.btn_get_livehelp_locator)
        self.btn_search_expert = super().get_element(self.btn_search_expert_locator)
        self.btn_become_expert = super().get_element(self.btn_become_expert_locator)