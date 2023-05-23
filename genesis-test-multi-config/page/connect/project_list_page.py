from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    div_article_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/a")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.div_article = None
        self.present_locator = self.div_article_locator

    def init_elements(self):
        super().init_elements()
        self.div_article = super().get_element(self.div_article_locator)
