from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Page(BasePage):
    base_url = "https://urdp-int.unity.cn/cloud-desktop"
    DailyCheckInWindow_btn_locator = (By.XPATH, '//*[@id="mat-dialog-0"]/checkin-dialog/div[2]/button')
    DailyCheckInWindow_locator = (By.XPATH, '//*[@id="mat-dialog-0"]')

    console_btn_locator=(By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/header-component/div[2]/a")
    dailycheckin_btn_locator=(By.XPATH, '/html/body/app-component/cloud-desktop-component/default-layout-component/div/daily-checkin-floating-component/img')

    #int环境
    beijing_btn_locator=(By.XPATH, '//*[@id="mat-tab-label-0-1"]')
    shanghai_btn_locator = (By.XPATH, '//*[@id="mat-tab-label-0-0"]')
    suqian_btn_locator = (By.XPATH, '//*[@id="mat-tab-label-0-2"]')
    buybeijingNV4jichu_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li/product-card-component/div/div[2]/button")
    buyshanghaiT4jichu_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li[1]/product-card-component/div/div[2]/button")
    buyshanghaiT4gaoji_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li[2]/product-card-component/div/div[2]/button")
    buysuqian3090biaozhun_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li/product-card-component/div/div[2]/button")

    agree_btn_locator=(By.XPATH,'//*[@id="mat-checkbox-1"]')
    commit_btn_locator=(By.XPATH,'//*[@id="mat-dialog-0"]/payment-confirm-dialog/div[3]/button')

    #prod环境元素
    # beijing_btn_locator=(By.XPATH, '//*[@id="mat-tab-label-0-0"]')
    # shanghai_btn_locator = (By.XPATH, '//*[@id="mat-tab-label-0-1"]')
    # suqian_btn_locator = (By.XPATH, '//*[@id="mat-tab-label-0-2"]')
    # huabei_btn_locator = (By.XPATH, '//*[@id="mat-tab-label-0-3"]')
    # buybeijingA10jichu_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li/product-card-component/div/div[2]/button")
    # buyshanghaiT4jichu_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li[1]/product-card-component/div/div[2]/button")
    # buyshanghaiT4gaoji_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li[2]/product-card-component/div/div[2]/button")
    # buyshanghaiT4jingjie_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li[3]/product-card-component/div/div[2]/button")
    # buyshanghaiA10jichu_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li[4]/product-card-component/div/div[2]/button")
    # buyshuqian3090biaozhun_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li/product-card-component/div[1]/div[2]/button")
    # buyhuabeiA5intel_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li[1]/product-card-component/div/div[2]/button")
    # buyhuabeiA5intel_btn_locator = (By.XPATH,"/html/body/app-component/cloud-desktop-component/default-layout-component/div/div/ul/li[2]/product-card-component/div/div[2]/button")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_email = None
        self.input_password = None
        self.login_btn = None
        self.DailyCheckIn_btn = None
        self.DailyCheckIn = None

        self.beijing_btn=self.beijing_btn_locator
        self.shanghai_btn=self.shanghai_btn_locator
        self.suqian_btn=self.suqian_btn_locator
        self.buybeijingNV4jichu_btn=None
        self.buyshanghaiT4gaoji_btn=None
        self.buyshanghaiT4jichu_btn=None
        self.buysuqian3090biaozhun_btn=None
        self.console_btn =self.console_btn_locator
        self.agree_btn=self.agree_btn_locator
        self.commit_btn=self.commit_btn_locator

        self.present_locator = self.console_btn_locator


    def init_elements(self):
        super().init_elements()


        self.beijing_btn = super().get_element(self.beijing_btn_locator)
        self.shanghai_btn = super().get_element(self.shanghai_btn_locator)
        self.suqian_btn = super().get_element(self.suqian_btn_locator)
        self.buybeijingNV4jichu_btn = super().get_element(self.buybeijingNV4jichu_btn_locator)
        self.buyshanghaiT4jichu_btn = super().get_element(self.buyshanghaiT4jichu_btn_locator)
        self.buyshanghaiT4gaoji_btn = super().get_element(self.buyshanghaiT4gaoji_btn_locator)
        self.buysuqian3090biaozhun_btn = super().get_element(self.buysuqian3090biaozhun_btn_locator)
        self.agree_btn = super().get_element(self.agree_btn_locator)
        self.commit_btn = super().get_element(self.commit_btn_locator)
        self.console_btn = super().get_element(self.console_btn_locator)
        self.DailyCheckIn = super().get_element(self.DailyCheckInWindow_locator)
        self.DailyCheckIn_btn = super().get_element(self.DailyCheckInWindow_btn_locator)



