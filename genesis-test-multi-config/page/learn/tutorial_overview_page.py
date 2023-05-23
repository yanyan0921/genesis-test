from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://learn-int.unity.com/tutorial/create-your-first-unity-project-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1"
    comment_locator = (
        By.XPATH, "//*[@id='pageBody']/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/a[2]")
    comment_icon_locator = (
        By.XPATH, "//*[@id='pageBody']/div[4]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]")
    general_sign_in_comment_locator = (
        By.XPATH, "//*[@id='pageBody']/div[4]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]")
    sign_in_to_comment_locator = (
        By.XPATH, "//div[@id='pageBody']/div[4]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]")
    blue_bar_locator = (By.XPATH, "//*[@id='pageBody']/div[2]/div[2]/div/div[1]/div[5]")
    blue_bar_login_locator = (By.XPATH, "//*[@id='pageBody']/div[2]/div[2]/div/div[1]/div[5]/div/div[2]/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.comment = None
        self.comment_icon = None
        self.general_sign_in_comment = None
        self.sign_in_to_comment = None
        self.blue_bar_login = None
        self.present_locator = self.blue_bar_locator

    def init_elements(self):
        super().init_elements()
        self.comment = super().get_element(self.comment_locator)
        self.comment_icon = super().get_element(self.comment_icon_locator)
        self.general_sign_in_comment = super().get_element(self.general_sign_in_comment_locator)
        self.sign_in_to_comment = super().get_element(self.sign_in_to_comment_locator)
        self.blue_bar_login = super().get_element(self.blue_bar_login_locator)
