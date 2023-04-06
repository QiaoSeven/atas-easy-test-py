import datetime
import platform
import time

from selenium.webdriver import Keys

from object.CaseObject import CaseObject
from object.ProjectObject import ProjectObject
from object.SuiteObject import SuiteObject
from task.BaseTask import BaseTask
from util.TimeUtil import TimeUtil


class CaseTask(BaseTask):

    def __init__(self, driver, data, capture, logger, atas_api):
        BaseTask.__init__(self, driver, data, capture, logger, atas_api)
        self.pro = ProjectObject(self.driver)
        self.suite = SuiteObject(self.driver)
        self.case = CaseObject(self.driver)

    # def create_case(self, if_verify):
    #     case_desc = self.data['case_desc']
    #     name = self.data['name']
    #     desc = self.data['description']
    #     case = self.data['case']
    #     precondition = self.data['precondition']
    #     steps = self.data['steps']
    #     expect = self.data['expect']
    #     suffix_time = str(int(time.time()))
    #     self.if_upload_rp = strtobool(CoreConfig.if_report_portal())
    #     project_element = self.pro.project_to_case_btn()
    #     project_element.click()
    #     suite_element = self.suite.get_first_suite()
    #     suite_element.click()
    #     self.case.new_section().click()
    #     self.case.add_section().click()
    #     self.case.parent_section().click()
    #     self.case.parent_section_item().click()
    #     self.case.section_name().send_keys(name + suffix_time)
    #     self.case.section_desc().send_keys(desc)
    #     self.case.save_section().click()
    #     self.capture.capture_all(case_desc + "-1.png")
    #     if self.if_upload_rp:
    #         self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Add new section")
    #     self.case.new_case().click()
    #     self.case.case_name().send_keys(case + suffix_time)
    #     self.case.section_select().click()
    #     self.case.section_select_last_item().click()
    #     self.case.case_template().click()
    #     time.sleep(1)
    #     self.case.case_template_item().click()
    #     self.case.precondition().send_keys(precondition)
    #     self.case.add_step().click()
    #     self.case.steps().send_keys(steps)
    #     self.case.expect().send_keys(expect)
    #     self.case.save_close().click()
    #     time.sleep(5)
    #     if "opened" not in self.case.section_if_collapse().get_attribute("class"):
    #         self.case.section_collapse_button().click()
    #     if if_verify:
    #         actual_case_name = self.case.list_case_name().text
    #         expect_case_name = case + suffix_time
    #         self.verify.verify_case_list(actual_case_name, expect_case_name)
    #     self.capture.capture_all(case_desc + "-2.png")
    #     if self.if_upload_rp:
    #         self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Add new case")

    def create_case(self, if_project, if_suite, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        section_name = self.data['section_name']
        desc = self.data['description']
        case_name = self.data['case_name']
        priority = self.data['priority']
        estimation = self.data['estimation']
        precondition = self.data['precondition']
        steps = self.data['step_desc']
        step_num = int(self.data['step_num'])
        expect = self.data['expect_result']
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        # 二、开始操作。创建新的test case
        if if_project:
            time.sleep(2)
            project_element = self.pro.project_to_case_btn()
            project_element.click()
        if if_suite:
            time.sleep(2)
            suite_element = self.suite.get_first_suite()
            suite_element.click()
        time.sleep(2)
        self.case.new_section().click()
        time.sleep(0.5)
        self.case.add_section().click()
        time.sleep(0.5)
        self.case.parent_section().click()
        time.sleep(0.5)
        self.case.parent_section_item().click()
        self.case.section_name().send_keys(section_name + suffix_time)
        self.case.section_desc().send_keys(desc)
        self.case.save_section().click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Create new section")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Create new section',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        # self.driver.page_refresh()
        time.sleep(3)
        self.case.new_case().click()
        self.case.case_name().send_keys(case_name + suffix_time)
        self.case.section_select().click()
        time.sleep(0.5)
        self.case.section_select_last_item().click()

        self.case.case_priority_open().click()
        time.sleep(0.5)
        self.case.case_priority_dropdown(priority).click()
        self.case.case_estimation().click()
        self.case.case_estimation().send_keys(estimation)
        self.case.precondition().send_keys(precondition)
        i = 1
        while i <= step_num:
            self.case.add_step().click()
            time.sleep(0.5)
            self.case.steps().send_keys(steps)
            time.sleep(0.5)
            self.case.expect().send_keys(expect)
            i += 1

        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Create new case")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Create new case',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.case.save_close().click()
        time.sleep(5)
        if "opened" not in self.case.section_if_collapse().get_attribute("class"):
            self.case.section_collapse_button().click()
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            case_modal_window = self.case.case_modal_window()
            self.verify.verify_modal_window(case_modal_window)
            # 校验点2：case name更新
            actual_case_name = self.case.list_case_name().text
            expect_case_name = case_name + suffix_time
            self.verify.verify_case_list(actual_case_name, expect_case_name)
            # 校验点3：case priority更新
            actual_case_prio = self.case.list_case_priority().text
            expect_case_prio = priority
            self.verify.verify_case_list(actual_case_prio, expect_case_prio)
            # 校验点4：case estimation更新
            actual_case_est = self.case.list_case_estimation().text
            expect_case_est = str(estimation) + " min(s)"
            self.verify.verify_case_list(actual_case_est, expect_case_est)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-3.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-3.png", "New case is created")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('New case is created',
                                                                      self.capture.get_full_path(case_desc + "-3.png"),
                                                                      None, start_time,
                                                                      end_time))

    def delete_case(self, if_project, if_suite, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        # 二、开始操作。删除最后1个test case
        if if_project:
            project_element = self.pro.project_to_case_btn()
            project_element.click()
        if if_suite:
            time.sleep(2)
            suite_element = self.suite.get_first_suite()
            suite_element.click()
        time.sleep(2)
        deleted_case_name = self.case.list_case_name().text
        self.driver.action_hover(self.case.section_delete_check_icon())

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Select one case's section to be deleted")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Select one case's section to be deleted",
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))
        self.case.section_delete_icon_button().click()
        self.case.section_delete_yes_button().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            delete_modal_window = self.case.section_delete_modal_window()
            self.verify.verify_modal_window(delete_modal_window)
            # 校验点2：确认case被删除
            names = []
            cases = self.case.case_names_list()
            for case_list in cases:
                name = case_list.text
                names.append(name)
            self.verify.verify_delete(names, deleted_case_name)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Delete section with case successfully")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Delete section with case successfully",
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def create_filter(self, if_project, which_column, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        filter_name = self.data['filter_name']
        column_name = self.data['column_name']
        condition = self.data['condition_name']
        criteria = self.data['criteria_name']
        column = self.data['column_select']
        # suffix_time = str(int(time.time()))
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        # 二、开始操作。创建新的filter
        if if_project:
            project_element = self.pro.project_to_case_btn()
            project_element.click()
        self.case.filter_view().click()
        self.case.new_test_case_filter_btn().click()
        time.sleep(1)
        self.case.filter_information_filter_name().send_keys(filter_name + suffix_time)
        self.case.filter_criteria_column_name_arrow_icon().click()
        time.sleep(0.5)
        self.case.filter_criteria_column_name_dropdown(column_name).click()
        self.case.filter_criteria_condition_arrow_icon().click()
        time.sleep(0.5)
        self.case.filter_criteria_condition_dropdown(condition).click()
        time.sleep(1)
        dropdown_exist = self.verify.verify_filter_criteria_dropdown(self.case.filter_criteria_criteria_arrow_icon())
        if dropdown_exist:
            self.case.filter_criteria_criteria_textbox().click()
            time.sleep(0.5)
            self.case.filter_criteria_criteria_dropdown(criteria).click()
        else:
            self.case.filter_criteria_criteria_textbox().send_keys(criteria)

        if which_column == "Single":
            self.case.filter_columns_select_single(column).click()
        elif which_column == "All":
            self.case.filter_columns_select_all().click()
        else:
            # which_column == "None"
            pass

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Create new filter")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Create new filter",
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))
        self.case.filter_save_btn().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            create_filter_modal_window = self.case.filter_modal_window()
            self.verify.verify_modal_window(create_filter_modal_window)
            # 校验点2：左侧列表中新增正确的filter名称
            actual_created_filter_name = self.case.last_filter_name().text
            expect_created_filter_name = filter_name + suffix_time
            self.verify.verify_consistent_display(actual_created_filter_name, expect_created_filter_name)
            # 校验点3：搜索结果的表头新增正确的column列(如果是选择显示所有列或不增加列，则不进行该校验)
            actual_filter_result_new_column = self.case.filter_results_list_new_column().text
            expect_filter_result_new_column = column
            if which_column == "Single":
                self.verify.verify_consistent_display(actual_filter_result_new_column, expect_filter_result_new_column)
            # 校验点4：搜索结果的表头的第一列始终是Case Name
            actual_filter_result_first_column = self.case.filter_results_list_first_column().text
            expect_filter_result_first_column = "Case Name"
            self.verify.verify_consistent_display(actual_filter_result_first_column, expect_filter_result_first_column)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "New filter is created")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("New filter is created",
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def edit_filter(self, if_project, if_verify, browser_data):
        # 一、准备数据
        case_desc = self.data['case_desc']
        new_filter_name = self.data['new_filter_name']
        # suffix_time = str(int(time.time()))
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        # 二、开始操作。编辑最后一个filter
        if if_project:
            project_element = self.pro.project_to_case_btn()
            project_element.click()
            self.case.filter_view().click()
        self.driver.action_move_click(self.case.filter_action_check_icon())
        self.case.filter_edit_icon_button().click()
        self.case.filter_information_filter_name().click()
        plat = platform.system().lower()
        if plat == "darwin" and ('remote' not in str(browser_data)):
            self.case.filter_information_filter_name().send_keys(Keys.COMMAND, "a")
        else:
            self.case.filter_information_filter_name().send_keys(Keys.CONTROL, "a")
        self.case.filter_information_filter_name().send_keys(Keys.DELETE)
        self.case.filter_information_filter_name().send_keys(new_filter_name + suffix_time)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Edit created filter")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Edit created filter",
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))
        self.case.filter_save_btn().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            edit_filter_modal_window = self.case.filter_modal_window()
            self.verify.verify_modal_window(edit_filter_modal_window)
            # 校验点2：test case filter的名字成功更新
            actual_filter_new_name = self.case.last_filter_name().text
            expect_filter_new_name = new_filter_name + suffix_time
            self.verify.verify_consistent_display(actual_filter_new_name, expect_filter_new_name)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Created filter is edited")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Created filter is edited",
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def delete_filter(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        # 二、开始操作。删除最后一个filter
        if if_project:
            project_element = self.pro.project_to_case_btn()
            project_element.click()
            self.case.filter_view().click()
        deleted_filter_name = self.case.last_filter_name().text
        self.driver.action_move_click(self.case.filter_action_check_icon())
        self.case.filter_delete_icon_button().click()
        time.sleep(0.5)
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Delete created filter")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Delete created filter",
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.case.filter_delete_yes_button().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            delete_filter_modal_window = self.case.delete_filter_modal_window()
            self.verify.verify_modal_window(delete_filter_modal_window)
            # 校验点2：确认filter被删除
            names = []
            filters = self.case.filter_names_list()
            for filter_list in filters:
                name = filter_list.text
                names.append(name)
            self.verify.verify_delete(names, deleted_filter_name)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Created filter is deleted")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Created filter is deleted",
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))
