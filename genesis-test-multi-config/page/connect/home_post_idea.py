from typing import Tuple

from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    div_input1_locator = (By.XPATH, "//div[@id='feed-top']/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div")
    div_input2_locator = (By.CSS_SELECTOR, "/html/body/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div")
   #input_idea_locator = (By.XPATH, "//div[@id='feed-top']/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div")
    input_idea_locator = (By.CSS_SELECTOR, ".notranslate")
    button_idea_pic_locator = (By.XPATH,"//button[@class=\"menu-button_1pxU6I-v image_1mBsqimj\"]")
    input_pic_locator = (By.XPATH,"//input[@type='file']")
    input_pic_add_locator = (By.CLASS_NAME,"attachment-new_3siY2RgT")
    input_pic2_locator = (By.XPATH, "//input[@type='file']")
    cancel_pic_locator = (By.XPATH ,"//div[@id='feed-top']/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div[2]/button/div")
    verify_pic_count_locator = (By.CLASS_NAME,"text_2IdsEZSR")
    btn_post_locator = (By.CSS_SELECTOR, ".raised-btn-blue_37QDrHj0")
    icon_job_locator = (By.XPATH, "//*[@id=\"feed-top\"]/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/button[1]")
    icon_article_locator = (By.XPATH, "//*[@id=\"feed-top\"]/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/button[2]")
    icon_game_locator = (By.XPATH, "//*[@id=\"feed-top\"]/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/button[3]")
    icon_showcase_locator = (By.XPATH, "//*[@id=\"feed-top\"]/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/button[4]")
    #评论
    btn_comment_locator = (By.XPATH,"//div[@class=\"icon_2ylAPi56 ifont ifont-material-outline-mode_comment\"]")
    #编辑
    icon_menu_locator = (By.XPATH,"//div[@class=\"left-container_3Y3AANwf\"]/div[2]/div/div/div/div/div/div/div[4]")
    icon_edit_locator = (By.XPATH,"//div[@class=\"left-container_3Y3AANwf\"]/div[2]/div/div/div/div/div/div/div[4]/div/div/div[3]/div/div")
    icon_delete_locator = (By.XPATH,"//div[@class=\"left-container_3Y3AANwf\"]/div[2]/div/div/div/div/div/div/div[4]/div/div/div[3]/div[2]/div")
    div_modify_locator = (By.XPATH,"//*[@id=\"feed-top\"]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/div")
    input_modify_locator=(By.XPATH,"//*[@id=\"feed-top\"]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/div/span/span")
    btn_save_locator = (By.CLASS_NAME,".raised-btn-blue_37QDrHj0")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.div_input1 = None
        self.div_input2 = None
        self.input_idea = None
        self.button_idea_pic = None
        self.input_pic = None
        self.input_pic_add = None
        self.input_pic2 = None
        self.cancel_pic = None
        self.verify_pic_count = None
        self.btn_post = None
        self.icon_job = None
        self.icon_article = None
        self.icon_game = None
        self.icon_showcase = None
        self.btn_comment = None
        self.icon_menu = None
        self.icon_edit = None
        self.icon_delete = None
        self.div_modify = None
        self.input_modify = None
        self.btn_save = None
        self.present_locator = self.div_input1_locator

    def init_elements(self):
        super().init_elements()
        self.div_input1 = super().get_element(self.div_input1_locator)
        self.div_input2 = super().get_element(self.div_input1_locator)
        self.input_idea = super().get_element(self.input_idea_locator)
        self.button_idea_pic = super().get_element(self.button_idea_pic_locator)
        self.input_pic = super().get_element(self.input_pic_locator)
        self.input_pic_add = super().get_element(self.input_pic_add_locator)
        self.input_pic2 = super().get_element(self.input_pic2_locator)
        self.cancel_pic = super().get_element(self.cancel_pic_locator)
        self.verify_pic_count = super().get_element(self.verify_pic_count_locator)
        self.btn_post = super().get_element(self.btn_post_locator)
        self.icon_job = super().get_element(self.icon_job_locator)
        self.icon_article = super().get_element(self.icon_article_locator)
        self.icon_game = super().get_element(self.icon_game_locator)
        self.icon_showcase = super().get_element(self.icon_showcase_locator)
        self.btn_comment = super().get_element(self.btn_comment_locator)
        self.icon_menu = super().get_element(self.icon_menu_locator)
        self.icon_edit = super().get_element(self.icon_edit_locator)
        self.icon_delete = super().get_element(self.icon_delete_locator)
        self.div_modify = super().get_element(self.div_modify_locator)
        self.input_modify = super().get_element(self.input_modify_locator)
        self.btn_save = super().get_element(self.btn_save_locator)