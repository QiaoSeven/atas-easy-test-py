import sys

import pytest

from task.CaseTask import CaseTask
from task.LoginTask import LoginTask
from task.NavigateTask import NavigateTask

# browser_data = [{'browser_type': 'chrome', 'if_head': True}, {'browser_type': 'firefox', 'if_head': True}]
from task.ProjectTask import ProjectTask
from task.RunTask import RunTask
from task.SuiteTask import SuiteTask

browser_data = [{'browser_type': 'remote-chrome', 'if_head': False}]


class TestRun:
    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_create_run(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        run = RunTask(driver, data, capture, logger, atas_api)
        run.create_run(True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_edit_run(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        run = RunTask(driver, data, capture, logger, atas_api)
        # run.create_run(True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        run.edit_run(True, "Run List Page", True, browser_data)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # where可选择"Run List Page"/"Run Detail Page"。表示在哪个页面编辑test run
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_duplicate_run(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        run = RunTask(driver, data, capture, logger, atas_api)
        # run.create_run(True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        run.duplicate_run(True, True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_reset可选择True/False。表示是否要选择duplicate and reset
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_delete_run(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        run = RunTask(driver, data, capture, logger, atas_api)
        run.create_run(True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        run.delete_run(False, "Run List Page", True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # where可选择"Run List Page" / "Run Detail Page"。表示在哪个页面删除test run
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_edit_run_scope(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        # case = CaseTask(driver, data, capture, logger, atas_api)
        # case.create_case(True, True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_suite可选择True/False。表示是否需要从suite page进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        run = RunTask(driver, data, capture, logger, atas_api)
        run.edit_run_scope(True, True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_list_page可选择True/False。表示是否需要从run list page进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_assign_cases(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        # case = CaseTask(driver, data, capture, logger, atas_api)
        # case.create_case(True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        run = RunTask(driver, data, capture, logger, atas_api)
        # run.create_run(False, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        # run.edit_run_scope(False)
        run.assign_cases(True, True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_list_page可选择True/False。表示是否需要从run list page进入自从子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_filter_cases(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        # case = CaseTask(driver, data, capture, logger, atas_api)
        # case.create_case(True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        run = RunTask(driver, data, capture, logger, atas_api)
        # run.create_run(False, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        # run.edit_run_scope(False)
        run.filter_cases(True, True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_list_page可选择True/False。表示是否需要从run list page进入自从子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_search_cases(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        # case = CaseTask(driver, data, capture, logger, atas_api)
        # case.create_case(True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        run = RunTask(driver, data, capture, logger, atas_api)
        # run.create_run(False, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        # run.edit_run_scope(False)
        run.search_cases(True, True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_list_page可选择True/False。表示是否需要从run list page进入自从子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_execute_case(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        # case = CaseTask(driver, data, capture, logger, atas_api)
        # case.create_case(True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        run = RunTask(driver, data, capture, logger, atas_api)
        # run.create_run(False, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        # run.edit_run_scope(False)
        run.execute_case(True, True, True, "Untest", True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_list_page可选择True/False。表示是否需要从run list page进入自从子层级
        # if_detail_page可选择True/False。表示是否需要从run detail page进入自从子层级
        # where_start可选择"Untest"/"First"。表示从run的第1个（Untested的）case开始执行
        # if_attach可选择True/False。表示是否上传attachment
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_check_case_history(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        run = RunTask(driver, data, capture, logger, atas_api)
        run.run_history(True, True, True, "Untest", "before", "None", True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_list_page可选择True/False。表示是否需要从run list page进入自从子层级
        # if_detail_page可选择True/False。表示是否需要从run detail page进入自从子层级
        # where_start可选择"Untest"/"First"。表示从run的第1个（Untested的）case开始执行（要和execute一致）
        # when可选择"before"/"after"。表示是在执行前还是执行后检查history
        # which可选择"Issue"/"Attachment"/"None"/"All"。表示记录哪些项目的history（要和execute一致）
        # if_verify可选择True/False。表示是否需要校验操作结果
        run.execute_case(False, False, False, "Untest", True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_list_page可选择True/False。表示是否需要从run list page进入自从子层级
        # if_detail_page可选择True/False。表示是否需要从run detail page进入自从子层级
        # where_start可选择"Untest"/"First"。表示从run的第1个（Untested的）case开始执行
        # if_attach可选择True/False。表示是否上传attachment
        # if_verify可选择True/False。表示是否需要校验操作结果
        run.run_history(False, False, False, "Untest", "after", "None", True)
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_unlink_issue(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        run = RunTask(driver, data, capture, logger, atas_api)
        run.unlink_issue(True, True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_list_page可选择True/False。表示是否需要从run list page进入自从子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()
