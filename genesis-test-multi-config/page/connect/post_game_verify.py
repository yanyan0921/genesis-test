from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    text_game_verify_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/span/span")
    agree_post_locator = (By.XPATH,"//div[@class='button-wrap_2jwj_YrC']/button")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.text_game_verify = None
        self.agree_post = None
        self.present_locator = self.agree_post_locator

    def init_elements(self):
        super().init_elements()
        self.text_game_verify = super().get_element(self.text_game_verify_locator)
        self.agree_post = super().get_element(self.agree_post_locator)

