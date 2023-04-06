import time

from business.TravelVerify import TravelVerify
from object.TravelHomeObject import TravelHomeObject
from task.BaseTask import BaseTask
from util.TimeUtil import TimeUtil


class TravelHomeTask(BaseTask):
    def __init__(self, driver, data, capture, logger, atas_api):
        BaseTask.__init__(self, driver, data, capture, logger, atas_api)
        self.verify = TravelVerify(self.logger)

    def search_hotel(self):
        case_desc = self.data['case_desc']
        result = self.data['search_result']
        name = self.data['search_name']
        hotel = TravelHomeObject(self.driver)
        hotel.search_place().click()
        hotel.search_place_input().send_keys(name)
        hotel.search_select().click()
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Search place")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Search place',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        hotel.search_date().click()
        hotel.search_date_select().click()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Select date")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Select date',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

        hotel.complete_button().click()
        hotel.search_button().click()
        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-3.png")
        self.verify.verify_search_no_result(hotel.search_result().text, result)
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-3.png", "Not find results")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Not find results',
                                                                      self.capture.get_full_path(case_desc + "-3.png"),
                                                                      None, start_time,
                                                                      end_time))

    def login_hotel_i(self):
        case_desc = self.data['case_desc']
        result = self.data['login_result']
        name = self.data['username']
        hotel = TravelHomeObject(self.driver)
        hotel.order_icon().click()
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Click order icon")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Click order icon',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        hotel.login_button().click()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Click login button")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Click login button',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

        if self.driver.get_browser_type() == "ios":
            hotel.ensure_pop().click()
        if self.driver.get_browser_type() == "android":
            time.sleep(3)
            self.driver.navigate_to_webview()
        hotel.mail_input().click()
        hotel.mail_input().send_keys(name)
        self.capture.capture_all(case_desc + "-3.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-3.png", "Input mail and login")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Input mail and login',
                                                                      self.capture.get_full_path(case_desc + "-3.png"),
                                                                      None, start_time,
                                                                      end_time))

        hotel.ensure_button().click()
        if self.driver.get_browser_type() == "android":
            self.driver.navigate_to_app()
        self.verify.verify_login_fail(result, hotel.login_message().text)
        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-4.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-4.png", "Login fail")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Login fail',
                                                                      self.capture.get_full_path(case_desc + "-4.png"),
                                                                      None, start_time,
                                                                      end_time))

    def login_hotel(self):
        case_desc = self.data['case_desc']
        result = self.data['login_result']
        name = self.data['username']
        hotel = TravelHomeObject(self.driver)
        hotel.order_icon().click()
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Click order icon")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Click order icon',
                                                                      self.capture.get_full_path(case_desc + "1.png"),
                                                                      None, start_time,
                                                                      end_time))

        hotel.login_button().click()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Click login button")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Click login button',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

        time.sleep(5)
        self.driver.get_driver().press_keycode(32)
        self.driver.get_driver().press_keycode(37)
        self.driver.get_driver().press_keycode(42)
        self.driver.get_driver().press_keycode(35)
        self.driver.get_driver().press_keycode(48)
        self.driver.get_driver().press_keycode(29)
        self.driver.get_driver().press_keycode(43)
        self.driver.get_driver().press_keycode(77)
        self.driver.get_driver().press_keycode(8)
        self.driver.get_driver().press_keycode(13)
        self.driver.get_driver().press_keycode(10)
        self.driver.get_driver().press_keycode(56)
        self.driver.get_driver().press_keycode(31)
        self.driver.get_driver().press_keycode(43)
        self.driver.get_driver().press_keycode(41)
        self.capture.capture_all(case_desc + "-3.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-3.png", "Input mail and login")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Input mail and login',
                                                                      self.capture.get_full_path(case_desc + "-3.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.driver.get_driver().press_keycode(61)
        self.driver.get_driver().press_keycode(66)
        self.verify.verify_login_fail(result, hotel.login_message().text)
        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-4.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-4.png", "Login fail")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Login fail',
                                                                      self.capture.get_full_path(case_desc + "-4.png"),
                                                                      None, start_time,
                                                                      end_time))

    def kobiton_test(self):
        case_desc = self.data['case_desc']
        user_name = self.data['username']
        password = self.data['password']

        hotel = TravelHomeObject(self.driver)
        hotel.point_login_bt().click()
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Navigate to login page")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Navigate to login page',
                                                                      self.capture.get_full_path(case_desc + "1.png"),
                                                                      None, start_time,
                                                                      end_time))

        hotel.point_user().send_keys(user_name)
        hotel.point_passwd().send_keys(password)
        hotel.point_login_ensure().click()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Input username and password")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Input username and password',
                                                                      self.capture.get_full_path(case_desc + "2.png"),
                                                                      None, start_time,
                                                                      end_time))

        hotel.point_submit_bt().click()
        self.verify.verify_login_fail_bt(hotel.point_fail_bt())
        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-3.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-3.png", "Login fail")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Login fail',
                                                                      self.capture.get_full_path(case_desc + "3.png"),
                                                                      None, start_time,
                                                                      end_time))

    def kobiton_ios(self):
        case_desc = self.data['case_desc']
        user_name = self.data['username']
        password = self.data['password']

        hotel = TravelHomeObject(self.driver)
        hotel.edy_login_bt().click()
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Navigate to login page")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Navigate to login page',
                                                                      self.capture.get_full_path(case_desc + "1.png"),
                                                                      None, start_time,
                                                                      end_time))

        hotel.edy_username().send_keys(user_name)
        hotel.edy_password().send_keys(password)
        hotel.edy_checkbox().click()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Input username and password")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Input username and password',
                                                                      self.capture.get_full_path(case_desc + "2.png"),
                                                                      None, start_time,
                                                                      end_time))

        hotel.edy_submit().click()
        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-3.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-3.png", "Login fail")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Login fail',
                                                                      self.capture.get_full_path(case_desc + "3.png"),
                                                                      None, start_time,
                                                                      end_time))
