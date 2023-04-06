import sys

import pytest

from task.LoginTask import LoginTask
from task.NavigateTask import NavigateTask

# browser_data = [{'browser_type': 'chrome', 'if_head': True}, {'browser_type': 'firefox', 'if_head': True}]
from task.ProjectTask import ProjectTask

browser_data = [{'browser_type': 'chrome', 'if_head': False}]


class TestProject:
    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_create_project(driver, data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        nv = NavigateTask(driver, data)
        nv.navigate()
        login = LoginTask(driver, data, capture, logger, atas_api)
        login.login_with_auth_success()
        project = ProjectTask(driver, data, capture, logger, atas_api)
        project.create_project()
        driver.get_driver().quit()
