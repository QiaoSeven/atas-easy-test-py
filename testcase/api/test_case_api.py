import json
import sys

import pytest

from core import CoreResult
from core.CoreATASApi import CoreATASApi
from core.CoreJson import CoreJson
from core.CoreResult import global_list
from util.HttpUtil import HttpUtil
from util.JsonUtil import JsonUtil
from util.TimeUtil import TimeUtil


class TestCaseApi:
    @pytest.mark.parametrize('data_set', CoreJson.get_json('data'))
    @pytest.mark.skipif(CoreJson.get_json('data') is None, reason='Data is null')
    @pytest.mark.issue(issue_id="111111", reason="Some bug", issue_type="PB")
    def test_api(self, data_set, rp_logger, atas_api, logger):
        start_time = TimeUtil.get_current_time()
        # rp_logger.info(data_set.get('url') + "||" + data_set.get('method') + "||" + data_set.get('case_name'))
        # rp_logger.info("Input: " + json.dumps(data_set.get('data')))
        headers = eval(data_set.get('header'))
        if data_set.get('method') == 'GET':
            try:
                res = HttpUtil.http_request(data_set.get('url'), data_set.get('method'), data_set.get('data'), None,
                                            None,
                                            headers=headers)
            except Exception as e:
                # rp_logger.error(e)
                print(sys.stdout)
                assert Exception
        else:
            try:
                res = HttpUtil.http_request(data_set.get('url'), data_set.get('method'), None, None,
                                            data_set.get('data'),
                                            headers=headers)
            except Exception as e:
                # rp_logger.error(e)
                assert Exception
        result = json.loads(res)
        end_time = TimeUtil.get_current_time()
        print(result['data'])
        verify = JsonUtil.diff_json(data_set.get('verify'), result['data'])
        if not verify:
            # rp_logger.info("pass")
            # CoreResult.append_list(global_list, 'test_case_api', data_set.get('url'), "", "", "pass")
            atas_api.upload_result(CoreResult.get_upload_result(
                data_set.get('url') + '-' + data_set.get('method'),
                None,
                None, start_time,
                end_time))
            assert True
        else:
            # rp_logger.warn("fail")
            atas_api.upload_result(CoreResult.get_upload_result(verify,
                                                                None,
                                                                None, start_time,
                                                                end_time, 'fail', 'fail'))
            assert False
        # rp_logger.info("Output: " + json.dumps(result))
