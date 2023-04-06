import sys

import pytest
from selenium.webdriver.common.by import By

from task.LoginTask import LoginTask
from task.NavigateTask import NavigateTask

# browser_data = [{'browser_type': 'chrome', 'if_head': True}, {'browser_type': 'firefox', 'if_head': True}]
from task.TravelHomeTask import TravelHomeTask

browser_data = [{'browser_type': 'ios', 'if_head': True}]


class TestIos:
    @pytest.mark.parametrize("driver", browser_data, indirect=True)
    def test_ios(self, driver, get_data, capture, logger, atas_api):
        def_name = sys._getframe().f_code.co_name
        # 数据
        data = get_data[def_name]
        hotel = TravelHomeTask(driver, data, capture, logger, atas_api)
        hotel.login_hotel_i()
        driver.get_driver().quit()
