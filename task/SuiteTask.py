import datetime
import time

from object.ProjectObject import ProjectObject
from object.SuiteObject import SuiteObject
from task.BaseTask import BaseTask
from util.TimeUtil import TimeUtil


class SuiteTask(BaseTask):

    def __init__(self, driver, data, capture, logger, atas_api):
        BaseTask.__init__(self, driver, data, capture, logger, atas_api)
        self.pro = ProjectObject(self.driver)
        self.suite = SuiteObject(self.driver)

    def create_suite(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        title = self.data['title']
        desc = self.data['description']
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

        # 二、开始操作。创建新的test suite
        # start_time = TimeUtil.get_current_time()
        if if_project:
            time.sleep(2)
            project_element = self.pro.project_to_case_btn()
            project_element.click()
        time.sleep(2)
        self.suite.new_suite_bt().click()
        time.sleep(1)
        self.suite.suite_title().send_keys(title + suffix_time)
        self.suite.suite_desc().send_keys(desc)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png",
                                                         "Create new suite")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Create new suite',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))
        self.suite.suite_save().click()
        # 三、结束操作。建立 ATAS run信息
        # end_time = TimeUtil.get_current_time()
        # self.result.set_run_data(
        #     {'caseName': 'create test suite success', 'path': '/Cases/Suite/',
        #      'stepDescription': 'New suite is created successfully', 'startTime': start_time,
        #      'endTime': end_time})
        time.sleep(3)
        # 四、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            suite_modal_window = self.suite.suite_modal_window()
            self.verify.verify_modal_window(suite_modal_window)
            # 校验点2：list成功新建suite
            actual_suite_name = self.suite.suite_in_list().text
            expect_suite_name = title + suffix_time
            # expect_suite_name = title
            self.verify.verify_test_suite_name(actual_suite_name, expect_suite_name)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "New suite is created")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('New suite is created',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))
