from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    icon_user_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[2]/div[3]/span/img")
    btn_log_out_locator = (By.XPATH, "//*[@id=\"menuitem_5\"]")
    btn_repo_search_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/a[2]")
    input_search_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[1]/input")
    btn_search_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[1]/button")
    info_repo_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[4]/div/div[1]/div[1]/a")
    btn_user_page_locator = (By.XPATH, "//*[@id=\"navbar\"]/div/div[1]/a")
    btn_repo_page_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[1]/a")
    btn_repo_page2_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/a")
    btn_visibility_span_locator = (By.ID, "menutext_2")
    btn_span_private_locator = (By.ID, "menuitem_20")
    btn_create_repo_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[4]/div/div/button")
    btn_folder_detail_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/h4/a")


    # Discovery page
    btn_tag_locator = (By.XPATH, "//*[@id=\"repo-topics\"]/a[1]")
    btn_dis_repo_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/a/img")
    btn_fork_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[2]/form/button")
    btn_banner_switch_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/ul/li[1]")
    btn_banner_repo_locator = (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/form/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.icon_user = None
        self.btn_log_out = None
        self.btn_repo_search = None
        self.input_search = None
        self.btn_search = None
        self.info_repo = None
        self.btn_user_page = None
        self.btn_repo_page = None
        self.btn_repo_page2 = None
        self.btn_visibility_span = None
        self.btn_span_private = None
        self.btn_create_repo = None
        self.btn_folder_detail = None
        # discovery
        self.btn_tag = None
        self.btn_dis_repo = None
        self.btn_fork = None
        self.btn_banner_switch = None
        self.btn_banner_repo = None
        self.present_locator = self.icon_user_locator

    def init_elements(self):
        super().init_elements()
        self.icon_user = super().get_element(self.icon_user_locator)
        self.btn_log_out = super().get_element(self.btn_log_out_locator)
        self.btn_repo_search = super().get_element(self.btn_repo_search_locator)
        self.input_search = super().get_element(self.input_search_locator)
        self.btn_search = super().get_element(self.btn_search_locator)
        self.info_repo = super().get_element(self.info_repo_locator)
        self.btn_user_page = super().get_element(self.btn_user_page_locator)
        self.btn_repo_page = super().get_element(self.btn_repo_page_locator)
        self.btn_repo_page2 = super().get_element(self.btn_repo_page2_locator)
        self.btn_visibility_span = super().get_element(self.btn_visibility_span_locator)
        self.btn_span_private = super().get_element(self.btn_span_private_locator)
        self.btn_create_repo = super().get_element(self.btn_create_repo_locator)
        self.btn_folder_detail = super().get_element(self.btn_folder_detail_locator)
        # Discovery
        self.btn_tag = super().get_element(self.btn_tag_locator)
        self.btn_dis_repo = super().get_element(self.btn_dis_repo_locator)
        self.btn_fork = super().get_element(self.btn_fork_locator)
        self.btn_banner_switch = super().get_element(self.btn_banner_switch_locator)
        self.btn_banner_repo = super().get_element(self.btn_banner_repo_locator)
