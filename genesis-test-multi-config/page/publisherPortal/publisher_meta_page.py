from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    input_title_locator = (By.XPATH, "//*[@id=\"title\"]")
    save_btn_locator = (By.XPATH,"//*[@id=\"submit\"]")
    ok_btn_locator = (By.XPATH,"/html/body/div[4]/div[2]/div/input")
    go_Back_locator = (By.XPATH,"//*[@id=\"goBack\"]")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.input_title = None
        self.save_btn = None
        self.go_Back = None
        self.ok_btn = None
        self.present_locator = self.save_btn_locator

    def init_elements(self):
        super().init_elements()
        self.input_title = super().get_element(self.input_title_locator)
        self.save_btn = super().get_element(self.save_btn_locator)
        self.go_Back = super().get_element(self.go_Back_locator)
        self.ok_btn = super().get_element(self.ok_btn_locator)
