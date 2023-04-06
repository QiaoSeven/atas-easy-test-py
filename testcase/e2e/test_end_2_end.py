import json
import sys

import pytest

from core.CoreJson import CoreJson
from task.LoginTask import LoginTask
from task.NavigateTask import NavigateTask

# browser_data = [{'browser_type': 'chrome', 'if_head': True}, {'browser_type': 'firefox', 'if_head': True}]
from util.HttpUtil import HttpUtil

browser_data = [{'browser_type': 'chrome', 'if_head': False}]


@pytest.mark.parametrize("driver", browser_data, indirect=True)
def test_login_success(driver, get_data, capture, logger):
    def_name = sys._getframe().f_code.co_name
    # 数据
    data = get_data[def_name]
    nv = NavigateTask(driver, data)
    nv.navigate()
    login = LoginTask(driver, data, capture, logger, atas_api)
    login.login_with_auth_success()
    driver.get_driver().quit()


@pytest.mark.parametrize("driver", browser_data, indirect=True)
def test_login_fail(driver, get_data, capture, logger):
    def_name = sys._getframe().f_code.co_name
    # 数据
    data = get_data[def_name]
    nv = NavigateTask(driver, data)
    nv.navigate()
    login = LoginTask(driver, data, capture, logger, atas_api)
    login.login_with_auth_fail()
    driver.get_driver().quit()


@pytest.mark.parametrize('data_set', CoreJson.get_json('data'))
@pytest.mark.skipif(CoreJson.get_json('data') is None, reason='Data is null')
@pytest.mark.issue(issue_id="111111", reason="Some bug", issue_type="PB")
def test_api(data_set, rp_logger):
    rp_logger.info(data_set.get('case_name'))
    headers = eval(data_set.get('header'))
    if data_set.get('method') == 'GET':
        try:
            res = HttpUtil.http_request(data_set.get('url'), data_set.get('method'), data_set.get('data'), None,
                                        None,
                                        headers=headers)
        except Exception as e:
            rp_logger.error(e)
            assert Exception
    else:
        try:
            res = HttpUtil.http_request(data_set.get('url'), data_set.get('method'), None, None,
                                        data_set.get('data'),
                                        headers=headers)
        except Exception as e:
            rp_logger.error(e)
    result = json.loads(res)
    if result.get('success'):
        rp_logger.info("pass")
        assert True
    else:
        rp_logger.warn("fail")
        assert False