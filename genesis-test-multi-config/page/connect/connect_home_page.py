from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    btn_avatar_locator = (By.XPATH, "//div[@id='pageContent']/div/div[4]/div/div[2]/div/div[2]/div[2]/a")
    btn_sign_in_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[1]/div[4]/div/div[3]/div/div[3]/div[2]/div/div/div[2]/a[2]")
    frame_login_locator = (By.ID, "iFrameResizer0")
    input_email_locator = (By.ID, "conversations_create_session_form_email")
    input_password_locator = (By.ID, "conversations_create_session_form_password")
    btn_login_locator = (By.NAME, "commit")
    btn_post_project_locator = (By.XPATH,"//a[@class=\"link_1vCaVFnC GA_btn_header_postProject\"]")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_avatar = None
        self.btn_sign_in = None
        self.frame_login = None
        self.input_email = None
        self.input_password = None
        self.btn_login = None
        self.btn_post_project = None
        self.present_locator = self.btn_post_project_locator

    def init_elements(self):
        super().init_elements()
        self.btn_avatar = super().get_element(self.btn_avatar_locator)
        self.btn_sign_in = super().get_element(self.btn_sign_in_locator)
        self.frame_login = super().get_element(self.frame_login_locator)
        self.input_email = super().get_element(self.input_email_locator)
        self.input_password = super().get_element(self.input_password_locator)
        self.btn_login = super().get_element(self.btn_login_locator)
        self.btn_post_project = super().get_element(self.btn_post_project_locator)
