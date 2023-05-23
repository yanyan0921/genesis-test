from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    task_title_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[1]/div[2]/div/input")
    error_title_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[1]/div[2]/div[2]")
    icon_role_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[2]/div[1]/button/div/div[2]")
    select_role_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[12]")
    error_role_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[2]/div[2]")
    input_spot_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[3]/div[2]/div/div/div/input")
    click_spot_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[3]/div[2]/div/div/div/input")
    error_spot_locator =(By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[3]/div[2]/div/div/div[2]")
    radio_job_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[4]/div[2]/div[1]/div/button")
    icon_pay_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[5]/div[2]/button/div/div[2]")
    select_pay_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[5]/div[2]/div/div/div[3]")
    begin_money_locator = (By.XPATH, "//div[@id='pageBody']/div/div[2]/div[6]/div[2]/div/div/div/div/input")
    end_money_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[6]/div[2]/div[1]/div[3]/div[1]/div/input")
    icon_type_money_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[6]/div[2]/div[1]/div[4]/button/div/div[1]")
    select_type_money_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[6]/div[2]/div[1]/div[4]/div/div/div[1]/div/div[31]")
    error_money_locator =(By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[6]/div[2]/div[2]")
    input_skill_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[8]/div[2]/div/div/div/input")
    click_skill_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[8]/div[2]/div/div/div/input")
    error_skill_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[8]/div[2]/div/div/div[2]")
    div_task_content_locator = (By.XPATH, "//div[@id='pageBody']/div/div[2]/div[17]/div/div[2]/div/div/div/div/div/div")
    input_task_content_locator =(By.XPATH,"//div[@id='pageBody']/div/div[2]/div[17]/div/div[2]/div/div/div")
    btn_task_content_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[19]/div/button[1]")
    btn_post_locator = (By.XPATH,"//button[@class=\"raised-btn_2vTjL538 raised-btn-primary_MYOE9bp7 create_1RHQCipa GA_btn_jobForm_post_task\"]")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.task_title = None
        self.icon_role = None
        self.select_role = None
        self.input_spot = None
        self.click_spot = None
        self.radio_job = None
        self.icon_pay = None
        self.select_pay = None
        self.begin_money = None
        self.end_money = None
        self.icon_type_money = None
        self.select_type_money = None
        self.input_skill = None
        self.click_skill = None
        self.div_task_content = None
        self.input_task_content = None
        self.btn_post = None
        self.present_locator = self.btn_post_locator
    def init_elements(self):
        super().init_elements()
        self.task_title = super().get_element(self.task_title_locator)
        self.icon_role = super().get_element(self.icon_role_locator)
        self.select_role = super().get_element(self.select_role_locator)
        self.input_spot = super().get_element(self.input_spot_locator)
        self.click_spot = super().get_element(self.click_spot_locator)
        self.radio_job = super().get_element(self.radio_job_locator)
        self.icon_pay = super().get_element(self.icon_pay_locator)
        self.select_pay = super().get_element(self.select_pay_locator)
        self.begin_money = super().get_element(self.begin_money_locator)
        self.end_money = super().get_element(self.end_money_locator)
        self.icon_type_money = super().get_element(self.icon_type_money_locator)
        self.select_type_money = super().get_element(self.select_type_money_locator)
        self.input_skill = super().get_element(self.input_skill_locator)
        self.click_skill = super().get_element(self.click_skill_locator)
        self.div_task_content = super().get_element(self.div_task_content_locator)
        self.input_task_content = super().get_element(self.input_task_content_locator)
        self.btn_post = super().get_element(self.btn_post_locator)