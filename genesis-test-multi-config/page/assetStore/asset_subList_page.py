from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    share_btn_locator = (By.CSS_SELECTOR, "[class = '_3UE3J ZQFsR auto _2PAai']")
    edit_btn_locator = (By.CSS_SELECTOR, "[class = '_3UE3J ZQFsR auto _3kYVA']")
    assetName_locator = (
    By.XPATH, "//*[@id=\"main-layout-scroller\"]/div/div[1]/div[2]/div/div[2]/div/div[1]/div/a/div[2]/div[2]/div")
    delete_list_locator = (By.CSS_SELECTOR, "[class = '_1lTqV']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.share_btn = self.share_btn_locator
        self.edit_btn = self.edit_btn_locator
        self.assetName = self.assetName_locator
        self.delete_list = None
        self.present_locator = self.edit_btn_locator

    def init_elements(self):
        super().init_elements()
        self.share_btn = super().get_element(self.share_btn_locator)
        self.edit_btn = super().get_element(self.edit_btn_locator)
        self.assetName = super().get_element(self.assetName_locator)
        self.delete_list = super().get_element(self.delete_list_locator)
