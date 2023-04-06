from object.LoginObject import LoginObject
from task.BaseTask import BaseTask
from util.TimeUtil import TimeUtil


class CommonTask(BaseTask):
    def __init__(self, driver, data, capture, logger, atas_api):
        self.case_desc = None
        BaseTask.__init__(self, driver, data, capture, logger, atas_api)

    def url(self):
        url_data = self.data['url']
        self.driver.get_driver().get(url_data)

    def desc(self):
        self.case_desc = self.data['desc']

    def login(self):
        case_desc = self.data['desc']
        name = self.data['login'].split(";")[0]
        password = self.data['login'].split(";")[1]
        login = LoginObject(self.driver)
        login.account_tab().click()
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Navigate to account tab")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Navigate to account tab",
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))
        login.user_name().send_keys(name)
        login.user_pwd().send_keys(password)
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png",
                                                         "Fill username amd password, then click login button")
        if self.if_upload_atas:
            self.atas_api.upload_result(
                self.result.get_upload_result("Fill username amd password, then click login button",
                                              self.capture.get_full_path(case_desc + "-2.png"),
                                              None, start_time,
                                              end_time))
        login.login_bt().click()
        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-3.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-3.png",
                                                         "Login success and navigate to all projects page")
        if self.if_upload_atas:
            self.atas_api.upload_result(
                self.result.get_upload_result("Login success and navigate to all projects page",
                                              self.capture.get_full_path(case_desc + "-3.png"),
                                              None, start_time,
                                              end_time))
        if login.new_project_bt() is not None:
            assert login.new_project_bt().is_enabled()
        else:
            self.logger.error('Login fail')
            assert False
