import datetime
import time

from selenium.webdriver import Keys

from object.IssueObject import IssueObject
from object.ProjectObject import ProjectObject
from task.BaseTask import BaseTask
from util.TimeUtil import TimeUtil


class IssueTask(BaseTask):
    def __init__(self, driver, data, capture, logger, atas_api):
        BaseTask.__init__(self, driver, data, capture, logger, atas_api)
        self.pro = ProjectObject(self.driver)
        self.issue = IssueObject(self.driver)

    def project_key(self, if_project):
        if if_project:
            project_element = self.pro.project_to_issue_btn()
            project_element.click()
            time.sleep(3)
        self.issue.settings_btn().click()
        time.sleep(0.5)
        self.issue.edit_pro_option().click()
        # url = self.issue.edit_pro_url_input().get_attribute('value')
        # if url != 'https://jira.rakuten-it.com':
        #     self.issue.edit_pro_url_input().send_keys('https://jira.rakuten-it.com')
        key = self.issue.edit_pro_key_input().get_attribute('value')
        if key != 'CNTDAP':
            self.issue.edit_pro_key_input().send_keys('CNTDAP')
        self.issue.edit_pro_save_btn().click()

    def create_issue(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        issue_summary = self.data['issue_summary']
        issue_priority = self.data['issue_priority']
        issue_assignee = self.data['issue_assignee']
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        # 二、开始操作。创建新的requirement
        if if_project:
            project_element = self.pro.project_to_issue_btn()
            project_element.click()
            time.sleep(1)
        self.issue.create_jira_btn().click()
        self.issue.jira_modal_summary().send_keys(issue_summary + suffix_time)
        self.issue.jira_modal_pri_arrow().click()
        time.sleep(0.5)
        self.issue.jira_modal_pri_dropdown(issue_priority).click()
        self.issue.jira_modal_assignee().send_keys(issue_assignee)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Create JIRA issue")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Create JIRA issue',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.issue.jira_modal_save_btn().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            create_issue_modal_window = self.issue.jira_modal_window()
            self.verify.verify_modal_window(create_issue_modal_window)
            # 校验点2：issue列表新增正确的issue名称
            actual_issue_name = self.issue.jira_name_first().text
            expect_issue_name = issue_summary + suffix_time
            self.verify.verify_issue_create(actual_issue_name, expect_issue_name)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "JIRA issue is created")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('JIRA issue is created',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def link_issue(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        jira_issue = self.data['jira_issue']
        # 二、开始操作。创建新的requirement
        if if_project:
            project_element = self.pro.project_to_issue_btn()
            project_element.click()
            time.sleep(1)
        self.issue.create_jira_arrow().click()
        time.sleep(0.5)
        self.issue.dropdown_link_jira().click()
        self.issue.link_to_issue_input().click()
        self.issue.link_to_issue_input().send_keys(jira_issue)
        self.issue.link_to_issue_search().click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Link JIRA issue")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Link JIRA issue',
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.issue.link_to_issue_link().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            link_issue_modal_window = self.issue.jira_modal_window()
            self.verify.verify_modal_window(link_issue_modal_window)
            # 校验点2：issue列表新增正确的issue id
            actual_issue_id = self.issue.jira_id_first().text
            expect_issue_id = jira_issue
            self.verify.verify_issue_create(actual_issue_id, expect_issue_id)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "JIRA issue is linked")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('JIRA issue is linked',
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def search_issue(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        search_key = self.data['search_keyword']
        # 二、开始操作。搜索issue
        if if_project:
            time.sleep(2)
            project_element = self.pro.project_to_issue_btn()
            project_element.click()
        time.sleep(2)
        self.issue.search_bar().send_keys(search_key)
        time.sleep(0.5)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Search issue by "+str(search_key)+"")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Search issue by "+str(search_key)+"",
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.issue.search_bar().send_keys(Keys.ENTER)
        # 三、校验结果
        if if_verify:
            no_data = self.issue.no_data()
            self.verify.verify_no_data(no_data)
            # 校验点1：搜索结果都包含搜索关键字
            result = []
            names = self.issue.jira_name_list()
            for name in names:
                result.append(name.text)
            self.verify.verify_issue_search(result, search_key)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Issue is searched")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Issue is searched",
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def refresh_issue(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        # 二、开始操作。搜索issue
        if if_project:
            time.sleep(2)
            project_element = self.pro.project_to_issue_btn()
            project_element.click()
        time.sleep(2)
        self.issue.jira_refresh_first().click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Refresh issue")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Refresh issue",
                                                                      self.capture.get_full_path(case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        time.sleep(5)
        # 三、校验结果
        if if_verify:
            # 校验点1：刷新后status和priority不为空
            status = self.issue.jira_status_first().text
            priority = self.issue.jira_pri_first().text
            self.verify.verify_refresh_issue(status)
            self.verify.verify_refresh_issue(priority)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Issue is refreshed")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Issue is refreshed",
                                                                      self.capture.get_full_path(case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

