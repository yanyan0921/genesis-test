from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/jobs?t=bookmarked"
    count_bookmarked_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div/div/div[2]/div[1]/div/div[1]/a[5]/div[2]")
    icon_bookmarked_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div/div/div[2]/div[1]/div/div[1]/a[5]/div[1]")
    button_bookmarked_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div/div/div[3]/div[3]/div/div/div/div/button/div/div")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.count_bookmarked = None
        self.icon_bookmarked = None
        self.button_bookmarked = None
        self.present_locator = self.icon_bookmarked_locator


    def init_elements(self):
        super().init_elements()
        self.count_bookmarked = super().get_element(self.count_bookmarked_locator)
        self.icon_bookmarked = super().get_element(self.icon_bookmarked_locator)
        self.button_bookmarked = super().get_element(self.button_bookmarked_locator)