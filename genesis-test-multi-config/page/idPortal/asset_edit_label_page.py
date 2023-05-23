from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://id-staging.unity.com"
    input_box_locator = (By.XPATH,"//*[@id=\"alert_edit_label\"]/div/div/div[1]/div[2]/input")
    label_delete_locator = (By.XPATH,"//*[@id=\"alert_edit_label\"]/div/div/div[2]/span/i")
    close_window_button_locator = (By.XPATH,"//*[@id=\"alert_edit_label\"]/div/h2/i")
    remove_btn_locator = (By.CSS_SELECTOR,"[class = 'btn bg-re']")
    add_btn_locator = (By.CSS_SELECTOR,"[class = 'btn mr10 bg-gr']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_box = None
        self.label_delete = None
        self.close_window_button = None
        self.remove_btn = None
        self.add_btn = None
        self.present_locator = self.close_window_button_locator

    def init_elements(self):
        super().init_elements()
        self.input_box = super().get_element(self.input_box_locator)
        self.label_delete = super().get_element(self.label_delete_locator)
        self.close_window_button = super().get_element(self.close_window_button_locator)
        self.remove_btn = super().get_element(self.remove_btn_locator)
        self.add_btn = super().get_element(self.add_btn_locator)