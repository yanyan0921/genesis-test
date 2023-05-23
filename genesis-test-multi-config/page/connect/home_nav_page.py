from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    btn_post_project_locator = (By.XPATH, "//a[@class=\"link_1vCaVFnC GA_btn_header_postProject\"]")
    icon_discover_locator = (By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[4]/div/div[2]/div/div[1]/div[1]/div[1]")
    icon_project_locator = (By.CLASS_NAME, "icon-wrapper_TPumiF4f")
    icon_jobs_locator = (By.XPATH,"/html/body/div[2]/div/div[1]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]")
    icon_group_locator = (By.XPATH, "//*[@id=\"pageContent\"]/div[1]/div[4]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/a[1]")
    icon_talent_locator = (By.CSS_SELECTOR, ".menu-wrap_2w_GvYUd .item_1xCevqmY:nth-child(2)")
    icon_LiveHelp_locator = (By.XPATH, "//a[contains(text(),'Live Help')]")
    icon_companies_locator = (By.CSS_SELECTOR, ".menu-wrap_2w_GvYUd .item_1xCevqmY:nth-child(4)")
    icon_schools_locator = (By.CSS_SELECTOR, ".menu-wrap_2w_GvYUd .item_1xCevqmY:nth-child(5)")
    icon_channels_locator = (By.CSS_SELECTOR, ".menu-wrap_2w_GvYUd .item_1xCevqmY:nth-child(6)")
    icon_challenges_locator = (By.CSS_SELECTOR, ".menu-wrap_2w_GvYUd .item_1xCevqmY:nth-child(7)")
    icon_events_locator = (By.CSS_SELECTOR, ".menu-wrap_2w_GvYUd .item_1xCevqmY:nth-child(8)")
    icon_connections_locator = (By.CSS_SELECTOR, ".menu-wrap_2w_GvYUd .item_1xCevqmY:nth-child(9)")
    icon_articles_locator = (By.CSS_SELECTOR, ".menu-wrap_3QAHkrqg .item_1xCevqmY:nth-child(1)")
    icon_showcases_locator = (By.CSS_SELECTOR, ".menu-wrap_3QAHkrqg .item_1xCevqmY:nth-child(2)")
    icon_games_locator = (By.CSS_SELECTOR, ".menu-wrap_3QAHkrqg .item_1xCevqmY:nth-child(3)")
    icon_search_jobs_locator = (By.CSS_SELECTOR, ".menu-wrap_3skhSRHM .item_1xCevqmY:nth-child(1)")
    icon_post_jobs_locator = (By.CSS_SELECTOR, ".menu-wrap_3skhSRHM .item_1xCevqmY:nth-child(2)")
    icon_manage_jobs_locator = (By.CSS_SELECTOR, ".menu-wrap_3skhSRHM .item_1xCevqmY:nth-child(3)")
    input_search_locator = (By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/input")
    icon_search_locator = (By.XPATH,'//*[@id="pageContent"]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/a')
    drop_down_locator =(By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[4]/div/div[3]/div/div[3]/div[4]/button/div/div[2]")
    create_school_locator =(By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[4]/div/div[3]/div/div[3]/div[4]/div/div/a[3]")
    my_company_locator =(By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[4]/div/div[3]/div/div[3]/div[4]/div/div[1]/a[1]/div[1]")
    create_company_locator =(By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[4]/div/div[3]/div/div[3]/div[4]/div/div[2]/a")
    drop_down2_locator = (By.XPATH,"//div[@class=\"down-icon_2La7glGl ifont ifont-material-baseline-arrow_drop_down\"]")
    verify_username_locator = (By.XPATH,"//div[@class='profile-account_16ouBH7U']/a")
    icon_sign_out_locator = (By.XPATH,'//div[@class="other-items"]/a[2]')
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_post_project = None
        self.icon_discover = None
        self.icon_project = None
        self.icon_jobs = None
        self.icon_group = None
        self.icon_talent = None
        self.icon_LiveHelp = None
        self.icon_companies = None
        self.icon_schools = None
        self.icon_channels = None
        self.icon_challenges = None
        self.icon_events = None
        self.icon_connections = None
        self.icon_articles = None
        self.icon_showcases = None
        self.icon_games = None
        self.icon_search_jobs = None
        self.icon_post_jobs = None
        self.icon_manage_jobs = None
        self.input_search = None
        self.icon_search = None
        self.drop_down = None
        self.create_school = None
        self.my_company = None
        self.create_company = None
        self.drop_down2 = None
        self.verify_username = None
        self.icon_sign_out = None
        self.present_locator = self.btn_post_project_locator

    def init_elements(self):
        super().init_elements()
        self.btn_post_project = super().get_element(self.btn_post_project_locator)
        self.icon_discover = super().get_element(self.icon_discover_locator)
        self.icon_project = super().get_element(self.icon_project_locator)
        self.icon_jobs = super().get_element(self.icon_jobs_locator)
        self.icon_group = super().get_element(self.icon_group_locator)
        self.icon_LiveHelp = super().get_element(self.icon_LiveHelp_locator)
        self.icon_talent = super().get_element(self.icon_talent_locator)
        self.icon_companies = super().get_element(self.icon_companies_locator)
        self.icon_schools = super().get_element(self.icon_schools_locator)
        self.icon_channels = super().get_element(self.icon_channels_locator)
        self.icon_challenges = super().get_element(self.icon_challenges_locator)
        self.icon_events = super().get_element(self.icon_events_locator)
        self.icon_connections = super().get_element(self.icon_connections_locator)
        self.icon_articles = super().get_element(self.icon_articles_locator)
        self.icon_showcases = super().get_element(self.icon_showcases_locator)
        self.icon_games = super().get_element(self.icon_games_locator)
        self.icon_search_jobs = super().get_element(self.icon_search_jobs_locator)
        self.icon_manage_jobs = super().get_element(self.icon_manage_jobs_locator)
        self.icon_post_jobs = super().get_element(self.icon_post_jobs_locator)
        self.input_search = super().get_element(self.input_search_locator)
        self.icon_search = super().get_element(self.icon_search_locator)
        self.drop_down = super().get_element(self.drop_down_locator)
        self.create_school = super().get_element(self.create_school_locator)
        self.my_company = super().get_element(self.my_company_locator)
        self.create_company = super().get_element(self.create_company_locator)
        self.drop_down2 = super().get_element(self.drop_down2_locator)
        self.verify_username = super().get_element(self.verify_username_locator)
        self.icon_sign_out = super().get_element(self.icon_sign_out_locator)