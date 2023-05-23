from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://urdp.unity.cn/host-list"
    addhost_btn_locator = (By.XPATH,
                           '/html/body/app-component/host-list-component/admin-layout-component/mat-sidenav-container/mat-sidenav-content/div/top-banner-component/div[2]/button')
    threepoint1_btn_locator = (By.XPATH,
                               '/html/body/app-component/host-list-component/admin-layout-component/mat-sidenav-container/mat-sidenav-content/div/div/div/mat-card/div[2]/a/host-item-component/div[1]/div[6]/button[2]')
    shutdown_btn_locator = (By.XPATH,
                            "/html/body/app-component/host-list-component/admin-layout-component/mat-sidenav-container/mat-sidenav-content/div/div/div/mat-card/div[2]/a/host-item-component/div[1]/div[6]/button[1]")
    shutdow_btn2_locator = (By.XPATH, '//*[@id="mat-dialog-1"]/boot-instance-dialog/div[3]/div/button[2]')
    hoststate_locator = (By.XPATH,
                         '/html/body/app-component/host-list-component/admin-layout-component/mat-sidenav-container/mat-sidenav-content/div/div/div/mat-card/div[2]/a/host-item-component/div[1]/div[4]')

    shutdowbtntip_btn_locator = (By.XPATH, '//*[@id="mat-dialog-0"]/new-feature-dialog/div[3]/button')

    autoboot_btn_locator = (By.XPATH, '//*[@id="mat-menu-panel-1"]/div/button[2]')
    deletehost_locator = (By.XPATH, '//*[@id="mat-menu-panel-2"]/div/button[2]')
    deleteconfirm_locator = (By.XPATH, '//*[@id="mat-dialog-5"]/confirm-dialog/div[2]/button[2]')
    balance_btn_locator = (By.XPATH,
                           '/html/body/app-component/host-list-component/admin-layout-component/mat-sidenav-container/mat-sidenav/div/side-menu-component/nav-link-component[2]/a')

    cursor_locator = (By.CLASS_NAME, 'cursor')
    dialogue_locator = (By.CLASS_NAME, 'cdk-overlay-pane')
    confirm_locator = (By.CLASS_NAME, 'mat-focus-indicator.button-confirm.mat-flat-button.mat-button-base.mat-primary')
    clouddesktop_btn_locator=(By.XPATH,'/html/body/app-component/host-list-component/admin-layout-component/header-component/div[1]/header-menu-component/li[1]')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.addhost_btn = None
        self.threepoint1_btn = None
        self.shutdown_btn = None
        self.shutdow_btn2 = None
        self.hoststate = None
        self.autoboot_btn = None
        self.deletehost = None
        self.deleteconfirm = None
        self.cursor = None
        self.shutdowbtntip_btn = None
        self.balance_btn = None
        self.dialogue_window = None
        self.confirm = None
        self.clouddesktop_btn=None
        self.present_locator = self.addhost_btn_locator

    def init_elements(self):
        super().init_elements()
        self.addhost_btn = super().get_element(self.addhost_btn_locator)
        self.threepoint1_btn = super().get_element(self.threepoint1_btn_locator)
        self.shutdown_btn = super().get_element(self.shutdown_btn_locator)
        self.shutdow_btn2 = super().get_element(self.shutdow_btn2_locator)
        self.hoststate = super().get_element(self.hoststate_locator)
        self.autoboot_btn = super().get_element(self.autoboot_btn_locator)
        self.deletehost = super().get_element(self.deletehost_locator)
        self.deleteconfirm = super().get_element(self.deleteconfirm_locator)
        self.cursor = super().get_element(self.cursor_locator)
        self.shutdowbtntip_btn = super().get_element(self.shutdowbtntip_btn_locator)
        self.balance_btn = super().get_element(self.balance_btn_locator)
        self.dialogue_window = super().get_element(self.dialogue_locator)
        self.confirm = super().get_element(self.confirm_locator)
        self.clouddesktop_btn=super().get_element(self.clouddesktop_btn_locator)
