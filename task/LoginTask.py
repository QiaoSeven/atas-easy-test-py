import time

from object.LoginObject import LoginObject
from task.BaseTask import BaseTask

from util.TimeUtil import TimeUtil


class LoginTask(BaseTask):
    def __init__(self, driver, data, capture, logger, atas_api):
        BaseTask.__init__(self, driver, data, capture, logger, atas_api)
        self.login = LoginObject(self.driver)

    def login_with_auth_success(self):
        case_desc = self.data['case_desc']
        name = self.data['user_name']
        password = self.data['password']

        self.login.account_tab().click()
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Navigate to account tab")

        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Navigate to account tab',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.login.user_name().send_keys(name)
        self.login.user_pwd().send_keys(password)
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png",
                                                         "Fill username amd password, then click login button")
        if self.if_upload_atas:
            self.atas_api.upload_result(
                self.result.get_upload_result('Fill username amd password, then click login button',
                                              self.capture.get_full_path(case_desc + "-2.png"),
                                              None, start_time,
                                              end_time))
        self.login.login_bt().click()

        # self.verify.verify_new_project_bt(self.login.new_project_bt())
        end_time = TimeUtil.get_current_time()
        self.verify.verify_new_project_bt(self.login.new_project_bt())
        self.capture.capture_all(case_desc + "-3.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-3.png",
                                                         "Login success and navigate to all projects page")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Login success and navigate to all projects page',
                                                                      self.capture.get_full_path(case_desc + "-3.png"),
                                                                      None, start_time,
                                                                      end_time))

    def login_with_auth_fail(self):
        case_desc = self.data['case_desc']
        name = self.data['user_name']
        password = self.data['password']
        self.login.account_tab().click()
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Navigate to account tab")

        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Navigate to account tab',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))
        self.login.user_name().send_keys(name)
        self.login.user_pwd().send_keys(password)
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png",
                                                         "Fill wrong username and password, then click login button")
        if self.if_upload_atas:
            self.atas_api.upload_result(
                self.result.get_upload_result('Fill wrong username and password, then click login button',
                                              self.capture.get_full_path(case_desc + "-2.png"),
                                              None, start_time,
                                              end_time))
        self.login.login_bt().click()
        self.capture.capture_all(case_desc + "-3.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-3.png",
                                                         "Login fail and stay in login page")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Login fail and stay in login page',
                                                                      self.capture.get_full_path(case_desc + "-3.png"),
                                                                      None, start_time,
                                                                      end_time))
        # pop_element = self.login.login_fail_pop()
        # end_time = TimeUtil.get_current_time()
        # self.verify.verify_login_fail_pop(pop_element)
        # self.capture.capture_element(case_desc + "-4.png", pop_element)

        login_bt = self.login.login_bt_exist()
        end_time = TimeUtil.get_current_time()
        self.verify.verify_login_fail(login_bt)

        # pop_element = self.login.login_fail_pop()
        # end_time = TimeUtil.get_current_time()
        # self.verify.verify_login_fail_pop(pop_element)
        # self.capture.capture_element(case_desc + "-4.png", pop_element)
        self.capture.capture_all(case_desc + "-4.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-4.png",
                                                         "Login fail is expected")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Login fail is expected',
                                                                      self.capture.get_full_path(case_desc + "-4.png"),
                                                                      None, start_time,
                                                                      end_time))

    def logout(self):
        case_desc = self.data['case_desc']
        name = self.data['user_name']
        password = self.data['password']

        self.login.account_tab().click()
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Navigate to account tab")

        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Navigate to account tab',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.login.user_name().send_keys(name)
        self.login.user_pwd().send_keys(password)
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png",
                                                         "Fill username amd password, then click login button")
        if self.if_upload_atas:
            self.atas_api.upload_result(
                self.result.get_upload_result('Fill username amd password, then click login button',
                                              self.capture.get_full_path(case_desc + "-2.png"),
                                              None, start_time,
                                              end_time))

        self.login.login_bt().click()
        time.sleep(3)

        # self.verify.verify_new_project_bt(self.login.new_project_bt())
        self.capture.capture_all(case_desc + "-3.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-3.png",
                                                         "Login success and navigate to all projects page")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Login success and navigate to all projects page',
                                                                      self.capture.get_full_path(case_desc + "-3.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.login.logout_label().click()
        self.login.logout_button().click()
        end_time = TimeUtil.get_current_time()

        self.verify.verify_logout(self.login.account_tab())

        self.capture.capture_all(case_desc + "-4.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-4.png",
                                                         "Logout success and navigate to login page")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Logout success and navigate to login page',
                                                                      self.capture.get_full_path(case_desc + "-4.png"),
                                                                      None, start_time,
                                                                      end_time))

    def login_with_sso(self):
        case_desc = self.data['case_desc']

        self.login.login_sso_button().click()
        self.login.login_sso_input().send_keys("tao.ding@rakuten.com")
        self.login.login_okta_input().send_keys("tao.ding@rakuten.com")
        self.login.login_okta_password().send_keys("xxx")
        self.verify.verify_new_project_bt(self.login.new_project_bt())
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Login with sso successfully")
