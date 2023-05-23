from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    title_txt_locator =(By.CLASS_NAME,"title_UXz7qZxQ")
    div_txt_locator = (By.XPATH,"//div[@id='pageBody']/div/div/div/div[5]/div[2]/div")
    input_txt_locator = (By.CSS_SELECTOR,".hide_H_UwDxpB")
    select_project1_locator = (By.XPATH,"//div[@class='projects_beGZFyS4']/div/div/div/button")
    select_project2_locator = (By.XPATH,"//div[@class='projects_beGZFyS4']/div[2]/div/div/button")
    select_project3_locator = ( By.XPATH, "//div[@class='projects_beGZFyS4']/div[3]/div/div/button")
    button_apply_job_locator = ( By.XPATH, "//button[@class=\"raised-btn_2vTjL538 raised-btn-thirdly_QAfXf1ST apply_13JavH_R\"]")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.title_txt = None
        self.div_txt = None
        self.input_txt = None
        self.select_project1 = None
        self.select_project2 = None
        self.select_project3 = None
        self.button_apply_job = None
        self.present_locator = self.button_apply_job_locator


    def init_elements(self):
        super().init_elements()
        self.title_txt = super().get_element(self.title_txt_locator)
        self.div_txt = super().get_element(self.div_txt_locator)
        self.input_txt = super().get_element(self.input_txt_locator)
        self.select_project1 = super().get_element(self.select_project1_locator)
        self.select_project2 = super().get_element(self.select_project2_locator)
        self.select_project3 = super().get_element(self.select_project3_locator)
        self.button_apply_job = super().get_element(self.button_apply_job_locator)