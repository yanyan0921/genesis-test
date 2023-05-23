from page.base_page import BasePage
from selenium.webdriver.common.by import By


class Page(BasePage):
    base_url = "https://connect-dev.unity.com/"
    div_event_title_locator = (By.XPATH,
                                 "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[2]/div[3]/div/div/div/div/div[2]/div/div/div/div")
    input_event_title_locator = (By.CSS_SELECTOR, ".title-wrap_YcoBnqyq .public-DraftEditor-content")
    div_event_content_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[1]/div/div/div/div/div/div[1]/div/div/div/div/div/div[3]/div")
    input_event_content_locator = (By.XPATH, "//div[@id='Event/EditorController']/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div")
    btn_bgground_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[2]/div[2]/div/button")
    input_bgground_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[2]/div[1]/input")
    btn_display_picture_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/dl[1]/dd/div/div")
    input_display_picture_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/dl[1]/dd/div/input")
    icon_class_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/div/dl[1]/dd/div/button/div/div[2]")
    select_class_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/div/dl[1]/dd/div/div/div/div[1]/div/div[1]")
    url_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/div/dl[2]/dd/div/div/input")
    hoster_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/div/dl[3]/dd[1]/div/div/input")
    register_date_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/div/dl[4]/dd/div/div[1]/div[1]/input")
    register_time_locator = (By.CSS_SELECTOR,"dl:nth-child(5) .input_TX8JkZK8")
    register_time2_locator = (By.CSS_SELECTOR, ".valued_1dTuEj22:nth-child(6)")
    start_time_locator = (By.CSS_SELECTOR, ".when_3luUW0K0 .date-row_jtRx4Vl6:nth-child(1) .input_TX8JkZK8")
    start_time2_locator = (By.CSS_SELECTOR,".when_3luUW0K0 .date-row_jtRx4Vl6:nth-child(1) .input_TX8JkZK8")
    end_time_locator = (By.CSS_SELECTOR, ".date-row_jtRx4Vl6:nth-child(2) .input_TX8JkZK8")
    end_time2_locator = (By.CSS_SELECTOR,".valued_1dTuEj22:nth-child(7)")
    online_type_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/div/dl[6]/dd/div[1]/div[1]/div/button")
    offline_type_locator = (By.XPATH,"//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/div/dl[6]/dd/div[1]/div[2]/div/button")
    input_city_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/div/dl[6]/dd/div[3]/div/div/input")
    input_speaker_locator = ( By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/dl[2]/dd[1]/div/div/input")
    input_tag_locator = (By.XPATH, "//*[@id=\"Event/EditorController\"]/div/div/div[1]/div[3]/div[2]/dl[3]/dd/div/div/div/div/input")
    btn_post_locator = (By.XPATH, "//*[@id=\"prepublication\"]/button")
    publish_event_locator =(By.XPATH,"//*[@id=\"prepublication\"]/div/div/div/div[1]/div/div/button")
    def __init__(self, driver, wait):
        super().__int__(driver, wait)
        self.url = self.base_url
        self.div_event_title = None
        self.input_event_title = None
        self.div_event_content = None
        self.input_event_content = None
        self.btn_bgground = None
        self.input_bgground = None
        self.btn_display_picture = None
        self.input_display_picture = None
        self.icon_class = None
        self.select_class = None
        self.url = None
        self.hoster = None
        self.register_date = None
        self.register_time = None
        self.register_time2 = None
        self.start_time = None
        self.start_time2 = None
        self.end_time = None
        self.end_time2 = None
        self.online_type = None
        self.offline_type = None
        self.input_city = None
        self.input_speaker = None
        self.input_tag = None
        self.btn_post = None
        self.publish_event = None
        self.present_locator = self.btn_post_locator

    def init_elements(self):
        super().init_elements()
        self.div_event_title = super().get_element(self.div_event_title_locator)
        self.input_event_title = super().get_element(self.input_event_title_locator)
        self.div_event_content = super().get_element(self.div_event_content_locator)
        self.input_event_content = super().get_element(self.input_event_content_locator)
        self.btn_bgground = super().get_element(self.btn_bgground_locator)
        self.input_bgground = super().get_element(self.input_bgground_locator)
        self.btn_display_picture = super().get_element(self.btn_display_picture_locator)
        self.input_display_picture = super().get_element(self.input_display_picture_locator)
        self.icon_class = super().get_element(self.icon_class_locator)
        self.select_class = super().get_element(self.select_class_locator)
        self.url = super().get_element(self.url_locator)
        self.hoster = super().get_element(self.hoster_locator)
        self.register_date = super().get_element(self.register_date_locator)
        self.register_time = super().get_element(self.register_time_locator)
        self.start_time = super().get_element(self.start_time_locator)
        self.end_time = super().get_element(self.end_time_locator)
        self.online_type = super().get_element(self.online_type_locator)
        self.offline_type = super().get_element(self.offline_type_locator)
        self.input_city = super().get_element(self.input_city_locator)
        self.input_speaker = super().get_element(self.input_speaker_locator)
        self.input_tag = super().get_element(self.input_tag_locator)
        self.btn_post = super().get_element(self.btn_post_locator)
        self.btn_post = super().get_element(self.publish_event_locator)
