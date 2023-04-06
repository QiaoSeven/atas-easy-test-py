import datetime
import os
import platform
import time

from selenium.webdriver import Keys

from object.RequirementObject import RequirementObject
from object.ProjectObject import ProjectObject
from task.BaseTask import BaseTask
from util.TimeUtil import TimeUtil


class RequirementTask(BaseTask):
    def __init__(self, driver, data, capture, logger, atas_api):
        BaseTask.__init__(self, driver, data, capture, logger, atas_api)
        self.pro = ProjectObject(self.driver)
        self.rqm = RequirementObject(self.driver)

    def create_requirement(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        rqm_title = self.data['rqm_title']
        rqm_type = self.data['rqm_type']
        rqm_priority = self.data['rqm_priority']
        rqm_status = self.data['rqm_status']
        rqm_feature = self.data['rqm_feature']
        rqm_release = self.data['rqm_release']
        rqm_version = self.data['rqm_version']
        rqm_sprint = self.data['rqm_sprint']
        rqm_tags = self.data['rqm_tags']
        rqm_summary = self.data['rqm_summary']
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        # 二、开始操作。创建新的requirement
        if if_project:
            project_element = self.pro.project_to_rqm_btn()
            project_element.click()
            time.sleep(1)
        self.rqm.create_rqm_btn().click()
        self.rqm.rqm_modal_title().send_keys(rqm_title + suffix_time)
        self.rqm.rqm_modal_type_arrow().click()
        time.sleep(0.5)
        self.rqm.rqm_modal_type_dropdown(rqm_type).click()
        self.rqm.rqm_modal_pri_arrow().click()
        time.sleep(0.5)
        self.rqm.rqm_modal_pri_dropdown(rqm_priority).click()
        self.rqm.rqm_modal_status_arrow().click()
        time.sleep(0.5)
        self.rqm.rqm_modal_status_dropdown(rqm_status).click()
        self.rqm.rqm_modal_feature_input().click()
        time.sleep(0.5)
        has_option = self.verify.verify_requirement_dropdown(self.rqm.rqm_modal_dropdown_null())
        if not has_option:
            self.rqm.rqm_modal_dropdown_input().send_keys(rqm_feature)
            self.rqm.rqm_modal_dropdown_add_btn().click()
            expect_rqm_ftr = rqm_feature
        else:
            expect_rqm_ftr = self.rqm.rqm_modal_dropdown_first().text
        self.rqm.rqm_modal_dropdown_first().click()
        self.rqm.rqm_modal_release_input().click()
        time.sleep(0.5)
        has_option = self.verify.verify_requirement_dropdown(self.rqm.rqm_modal_dropdown_null())
        if not has_option:
            self.rqm.rqm_modal_dropdown_input().send_keys(rqm_release)
            self.rqm.rqm_modal_dropdown_add_btn().click()
            expect_rqm_rls = rqm_release
        else:
            expect_rqm_rls = self.rqm.rqm_modal_dropdown_first().text
        self.rqm.rqm_modal_dropdown_first().click()
        self.rqm.rqm_modal_version_input().click()
        time.sleep(0.5)
        has_option = self.verify.verify_requirement_dropdown(self.rqm.rqm_modal_dropdown_null())
        if not has_option:
            self.rqm.rqm_modal_dropdown_input().send_keys(rqm_version)
            self.rqm.rqm_modal_dropdown_add_btn().click()
        self.rqm.rqm_modal_dropdown_first().click()
        self.rqm.rqm_modal_sprint_input().click()
        time.sleep(0.5)
        has_option = self.verify.verify_requirement_dropdown(self.rqm.rqm_modal_dropdown_null())
        if not has_option:
            self.rqm.rqm_modal_dropdown_input().send_keys(rqm_sprint)
            self.rqm.rqm_modal_dropdown_add_btn().click()
        self.rqm.rqm_modal_dropdown_first().click()
        self.rqm.rqm_modal_tags_input().click()
        time.sleep(0.5)
        has_option = self.verify.verify_requirement_dropdown(self.rqm.rqm_modal_dropdown_null())
        if not has_option:
            self.rqm.rqm_modal_dropdown_input().send_keys(rqm_tags)
            self.rqm.rqm_modal_dropdown_add_btn().click()
        self.rqm.rqm_modal_dropdown_first().click()
        self.rqm.rqm_modal_tags_input().click()
        self.rqm.rqm_modal_sum_input().send_keys(rqm_summary)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Create new requirement")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Create new requirement',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.rqm.rqm_modal_save_btn().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            create_rqm_modal_window = self.rqm.rqm_modal_window()
            self.verify.verify_modal_window(create_rqm_modal_window)
            # 校验点2：requirement列表新增正确的rqm名称
            actual_rqm_name = self.rqm.rqm_name_first().text
            expect_rqm_name = rqm_title + suffix_time
            self.verify.verify_requirement_create(actual_rqm_name, expect_rqm_name)
            # 校验点3：requirement列表新增正确的rqm优先级
            actual_rqm_pri = self.rqm.rqm_pri_first().text
            expect_rqm_pri = rqm_priority
            self.verify.verify_requirement_create(actual_rqm_pri, expect_rqm_pri)
            # 校验点4：requirement列表新增正确的rqm特点
            actual_rqm_ftr = self.rqm.rqm_feature_first().text
            self.verify.verify_requirement_create(actual_rqm_ftr, expect_rqm_ftr)
            # 校验点5：requirement列表新增正确的rqm发布时间
            actual_rqm_rls = self.rqm.rqm_release_first().text
            self.verify.verify_requirement_create(actual_rqm_rls, expect_rqm_rls)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "New requirement is created")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('New requirement is created',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def link_requirement(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        jira_id = self.data['jira_id']
        rqm_status = self.data['rqm_status']
        # 二、开始操作。链接新的requirement
        if if_project:
            project_element = self.pro.project_to_rqm_btn()
            project_element.click()
            time.sleep(1)
        self.rqm.create_rqm_arrow().click()
        time.sleep(0.5)
        self.rqm.dropdown_link_rqm().click()
        self.rqm.link_modal_ticket_input().send_keys(jira_id)
        self.rqm.link_modal_search_btn().click()
        self.rqm.rqm_modal_status_arrow().click()
        time.sleep(0.5)
        self.rqm.rqm_modal_status_dropdown(rqm_status).click()
        expect_priority = self.rqm.link_modal_priority().text

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Link JIRA requirement")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Link JIRA requirement',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.rqm.link_modal_add_btn().click()
        time.sleep(5)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            link_rqm_modal_window = self.rqm.rqm_modal_window()
            self.verify.verify_modal_window(link_rqm_modal_window)
            # 校验点2：requirement列表新增正确的rqm优先级
            actual_rqm_pri = self.rqm.rqm_pri_first().text
            expect_rqm_pri = expect_priority
            self.verify.verify_rqm_link_pri(actual_rqm_pri, expect_rqm_pri)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "JIRA requirement is linked")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('JIRA requirement is linked',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def search_requirement(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        search_key = self.data['search_keyword']
        # 二、开始操作。搜索requirement
        if if_project:
            time.sleep(2)
            project_element = self.pro.project_to_rqm_btn()
            project_element.click()
        time.sleep(2)
        self.rqm.search_bar().send_keys(search_key)
        time.sleep(0.5)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Search requirement by "+str(search_key)+"")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Search requirement by "+str(search_key)+"",
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.rqm.search_bar().send_keys(Keys.ENTER)
        # 三、校验结果
        if if_verify:
            no_data = self.rqm.no_data()
            self.verify.verify_no_data(no_data)
            # 校验点1：搜索结果都包含搜索关键字
            result = []
            names = self.rqm.rqm_name_list()
            for name in names:
                result.append(name.text)
            self.verify.verify_requirement_search(result, search_key)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Requirement is searched")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Requirement is searched',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def edit_requirement(self, if_project, if_verify, browser_data):
        # 一、准备数据
        case_desc = self.data['case_desc']
        new_title = self.data['new_title']
        plat = platform.system().lower()
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        # 二、开始操作。编辑第一个requirement
        if if_project:
            project_element = self.pro.project_to_rqm_btn()
            project_element.click()
            time.sleep(1)
        self.rqm.rqm_name_first().click()
        self.rqm.edit_modal_edit_btn().click()
        self.rqm.rqm_modal_title().click()
        if plat == "darwin" and ('remote' not in str(browser_data)):
            self.rqm.rqm_modal_title().send_keys(Keys.COMMAND, "a")
        else:
            self.rqm.rqm_modal_title().send_keys(Keys.CONTROL, "a")
        self.rqm.rqm_modal_title().send_keys(Keys.DELETE)
        self.rqm.rqm_modal_title().send_keys(new_title + suffix_time)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Edit created requirement")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Edit created requirement",
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.rqm.edit_modal_save_btn().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：名字成功更新
            actual_new_title = self.rqm.edit_modal_title().text
            expect_new_title = new_title + suffix_time
            self.verify.verify_requirement_edit(actual_new_title, expect_new_title)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Requirement is edited")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Requirement is edited",
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def link_case(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        case_name = self.data['case_name']
        # 二、开始操作。编辑第一个requirement
        if if_project:
            project_element = self.pro.project_to_rqm_btn()
            project_element.click()
            time.sleep(1)
        self.rqm.rqm_name_first().click()
        self.rqm.edit_modal_cases_tab().click()
        self.rqm.edit_modal_link_btn().click()
        self.rqm.edit_modal_case_input().send_keys(case_name)
        expect_case_name = self.rqm.edit_modal_dropdown_first_case().text

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Link case to requirement")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Link case to requirement",
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.rqm.edit_modal_dropdown_first_case().click()
        time.sleep(5)
        # 三、校验结果
        if if_verify:
            # 校验点1：名字成功更新
            actual_case_name = self.rqm.edit_modal_list_first_case().text
            self.verify.verify_requirement_link_case(actual_case_name, expect_case_name)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Case is linked to requirement")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Case is linked to requirement",
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def add_attachment(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        file_path = self.data['file_path']
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = curPath[:curPath.find("atas-easy-test-py") + len("atas-easy-test-py")]
        # 二、开始操作。给requirement上传attachment
        if if_project:
            project_element = self.pro.project_to_rqm_btn()
            project_element.click()
            time.sleep(1)
        self.rqm.rqm_name_first().click()
        time.sleep(2)
        attach_exist = self.verify.verify_attach_exist(self.rqm.edit_modal_attachments())
        if attach_exist:
            a_rows = self.rqm.edit_modal_attachment_list()
            previous_attach_count = len(a_rows)
        else:
            previous_attach_count = 0
        self.rqm.edit_modal_edit_btn().click()
        upload = self.rqm.edit_modal_attachment_add()
        time.sleep(1)
        upload.send_keys(rootPath + file_path)
        time.sleep(1)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Add attachment to requirement")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Add attachment to requirement",
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.rqm.edit_modal_save_btn().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：名字成功更新
            a_new_rows = self.rqm.edit_modal_attachment_list()
            after_attach_count = len(a_new_rows)
            self.verify.verify_add_attachment(previous_attach_count, after_attach_count)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Attachment is added to requirement")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Attachment is added to requirement",
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))
















