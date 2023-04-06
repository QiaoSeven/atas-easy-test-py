import sys
import pytest

from task.RequirementTask import RequirementTask
from task.LoginTask import LoginTask
from task.NavigateTask import NavigateTask

# browser_data = [{'browser_type': 'chrome', 'if_head': True}, {'browser_type': 'firefox', 'if_head': True}]
from task.ProjectTask import ProjectTask
from task.SuiteTask import SuiteTask

browser_data = [{'browser_type': 'remote-chrome', 'if_head': False}]


class TestRequirements:
    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_create_requirement(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        rqm = RequirementTask(driver, data, capture, logger, atas_api)
        rqm.create_requirement(True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_link_requirement(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        rqm = RequirementTask(driver, data, capture, logger, atas_api)
        rqm.link_requirement(True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_search_requirement(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        rqm = RequirementTask(driver, data, capture, logger, atas_api)
        # rqm.create_requirement(True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        rqm.search_requirement(True, False)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_edit_requirement(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        rqm = RequirementTask(driver, data, capture, logger, atas_api)
        rqm.create_requirement(True, False)
        rqm.edit_requirement(False, True, browser_data)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_link_case(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        rqm = RequirementTask(driver, data, capture, logger, atas_api)
        rqm.link_case(True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_add_attachment(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        rqm = RequirementTask(driver, data, capture, logger, atas_api)
        rqm.add_attachment(True, True)
        # if_project可选择True/False。表示是否需要从project菜单进入子层级
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()
