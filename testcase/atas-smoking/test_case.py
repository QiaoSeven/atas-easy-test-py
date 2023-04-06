import sys

import pytest

from task.CaseTask import CaseTask
from task.LoginTask import LoginTask
from task.NavigateTask import NavigateTask

# browser_data = [{'browser_type': 'chrome', 'if_head': True}, {'browser_type': 'firefox', 'if_head': True}]
from task.ProjectTask import ProjectTask
from task.SuiteTask import SuiteTask

browser_data = [{'browser_type': 'remote-chrome', 'if_head': False}]


class TestCase:
    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_create_case(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        case = CaseTask(driver, data, capture, logger, atas_api)
        case.create_case(True, True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_suite可选择True/False。表示是否需要从suite page进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_delete_case(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        case = CaseTask(driver, data, capture, logger, atas_api)
        case.create_case(True, True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_suite可选择True/False。表示是否需要从suite page进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        case.delete_case(False, False, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_suite可选择True/False。表示是否需要从suite page进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_create_filter(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        case = CaseTask(driver, data, capture, logger, atas_api)
        case.create_filter(True, "All", True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # which_column可选择"Single"/"All"/"None"。表示想在filter的Results展示多少列
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_edit_filter(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        case = CaseTask(driver, data, capture, logger, atas_api)
        case.create_filter(True, "Single", False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # which_column可选择"Single"/"All"/"None"。表示想在filter的Results展示多少列
        # if_verify可选择True/False。表示是否需要校验操作结果
        case.edit_filter(False, True, browser_data)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_delete_filter(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        case = CaseTask(driver, data, capture, logger, atas_api)
        case.create_filter(True, "None", False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # which_column可选择"Single"/"All"/"None"。表示想在filter的Results展示多少列
        # if_verify可选择True/False。表示是否需要校验操作结果
        case.delete_filter(False, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

