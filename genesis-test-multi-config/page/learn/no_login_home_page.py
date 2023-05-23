from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://learn-int.unity.com/"
    cookies_bar_locator = (By.XPATH, "//*[@id='onetrust-banner-sdk']/div/div")
    accept_cookies_btn_locator = (By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
    dismiss_btn_locator = (
        By.XPATH, "//*[@id='pageContent']/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[4]/div[1]/button")
    browse_btn_locator = (
        By.XPATH, "//*[@id='pageBody']/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[1]/div/div")
    tutorial_tab_locator = (
        By.XPATH, "//*[@id='pageBody']/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[2]/div/div/div/div[3]/div[1]/div[5]")
    tutorial_card_elem_locator = (
        By.XPATH, "//*[@id='pageBody']/div[1]/div[2]/div/div[3]/div[1]/div[3]/div[2]/div/div/div/div[3]/div[3]/div["
                  "1]/a/div/div[3] ")
    sign_in_btn_locator = (
        By.XPATH, "//*[@id='pageBody']/div[2]/div[1]/div/div[2]/div/button")
    language_select_btn_locator = (
        By.XPATH, "//*[@id='pageBody']/div[3]/div/div[2]/div[2]/div/div/button")
    language_option_btn_locator = (
        By.XPATH, "//*[@id='pageBody']/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.accept_cookies_btn = None
        self.dismiss_btn = None
        self.browse_btn = None
        self.tutorial_tab = None
        self.tutorial_card_elem = None
        self.sign_in_btn = None
        self.language_select_btn = None
        self.language_option_btn = None
        self.present_locator = self.cookies_bar_locator

    def init_elements(self):
        super().init_elements()
        self.accept_cookies_btn = self.get_element(self.accept_cookies_btn_locator)
        self.dismiss_btn = self.get_element(self.dismiss_btn_locator)
        self.browse_btn = self.get_element(self.browse_btn_locator)
        self.tutorial_tab = self.get_element(self.tutorial_tab_locator)
        self.tutorial_card_elem = self.get_element(self.tutorial_card_elem_locator)
        self.sign_in_btn = self.get_element(self.sign_in_btn_locator)
        self.language_select_btn = self.get_element(self.language_select_btn_locator)
        self.language_option_btn = self.get_element(self.language_option_btn_locator)
