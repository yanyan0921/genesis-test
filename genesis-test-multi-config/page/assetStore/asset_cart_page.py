from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    btn_proceed_to_checkout_locator = (By.CSS_SELECTOR, "[class = '_3UE3J _3zD70 auto _253jd']")
    label_price_locator = (By.CLASS_NAME, "_2QWFt")
    SaveForLater_btn_locator = (By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[3]/div[2]/button[2]')
    remove_btn_locator = (By.CLASS_NAME, "_2V-G7")
    Accept_btn_locator = (By.CSS_SELECTOR, 'class="_3UE3J pDJt- auto"')
    Clear_Cart_btn_locator = (
        By.XPATH, "//*[@id=\"main-layout-scroller\"]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/span")
    Clear_confirm_btn_locator = (By.CSS_SELECTOR, "[class = '_3UE3J pDJt- auto _2YXi8']")
    Qty_box_locator = (By.CSS_SELECTOR, "[class = 'Y1yB6']")
    Qty_1_locator = (By.CSS_SELECTOR,'[class = "_3BlIq _3n8G7 _3QM4s"]')
    Qty_10_locator = (By.XPATH,'//*[@id="main-layout-scroller"]/div/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div/div/div[1]/div/div[10]')
    Qty_input_box_locator = (By.CLASS_NAME,'_3ZBsL')
    right_slide_button_locator = (By.CLASS_NAME, "tCXxf")
    left_slide_button_locator = (By.CLASS_NAME, "_1pk5r")

    submit_for_approval_btn_locator = (By.CSS_SELECTOR,"[class = '_3UE3J _3zD70 auto _2V-EA']")
    input_search_box_locator = (By.XPATH, "//*[@id='Cart/CartController']/div/div/div/di/div/div[1]/div[2]/div/div[1]/form/div/input")
    sfl_view_button_locator = (By.CSS_SELECTOR, "[class ='_23d7p']")
    div_support_creator_locator= (By.CLASS_NAME, '_3paB7')
    div_edit_locator = (By.CLASS_NAME, '_3VYJ9')
    btn_fixedtips_3_locator = (
    By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]')
    btn_fixedtips_5_locator = (
        By.XPATH,
        '/html/body/div[3]/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]')
    btn_customer_locator = (
    By.XPATH, '/html/body/div[5]/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[3]')
    btn_confirm_locator = (
        By.XPATH,
        '/html/body/div[3]/div/div[2]/div/div/div[1]/div/div/button')
    item_name_locator = (By.XPATH, '//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div[1]/div[2]/div/div[2]/div[3]/div[1]/div[2]/a')
    site_package_1_price_locator = (By.XPATH ,'//*[@id="main-layout-scroller"]/div/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/a/div[3]/div/div/div')
    add_to_cart_locator = (By.CLASS_NAME,"_3UE3J _3vV3- auto _1EJPn hnQ7H")
    view_in_cart_locator = (By.CLASS_NAME,"[class = '_3UE3J _3vV3- auto _1EJPn hnQ7H']")
    visibility_locator = (By.CLASS_NAME, "_1yJAY")
    ABtest_locator = (By.CSS_SELECTOR, '[class = "ifont ifont-close _1sqyZ"]')

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.btn_proceed_to_checkout = None
        self.label_price = None
        self.SaveForLater_btn = None
        self.remove_btn = None
        self.Accept_btn = None
        self.Clear_Cart_btn = None
        self.Clear_confirm_btn = None
        self.Qty_box = None
        self.Qty_1 = None
        self.Qty_10 = None
        self.Qty_input_box = None
        self.right_slide_button = None
        self.left_slide_button = None
        self.sfl_view_button = None
        self.submit_for_approval_btn = None
        self.input_search_box = None
        self.div_support_creator = None
        self.div_edit = None
        self.btn_fixedtips_5 = None
        self.btn_fixedtips_3 = None
        self.btn_customer = None
        self.btn_confirm = None
        self.item_name = None
        self.site_package_1_price = None
        self.add_to_cart = None
        self.view_in_cart = None
        self.visibility = None
        self.ABtest = None
        self.present_locator = self.label_price_locator

    def init_elements(self):
        super().init_elements()
        self.btn_proceed_to_checkout = super().get_element(self.btn_proceed_to_checkout_locator)
        self.label_price = super().get_element(self.label_price_locator)
        self.SaveForLater_btn = super().get_element(self.SaveForLater_btn_locator)
        self.remove_btn = super().get_element(self.remove_btn_locator)
        self.Accept_btn = super().get_element(self.Accept_btn_locator)
        self.Clear_Cart_btn = super().get_element(self.Clear_Cart_btn_locator)
        self.Clear_confirm_btn = super().get_element(self.Clear_confirm_btn_locator)
        self.Qty_box = super().get_element(self.Qty_box_locator)
        self.Qty_1 = super().get_element(self.Qty_1_locator)
        self.Qty_10 = super().get_element(self.Qty_10_locator)
        self.Qty_input_box = super().get_element(self.Qty_input_box_locator)
        self.right_slide_button = super().get_element(self.right_slide_button_locator)
        self.left_slide_button = super().get_element(self.left_slide_button_locator)
        self.sfl_view_button = super().get_element(self.sfl_view_button_locator)
        self.input_search_box = super().get_element(self.input_search_box_locator)
        self.submit_for_approval_btn = super().get_element(self.submit_for_approval_btn_locator)
        self.div_support_creator = super().get_element(self.div_support_creator_locator)
        self.div_edit = super().get_element(self.div_edit_locator)
        self.btn_fixedtips_5 = super().get_element(self.btn_fixedtips_5_locator)
        self.btn_fixedtips_3 = super().get_element(self.btn_fixedtips_3_locator)
        self.btn_confirm = super().get_element(self.btn_confirm_locator)
        self.item_name = super().get_element(self.item_name_locator)
        self.btn_customer = super().get_element(self.btn_customer_locator)
        self.site_package_1_price = super().get_element(self.site_package_1_price_locator)
        self.add_to_cart = super().get_element(self.add_to_cart_locator)
        self.view_in_cart = super().get_element(self.view_in_cart_locator)
        self.visibility = super().get_element(self.visibility_locator)
        self.ABtest = super().get_element(self.ABtest_locator)
