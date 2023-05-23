from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_create_new_draft_locator = (
    By.XPATH, '/html/body/div[1]/main/div/header/div[1]/div[1]/div[2]/div[3]/button/span[1]')
    btn_new_draft_locator = (By.XPATH, '//*[@id="app"]/main/div/header/div[1]/div/div[2]/div[3]/button/span[1]')
    btn_new_draft_pending_page_locator = (By.XPATH, '//*[@id="app"]/main/div/header/div[1]/div[1]/div[2]/div[2]/button/span[1]')
    btn_publish_locator = (By.XPATH, '/html/body/div[1]/main/div/header/div[1]/div[1]/div[2]/div[3]/button/span[1]')
    label_depercated_locator = (By.XPATH, '/html/body/div[1]/main/div/header/div[1]/div/div[2]/div[2]/button/span[1]')
    label_status_locator = (By.CSS_SELECTOR, "[class='MuiChip-label MuiChip-labelSmall']")
    checkbox_terms_locator = (By.XPATH, '/html/body/div[3]/div[3]/div/section/dd/label/span[1]/span/input')
    btn_depercated_locator = (By.XPATH, '/html/body/div[3]/div[3]/div/div/div[2]/div[2]/button/span[1]')

    label_published_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div/div/button[4]/span[1]')
    label_package_locator = (By.XPATH, '/html/body/div[1]/main/div/div/div[3]/div[1]/dl/dd[1]/a')

    logout_tab_locator = (By.XPATH, "//*[@id=\"unav\"]/div/a[2]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_create_new_draft = None
        self.btn_new_draft = None
        self.btn_new_draft_pending_page = None
        self.btn_publish = None
        self.label_depercated = None
        self.label_status = None
        self.checkbox_terms = None
        self.btn_depercated = None

        self.label_published = None
        self.label_package = None

        self.present_locator = self.label_status_locator

    def init_elements(self):
        super().init_elements()
        self.btn_create_new_draft = super().get_element(self.btn_create_new_draft_locator)
        self.btn_new_draft = super().get_element(self.btn_new_draft_locator)
        self.btn_new_draft_pending_page = super().get_element(self.btn_new_draft_pending_page_locator)
        self.btn_publish = super().get_element(self.btn_publish_locator)
        self.label_depercated = super().get_element(self.label_depercated_locator)
        self.label_status = super().get_element(self.label_status_locator)
        self.checkbox_terms = super().get_element(self.checkbox_terms_locator)
        self.btn_depercated = super().get_element(self.btn_depercated_locator)

        self.label_published = super().get_element(self.label_published_locator)
        self.label_package = super().get_element(self.label_package_locator)