from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    div_troubleshooting_locator = (By.XPATH,"//div[@class=\"content_2p10Yz92\"]/div")
    summarize_problem_locator = (By.XPATH,"//div[@class=\"text-input_1zwaVtSr text-input_2q6p8KHa theme-dark_2f3h2N29\"]/div/input")
    description_problem_locator = (By.XPATH,"//div[@class=\"textarea-box_1isekI-W\"]/div/textarea")
    unity_version_locator = (By.XPATH,"//button[@class=\"currentText_15f1QOEr select-list-button_2mrqCuUg error-border_l1TDgMzh\"]")
    select_version_locator = (By.XPATH,"//div[@class=\"selects_2ppiVyIj\"]/div[3]")
    div_shootscreen_locator = (By.CLASS_NAME,"add-attachment-wrapper_tBVyIPug")
    input_shootscreen_locator = (By.XPATH,"//div[@class=\"add-attachment-wrapper_tBVyIPug\"]/input")
    div_category_locator = (By.XPATH,"//div[@class=\"select-default-wrap_QdE63_vL\"]/div[5]/div/div")
    look_expert_locator = (By.XPATH,'//*[@id="pageBody"]/div/div[1]/div[7]/div/div[2]/div/div[2]/div[2]/div[5]/div')
    btn_language_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[1]/div[9]/div/div[2]/div/button")
    select_language_locator = (By.XPATH,'//*[@id="pageBody"]/div/div[1]/div[9]/div/div[2]/div/div/div/div[1]/div/div[3]')
    prize_one_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[1]/div[10]/div[2]/div/div/a[1]")
    btn_sumbit_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[1]/div[11]/button")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.div_troubleshooting = None
        self.summarize_problem= None
        self.description_problem = None
        self.unity_version = None
        self.select_version = None
        self.div_shootscreen = None
        self.input_shootscreen = None
        self.input_display_picture = None
        self.icon_class = None
        self.select_class = None
        self.url = None
        self.hoster = None
        self.register_date = None
        self.link_challenge = None
        self.present_locator = self.div_troubleshooting_locator


    def init_elements(self):
        super().init_elements()
        self.get_livehelp = super().get_element(self.get_livehelp_locator)