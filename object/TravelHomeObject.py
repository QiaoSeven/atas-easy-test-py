from selenium.webdriver.common.by import By


class TravelHomeObject:
    def __init__(self, driver):
        self.driver = driver

    def search_place(self):
        if self.driver.get_browser_type() == 'ios':
            element = self.driver.wait_and_find_element(By.XPATH, "//XCUIElementTypeStaticText[@name=\"输入目的地或住宿设施名称\"]",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View",
                                                        10)
        return element

    def search_place_input(self):
        if self.driver.get_browser_type() == 'ios':
            element = self.driver.wait_and_find_element(By.XPATH, "", 10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText",
                                                        10)
        return element

    def search_select(self):
        if self.driver.get_browser_type() == 'ios':
            element = self.driver.wait_and_find_element(By.XPATH, "", 10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View[1]",
                                                        10)
        return element

    def search_button(self):
        if self.driver.get_browser_type() == 'ios':
            element = self.driver.wait_and_find_element(By.XPATH, "", 10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.Button",
                                                        10)
        return element

    def complete_button(self):
        if self.driver.get_browser_type() == 'ios':
            element = self.driver.wait_and_find_element(By.XPATH, "", 10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button",
                                                        10)
        return element

    def search_date(self):
        if self.driver.get_browser_type() == 'ios':
            element = self.driver.wait_and_find_element(By.XPATH, "", 10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View",
                                                        10)
        return element

    def search_date_select(self):
        if self.driver.get_browser_type() == 'ios':
            element = self.driver.wait_and_find_element(By.XPATH, "", 10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.LinearLayout[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout[6]/android.widget.TextView",
                                                        10)
        return element

    def search_result(self):
        if self.driver.get_browser_type() == 'ios':
            element = self.driver.wait_and_find_element(By.XPATH, "", 10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView",
                                                        10)
        return element

    def order_icon(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH, "//XCUIElementTypeStaticText[@name=\"订单\"]",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "//android.widget.FrameLayout[@content-desc=\"订单\"]/android.view.ViewGroup/android.widget.TextView",
                                                        10)
        return element

    def login_button(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "//XCUIElementTypeStaticText[@name=\"使用您的Rakuten账户登录\"]",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button",
                                                        10)
        return element

    def ensure_pop(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH, "//XCUIElementTypeButton[@name=\"继续\"]",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH, "", 10)
        return element

    def mail_input(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "//XCUIElementTypeOther[@name=\"Rakuten - 登录\"]/XCUIElementTypeOther[3]",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH, "//*[@id=\"user_id\"]", 10)
        return element

    def ensure_button(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH, "//XCUIElementTypeButton[@name=\"确认\"]",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH, "//*[@id=\"cta\"]", 10)
        return element

    def login_message(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "//XCUIElementTypeStaticText[@name=\"会员账号不存在或尚未注册。如果问题持续发生，\"]",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH, "//*[@id=\"ie-flex-fix-320\"]/div[1]", 10)
        return element

    def point_login_bt(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH, "",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[1]",
                                                        10)
        return element

    def point_user(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH, "",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.EditText[1]",
                                                        10)
        return element

    def point_passwd(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH, "",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.EditText[2]",
                                                        10)
        return element

    def point_login_ensure(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH, "",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.CheckBox",
                                                        10)
        return element

    def point_submit_bt(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH, "",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[1]",
                                                        10)
        return element

    def point_fail_bt(self):
        if self.driver.get_browser_type() == "ios":
            element = self.driver.wait_and_find_element(By.XPATH, "",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button",
                                                        20)
        return element

    def edy_login_bt(self):
        if self.driver.get_browser_type() == "ios_kobiton":
            element = self.driver.wait_and_find_element(By.ID, "楽天ID, でログインする", 30)
            # element = self.driver.wait_and_find_element(By.XPATH, "//XCUIElementTypeButton[@name=\"楽天ID, でログインする\"]",
            #                                             10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH, "", 20)
        return element

    def edy_username(self):
        if self.driver.get_browser_type() == "ios_kobiton":
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "//XCUIElementTypeTextField[@name=\"jp.co.rakuten.sdk.ecosystemdemo:id/user__userid\"]",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH, "",
                                                        20)
        return element

    def edy_password(self):
        if self.driver.get_browser_type() == "ios_kobiton":
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "//XCUIElementTypeSecureTextField[@name=\"jp.co.rakuten.sdk.ecosystemdemo:id/user__password\"]",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH, "",
                                                        20)
        return element

    def edy_checkbox(self):
        if self.driver.get_browser_type() == "ios_kobiton":
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "//XCUIElementTypeButton[@name=\"jp.co.rakuten.sdk.ecosystemdemo:id/user__show_password\"]",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH, "",
                                                        20)
        return element

    def edy_submit(self):
        if self.driver.get_browser_type() == "ios_kobiton":
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "//XCUIElementTypeButton[@name=\"jp.co.rakuten.sdk.ecosystemdemo:id/user__login\"]",
                                                        10)
        else:
            element = self.driver.wait_and_find_element(By.XPATH, "",
                                                        20)
        return element
