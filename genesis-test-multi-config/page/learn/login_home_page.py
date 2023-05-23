from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-next.unity.com/learn"
    navigate_browse_locator = (
        By.XPATH, "//*[@id='pageBody']/div[1]/div[2]/div/div[3]/div[1]/div[3]")
    profile_overview_locator = (By.XPATH, "//*[@id='pageBody']/div[2]/div[1]/div[1]")
    browse_tutorial_tab_locator = (
        By.XPATH, "//*[@id='pageBody']/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[2]/div/div/div/div[3]/div[1]/div[5]/a")
    browse_tutorial_card_locator = (
        By.XPATH, "//*[@id='pageBody']/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[2]/div/div/div/div[3]/div[3]/div[1]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.navigate_browse = None
        self.browse_tutorial_tab = None
        self.browse_tutorial_card = None
        self.present_locator = self.profile_overview_locator

    def init_elements(self):
        super().init_elements()
        self.navigate_browse = self.get_element(self.navigate_browse_locator)
        self.browse_tutorial_tab = self.get_element(self.browse_tutorial_tab_locator)
        self.browse_tutorial_card = self.get_element(self.browse_tutorial_card_locator)


