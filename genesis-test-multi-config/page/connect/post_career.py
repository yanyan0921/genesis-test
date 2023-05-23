from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/jobs/0/new"
    btn_task_locator = (By.XPATH, "//button[@class=\"raised-btn_2vTjL538 raised-btn-primary_MYOE9bp7 post_l3N_Kckn GA_btn_decision_postTask\"]")
    btn_job_locator = (By.XPATH, "//button[@class=\"raised-btn_2vTjL538 raised-btn-primary_MYOE9bp7 post_l3N_Kckn GA_btn_decision_postJob\"]")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_task = None
        self.btn_job = None
        self.present_locator = self.btn_job_locator


    def init_elements(self):
        super().init_elements()
        self.btn_task = super().get_element(self.btn_task_locator)
        self.btn_job = super().get_element(self.btn_job_locator)