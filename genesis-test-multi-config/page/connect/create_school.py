from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    btn_bgground_locator = (By.XPATH, "//div[@id='pageBody']/div/div/div/button")
    input_bgground_locator = (By.CSS_SELECTOR, ".hide_1NU8pgfD")
    btn_save_locator = (By.XPATH,"//button[@class='raised-btn_2vTjL538 raised-btn-primary_MYOE9bp7 button_tbfK590K']")
    error_bgground_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[1]/div/div[4]")
    div_camera_locator = (By.CSS_SELECTOR, ".camera_3E0m4BTH")
    input_camera_locator = (By.CSS_SELECTOR, ".hide_3N_qgKYS")
    error_camera_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[1]/div/div[3]")
    btn_picture_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[3]/div/div[2]/div/div/div[1]/div/div/div[3]/button")
    school_name_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[1]/div[2]/div/div/input")
    error_name_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]")
    thumbnail_change_locator = (By.CSS_SELECTOR,".change_1jRCWfsk")
    thumbnail_input_locator = (By.CSS_SELECTOR,".hide_2RMws7Hd")
    error_thumbnail_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[2]/div[2]/div")
    description_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[3]/div[2]/div/textarea")
    error_description_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[3]/div[2]/div/div")
    input_email_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[4]/div[2]/div/input")
    input_website_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[5]/div[2]/div/input")
    error_website_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[5]/div[2]/div[2]")
    input_location_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[6]/div[2]/div/div/div/input")
    error_location_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[6]/div[2]/div/div/div[2]")
    btn_create_locator = (By.XPATH, "//button[@class='raised-btn_2vTjL538 raised-btn-primary_MYOE9bp7 create_1azIassC']")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_bgground = None
        self.input_bgground = None
        self.btn_save = None
        self.error_bgground = None
        self.div_camera = None
        self.input_camera = None
        self.error_camera = None
        self.btn_picture = None
        self.school_name = None
        self.error_name = None
        self.thumbnail_change = None
        self.thumbnail_input = None
        self.error_thumbnail = None
        self.description = None
        self.error_description = None
        self.input_email = None
        self.input_website = None
        self.error_website = None
        self.input_location = None
        self.error_location = None
        self.btn_create = None
        self.present_locator = self.btn_create_locator


    def init_elements(self):
        super().init_elements()
        self.btn_bgground = super().get_element(self.btn_bgground_locator)
        self.input_bgground = super().get_element(self.input_bgground_locator)
        self.btn_save = super().get_element(self.btn_save_locator)
        self.error_bgground = super().get_element(self.error_bgground_locator)
        self.div_camera = super().get_element(self.div_camera_locator)
        self.input_camera = super().get_element(self.input_camera_locator)
        self.error_camera = super().get_element(self.error_camera_locator)
        self.btn_picture = super().get_element(self.btn_picture_locator)
        self.school_name = super().get_element(self.school_name_locator)
        self.error_name = super().get_element(self.error_name_locator)
        self.thumbnail_change = super().get_element(self.thumbnail_change_locator)
        self.thumbnail_input = super().get_element(self.thumbnail_input_locator)
        self.error_thumbnail = super().get_element(self.error_thumbnail_locator)
        self.description = super().get_element(self.description_locator)
        self.error_description = super().get_element(self.error_description_locator)
        self.input_email = super().get_element(self.input_email_locator)
        self.input_website = super().get_element(self.input_website_locator)
        self.error_website = super().get_element(self.error_website_locator)
        self.input_location = super().get_element(self.input_location_locator)
        self.error_location = super().get_element(self.error_location_locator)
        self.btn_create = super().get_element(self.btn_create_locator)
     