from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/groups"
    input_group_name_locator = (By.XPATH, "//div[@class='text-input_1zwaVtSr theme-dark_2f3h2N29']/div/input[@class='input_3yaUP2ah']")
    error_msg_groupname_locator = (By.XPATH, "//div[@class=\"right_2_s_Jd28\"]/div/div[2]/div[2]")
    #input_group_name_locator = (By.CSS_SELECTOR,".active_1tGpmPsf > .input_3yaUP2ah")
    icon_down_locator = (By.XPATH,"//div[@class='triangle_20fmw_FF ifont ifont-icon-triangle-down']")
    #icon_down_locator = (By.CSS_SELECTOR,".category_303N_-Dp .innerCurrentText_F-JXwypx")
    select_class_locator = (By.XPATH, "//div[@class='selects_2ppiVyIj']/div[2]")
    error_msg_category_locator = (By.XPATH, "//div[@class=\"field_3MfJ7F9t category_303N_-Dp\"]/div[2]/div[2]")
    #select_class_locator = (By.CSS_SELECTOR,".container_1NEeLFjP: nth - child(1).scroller - wrap_2ebVUni0.selectItem_2K6fI4KB:nth - child(3)")
    text_content_locator = (By.CSS_SELECTOR, "textarea")
    error_msg_content_locator = (By.XPATH, "//div[@class='fields_2auNdYNB']/div[2]/div[2]/div[2]")
    #图片
    icon_picture_locator = (By.CSS_SELECTOR, ".avatar_2FX0FCbc")
    input_picture_locator = (By.CSS_SELECTOR, ".hide_3N_qgKYS")
    div_picture_locator=(By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[7]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div/div[3]")
    error_msg_picture_locator =(By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[7]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div")
    #btn_picture_locator = (By.CSS_SELECTOR,".raised-btn-primary_MYOE9bp7")
    btn_picture_locator = (By.XPATH, "//div[@class='buttons_16lIDcK0']/button[@class='raised-btn_2vTjL538 raised-btn-primary_MYOE9bp7 add_1LW0yga-']")
    #小组类型-public\private\closed
    icon_down2_locator = (By.CSS_SELECTOR, ".select-container_1eYYJlYk .triangle_20fmw_FF")
    public_group_locator = (By.CSS_SELECTOR, ".active_137ZXAvm .hint_30yEe9i8")
    private_group_locator = (By.CSS_SELECTOR, ".selectItem_2K6fI4KB:nth-child(3) .hint_30yEe9i8")
    closed_group_locator = (By.CSS_SELECTOR, ".selectItem_2K6fI4KB:nth-child(2) .hint_30yEe9i8")
    error_msg_type_locator = (By.XPATH,"//*[@id=\"pageContent\"]/div[1]/div[7]/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div/div[3]/div[2]/div[2]")
    btn_ok_locator = (By.CSS_SELECTOR, ".raised-btn-blue_37QDrHj0")
    btn_cancel_locator = (By.CSS_SELECTOR, ".raised-btn-default_3M_uvHPG")
    #选择偏好语言
    icon_language_locator = (By.CSS_SELECTOR, ".input-wrapper_3Q82pEu2 .triangle_20fmw_FF")
    select_language_locator = (By.CSS_SELECTOR, ".selectItem_2K6fI4KB:nth-child(45)")
    btn_lan_locator = (By.CSS_SELECTOR, ".blue_1N0NIlL6")
    #验证
    group_name_locator=(By.XPATH,"//*[@id=\"pageBody\"]/div/div[1]/div[2]/div[2]/div[1]/div[1]")

    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.input_group_name = None
        self.error_msg_groupname = None
        self.icon_down = None
        self.select_class = None
        self.error_msg_category = None
        self.text_content = None
        self.error_msg_content = None
        self.icon_picture = None
        self.input_picture = None
        self.div_picture = None
        self.error_msg_picture = None
        self.btn_picture = None
        self.icon_down2 = None
        self.public_group = None
        self.private_group = None
        self.closed_group = None
        self.error_msg_type = None
        self.btn_ok = None
        self.btn_cancel = None
        self.icon_language = None
        self.select_language = None
        self.btn_lan = None
        self.group_name = None
        self.present_locator = self.btn_ok_locator

    def init_elements(self):
        super().init_elements()
        self.input_group_name = super().get_element(self.input_group_name_locator)
        self.icon_down = super().get_element(self.icon_down_locator)
        self.select_class = super().get_element(self.select_class_locator)
        self.text_content = super().get_element(self.text_content_locator)
        self.icon_picture = super().get_element(self.icon_picture_locator)
        self.input_picture = super().get_element(self.input_picture_locator)
        self.div_picture = super().get_element(self.div_picture_locator)
        self.btn_picture = super().get_element(self.btn_picture_locator)
        self.icon_down2 = super().get_element(self.icon_down2_locator)
        self.public_group = super().get_element(self.public_group_locator)
        self.private_group = super().get_element(self.private_group_locator)
        self.closed_group = super().get_element(self.closed_group_locator)
        self.btn_ok = super().get_element(self.btn_ok_locator)
        self.btn_cancel = super().get_element(self.btn_cancel_locator)
        self.icon_language = super().get_element(self.icon_language_locator)
        self.select_language = super().get_element(self.select_language_locator)
        self.btn_lan = super().get_element(self.btn_lan_locator)
        self.error_msg_groupname = super().get_element(self.error_msg_groupname_locator)
        self.error_msg_category = super().get_element(self.error_msg_category_locator)
        self.error_msg_content = super().get_element(self.error_msg_content_locator)
        self.error_msg_picture = super().get_element(self.error_msg_picture_locator)
        self.error_msg_type = super().get_element(self.error_msg_type_locator)
        self.group_name = super().get_element(self.group_name_locator)