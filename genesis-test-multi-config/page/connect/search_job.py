from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/jobs"
    sel_task_name_locator = (By.LINK_TEXT, "test task")
    input_search_locator = (By.XPATH,"/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/input")
    icon_search_locator = (By.XPATH,"//div[@class=\"search-icon_WW-xLsIp ifont ifont-search\"]")
    result_search_locator = (By.CLASS_NAME,"name_qedMhkTg")
    div_job_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div/div/div[3]/div[3]/div/div/div")
    button_apply_job_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div/div/div[3]/div[3]/div/div/div/div[2]/div/button")
    nav_applied_locator =(By.XPATH,"//*[@id=\"pageBody\"]/div/div/div/div[2]/div[1]/div/div[1]/a[3]/div[1]")
    job_title_locator =(By.LINK_TEXT,"Automotive Software Programmer")
    icon_bookmark_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div/div/div[3]/div[3]/div/div/div/div[1]/button[1]/div/div")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.sel_task_name = None
        self.input_search = None
        self.icon_search = None
        self.result_search = None
        self.div_job = None
        self.button_apply_job = None
        self.nav_applied = None
        self.job_title = None
        self.icon_bookmark = None
        self.present_locator = self.input_search_locator


    def init_elements(self):
        super().init_elements()
        self.input_search = super().get_element(self.result_search_locator)
        self.sel_task_name = super().get_element(self.sel_task_name_locator)
        self.input_search = super().get_element(self.input_search_locator)
        self.icon_search = super().get_element(self.icon_search_locator)
        self.result_search = super().get_element(self.result_search_locator)
        self.div_job = super().get_element(self.div_job_locator)
        self.button_apply_job = super().get_element(self.button_apply_job_locator)
        self.nav_applied = super().get_element(self.nav_applied_locator)
        self.job_title = super().get_element(self.job_title_locator)
        self.icon_bookmark = super().get_element(self.icon_bookmark_locator)