from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://distribute-staging.dashboard.unity.com/"
    btn_mygames_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[1]/div/div/span")
    btn_reporting_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[2]/div/div/span")
    btn_partnerstores_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[3]/div/div/span")
    btn_documentation_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[1]/div/div/div[1]/div/a[4]/div/div/span")
    btn_importfromGooglePlay_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[1]/div[2]")
    btn_gamecancel_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[1]/div[2]/div[1]/button")
    btn_gamesave_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[1]/div[2]/div[2]/button")
    btn_editinfo_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[1]/div[2]/div[1]")
    btn_release_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[1]/div[2]/div[2]/button")
    input_gametitle_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div/div/input")
    icon_genre_dropdown_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/button/div/div[2]")
    icon_genre_board_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/div[4]")
    icon_gameicon_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[5]/div[2]/div/div[1]/div/div/div/div[2]")
    input_gameicon_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[5]/div[2]/div/div[1]/div/input")
    input_description_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[6]/div[2]/div/div/textarea")
    btn_gamebanner_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[7]/div[2]/div/div[1]/div/div/div/div[2]")
    input_gamebanner_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[7]/div[2]/div/div[1]/div/input")
    btn_uploadimage_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[8]/div/div[1]/div[2]/div[1]")
    input_uploadimage_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[8]/div/input[1]")
    btn_uploadvideo_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[8]/div/div[1]/div[2]/div[2]")
    input_uploadvideo_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[8]/div/input[2]")
    btn_uploadyoutubelink_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[2]/div/div[8]/div/div[1]/div[2]/div[3]")
    btn_uploadapkfile_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div[2]/div/div")
    txt_premiumprice_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[2]/div/div/div/div[4]/div[1]/div/div[1]")
    btn_additem_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[3]/div/div[1]/div[2]/span[2]")
    btn_addIAPprice_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]")
    input_IAPprice_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[3]/div/div[4]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/input")
    btn_saveIAPprice_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[3]/div/div[4]/div[2]/div/div/div[1]/div/div/div[3]/div[2]/button")
    input_projectid_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[4]/div/div[2]/div[1]/div[1]/div/div[2]/div/div/input")
    input_CallbackURL_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[4]/div/div[2]/div[2]/div[5]/div[2]/div/div/input")
    btn_addnewaccount_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[5]/div/div[1]/div[2]/span[2]")
    input_searchuser_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[7]/div/div[3]/div/div[1]/div/div/input")
    btn_newuser_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[3]/div[7]/div/div[3]/div/div[2]/div[1]/div[1]/span[2]")
    icon_language_dropdown_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div[4]/div[3]/div/button/div/div[2]")


    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.btn_mygames = None
        self.btn_reporting = None
        self.btn_partnerstores = None
        self.btn_documentation = None
        self.btn_importfromGooglePlay = None
        self.btn_gamecancel = None
        self.btn_gamesave = None
        self.btn_editinfo = None
        self.btn_release = None
        self.input_gametitle = None
        self.icon_genre_dropdown = None
        self.icon_genre_board = None
        self.icon_gameicon = None
        self.input_gameicon = None
        self.input_description = None
        self.btn_gamebanner = None
        self.btn_uploadimage = None
        self.btn_uploadvideo = None
        self.btn_uploadyoutubelink = None
        self.btn_uploadapkfile = None
        self.txt_premiumprice = None
        self.btn_additem = None
        self.btn_addIAPprice = None
        self.input_IAPprice = None
        self.btn_saveIAPprice = None
        self.input_projectid = None
        self.input_CallbackURL = None
        self.btn_addnewaccount = None
        self.input_searchuser = None
        self.btn_newuser = None
        self.present_locator = self.icon_language_dropdown_locator

    def init_elements(self):
        super().init_elements()
        self.btn_mygames = super().get_element(self.btn_mygames_locator)
        self.btn_reporting = super().get_element(self.btn_reporting_locator)
        self.btn_partnerstores = super().get_element(self.btn_partnerstores_locator)
        self.btn_documentation = super().get_element(self.btn_documentation_locator)
        self.btn_importfromGooglePlay = super().get_element(self.btn_importfromGooglePlay_locator)
        self.btn_gamecancel = super().get_element(self.btn_gamecancel_locator)
        self.btn_gamesave = super().get_element(self.btn_gamesave_locator)
        self.btn_editinfo = super().get_element(self.btn_editinfo_locator)
        self.btn_release = super().get_element(self.btn_release_locator)
        self.input_gametitle = super().get_element(self.input_gametitle_locator)
        self.icon_genre_dropdown = super().get_element(self.icon_genre_dropdown_locator)
        self.icon_genre_board = super().get_element(self.icon_genre_board_locator)
        self.icon_gameicon = super().get_element(self.icon_gameicon_locator)
        self.input_gameicon = super().get_element(self.input_gameicon_locator)
        self.input_description = super().get_element(self.input_description_locator)
        self.btn_gamebanner = super().get_element(self.btn_gamebanner_locator)
        self.btn_uploadimage = super().get_element(self.btn_uploadimage_locator)
        self.btn_uploadvideo = super().get_element(self.btn_uploadvideo_locator)
        self.btn_uploadyoutubelink = super().get_element(self.btn_uploadyoutubelink_locator)
        self.btn_uploadapkfile = super().get_element(self.btn_uploadapkfile_locator)
        self.txt_premiumprice = super().get_element(self.txt_premiumprice_locator)
        self.btn_additem = super().get_element(self.btn_additem_locator)
        self.btn_addIAPprice = super().get_element(self.btn_addIAPprice_locator)
        self.input_IAPprice = super().get_element(self.input_IAPprice_locator)
        self.btn_saveIAPprice = super().get_element(self.btn_saveIAPprice_locator)
        self.input_projectid = super().get_element(self.input_projectid_locator)
        self.input_CallbackURL = super().get_element(self.input_CallbackURL_locator)
        self.btn_addnewaccount = super().get_element(self.btn_addnewaccount_locator)
        self.input_searchuser = super().get_element(self.input_searchuser_locator)
        self.btn_newuser = super().get_element(self.btn_newuser_locator)
        self.icon_language_dropdown = super().get_element(self.icon_language_dropdown_locator)

