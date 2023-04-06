import sys

import pytest

from core.CoreConfig import CoreConfig
from task.LoginTask import LoginTask
from task.NavigateTask import NavigateTask

# browser_data = [{'browser_type': 'chrome', 'if_head': True}, {'browser_type': 'firefox', 'if_head': True}]
from util.ExcelUtil import ExcelUtil

browser_data = [{'browser_type': 'chrome', 'if_head': False}]


@pytest.mark.parametrize("driver", browser_data, indirect=True)
@pytest.mark.parametrize("data_list", ExcelUtil.get_all_data_dict_by_name(CoreConfig.get_data_full_path(),'test_login_success'))
def test_login_success(driver, data_list, capture, logger):
    # 数据
    nv = NavigateTask(driver, data_list)
    nv.navigate()
    login = LoginTask(driver, data_list, capture, logger)
    login.login_with_auth_success()
    driver.get_driver().quit()


@pytest.mark.parametrize("driver", browser_data,  indirect=True)
@pytest.mark.parametrize("data_list", ExcelUtil.get_all_data_dict_by_name(CoreConfig.get_data_full_path(),'test_login_fail'))
def test_login_fail(driver, data_list, capture, logger):
    # 数据
    nv = NavigateTask(driver, data_list)
    nv.navigate()
    login = LoginTask(driver, data_list, capture, logger)
    login.login_with_auth_fail()
    driver.get_driver().quit()
