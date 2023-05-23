from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    btn_bgground_locator = (By.CSS_SELECTOR, ".raised-btn-transparent_2agQEVMe")
    input_bgground_locator = (By.XPATH, "//input[@type='file']")
    div_game_title_locator = (By.XPATH,
                                 "//div[@id='Project/CreateV2Controller']/div/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div")
    input_game_title_locator = (By.CSS_SELECTOR, ".title-wrap_-ekColTs .public-DraftEditor-content")
    div_game_desc_locator = (By.XPATH,
                                  "//div[@id='Project/CreateV2Controller']/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div")
    input_game_desc_locator = (By.CSS_SELECTOR, ".desc-wrap_PnjADqsM .public-DraftEditor-content")
    btn_picture_locator = (By.XPATH, "//div[@class=\"button_dbLZhdMD\"]/button")
    input_picture_locator = (By.CSS_SELECTOR, ".hide_3lAUgXb9")
    btn_embed_locator = (By.CSS_SELECTOR,".raised-btn-white_eL_TEgAO")
    div_game_content_locator = (By.XPATH, "//div[@id='Project/CreateV2Controller']/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/div/div[5]/div")
    input_game_content_locator = (By.CSS_SELECTOR, ".notranslate")
    btn_thumbnail_locator = (By.CLASS_NAME, "upload-thumbnail-body_2LjUgX23")
    input_thumbnail_locator = (By.XPATH, "//input[@type='file']")
    btn_post_locator = (By.XPATH, "//div[@id='project-post']/button")
    label_error_msg_locator = (By.CLASS_NAME, "message_FGvdUVbA")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_bgground = None
        self.input_bgground = None
        self.div_game_title = None
        self.input_game_title = None
        self.div_game_desc = None
        self.input_game_desc = None
        self.btn_embed = None
        self.btn_picture = None
        self.input_picture = None
        self.div_game_content = None
        self.input_game_content = None
        self.btn_post = None
        self.label_error_msg = None
        self.present_locator = self.btn_post_locator

    def init_elements(self):
        super().init_elements()
        self.btn_bgground = super().get_element(self.btn_bgground_locator)
        self.input_bgground = super().get_element(self.input_bgground_locator)
        self.div_game_title = super().get_element(self.div_game_title_locator)
        self.input_game_title = super().get_element(self.input_game_title_locator)
        self.div_game_desc = super().get_element(self.div_game_desc_locator)
        self.input_game_desc = super().get_element(self.input_game_desc_locator)
        self.btn_embed = super().get_element(self.btn_embed_locator)
        self.btn_picture = super().get_element(self.btn_picture_locator)
        self.input_picture = super().get_element(self.input_picture_locator)
        self.div_game_content = super().get_element(self.div_game_content_locator)
        self.input_game_content = super().get_element(self.input_game_content_locator)
        self.btn_post = super().get_element(self.btn_post_locator)
        self.label_error_msg = super().get_element(self.label_error_msg_locator)
