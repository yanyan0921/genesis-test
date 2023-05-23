from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    create_new_package_btn_locator = (By.XPATH, '/html/body/div[1]/div[2]/div/aside/nav/ul[1]/li/a/span')
    input_packagename_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/section/dl[1]/dd/div/div/input')
    input_search_locator = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/input')
    category_select_box_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/section/dl[2]/dd/div/div/div/fieldset')
    btn_save_locator = (By.XPATH, '/html/body/div[4]/div[3]/div/footer/div[2]/div[2]/button/span[1]')
    draft_package_name_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div[3]/div[1]/dl/dd[1]/a')
    label_published_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div/div/button[4]/span[1]')
    label_pending_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div/div/button[3]/span[1]')
    label_rejected_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div/div/button[5]/span[1]')
    label_depercated_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[1]/div/div/button[7]/span[1]')
    label_draft_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div/div/button[3]/span[1]')
    label_package_locator = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[3]/div[1]/dl/dd[1]/div/div[2]/p[1]/a')
    label_pending_package_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[3]/div[2]/dl/dd[1]/div/div[2]/p[1]/a')
    btn_account_locator = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/nav/button[2]/span[1]/span')
    sort_size_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[3]/header/dl/dt[5]/div/p')
    btn_columns_locator = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[2]/div/div/div/button/span[1]')
    label_modified_locator = (By.XPATH, '/html/body/div[3]/div[3]/ul/li[6]')
    sort_modified_locator = (By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div[3]/header/dl/dt[6]')
    logout_tab_locator = (By.XPATH, '/html/body/div[4]/div[3]/ul/li')
    label_price_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[3]/div[1]/dl/dd[4]')
    icon_cookies_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div[3]/div[1]/dl/dd[3]')
    Reviews_management_locator = (By.XPATH, '/html/body/div[1]/div[2]/div/aside/nav/ul[2]/div[5]/li/a/span')
    sort_pending_page_modified_locator = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div[3]/header/dl/dt[7]/div/p')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.create_new_package_btn = None
        self.input_packagename = None
        self.input_search = None
        self.category_select_box = None
        self.btn_save = None
        self.draft_package_name = None
        self.label_published = None
        self.label_pending = None
        self.label_rejected = None
        self.label_depercated = None
        self.label_draft = None
        self.label_package = None
        self.label_pending_package = None
        self.btn_account = None
        self.sort_size = None
        self.btn_columns = None
        self.label_modified = None
        self.sort_modified = None
        self.logout_tab = None
        self.label_price = None
        self.icon_cookies = None
        self.Reviews_management = None
        self.sort_pending_page_modified = None

        self.present_locator = self.create_new_package_btn_locator

    def init_elements(self):
        super().init_elements()
        self.create_new_package_btn = super().get_element(self.create_new_package_btn_locator)
        self.input_packagename = super().get_element(self.input_packagename_locator)
        self.input_search = super().get_element(self.input_search_locator)
        self.btn_save = super().get_element(self.btn_save_locator)
        self.category_select_box = super().get_element(self.category_select_box_locator)
        self.draft_package_name = super().get_element(self.draft_package_name_locator)
        self.label_published = super().get_element(self.label_published_locator)
        self.label_pending = super().get_element(self.label_pending_locator)
        self.label_depercated = super().get_element(self.label_depercated_locator)
        self.label_rejected = super().get_element(self.label_rejected_locator)
        self.label_draft = super().get_element(self.label_draft_locator)
        self.label_package = super().get_element(self.label_package_locator)
        self.label_pending_package = super().get_element(self.label_pending_package_locator)
        self.btn_account = super().get_element(self.btn_account_locator)
        self.sort_size = super().get_element(self.sort_size_locator)
        self.btn_columns = super().get_element(self.btn_columns_locator)
        self.label_modified = super().get_element(self.label_modified_locator)
        self.sort_modified = super().get_element(self.sort_modified_locator)
        self.logout_tab = super().get_element(self.logout_tab_locator)
        self.label_price = super().get_element(self.label_price_locator)
        self.icon_cookies = super().get_element(self.icon_cookies_locator)
        self.Reviews_management = super().get_element(self.Reviews_management_locator)
        self.sort_pending_page_modified = super().get_element(self.sort_pending_page_modified_locator)

