import sys

import pytest

from task.LoginTask import LoginTask
from task.NavigateTask import NavigateTask

# browser_data = [{'browser_type': 'chrome', 'if_head': True}, {'browser_type': 'firefox', 'if_head': True}]
from task.ProjectTask import ProjectTask

browser_data = [{'browser_type': 'remote-chrome', 'if_head': False}]


class TestProject:

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_create_project(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        project = ProjectTask(driver, data, capture, logger, atas_api)
        project.create_project(True)
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_star_project(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        project = ProjectTask(driver, data, capture, logger, atas_api)
        project.create_project(False)
        # if_verify可选择True/False。表示是否需要校验操作结果
        project.star_project(True)
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_search_project(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        project = ProjectTask(driver, data, capture, logger, atas_api)
        project.search_project(True)
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()

    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_delete_project(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        project = ProjectTask(driver, data, capture, logger, atas_api)
        project.create_project(False)
        # if_verify可选择True/False。表示是否需要校验操作结果
        project.delete_project(True)
        # if_verify可选择True/False。表示是否需要校验操作结果
        driver.get_driver().quit()
