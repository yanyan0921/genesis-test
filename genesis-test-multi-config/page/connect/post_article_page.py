from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    div_article_title_locator = (By.XPATH,
                                 "//div[@id=\"Project/CreateV2Controller\"]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div")
    input_article_title_locator = (By.CSS_SELECTOR, ".title-wrap_2oXf8ZMG .public-DraftEditor-content")
    div_article_header_locator = (By.XPATH,
                                  "//div[@id=\"Project/CreateV2Controller\"]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/div")
    input_article_header_locator = (By.CSS_SELECTOR, ".subTitle-wrap_1vjY-uGP .public-DraftEditor-content")
    div_article_content_locator = (By.XPATH,
                                   "//div[@id='Project/CreateV2Controller']/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div/div/div/div/div/div/div/div[3]/div")
    input_article_content_locator = (By.CSS_SELECTOR, ".notranslate")
    div_add_plus_locator = (By.XPATH,"//*[@id=\"Project/CreateV2Controller\"]/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div/div[3]/div")
    btn_image_locator =(By.XPATH,"//*[@id=\"Project/CreateV2Controller\"]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[3]/div/div[3]/div[1]")
    input_image_locator = (By.XPATH, "//input[@type='file']")
    btn_upload_locator = (By.XPATH,"//button[@class='button_1SQc1Jkf upload_3HZpDKk6']")
    btn_embed_locator = (By.XPATH,"//button[@class='button_1SQc1Jkf video_3bVK-Jhh']")
    input_upload_locator = (By.XPATH,"//button[@class='button_1SQc1Jkf upload_3HZpDKk6']/input")
    btn_bgground_locator = (By.XPATH, "//button[@class='raised-btn_2vTjL538 raised-btn-transparent_2agQEVMe size-medium_3tC1AZkh']")
    input_bgground_locator = (By.XPATH, "//input[@type='file']")
    add_thumbnail_locator =(By.CLASS_NAME,"thumbnail-empty_1a-rSXkp")
    input_thumbnail_locator = (By.XPATH,"//input[@type='file']")
    link_add_contributor_locator = (By.XPATH,"//*[@id=\"Project/CreateV2Controller\"]/div/div[2]/div/div[2]/div/div[1]/div/div/div[3]/div[3]/button/div[1]")
    link_add_tag_locator =(By.XPATH,"//*[@id=\"Project/CreateV2Controller\"]/div/div[2]/div/div[2]/div/div[1]/div/div/div[4]/div[3]/button/div[1]")
    link_add_website_locator_locator = (By.XPATH,"//*[@id=\"Project/CreateV2Controller\"]/div/div[2]/div/div[2]/div/div[1]/div/div/div[5]/div[3]/button/div[1]")
    btn_post_locator = (By.XPATH, "//div[@id='project-post']/button")
    btn_post_succeed_locator = (By.XPATH, "//*[@id=\"project-post\"]/div/div/div/div[1]/div/div[4]/button")
    label_error_msg_locator = (By.CLASS_NAME,"message_FGvdUVbA")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.div_article_title = None
        self.input_article_title = None
        self.div_article_header = None
        self.input_article_header = None
        self.div_article_content = None
        self.input_article_content = None
        self.div_add_plus = None
        self.btn_image = None
        self.input_image = None
        self.btn_upload = None
        self.btn_embed = None
        self.input_upload = None
        self.btn_bgground = None
        self.input_bgground = None
        self.add_thumbnail = None
        self.input_thumbnail = None
        self.link_add_contributor = None
        self.link_add_tag = None
        self.link_add_website = None
        self.btn_post = None
        self.btn_post_succeed = None
        self.label_error_msg = None
        self.present_locator = self.btn_post_locator

    def init_elements(self):
        super().init_elements()
        self.div_article_title = super().get_element(self.div_article_title_locator)
        self.input_article_title = super().get_element(self.input_article_title_locator)
        self.div_article_header = super().get_element(self.div_article_header_locator)
        self.input_article_header = super().get_element(self.input_article_header_locator)
        self.div_article_content = super().get_element(self.div_article_content_locator)
        self.input_article_content = super().get_element(self.input_article_content_locator)
        self.div_add_plus = super().get_element(self.div_add_plus_locator)
        self.btn_image = super().get_element(self.btn_image_locator)
        self.input_image = super().get_element(self.input_image_locator)
        self.btn_upload = super().get_element(self.btn_upload_locator)
        self.btn_embed = super().get_element(self.btn_embed_locator)
        self.input_upload = super().get_element(self.input_upload_locator)
        self.btn_bgground = super().get_element(self.btn_bgground_locator)
        self.input_bgground = super().get_element(self.input_bgground_locator)
        self.add_thumbnail = super().get_element(self.add_thumbnail_locator)
        self.input_thumbnail = super().get_element(self.input_thumbnail_locator)
        self.link_add_contributor = super().get_element(self.input_upload_locator)
        self.btn_bgground = super().get_element(self.btn_bgground_locator)
        self.input_bgground = super().get_element(self.input_bgground_locator)
        self.btn_post = super().get_element(self.btn_post_locator)
        self.btn_post_succeed = super().get_element(self.btn_post_succeed_locator)
        self.label_error_msg = super().get_element(self.label_error_msg_locator)
