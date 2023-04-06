import sys
import pytest

from task.IssueTask import IssueTask
from task.LoginTask import LoginTask
from task.NavigateTask import NavigateTask

# browser_data = [{'browser_type': 'chrome', 'if_head': True}, {'browser_type': 'firefox', 'if_head': True}]
from task.ProjectTask import ProjectTask
from task.SuiteTask import SuiteTask

browser_data = [{'browser_type': 'remote-chrome', 'if_head': False}]


class TestIssue:
    # @pytest.mark.parametrize("driver", browser_data, indirect=True)
    # def test_create_issue(self, driver, get_data, capture, logger, atas_api):
    #     def_name = sys._getframe().f_code.co_name
    #     # 数据
    #     data = get_data[def_name]
    #     nv = NavigateTask(driver, data)
    #     nv.navigate()
    #     login = LoginTask(driver, data, capture, logger, atas_api)
    #     login.login_with_auth_success()
    #     issue = IssueTask(driver, data, capture, logger, atas_api)
    #     issue.project_key(True)
    #     # if_project可选择True/False。表示是否需要从project菜单进入子层级
    #     issue.create_issue(False, True)
    #     # if_project可选择True/False。表示是否需要从project菜单进入子层级
    #     # if_verify可选择True/False。表示是否需要校验操作结果
    #     driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_link_issue(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        issue = IssueTask(driver, data, capture, logger, atas_api)
        issue.project_key(True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        issue.link_issue(False, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_search_issue(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        issue = IssueTask(driver, data, capture, logger, atas_api)
        issue.search_issue(True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_refresh_issue(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        issue = IssueTask(driver, data, capture, logger, atas_api)
        issue.refresh_issue(True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()
