import sys

import pytest

from task.CommonTask import CommonTask

# browser_data = [{'browser_type': 'chrome', 'if_head': True}, {'browser_type': 'firefox', 'if_head': True}]
browser_data = [{'browser_type': 'chrome', 'if_head': True}]


class TestLogin:
    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_login_key_driven(driver, data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        login = CommonTask(driver, data, capture, logger, atas_api)
        for action in data.keys():
            c = getattr(login, action)
            c()
        driver.get_driver().quit()
