from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/search"
    search_button_locator = (By.CLASS_NAME,"search-button_2PPlNam3")
    nav_all_locator = (By.XPATH,"//*[@id=\"pageBody\"]/div/div[1]/div/div[2]/div/div/div/button[1]")
    nav_talent_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[1]/div/div[2]/div/div/div/button[2]")
    nav_group_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[1]/div/div[2]/div/div/div/button[3]")
    nav_jobs_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[1]/div/div[2]/div/div/div/button[4]")
    nav_projects_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[1]/div/div[2]/div/div/div/button[5]")
    nav_companies_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[1]/div/div[2]/div/div/div/button[6]")
    nav_schools_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[1]/div/div[2]/div/div/div/button[7]")
    nav_channels_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[1]/div/div[2]/div/div/div/button[8]")
    input_search_locator = (By.XPATH,'//*[@id="pageBody"]/div/div[1]/div/div[1]/div/div[1]/div/div/input')
    icon_search_locator =(By.XPATH,"//a[@class=\"search-icon_L61rVVxd ifont ifont-material-baseline-search\"]")
    result_search_project_locator = (By.CLASS_NAME,"title_1AvouMao")
    result_search_groups_locator = (By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/a[1]/div[2]/div[1]")
    result_search_company_locator = (By.XPATH,"/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/a/div[2]/div[1]")
    result_search_channels_locator = (By.XPATH, "//*[@id=\"pageBody\"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div")
    result_search_school_locator = (By.CLASS_NAME, "name_1cvUu70f")
    result_search_talent_locator = ( By.XPATH, "//div[@class=\"user_2_-HpI-V\"]/div/a")
    result_search_job_locator = (By.CLASS_NAME,"job-title_2t2Xp08X")
    click_test3_locator = (By.CLASS_NAME,"title_3JPBhCh8")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.search_button = None
        self.nav_all = None
        self.nav_talent = None
        self.nav_group = None
        self.nav_jobs = None
        self.nav_projects = None
        self.nav_companies = None
        self.nav_schools = None
        self.nav_channels = None
        self.input_search = None
        self.icon_search = None
        self.result_search_project = None
        self.result_search_groups = None
        self.result_search_company = None
        self.result_search_channels = None
        self.result_search_school = None
        self.result_search_talent = None
        self.result_search_job = None
        self.click_test3 = None
        self.present_locator = self.search_button_locator

    def init_elements(self):
        super().init_elements()
        self.search_button = super().get_element(self.search_button_locator)
        self.nav_all = super().get_element(self.nav_all_locator)
        self.nav_talent = super().get_element(self.nav_talent_locator)
        self.nav_group = super().get_element(self.nav_group_locator)
        self.nav_jobs = super().get_element(self.nav_jobs_locator)
        self.nav_projects = super().get_element(self.nav_projects_locator)
        self.nav_companies = super().get_element(self.nav_companies_locator)
        self.nav_schools = super().get_element(self.nav_schools_locator)
        self.nav_channels = super().get_element(self.nav_channels_locator)
        self.input_search = super().get_element(self.input_search_locator)
        self.icon_search = super().get_element(self.icon_search_locator)
        self.result_search_project = super().get_element(self.result_search_project_locator)
        self.result_search_groups = super().get_element(self.result_search_groups_locator)
        self.result_search_company = super().get_element(self.result_search_company_locator)
        self.result_search_channels = super().get_element(self.result_search_channels_locator)
        self.result_search_school = super().get_element(self.result_search_school_locator)
        self.result_search_talent = super().get_element(self.result_search_talent_locator)
        self.result_search_job = super().get_element(self.result_search_job_locator)
        self.click_test3 = super().get_element(self.click_test3_locator)