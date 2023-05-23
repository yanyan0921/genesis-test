from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    # 选择文章
    btn_article_locator = (By.CSS_SELECTOR, '.card_1dBBoTqX:nth-child(1)')
    btn_game_locator = (By.CSS_SELECTOR, '.card_1dBBoTqX:nth-child(2)')
    btn_showcase_locator = (By.CSS_SELECTOR, '.card_1dBBoTqX:nth-child(3)')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_article = None
        self.btn_game = None
        self.btn_showcase = None
        self.present_locator = self.btn_article_locator

    def init_elements(self):
        super().init_elements()
        self.btn_article = super().get_element(self.btn_article_locator)
        self.btn_game = super().get_element(self.btn_game_locator)
        self.btn_showcase = super().get_element(self.btn_showcase_locator)
