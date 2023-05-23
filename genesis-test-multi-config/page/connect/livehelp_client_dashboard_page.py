from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/livehelp/search/experts"
    input_search_locator = (By.CLASS_NAME,"input_1nJ-ppVU")
    input_search2_locator = (By.CLASS_NAME, "input_1nJ-ppVU")
    btn_become_expert_locator = (By.XPATH,"//button[@class=\"raised-btn_2vTjL538 raised-btn-violet_P77QoYei menu-button_YyixL-_9 guru_1sDCljQ5 GA_btn_global_become_expert size-new-medium_1KbDqy0a\"]")
    verify_search_title_locator = (By.XPATH,"//div[@class=\"question-title_2bb7O-E8 normal\"]")
    verify_search_category_locator = (By.XPATH,"//div[@class=\"skill-wrap_2PabZw-1\"]/div")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_search = None
        self.input_search2 = None
        self.btn_become_expert = None
        self.verify_search_title = None
        self.verify_search_category = None
        self.present_locator = self.input_search_locator


    def init_elements(self):
        super().init_elements()
        self.input_search = super().get_element(self.input_search_locator)
        self.input_search2 = super().get_element(self.input_search2_locator)
        self.btn_become_expert = super().get_element(self.btn_become_expert_locator)
        self.verify_search_title = super().get_element(self.verify_search_title_locator)
        self.verify_search_category = super().get_element(self.verify_search_category_locator)
