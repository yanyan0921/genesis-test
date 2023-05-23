from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/jobs/0/new/?type=job"
    sel_comp_name_locator = (By.CSS_SELECTOR,".currency_KpwQQJiF .triangle_20fmw_FF")
    button_comp_name_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div/div")
    create_comp_name_locator = (By.XPATH, "//div[@class='create-icon_3ApW6CeN']")
    input_job_name_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[2]/div[2]/div/input")
    icon_job_class_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[3]/div[2]/div[1]/button/div/div[2]")
    select_job_class_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]")
    input_spot_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[4]/div[2]/div/div/div/input")
    click_spot_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[4]/div[2]/div/div/div/input")
    input_skill_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[6]/div[2]/div/div/div/input")
    click_skill_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[6]/div[2]/div/div/div/input")
    icon_experience_class_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[7]/div[2]/button")
    select_experience_class_locator = (By.XPATH, "//div[@value=\"professional\"]")
    input_email_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[11]/div[2]/div/input")

    input_question1_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[1]/div[1]/div/input")
    link_add_question_locator = (By.LINK_TEXT,"Add new question")

    btn_question2_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[1]/div[2]/button")
    input_question2_locator =(By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[2]/div[1]/div/input")
    sel_multiple_choice_locator =(By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[1]/div[2]/div/div/div[2]")
    input_option11_locator =(By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[1]/div[3]/div/div/div[2]/div/input")
    btn_add_option1_locator =(By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[1]/div[3]/a/button")
    input_option21_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/input")

    input_question3_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[3]/div[1]/div/input")
    btn_question3_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[3]/div[2]/button")
    sel_checkBoxes_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[1]/div[2]/div/div/div[3]")
    input_option12_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[3]/div[3]/div[1]/div/div[2]/div/input")
    btn_add_option2_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[3]/div[3]/a/button")
    input_option22_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[13]/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/input")

    div_job_content_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[14]/div/div[2]/div/div/div/div/div/div")
    input_job_content_locator =(By.CSS_SELECTOR,".notranslate")
    btn_post_locator = (By.XPATH, "//button[@class='raised-btn_2vTjL538 raised-btn-primary_MYOE9bp7 create_1RHQCipa GA_btn_jobForm_post_job']")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.sel_comp_name = None
        self.button_comp_name = None
        self.create_comp_name = None
        self.input_job_name = None
        self.icon_job_class = None
        self.select_job_class = None
        self.input_spot = None
        self.click_spot = None
        self.input_skill = None
        self.click_skill = None
        self.icon_experience_class = None
        self.select_experience_class = None
        self.input_email = None
        self.div_job_content = None
        self.input_email = None
        self.div_job_content = None
        self.input_job_content = None
        self.btn_post = None

        self.input_question1 = None
        self.link_add_question = None

        self.input_question2 = None
        self.btn_question2 = None
        self.sel_multiple_choice = None
        self.input_option11 = None
        self.btn_add_option1 = None
        self.input_option21= None

        self.input_question3 = None
        self.btn_question3 = None
        self.sel_checkBoxes = None
        self.input_option12 = None
        self.btn_add_option2 = None
        self.input_option22 = None






        self.present_locator = self.btn_post_locator

    def init_elements(self):
        super().init_elements()
        self.sel_comp_name = super().get_element(self.sel_comp_name_locator)
        self.button_comp_name = super().get_element(self.button_comp_name_locator)
        self.create_comp_name = super().get_element(self.create_comp_name_locator)
        self.input_job_name = super().get_element(self.input_job_name_locator)
        self.icon_job_class = super().get_element(self.icon_job_class_locator)
        self.select_job_class = super().get_element(self.select_job_class_locator)
        self.input_spot = super().get_element(self.input_spot_locator)
        self.click_spot = super().get_element(self.click_spot_locator)
        self.input_skill = super().get_element(self.input_skill_locator)
        self.click_skill = super().get_element(self.click_skill_locator)
        self.icon_experience_class = super().get_element(self.icon_experience_class_locator)
        self.select_experience_class = super().get_element(self.select_experience_class_locator)
        self.input_email = super().get_element(self.input_email_locator)
        self.div_job_content = super().get_element(self.div_job_content_locator)
        self.input_job_content = super().get_element(self.input_job_content_locator)
        self.btn_post = super().get_element(self.btn_post_locator)

        self.input_question1 = super().get_element(self.input_question1_locator)
        self.link_add_question  = super().get_element(self.link_add_question_locator)

        self.btn_question2 = super().get_element(self.btn_question2_locator)
        self.input_question2 = super().get_element(self.input_question2_locator)
        self.sel_multiple_choice = super().get_element(self.sel_multiple_choice_locator)
        self.input_option11 = super().get_element(self.input_option11_locator)
        self.btn_add_option1 = super().get_element(self.btn_add_option1_locator)
        self.input_option21 = super().get_element(self.input_option21_locator)

        self.input_question3 = super().get_element(self.input_question3_locator)
        self.btn_question3 = super().get_element(self.btn_question3_locator)
        self.sel_checkBoxes = super().get_element(self.sel_checkBoxes_locator)
        self.input_option12 = super().get_element(self.input_option12_locator)
        self.btn_add_option2 = super().get_element(self.btn_add_option2_locator)
        self.input_option22 = super().get_element(self.input_option22_locator)
