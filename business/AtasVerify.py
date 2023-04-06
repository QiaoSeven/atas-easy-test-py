import re


class AtasVerify:
    def __init__(self, logger):
        self.logger = logger

    def check_member_email(self, actual, expect):
        if expect in actual:
            return True
        else:
            return False

    def verify_member_name(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Name of new member is incorrect')
            assert False

    def verify_member_email(self, actual, expect):
        if expect in actual:
            assert True
        else:
            self.logger.error('Email of new member is incorrect')
            assert False

    def verify_member_role(self, actual, expect):
        for role in actual:
            if expect not in role:
                self.logger.error('Role of new member is incorrect')
                assert False
        assert True

    def verify_member_assign(self, actual, expect):
        if set(expect).issubset(set(actual)):
            assert True
        else:
            self.logger.error('Roles are not assigned to member')
            assert False

    def check_add_role(self, r_list, role):
        if role in r_list:
            return True
        else:
            return False

    def verify_add_role(self, r_list, role):
        if role in r_list:
            assert True
        else:
            self.logger.error('Role is not added')
            assert False

    def verify_set_permission(self, text, value):
        if text in value:
            assert True
        else:
            self.logger.error('Permission is not set')
            assert False

    def verify_permission_enabled(self, element):
        if element:
            assert True
        else:
            self.logger.error('Permission is not activated')
            assert False

    def verify_permission_disabled(self, element):
        if not element:
            assert True
        else:
            self.logger.error('Permission is not activated')
            assert False

    def verify_field_preview_same(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Preview is displayed incorrectly')
            assert False

    def verify_field_preview_contain(self, actual, expect):
        if expect in actual:
            assert True
        else:
            self.logger.error('Preview is displayed incorrectly')
            assert False

    def verify_field_list_same(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Added field is displayed incorrectly in list')
            assert False

    def verify_field_list_similar(self, actual, expect):
        if re.compile(expect, re.IGNORECASE).search(actual):
            assert True
        else:
            self.logger.error('Added field is displayed incorrectly in list')
            assert False

    def verify_field_preview_disappear(self, element):
        if not element:
            assert True
        else:
            self.logger.error('Preview is displayed incorrectly')
            assert False

    def verify_template_add(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Template is not added')
            assert False

    def verify_new_project_bt(self, element):
        if element is not None:
            assert element.is_enabled()
        else:
            self.logger.error('Login fail')
            assert False

    def verify_login_fail_pop(self, element):
        if element.is_enabled():
            assert True
        else:
            self.logger.error('Not find login fail pop')
            assert False

    def verify_login_fail(self, element):
        if element:
            assert True
        else:
            self.logger.error('Fail to Login fail')
            assert False

    def verify_project_name(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Create project fail')
            assert False

    def verify_test_suite_name(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Create test suite fail')
            assert False

    def verify_case_list(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Create test case fail')
            assert False

    def verify_run_list(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Create test run fail')
            assert False

    def verify_run_rate(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Execute test run fail')
            assert False

    def verify_logout(self, element):
        if element.is_enabled():
            assert True
        else:
            self.logger.error('Logout is fail')
            assert False

    def verify_add_members(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Add members fail')
            assert False

    def verify_star_project(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Fail: Project is not starred')
            assert False

    def verify_switch_project(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Fail: Project is not switched')
            assert False

    def verify_search_project(self, actual, expect):
        if actual.lower() == expect.lower():
            assert True
        else:
            self.logger.error('Search project fail')
            assert False

    def verify_delete_project(self, actual, expect):
        if actual != expect:
            assert True
        else:
            self.logger.error('Delete project fail')
            assert False

    def verify_project_list_page(self, total_page, page_items, max_page, max_items_one_page):
        if total_page == max_page and page_items == max_items_one_page:
            assert True
        else:
            self.logger.error('Project list page is incorrect')
            assert False

    def verify_case_delete(self, element):
        if not element:
            assert True
        else:
            self.logger.error('Case delete fail')
            assert False

    def verify_filter_criteria_dropdown(self, element):
        if element:
            return True
        else:
            return False

    def verify_consistent_display(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Fail: Not displayed as expected')
            assert False

    def verify_modal_window(self, element):
        if not element:
            assert True
        else:
            self.logger.error('Modal window is not closed')
            assert False

    def verify_case_status(self, actual, expect):
        if re.compile(expect, re.IGNORECASE).search(actual):
            assert True
        else:
            self.logger.error('Fail: Case status is not updated')
            assert False

    def verify_step_status(self, step_list, expect):
        for step in step_list:
            if not re.compile(expect, re.IGNORECASE).search(step):
                self.logger.error('Fail: Step status is not updated')
                assert False
        assert True

    def verify_case_status_not_pass(self, actual, expect):
        if re.compile(expect, re.IGNORECASE).search(actual):
            assert True
        else:
            self.logger.error('Execute case fail')
            assert False

    def verify_link_issue(self, pre, now):
        if int(now) == int(pre) + 1:
            assert True
        else:
            self.logger.error('Fail: Issue is not linked / Linked the same issue')
            assert False

    def verify_link_same_issue(self, pre, now):
        if int(now) == int(pre):
            assert True
        else:
            self.logger.error('Fail: Issue is not linked / Linked the same issue')
            assert False

    def verify_issue_duplicate(self, new, ori_list):
        if new in ori_list:
            return True
        else:
            return False

    def verify_attach_exist(self, element):
        if element:
            return True
        else:
            return False

    def verify_add_attachment(self, pre, now):
        if now == pre + 1:
            assert True
        else:
            self.logger.error('Fail: Attachment is not added')
            assert False

    def verify_second_case(self, element):
        if not element:
            return False
        else:
            return True

    def verify_select_next_case(self, exec, pre):
        if pre == exec:
            assert True
        else:
            self.logger.error('Fail: Next case is not selected after execution')
            assert False

    def verify_run_edit(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Edit test run fail')
            assert False

    def verify_contain_text(self, actual, expect):
        if expect in actual:
            assert True
        else:
            self.logger.error('Fail: Does not contain expected value')
            assert False

    def verify_copied_run_name(self, after, before):
        if after == before + 1:
            assert True
        else:
            self.logger.error('Fail: Test run is not duplicated')
            assert False

    def verify_duplicate_run(self, after, before):
        if after == before:
            assert True
        else:
            self.logger.error('Fail: Test run is not duplicated')
            assert False

    def verify_duplicate_and_reset_run(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Fail: Test run is not reset')
            assert False

    def verify_priority_filter(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Fail: Priority filter is not selected ')
            assert False

    def verify_priority_result(self, result_list, expect):
        for result in result_list:
            if expect != result:
                self.logger.error('Fail: Priority result is different from selected option')
                assert False
        assert True

    def verify_assignee_exist(self, element):
        if not element:
            return True
        else:
            return False

    def verify_assignee_filter(self, actual, expect):
        if expect in actual:
            assert True
        else:
            self.logger.error('Fail: Assignee filter is not selected ')
            assert False

    def verify_assignee_result(self, result_list, expect):
        for result in result_list:
            if expect not in result:
                self.logger.error('Fail: Assignee result is different from selected option')
                assert False
        assert True

    def verify_status_filter(self, actual, expect):
        if re.compile(expect, re.IGNORECASE).search(actual):
            assert True
        else:
            self.logger.error('Fail: Status filter is not selected ')
            assert False

    def verify_status_result(self, result_list, expect):
        for result in result_list:
            if expect not in result:
                self.logger.error('Fail: Status result is different from selected option')
                assert False
        assert True

    def verify_project_search(self, result_list, expect):
        for result in result_list:
            if expect not in result:
                self.logger.error('Fail: Searched project name does not contain input keyword')
                assert False
        assert True

    def verify_requirement_dropdown(self, element):
        if not element:
            return True
        else:
            return False

    def verify_requirement_create(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Fail: Requirement is not created')
            assert False

    def verify_requirement_edit(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Fail: Requirement is not edited')
            assert False

    def verify_requirement_link_case(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Fail: Case is not linked to requirement')
            assert False

    def verify_rqm_link_pri(self, actual, expect):
        if expect in actual:
            assert True
        else:
            self.logger.error('Fail: Priority of linked requirement is incorrect')
            assert False

    def verify_requirement_search(self, result_list, expect):
        for result in result_list:
            if not re.compile(expect, re.IGNORECASE).search(result):
                self.logger.error('Fail: Searched requirement name does not contain input keyword')
                assert False
        assert True

    def verify_field_search(self, result_list, expect):
        for result in result_list:
            if not re.compile(expect, re.IGNORECASE).search(result):
                self.logger.error('Fail: Searched field name does not contain input keyword')
                assert False
        assert True

    def verify_search_result(self, result_list, expect):
        for result in result_list:
            if not re.compile(expect, re.IGNORECASE).search(result):
                self.logger.error('Search result does not contain input keyword')
                assert False
        assert True

    def verify_untest_case_exist(self, element):
        if element:
            return True
        else:
            return False

    def verify_no_assignee_exist(self, element):
        if element:
            return True
        else:
            return False

    def verify_case_assignee(self, actual, expect):
        if re.compile(actual, re.IGNORECASE).search(expect):
            assert True
        else:
            self.logger.error('Fail: Case is not assigned ')
            assert False

    def verify_cases_assignee(self, result_list, expect):
        for result in result_list:
            if not re.compile(result, re.IGNORECASE).search(expect):
                self.logger.error('Fail: Cases are not assigned')
                assert False
        assert True

    def verify_delete(self, all_list, delete):
        if delete not in all_list:
            assert True
        else:
            self.logger.error('Fail: Item is not deleted')
            assert False

    def verify_report_list(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Created report is not displayed correctly')
            assert False

    def verify_new_report_name(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Report is not successfully edited')
            assert False

    def verify_report_list_summary(self, actual, expect):
        if expect in actual:
            assert True
        else:
            self.logger.error('Fail: Report is not successfully created')
            assert False

    def verify_case_history_exist(self, element):
        if not element:
            return False
        else:
            return True

    def verify_case_history_update(self, before, after):
        if after == before + 1:
            assert True
        else:
            self.logger.error('Fail: History is not successfully updated')
            assert False

    def verify_issue_exist(self, issue_list):
        for issue in issue_list:
            count = int(issue.text)
            if count != 0:
                return 'Y'
        return 'N'

    def verify_issue_unlinked(self, element):
        if element:
            assert True
        else:
            self.logger.error('Fail: Issues are not unlinked')
            assert False

    def verify_report_deletion(self, element):
        if element:
            assert True
        else:
            self.logger.error('Fail: Report is not deleted')
            assert False

    def verify_view_report_same(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Fail: Report is not displayed correctly')
            assert False

    def verify_view_report_text_contain_text(self, actual, expect):
        if expect in actual:
            assert True
        else:
            self.logger.error('Fail: Report is not displayed correctly')
            assert False

    def verify_view_report_list_contain_text(self, actual, expect):
        for i in actual:
            if expect in i:
                return True
        return False

    def verify_view_report_contain_list(self, actual, expect):
        if set(expect).issubset(set(actual)):
            assert True
        else:
            self.logger.error('Fail: Report is not displayed correctly')
            assert False

    def verify_view_report_equal_to(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Report is not displayed correctly')
            assert False

    def verify_has_total(self, element):
        if element:
            return "No total"
        else:
            return "Has total"

    def verify_no_data(self, element):
        if not element:
            assert True
        else:
            self.logger.error('Fail: No search result. Please update the case')
            assert False

    def verify_empty(self, element):
        if not element:
            assert True
        else:
            self.logger.error('No item for current report type. Please update the case')
            assert False

    def verify_scope_to_run(self, actual, expect):
        if set(expect).issubset(set(actual)):
            assert True
        else:
            self.logger.error('Fail: Cases are not added in scope')
            assert False

    def verify_issue_create(self, actual, expect):
        if actual == expect:
            assert True
        else:
            self.logger.error('Fail: Issue is not created')
            assert False

    def verify_issue_search(self, result_list, expect):
        for result in result_list:
            if not re.compile(expect, re.IGNORECASE).search(result):
                self.logger.error('Fail: Searched issue name does not contain input keyword')
                assert False
        assert True

    def verify_refresh_issue(self, field):
        if field != '':
            assert True
        else:
            self.logger.error('Fail: Issue is not refreshed')
            assert False

    def verify_next_page(self, element):
        if element:
            return False
        else:
            return True

