from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    input_YouTubelink_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[8]/div/div[3]/div[2]/div/div/div/div[2]/div[1]/div/div/input")
    icon_closeYouTubelinkifont_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[8]/div/div[3]/div[2]/div/div/div/div[1]/button/div")
    btn_deleteYouTube_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[8]/div/div[3]/div[2]/div/div/div/div[3]/div[1]/div/div[2]/div/div[2]/div[2]/a")
    btn_OKYouTube_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[8]/div/div[3]/div[2]/div/div/div/div[4]/div/button")
    icon_language_dropdown_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div[4]/div[3]/div/button/div/div[2]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_YouTubelink = None
        self.icon_closeYouTubelinkifont = None
        self.btn_deleteYouTube = None
        self.btn_OKYouTubee = None
        self.present_locator = self.icon_language_dropdown_locator

    def init_elements(self):
        super().init_elements()
        self.input_YouTubelink = super().get_element(self.input_YouTubelink_locator)
        self.icon_closeYouTubelinkifont = super().get_element(self.icon_closeYouTubelinkifont_locator)
        self.btn_deleteYouTube = super().get_element(self.btn_deleteYouTube_locator)
        self.btn_OKYouTube = super().get_element(self.btn_OKYouTube_locator)
        self.icon_language_dropdown = super().get_element(self.icon_language_dropdown_locator)
