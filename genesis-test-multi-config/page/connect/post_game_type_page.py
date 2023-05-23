from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    # 选择文章
    webGL_game_locator = (By.LINK_TEXT, 'Post a WebGL game')
    video_game_locator = (By.LINK_TEXT, 'Post a game with images or videos')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.webGL_game = None
        self.video_game = None
        self.present_locator = self.webGL_game_locator

    def init_elements(self):
        super().init_elements()
        self.webGL_game = super().get_element(self.webGL_game_locator)
        self.video_game = super().get_element(self.video_game_locator)
