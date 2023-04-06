import datetime
import os
import platform
import re
import time

from selenium.webdriver.common.keys import Keys

from object.ProjectObject import ProjectObject
from object.RunObject import RunObject
from task.BaseTask import BaseTask
from util.TimeUtil import TimeUtil


class RunTask(BaseTask):
    def __init__(self, driver, data, capture, logger, atas_api):
        BaseTask.__init__(self, driver, data, capture, logger, atas_api)
        self.pro = ProjectObject(self.driver)
        self.run = RunObject(self.driver)

    def create_run(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        run_name = self.data['run_name']
        desc = self.data['run_description']
        # suffix_time = str(int(time.time()))
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        # 二、开始操作。创建新的test run
        if if_project:
            project_element = self.pro.project_to_run_btn()
            project_element.click()
        self.run.new_test_run_btn().click()
        time.sleep(1)
        self.run.test_run_name().send_keys(run_name + suffix_time)
        self.run.test_run_description().send_keys(desc)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Create new test run")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Create new test run',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.run.save_run_btn().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            create_run_modal_window = self.run.run_modal_window()
            self.verify.verify_modal_window(create_run_modal_window)
            # 校验点2：run列表新增正确的run名称
            actual_run_name = self.run.run_list_first_run().text
            expect_run_name = run_name + suffix_time
            self.verify.verify_run_list(actual_run_name, expect_run_name)
            # 校验点3：run列表新增正确的desc名称
            actual_run_desc = self.run.run_list_desc().text
            expect_run_desc = desc
            self.verify.verify_contain_text(actual_run_desc, expect_run_desc)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "New test run is created")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('New test run is created',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def edit_run(self, if_project, where, if_verify, browser_data):
        # 一、准备数据
        case_desc = self.data['case_desc']
        new_run_name = self.data['new_run_name']
        new_description = self.data['new_description']
        new_start_date = self.data['new_start_date']
        new_end_date = self.data['new_end_date']
        new_test_level = self.data['new_test_level']
        new_exec_type = self.data['new_exec_type']
        new_test_env = self.data['new_test_env']
        new_cal_pass_by = self.data['new_cal_pass_by']
        # suffix_time = str(int(time.time()))
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        plat = platform.system().lower()
        # 二、开始操作。编辑第一个test run
        if if_project:
            project_element = self.pro.project_to_run_btn()
            project_element.click()
        if where == "Run List Page":
            self.run.run_list_actions_btn().click()
            self.run.action_edit().click()
        else:
            # where == "Run Detail Page"
            suite_element = self.run.run_list_first_run()
            suite_element.click()
            time.sleep(1)
            self.run.start_test_arrow_icon().click()
            self.run.edit_run().click()
        self.run.test_run_name().click()
        if plat == "darwin" and ('remote' not in str(browser_data)):
            self.run.test_run_name().send_keys(Keys.COMMAND, "a")
        else:
            self.run.test_run_name().send_keys(Keys.CONTROL, "a")
        self.run.test_run_name().send_keys(Keys.DELETE)
        self.run.test_run_name().send_keys(new_run_name + suffix_time)
        self.run.run_desc().click()
        if plat == "darwin" and ('remote' not in str(browser_data)):
            self.run.run_desc().send_keys(Keys.COMMAND, "a")
        else:
            self.run.run_desc().send_keys(Keys.CONTROL, "a")
        self.run.run_desc().send_keys(Keys.DELETE)
        self.run.run_desc().send_keys(new_description)
        self.run.run_start_date().click()
        if plat == "darwin" and ('remote' not in str(browser_data)):
            self.run.run_start_date().send_keys(Keys.COMMAND, "a")
        else:
            self.run.run_start_date().send_keys(Keys.CONTROL, "a")
        self.run.run_start_date().send_keys(Keys.DELETE)
        self.run.run_start_date().send_keys(new_start_date)
        self.run.run_start_date().send_keys(Keys.ENTER)
        self.run.run_end_date().click()
        if plat == "darwin" and ('remote' not in str(browser_data)):
            self.run.run_end_date().send_keys(Keys.COMMAND, "a")
        else:
            self.run.run_end_date().send_keys(Keys.CONTROL, "a")
        self.run.run_end_date().send_keys(Keys.DELETE)
        self.run.run_end_date().send_keys(new_end_date)
        self.run.run_end_date().send_keys(Keys.ENTER)
        self.run.run_test_level_open().click()
        time.sleep(0.5)
        self.run.run_test_level_dropdown(new_test_level).click()
        self.run.run_execution_type_open().click()
        time.sleep(0.5)
        self.run.run_execution_type_dropdown(new_exec_type).click()
        self.run.run_test_env_open().click()
        time.sleep(0.5)
        self.run.run_test_env_dropdown(new_test_env).click()
        self.run.run_test_env_open().click()
        self.run.run_cal_pass_ratio_radio(new_cal_pass_by).click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Edit created test run")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Edit created test run',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.run.save_run_btn().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            edit_run_modal_window = self.run.run_modal_window()
            self.verify.verify_modal_window(edit_run_modal_window)
            if where == "Run List Page":
                actual_run_name = self.run.run_list_first_run().text
                actual_run_desc = self.run.run_list_desc().text
                dates = self.run.run_list_dates().text
                actual_run_start_date = "".join(re.findall(r'^(.*?)\/', dates))
                actual_run_end_date = "".join(re.findall('(?<=/).*$', dates))
                actual_run_test_level = self.run.run_list_test_level().text
                actual_run_exec_type = self.run.run_list_exec_type().text
                actual_run_test_env = self.run.run_list_test_env().text
                # 校验点2：run description成功更新
                expect_run_desc = new_description
                self.verify.verify_contain_text(actual_run_desc, expect_run_desc)
            else:
                # where == "Run Detail Page"
                actual_run_name = self.run.run_detail_run_name().text
                actual_run_start_date = self.run.run_detail_start_date().text
                actual_run_end_date = self.run.run_detail_end_date().text
                actual_run_test_level = self.run.run_detail_test_level().text
                actual_run_exec_type = self.run.run_detail_exec_type().text
                actual_run_test_env = self.run.run_detail_test_env().text
            # 校验点3：test run的名字成功更新
            expect_run_name = new_run_name + suffix_time
            self.verify.verify_consistent_display(actual_run_name, expect_run_name)
            # 校验点4：date成功更新
            expect_run_start_date = new_start_date
            self.verify.verify_contain_text(actual_run_start_date, expect_run_start_date)
            expect_run_end_date = new_end_date
            self.verify.verify_contain_text(actual_run_end_date, expect_run_end_date)
            # 校验点5：test level成功更新
            expect_run_test_level = new_test_level
            self.verify.verify_consistent_display(actual_run_test_level, expect_run_test_level)
            # 校验点6：exec type成功更新
            expect_run_exec_type = new_exec_type
            self.verify.verify_consistent_display(actual_run_exec_type, expect_run_exec_type)
            # 校验点7：test env成功更新
            expect_run_test_env = new_test_env
            self.verify.verify_consistent_display(actual_run_test_env, expect_run_test_env)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Created test run is edited")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Created test run is edited',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def duplicate_run(self, if_project, if_reset, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        # 二、开始操作。复制第一个test run
        if if_project:
            project_element = self.pro.project_to_run_btn()
            project_element.click()
        before_status = self.run.run_list_status().text
        before_ratio = self.run.run_list_passed_ratio().text
        run_name = self.run.run_list_first_run().text
        copied_count_before = run_name.count('Copied')
        self.run.run_list_actions_btn().click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Duplicate test run")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Duplicate test run',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        if if_reset:
            self.run.action_duplicate_and_reset().click()
        else:
            self.run.action_duplicate().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：复制的run出现在第1行; 复制的run的名字包含名称
            actual_copied_run_name = self.run.run_list_first_run().text
            expect_copied_run_name_front = run_name
            self.verify.verify_contain_text(actual_copied_run_name, expect_copied_run_name_front)
            # 校验点2：复制的run的名字新增一个Copied
            copied_count_after = actual_copied_run_name.count('Copied')
            self.verify.verify_copied_run_name(copied_count_after, copied_count_before)
            if if_reset:
                # 校验点3：复制并重置的run的status是Not Started，Pass Ratio是0
                actual_reset_status = self.run.run_list_status().text
                expect_reset_status = "Not Started"
                self.verify.verify_duplicate_and_reset_run(actual_reset_status, expect_reset_status)
                actual_reset_ratio = self.run.run_list_passed_ratio().text
                expect_reset_ratio = "0.0%"
                self.verify.verify_duplicate_and_reset_run(actual_reset_ratio, expect_reset_ratio)
            else:
                # 校验点3：复制的run的status和Pass Ratio不变
                after_status = self.run.run_list_status().text
                self.verify.verify_duplicate_run(after_status, before_status)
                after_ratio = self.run.run_list_passed_ratio().text
                self.verify.verify_duplicate_run(after_ratio, before_ratio)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Test run is duplicated")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Test run is duplicated',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def delete_run(self, if_project, where, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        # 二、开始操作。删除第一个test run
        if if_project:
            project_element = self.pro.get_first_project()
            project_element.click()
        deleted_name = self.run.run_list_first_run().text
        if where == "Run List Page":
            self.run.run_list_actions_btn().click()
            self.run.action_delete().click()
            time.sleep(0.5)
        else:
            # where == "Run Detail Page"
            self.run.run_list_first_run().click()
            self.run.start_test_arrow_icon().click()
            self.run.delete_run().click()
            time.sleep(0.5)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Delete created run")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Delete created run',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.run.delete_yes_button().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            delete_modal_window = self.run.run_delete_modal_window()
            self.verify.verify_modal_window(delete_modal_window)
            # 校验点2：确认run被删除
            names = []
            runs = self.run.run_names_list()
            for run_list in runs:
                name = run_list.text
                names.append(name)
            self.verify.verify_delete(names, deleted_name)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Created run is deleted")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Created run is deleted',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def edit_run_scope(self, if_project, if_list_page, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        section = self.data['section_select']
        # 二、开始操作。编辑run的case scope
        if if_project:
            project_element = self.pro.project_to_run_btn()
            project_element.click()
        if if_list_page:
            self.run.run_list_first_run().click()
        self.run.edit_scope_btn().click()
        self.run.suite_add_btn().click()
        self.run.suite_select_placeholder().click()
        self.run.suite_dropdown().click()
        self.run.section_item(section).click()
        if "checked" not in self.run.checkbox_case().get_attribute("class"):
            self.run.checkbox_case().click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Edit scope of test run")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Edit scope of test run',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        scope_lists = []
        scope_cases = self.run.scope_page_case_list()
        for scope_case in scope_cases:
            scope_list = scope_case.text
            scope_lists.append(scope_list)
        self.run.save_case().click()
        time.sleep(3)
        if "opened" not in self.run.section_if_collapse().get_attribute("class"):
            self.run.section_collapse_button().click()
        # 三、校验结果
        if if_verify:
            case_lists = []
            run_cases = self.run.run_page_case_list()
            for run_case in run_cases:
                case_list = run_case.text
                case_lists.append(case_list)
            self.verify.verify_scope_to_run(case_lists, scope_lists)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Scope of test run is edited")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Scope of test run is edited',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def assign_cases(self, if_project, if_list_page, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        select_case = self.data['select_case']
        assign_to = self.data['assign_to']
        user_name = self.data['user_name']
        # 二、开始操作。分配run detail page的cases
        if if_project:
            project_element = self.pro.project_to_run_btn()
            project_element.click()
            time.sleep(1)
        if if_list_page:
            self.run.run_list_first_run().click()
            time.sleep(3)
        if select_case != 'All':
            no_assignee_exist = self.verify.verify_no_assignee_exist(self.run.run_detail_no_assign_btn())
            if no_assignee_exist:
                time.sleep(1)
                self.run.run_detail_first_no_assign_btn().click()
                before_assign_id = self.run.run_detail_first_no_assign_id().text
            else:
                self.logger.info('Message: All cases have been assigned. Will assign the first case')
                self.run.run_detail_first_assign_btn().click()
        else:
            # select_case == 'All'
            time.sleep(1)
            self.run.run_detail_select_all_icon().click()
            time.sleep(1)
            self.run.run_detail_assign_to_btn().click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Assign cases in test run")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Assign cases in test run',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.run.run_detail_assign_dropdown(assign_to).click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：assignee成功更新
            if select_case != 'All':
                if no_assignee_exist:
                    actual_assignee = self.run.run_detail_id_to_assignee(before_assign_id).text
                    a_a = re.sub(re.compile(r'\s+'), "", actual_assignee)
                else:
                    actual_assignee = self.run.run_detail_first_assign_text().text
                    a_a = re.sub(re.compile(r'\s+'), '', actual_assignee)
                if assign_to == 'me':
                    expect_assignee = user_name
                else:
                    expect_assignee = assign_to
                self.verify.verify_case_assignee(a_a, expect_assignee)
            else:
                # select_case == 'All'
                names = []
                rows = self.run.run_detail_assignee_list()
                for row in rows:
                    name = re.sub(re.compile(r'\s+'), "", row.text)
                    names.append(name)
                if assign_to == 'me':
                    expect_assignee = user_name
                else:
                    expect_assignee = assign_to
                self.verify.verify_cases_assignee(names, expect_assignee)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Cases in test run are assigned")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Cases in test run are assigned',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def filter_cases(self, if_project, if_list_page, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        priority = self.data['fil_priority']
        assignee = self.data['fil_assignee']
        status = self.data['fil_status']
        # 二、开始操作。筛选run detail page的cases
        if if_project:
            project_element = self.pro.project_to_run_btn()
            project_element.click()
        if if_list_page:
            self.run.run_list_first_run().click()
        self.run.all_priorities_arrow_icon().click()
        time.sleep(0.5)
        self.run.all_priorities_dropdown(priority).click()
        self.run.all_assignees_arrow_icon().click()
        time.sleep(2)
        if_assignee = self.verify.verify_assignee_exist(self.run.all_assignees_none())
        if if_assignee:
            self.run.all_assignees_dropdown(assignee).click()
        self.run.all_status_arrow_icon().click()
        time.sleep(0.5)
        self.run.all_status_dropdown(status).click()
        self.run.all_assignees_arrow_icon().click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Filter cases in test run")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Filter cases in test run',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：filter的显示和选择的一致
            # priority
            actual_priority_name = self.run.all_priorities_selected().text
            expect_priority_name = priority
            self.verify.verify_priority_filter(actual_priority_name, expect_priority_name)
            # assignee
            if if_assignee:
                actual_assignee_name = self.run.all_assignees_selected().text
                expect_assignee_name = assignee
                self.verify.verify_assignee_filter(actual_assignee_name, expect_assignee_name)
            # status
            actual_status_name = self.run.all_status_selected().get_attribute('xlink:href')
            expect_status_name = status
            self.verify.verify_status_filter(actual_status_name, expect_status_name)

            no_data = self.run.no_data()
            self.verify.verify_no_data(no_data)

            # 校验点2：所有filter结果符合选中的filter
            # priority
            p_names = []
            p_rows = self.run.all_priorities_result_list()
            for p_row in p_rows:
                p_name = p_row.text
                p_names.append(p_name)
            self.verify.verify_priority_result(p_names, priority)
            # assignee
            if if_assignee:
                a_names = []
                a_rows = self.run.all_assignees_result_list()
                for a_row in a_rows:
                    a_name = a_row.text
                    a_names.append(a_name)
                self.verify.verify_assignee_result(a_names, assignee)
            # status
            s_names = []
            s_rows = self.run.all_status_result_list()
            for s_row in s_rows:
                s_name = s_row.text
                s_names.append(s_name)
            self.verify.verify_status_result(s_names, status)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Cases in test run are filtered")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Cases in test run are filtered",
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def search_cases(self, if_project, if_list_page, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        search_keyword = self.data['search_keyword']
        # 二、开始操作。搜索run detail page的cases
        if if_project:
            project_element = self.pro.project_to_run_btn()
            project_element.click()
        if if_list_page:
            self.run.run_list_first_run().click()
        time.sleep(1)
        self.run.search_bar().click()
        self.run.search_bar().send_keys(search_keyword)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Search cases in test run")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Search cases in test run',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        time.sleep(1)
        self.run.search_icon().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            no_data = self.run.no_data()
            self.verify.verify_no_data(no_data)

            # 校验点1：搜索结果都包含搜索关键字
            names = []
            rows = self.run.search_result_list()
            for row in rows:
                name = row.text
                names.append(name)
            self.verify.verify_status_result(names, search_keyword)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Cases in test run are searched")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Cases in test run are searched',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    # def execute_run(self, verify_points):
    #     case_desc = self.data['case_desc']
    #     self.if_upload_rp = strtobool(CoreConfig.if_report_portal())
    #     project_element = self.pro.project_to_run_btn()
    #     project_element.click()
    #     suite_element = self.run.run_list_last_run()
    #     suite_element.click()
    #     self.run.start_test_btn().click()
    #     self.run.first_case_name().click()
    #     self.run.add_result().click()
    #     time.sleep(3)
    #     # self.run.step_hover()
    #     self.run.pass_fail_button(verify_points).click()
    #     self.run.submit_next().click()
    #     time.sleep(1)
    #     self.run.plan_menu().click()
    #     time.sleep(3)
    #     expect_case_execution = self.data['expect_execute_rate']
    #     actual_case_execution = self.run.actual_case_rate().text
    #     self.verify.verify_run_rate(actual_case_execution, expect_case_execution)
    #     self.capture.capture_all(case_desc + "-1.png")
    #     if self.if_upload_rp:
    #         self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Execute test run")

    def execute_case(self, if_project, if_list_page, if_detail_page, where_start, if_attach, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        exec_option = self.data['exec_option']
        case_status = self.data['case_status']
        case_effort = self.data['case_effort']
        jira_issue = self.data['jira_issue']
        file_path = self.data['file_path']
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = curPath[:curPath.find("atas-easy-test-py") + len("atas-easy-test-py")]
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()

        if (case_status == 'Retest' or case_status == 'Pass') and exec_option == 'Add Result + Issue':
            self.logger.info('Cannot raise issue when retest/pass case. Will change case status to Fail')
            case_status = 'Fail'
        # 二、开始操作。执行第一个untested的case或第一个case
        if if_project:
                project_element = self.pro.project_to_run_btn()
                project_element.click()
                time.sleep(1)
        if if_list_page:
                self.run.run_list_first_run().click()
                time.sleep(3)
        if if_detail_page:
                if where_start == 'Untest':
                    untest_exist = self.verify.verify_untest_case_exist(self.run.run_detail_untest_case_name())
                    if untest_exist:
                        time.sleep(1)
                        self.run.run_detail_first_untest_case_name().click()
                    else:
                        self.logger.info('No untested cases. Will execute the first case')
                        time.sleep(1)
                        self.run.run_detail_first_case_name().click()
                else:
                    # where_start == 'First'
                    time.sleep(1)
                    self.run.run_detail_first_case_name().click()
        time.sleep(3)
        if "last" in self.run.case_list_selected_case().get_attribute('class'):
                case_last = True
        else:
                case_last = False
        exec_case_id = self.run.case_list_selected_case_id().text
        if if_attach:
                attach_exist = self.verify.verify_attach_exist(self.run.case_detail_attachment_title())
                if attach_exist:
                    a_rows = self.run.case_detail_attachment_list()
                    previous_attach_count = len(a_rows)
                else:
                    previous_attach_count = 0
        if exec_option == "Add Result + Close":
                time.sleep(2)
                self.run.add_result_btn().click()
                time.sleep(0.5)
                self.run.case_effort_min().click()
                self.run.case_effort_min().send_keys(case_effort)
                time.sleep(0.5)
                if if_attach:
                    upload = self.run.add_attachment()
                    time.sleep(1)
                    upload.send_keys(rootPath + file_path)
                    time.sleep(1)
                self.run.add_result_status_option(case_status).click()
                time.sleep(0.5)

                self.capture.capture_all(case_desc + "-1.png")
                if self.if_upload_rp:
                    self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Execute case by add result")
                if self.if_upload_atas:
                    self.atas_api.upload_result(self.result.get_upload_result('Execute case by add result',
                                                                              self.capture.get_full_path(
                                                                                  case_desc + "-1.png"),
                                                                              None, start_time,
                                                                              end_time))

                self.run.submit_and_next_arrow_icon().click()
                time.sleep(1)
                self.run.submit_and_close().click()
        elif exec_option == "Add Result + Next":
                time.sleep(2)
                self.run.add_result_btn().click()
                time.sleep(0.5)
                self.run.case_effort_min().click()
                self.run.case_effort_min().send_keys(case_effort)
                time.sleep(0.5)
                if if_attach:
                    upload = self.run.add_attachment()
                    time.sleep(1)
                    upload.send_keys(rootPath + file_path)
                    time.sleep(1)
                self.run.add_result_status_option(case_status).click()
                time.sleep(0.5)

                self.capture.capture_all(case_desc + "-1.png")
                if self.if_upload_rp:
                    self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Execute case by add result")
                if self.if_upload_atas:
                    self.atas_api.upload_result(self.result.get_upload_result('Execute case by add result',
                                                                              self.capture.get_full_path(
                                                                                  case_desc + "-1.png"),
                                                                              None, start_time,
                                                                              end_time))

                self.run.submit_and_next_btn().click()
        elif exec_option == "Add Result + Issue":
                previous_issue_count = self.run.case_page_issue_num().text
                time.sleep(2)
                self.run.case_issues_tab().click()
                time.sleep(0.5)
                issue_ids = []
                id_list = self.run.case_issue_id_all()
                for id_row in id_list:
                    name = id_row.text
                    issue_ids.append(name)
                time.sleep(2)
                self.run.case_details_tab().click()
                time.sleep(0.5)
                self.run.add_result_btn().click()
                time.sleep(0.5)
                self.run.case_effort_min().click()
                self.run.case_effort_min().send_keys(case_effort)
                time.sleep(0.5)
                if if_attach:
                    upload = self.run.add_attachment()
                    time.sleep(1)
                    upload.send_keys(rootPath + file_path)
                    time.sleep(1)
                self.run.add_result_status_option(case_status).click()
                time.sleep(0.5)

                self.capture.capture_all(case_desc + "-1.png")
                if self.if_upload_rp:
                    self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Execute case by add result")
                if self.if_upload_atas:
                    self.atas_api.upload_result(self.result.get_upload_result('Execute case by add result',
                                                                              self.capture.get_full_path(
                                                                                  case_desc + "-1.png"),
                                                                              None, start_time,
                                                                              end_time))

                self.run.submit_and_next_arrow_icon().click()
                time.sleep(0.5)
                self.run.submit_and_raise_issue().click()
                self.run.link_to_issue_radio().click()
                self.run.link_to_issue_input().click()
                self.run.link_to_issue_input().send_keys(jira_issue)
                self.run.link_to_issue_search().click()
                self.run.link_to_issue_link().click()
        else:
                # exec_option == "Pass All and Next"
                time.sleep(2)

                self.capture.capture_all(case_desc + "-1.png")
                if self.if_upload_rp:
                    self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Execute case by pass all and next")
                if self.if_upload_atas:
                    self.atas_api.upload_result(self.result.get_upload_result('Execute case by pass all and next',
                                                                              self.capture.get_full_path(
                                                                                  case_desc + "-1.png"),
                                                                              None, start_time,
                                                                              end_time))

                self.run.pass_all_and_next_btn().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
                # 校验点1：自动选中下一条case（只有1条case/执行最后1条case时不校验）
                if "Next" in exec_option:
                    if not case_last:
                        pre_case_id = self.run.case_list_above_selected_case_id().text
                        self.verify.verify_select_next_case(exec_case_id, pre_case_id)
                # 校验点2：case的状态更新为正确的status
                if "Next" in exec_option:
                    if case_last:
                        actual_case_status = self.run.case_list_selected_case_status().get_attribute('xlink:href')
                    else:
                        # not case_last
                        actual_case_status = self.run.case_list_above_selected_case_status().get_attribute('xlink:href')
                else:
                    actual_case_status = self.run.case_list_selected_case_status().get_attribute('xlink:href')
                if exec_option == "Pass All and Next":
                    expect_case_status = "Pass"
                else:
                    expect_case_status = case_status
                self.verify.verify_case_status(actual_case_status, expect_case_status)
                # 校验点3：所有step的状态更新为pass（只针对Pass All and Next）
                if exec_option == "Pass All and Next":
                    self.run.case_list_above_selected_case().click()
                    time.sleep(0.5)
                    names = []
                    s_rows = self.run.pass_all_steps_list()
                    for s_row in s_rows:
                        name = s_row.get_attribute('xlink:href')
                        names.append(name)
                    self.verify.verify_step_status(names, "Pass")
                # 校验点4：issue被添加
                if exec_option == "Add Result + Issue":
                    after_issue_count = self.run.case_page_issue_num().text
                    if self.verify.verify_issue_duplicate(jira_issue, issue_ids):
                        self.logger.info('Message: Add the same issue. The count will not increase')
                        self.verify.verify_link_same_issue(previous_issue_count, after_issue_count)
                    else:
                        self.verify.verify_link_issue(previous_issue_count, after_issue_count)
                # 校验点5：attachment被添加
                if exec_option != "Pass All and Next":
                    if if_attach:
                        if exec_option == "Add Result + Next":
                            if not case_last:
                                self.run.case_list_above_selected_case().click()
                                time.sleep(1)
                            a_new_rows = self.run.case_detail_attachment_list()
                            after_attach_count = len(a_new_rows)
                            self.verify.verify_add_attachment(previous_attach_count, after_attach_count)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
                self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Case is executed")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Case is executed',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def run_history(self, if_project, if_list_page, if_detail_page, where_start, when, which, if_verify):
        # 一、准备数据
        global num_exec_before, num_issue_before, num_attach_before, checked_case_id
        case_desc = self.data['case_desc']
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        # 二、开始操作。查看第一个untested的case或第一个case的执行历史
        if when == "before":
            if if_project:
                project_element = self.pro.project_to_run_btn()
                project_element.click()
                time.sleep(1)
            if if_list_page:
                self.run.run_list_first_run().click()
                time.sleep(3)
            if if_detail_page:
                if where_start == 'Untest':
                    untest_exist = self.verify.verify_untest_case_exist(self.run.run_detail_untest_case_name())
                    if untest_exist:
                        time.sleep(1)
                        self.run.run_detail_first_untest_case_name().click()
                    else:
                        self.logger.info('Message: No untested cases. Will start from the first case')
                        time.sleep(1)
                        self.run.run_detail_first_case_name().click()
                else:
                    # where_start == 'First'
                    time.sleep(1)
                    self.run.run_detail_first_case_name().click()
            time.sleep(3)
            checked_case_id = self.run.case_list_selected_case_id().text
            self.run.case_history_tab().click()
            time.sleep(0.5)

            self.capture.capture_all(case_desc + "-1.png")
            if self.if_upload_rp:
                self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Check history before execute case")
            end_time = TimeUtil.get_current_time()
            if self.if_upload_atas:
                self.atas_api.upload_result(self.result.get_upload_result('Check history before execute case',
                                                                          self.capture.get_full_path(
                                                                              case_desc + "-1.png"),
                                                                          None, start_time,
                                                                          end_time))

            time.sleep(3)
            # 1.记录执行次数
            if_execution = self.run.case_history_find_execution()
            exist_exec = self.verify.verify_case_history_exist(if_execution)
            if exist_exec:
                num_exec_before = len(self.run.case_history_count_execution())
                if which != "None":
                    if which != "All":
                        # 2.记录issue个数
                        if which == "Issue":
                            if_issue = self.run.case_history_find_issue()
                            exist_issue = self.verify.verify_case_history_exist(if_issue)
                            if exist_issue:
                                num_issue_before = len(self.run.case_history_count_issue())
                            else:
                                num_issue_before = 0
                        else:
                            # 3.记录attachment个数
                            # which == "Attachment"
                            if_attach = self.run.case_history_find_attachment()
                            exist_attach = self.verify.verify_case_history_exist(if_attach)
                            if exist_attach:
                                num_attach_before = len(self.run.case_history_count_attachment())
                            else:
                                num_attach_before = 0
                    else:
                        # which == "All"
                        if_issue = self.run.case_history_find_issue()
                        exist_issue = self.verify.verify_case_history_exist(if_issue)
                        if exist_issue:
                            num_issue_before = len(self.run.case_history_count_issue())
                        else:
                            num_issue_before = 0
                        if_attach = self.run.case_history_find_attachment()
                        exist_attach = self.verify.verify_case_history_exist(if_attach)
                        if exist_attach:
                            num_attach_before = len(self.run.case_history_count_attachment())
                        else:
                            num_attach_before = 0

            else:
                num_exec_before = 0
                num_issue_before = 0
                num_attach_before = 0
            self.run.case_details_tab().click()
        else:
            # when == "after"
            self.run.case_list_id_match_case(checked_case_id).click()
            self.run.case_history_tab().click()
            time.sleep(0.5)

            self.capture.capture_all(case_desc + "-2.png")
            if self.if_upload_rp:
                self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Check history after execute case")
            if self.if_upload_atas:
                self.atas_api.upload_result(self.result.get_upload_result('Check history after execute case',
                                                                          self.capture.get_full_path(
                                                                              case_desc + "-2.png"),
                                                                          None, start_time,
                                                                          end_time))

            time.sleep(3)
            # 三、校验结果
            if if_verify:
                # 校验点1：执行次数应该+1
                num_exec_after = len(self.run.case_history_count_execution())
                self.verify.verify_case_history_update(num_exec_before, num_exec_after)
                if which != "None":
                    if which != "All":
                        # 校验点2：issue个数应该+1
                        if which == "Issue":
                            num_issue_after = len(self.run.case_history_count_issue())
                            self.verify.verify_case_history_update(num_issue_before, num_issue_after)
                        else:
                            # 校验点3：attachment个数应该+1
                            # which == "Attachment"
                            num_attach_after = len(self.run.case_history_count_attachment())
                            self.verify.verify_case_history_update(num_attach_before, num_attach_after)
                    else:
                        # which == "All"
                        num_issue_after = len(self.run.case_history_count_issue())
                        self.verify.verify_case_history_update(num_issue_before, num_issue_after)
                        num_attach_after = len(self.run.case_history_count_attachment())
                        self.verify.verify_case_history_update(num_attach_before, num_attach_after)

            end_time = TimeUtil.get_current_time()
            self.capture.capture_all(case_desc + "-3.png")
            if self.if_upload_rp:
                self.capture.upload_capture_to_report_portal(case_desc + "-3.png", "History is updated")
            if self.if_upload_atas:
                self.atas_api.upload_result(self.result.get_upload_result('History is updated',
                                                                          self.capture.get_full_path(
                                                                              case_desc + "-3.png"),
                                                                          None, start_time,
                                                                          end_time))

    def unlink_issue(self, if_project, if_list_page, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        # 二、开始操作。删除case关联的issue
        if if_project:
            project_element = self.pro.project_to_run_btn()
            project_element.click()
            time.sleep(1)
        if if_list_page:
            self.run.run_list_first_run().click()
            time.sleep(3)
        self.run.run_detail_first_case_name().click()
        self.run.case_issues_tab().click()
        time.sleep(0.5)
        issue_list = self.run.run_detail_issues_list()
        issue_exist = self.verify.verify_issue_exist(issue_list)
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if issue_exist == 'N':
            self.logger.info('Message: Current run has no issue, no need to unlink issue')

            self.capture.capture_all(case_desc + "-1.png")
            if self.if_upload_rp:
                self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "No issue to be unlinked")
            end_time = TimeUtil.get_current_time()
            if self.if_upload_atas:
                self.atas_api.upload_result(self.result.get_upload_result('No issue to be unlinked',
                                                                          self.capture.get_full_path(
                                                                              case_desc + "-1.png"),
                                                                          None, start_time,
                                                                          end_time))

        else:
            i = 0
            row = 1
            while i == 0:
                i = int(self.run.run_detail_issues_row(row).text)
                case = self.run.run_detail_cases_row(row)
                row += 1


            self.capture.capture_all(case_desc + "-2.png")
            if self.if_upload_rp:
                self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Unlink issues")
            if self.if_upload_atas:
                self.atas_api.upload_result(self.result.get_upload_result('Unlink issues',
                                                                          self.capture.get_full_path(
                                                                              case_desc + "-2.png"),
                                                                          None, start_time,
                                                                          end_time))

            issue_actions = self.run.case_issue_action_all()
            issue_rows = len(issue_actions)
            i = 1
            while i <= issue_rows:
                self.run.case_issue_action_first().click()
                i += 1
                time.sleep(2)
            time.sleep(3)
            # 三、校验结果
            if if_verify:
                # 校验点1：Issue被全部解除关联
                no_data = self.run.no_data()
                self.verify.verify_issue_unlinked(no_data)

            self.capture.capture_all(case_desc + "-3.png")
            if self.if_upload_rp:
                self.capture.upload_capture_to_report_portal(case_desc + "-3.png", "Issues are unlinked")
            end_time = TimeUtil.get_current_time()
            if self.if_upload_atas:
                self.atas_api.upload_result(self.result.get_upload_result('Issues are unlinked',
                                                                          self.capture.get_full_path(
                                                                              case_desc + "-3.png"),
                                                                          None, start_time,
                                                                          end_time))





