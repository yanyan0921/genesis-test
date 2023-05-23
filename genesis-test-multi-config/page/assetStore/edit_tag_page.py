from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    # tag_input_locator=(By.CLASS_NAME,"_1rQVi")
    tag_input_locator = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div[4]/div/input")
    btn_add_locator = (By.CSS_SELECTOR, "[class='_3UE3J pDJt- auto _15Ii0']")
    remove_tag_locator = (By.CLASS_NAME, "_1_tq3")
    close_btn_locator = (By.CSS_SELECTOR,"[class='ifont ifont-close _3GSE9']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.tag_input = None
        self.btn_add = None
        self.remove_tag = None
        self.close_btn = None
        self.present_locator = self.tag_input_locator

    def init_elements(self):
        super().init_elements()
        self.tag_input = super().get_element(self.tag_input_locator)
        self.btn_add = super().get_element(self.btn_add_locator)
        self.remove_tag = super().get_element(self.remove_tag_locator)
        self.close_btn = super().get_element(self.close_btn_locator)
