from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    div_showcase_title_locator = (By.XPATH,
                                 "//div[@id='Project/CreateV2Controller']/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div")
    input_showcase_title_locator = (By.CSS_SELECTOR, ".title-wrap_1hoswwPg .public-DraftEditor-content")
    btn_picture_locator = (By.CSS_SELECTOR, ".button_dbLZhdMD > .raised-btn-blue_37QDrHj0")
    input_picture_locator = (By.CSS_SELECTOR, ".hide_3lAUgXb9")
    btn_embed_locator = (By.XPATH,"//button[@class=\"raised-btn_2vTjL538 raised-btn-white_eL_TEgAO size-medium_3tC1AZkh width-full_2wWLBFy9\"]")
    div_showcase_content_locator = (By.CSS_SELECTOR, "div:nth-child(6) > .public-DraftStyleDefault-block")
    input_showcase_content_locator = (By.XPATH, "//div[@id='Project/CreateV2Controller']/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")
    btn_post_locator = (By.XPATH, "//div[@id='project-post']/button")
    btn_post_now_locator = (By.XPATH, "//div[@id='project-post']/div/div/div/div/div/div[4]/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.div_showcase_title = None
        self.input_showcase_title = None
        self.btn_picture = None
        self.input_picture = None
        self.btn_embed = None
        self.div_showcase_content = None
        self.input_showcase_content = None
        self.btn_post = None
        self.btn_post_now= None
        self.present_locator = self.btn_post_locator

    def init_elements(self):
        super().init_elements()
        self.div_showcase_title = super().get_element(self.div_showcase_title_locator)
        self.input_showcase_title = super().get_element(self.input_showcase_title_locator)
        self.btn_picture = super().get_element(self.btn_picture_locator)
        self.input_picture = super().get_element(self.input_picture_locator)
        self.btn_embed = super().get_element(self.btn_embed_locator)
        self.div_showcase_content = super().get_element(self.div_showcase_content_locator)
        self.input_showcase_content = super().get_element(self.input_showcase_content_locator)
        self.btn_post = super().get_element(self.btn_post_locator)
        self.btn_post_now = super().get_element(self.btn_post_now_locator)
