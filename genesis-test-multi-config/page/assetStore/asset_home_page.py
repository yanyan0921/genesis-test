from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    myAssetsIcon_locator = (By.CLASS_NAME, 'wWQpa')
    myFavoritesIcon_locator = (By.XPATH, '//*[@id="Search/V3Controller"]/div/div/div/di/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/button/div')
    myCartIcon_locator = (By.XPATH, '//*[@id="header-menu-icon-assets"]/div/button/div')

    input_search_box_locator = (By.CLASS_NAME, "_3_gZI")
    btn_search_locator = (By.CLASS_NAME, "ifont ifont-search _2GQj8")
    icon_sign_in_locator = (By.XPATH, '//*[@id="Search/V3Controller"]/div/div/div/div/div[1]/div/div/div[1]/div/div[3]/div/div[3]/button/div/div')
    href_sign_in_locator = (By.XPATH, '//*[@id="login-action"]/div[2]/div[2]/div[2]')
    href_terms_of_services_locator = (By.XPATH, '//*[@id="login-action"]/div[1]/div[2]')
    item_name_locator = (By.CLASS_NAME, "_1-e15 _25P-Q")
    logined_account_locator = (By.XPATH ,'//*[@id="Search/V3Controller"]/div/div/div/div/div[1]/div/div/div[1]/div/div[3]/div/div[3]/button/div/div')
    sign_out_locator = (By.CSS_SELECTOR, "[class = '_2hXqt _1GsCa']")
    switch_org_locator = (By.XPATH, '//*[@id="profile-option"]/div[2]/div[2]/div[1]/i')
    order_request_org_locator = (By.XPATH, '//*[@id="profile-option"]/div[2]/div[2]/div[2]/div[1]/ul/li[2]')
    verify_tip_org_locator = (By.XPATH, "//*[@id=\"profile-option\"]/div[2]/div[2]/div[2]/div[1]/ul/li[2]/span")

    popular_assets_title_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div/div/div/div/div[9]/div/h2')
    page_header_locator = (By.CLASS_NAME, '_17EkZ')

    category_3D_locator = (By.CSS_SELECTOR, "[class = 'dF4_e main-nav-element _3OFKb']")
    Browse_by_categorys_locator = (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[8]/div/div/h2')
    category_tools_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div[2]/a[7]')
    btn_view_bundle_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div/div[2]/div[2]')
    onSale_locator = (By.CSS_SELECTOR,"[class = '_1Mlq- _10GC7 Xb3dE']")
    sale_tag_locator = (By.XPATH,
                        "//*[@id=\"main-layout-scroller\"]/div/div[1]/div/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div/a/div[2]/div")
    clear_filters_locator = (By.XPATH, "//*[@id=\"main-layout-scroller\"]/div/div[1]/div/div/div/div/div[2]/div/div[1]/a")

    footer_language_English_locator = (
        By.XPATH, '//*[@id="main-layout-scroller"]/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/a[1]')
    footer_language_Chinese_locator = (
        By.XPATH, '//*[@id="main-layout-scroller"]/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/a[2]')
    footer_language_Korean_locator = (
        By.XPATH, '//*[@id="main-layout-scroller"]/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/a[3]')
    footer_language_Japanese_locator = (
        By.XPATH, '//*[@id="main-layout-scroller"]/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/a[4]')
    footer_SellAssetsonUnity_submissionGuide_locator = (
        By.XPATH, '//*[@id="main-layout-scroller"]/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/a[2]')
    footer_SellAssetsonUnity_publisherLogin_locator = (
        By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/a[4]')
    footer_SellAssetsonUnity_FAQ_locator = (
        By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div[1]/a[5]')

    site_stg_1_locator = (By.XPATH, "//*[@id='main-layout-scroller']/div/div[1]/div[2]/div/div/div/div[1]/div[4]/div/div/div/div[3]/div/div/div/a/div[1]/div")
    ABtest_locator = (By.CSS_SELECTOR, '[class = "ifont ifont-close _1sqyZ"]')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.input_search_box = None
        self.btn_search = None
        self.href_sign_in = None
        self.icon_sign_in = None
        self.href_terms_of_services = None
        self.item_name = None
        self.logined_account = None
        self.sign_out = None
        self.switch_org = None
        self.order_request_org = None
        self.verify_tip_org = None
        self.btn_view_bundle = None

        self.category_3D = self.category_3D_locator
        self.myAssetsIcon = None
        self.myFavoritesIcon = None
        self.myCartIcon = None

        self.popular_assets_title = None
        self.page_header = None
        self.onSale = None
        self.sale_tag = None
        self.clear_filters = None

        self.footer_language_English = None
        self.footer_language_Chinese = None
        self.footer_language_Korean = None
        self.footer_language_Japanese = None

        self.footer_SellAssetsonUnity_submissionGuide = None
        self.footer_SellAssetsonUnity_publisherLogin = None
        self.footer_SellAssetsonUnity_FAQ = None
        self.site_stg_1 = None
        self.category_tools = None
        self.Browse_by_categorys = None
        self.ABtest = None
        self.present_locator = self.icon_sign_in_locator

    def init_elements(self):
        super().init_elements()
        self.myAssetsIcon = super().get_element(self.myAssetsIcon_locator)
        self.myFavoritesIcon = super().get_element(self.myFavoritesIcon_locator)
        self.myCartIcon = super().get_element(self.myCartIcon_locator)

        self.input_search_box = super().get_element(self.input_search_box_locator)
        self.btn_search = super().get_element(self.btn_search_locator)
        self.href_sign_in = super().get_element(self.href_sign_in_locator)
        self.icon_sign_in = super().get_element(self.icon_sign_in_locator)
        self.href_terms_of_services = super().get_element(self.href_terms_of_services_locator)
        self.item_name = super().get_element(self.item_name_locator)
        self.logined_account = super().get_element(self.logined_account_locator)
        self.sign_out = super().get_element(self.sign_out_locator)
        self.switch_org = super().get_element(self.switch_org_locator)
        self.order_request_org = super().get_element(self.order_request_org_locator)
        self.verify_tip_org = super().get_element(self.verify_tip_org_locator)

        self.popular_assets_title = super().get_element(self.popular_assets_title_locator)
        self.page_header = super().get_element(self.page_header_locator)


        self.onSale = super().get_element(self.onSale_locator)
        self.category_3D = super().get_element(self.category_3D_locator)
        self.btn_view_bundle = super().get_element(self.btn_view_bundle_locator)
        self.sale_tag = super().get_element(self.sale_tag_locator)
        self.clear_filters = super().get_element(self.clear_filters_locator)

        self.footer_language_English = super().get_element(self.footer_language_English_locator)
        self.footer_language_Chinese = super().get_element(self.footer_language_Chinese_locator)
        self.footer_language_Korean = super().get_element(self.footer_language_Korean_locator)
        self.footer_language_Japanese = super().get_element(self.footer_language_Japanese_locator)

        self.footer_SellAssetsonUnity_submissionGuide = super().get_element(
            self.footer_SellAssetsonUnity_submissionGuide_locator)
        self.footer_SellAssetsonUnity_publisherLogin = super().get_element(
            self.footer_SellAssetsonUnity_publisherLogin_locator)
        self.footer_SellAssetsonUnity_FAQ = super().get_element(self.footer_SellAssetsonUnity_FAQ_locator)
        self.category_tools = super().get_element(self.category_tools_locator)
        self.Browse_by_categorys = super().get_element(self.Browse_by_categorys_locator)
        self.ABtest = super().get_element(self.ABtest_locator)

        self.site_stg_1 = super().get_element(self.site_stg_1_locator)