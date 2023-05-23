from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    upload_icon_locator = (By.XPATH, "//*[@id=\"keyImageIconFile\"]")
    upload_card_locator = (By.XPATH,"//*[@id=\"keyImageSmallFile\"]")
    upload_cover_locator = (By.XPATH,"//*[@id=\"keyImageBigFile\"]")
    upload_social_locator = (By.XPATH,"//*[@id=\"socialImageFBFile\"]")

    go_Back_locator = (By.XPATH, "//*[@id=\"goBack\"]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.upload_icon = None
        self.upload_card = None
        self.upload_cover = None
        self.upload_social = None
        self.go_Back = None
        self.present_locator = self.go_Back_locator

    def init_elements(self):
        super().init_elements()
        self.upload_icon = super().get_element(self.upload_icon_locator)
        self.upload_card = super().get_element(self.upload_card_locator)
        self.upload_cover = super().get_element(self.upload_cover_locator)
        self.upload_social = super().get_element(self.upload_social_locator)
        self.go_Back = super().get_element(self.go_Back_locator)

