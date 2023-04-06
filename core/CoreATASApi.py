import json

from core.CoreConfig import CoreConfig
from util.HttpUtil import HttpUtil
from atas_client import atas_client


class CoreATASApi:
    def __init__(self, logger):
        self.logger = logger
        self.ip = CoreConfig.get_atas_config('ip')
        self.port = CoreConfig.get_atas_config('port')
        self.auth = CoreConfig.get_atas_config('auth-key')
        self.launch = CoreConfig.get_atas_config('launch')
        self.executor = CoreConfig.get_atas_config('executor')
        self.uri = CoreConfig.get_atas_config('uri')

    def upload_result(self, data):
        atas_client.upload_result(self.uri, self.auth, data['executionId'], data['caseName'], data['stepDescription'],
                                  data['stepStatus'], data['caseStatus'], self.executor, data['path'],
                                  data['screen_path'], data['attachment_path'], data['startTime'], data['endTime'])

    def upload_init(self):
        return atas_client.init(self.uri, self.auth, self.launch, self.executor)

    def upload_complete(self, execution_id):
        atas_client.complete(self.uri, self.auth, execution_id=execution_id, case_status='Completed')

    def init_result(self):
        headers = "{\"Content-Type\": \"application/json;charset=UTF-8\",\"auth-key\": \"" + self.auth + "\"}"
        url = self.uri + "/automation/launch/init"
        body = "{\"launchName\":\"" + self.launch + "\", \"executor\": \"" + self.executor + "\"}"
        method = "post"
        try:
            res = HttpUtil.http_request(url, method, None, None, json.loads(body), headers=eval(headers))
        except Exception as e:
            self.logger.error(e)
        execution_id = json.loads(res)['data']['executionId']
        return execution_id

    def save_result(self, data):
        url = self.uri + "/automation/launch/execute"
        item = {"executor": self.executor}
        data.update(**item)
        screen_path = data['screen_path']
        attachment_path = data['attachment_path']
        if screen_path is None:
            screen = ('snapshot', (
                '', '',
                'image/png'))
        else:
            screen = ('snapshot', (
                screen_path[screen_path.rindex("/") + 1:], open(screen_path, 'rb'),
                'image/png'))
        if attachment_path is None:
            attachment = ('attachment', (
                '', '',
                'image/png'))
        else:
            attachment = ('attachment', (
                attachment_path[attachment_path.rindex("/") + 1:], open(attachment_path, 'rb'),
                'image/png'))
        files = [screen, attachment]
        try:
            res = HttpUtil.http_multipart_request(url, data, files, auth_key=self.auth)
        except Exception as e:
            self.logger.error(e)
        return res

    def run_complete(self, execution_id, case_status):
        headers = "{\"Content-Type\": \"application/json;charset=UTF-8\",\"auth-key\": \"" + self.auth + "\"}"
        url = self.uri + "/automation/launch/execution/complete"
        body = "{\"executionId\":" + str(execution_id) + ", \"caseStatus\": \"" + case_status + "\"}"
        method = "post"
        try:
            res = HttpUtil.http_request(url, method, None, None, json.loads(body), headers=eval(headers))
        except Exception as e:
            self.logger.error(e)
        return res


if __name__ == '__main__':
    core = CoreATASApi(None)
    # print(core.init_result())
    # data = {'caseName': '2_test_case_001',
    #         'path': '/Suiite001/',
    #         'stepStatus': 'pass',
    #         'stepDescription': 'tester',
    #         'caseStatus': 'pass',
    #         'executor': 'dingtao',
    #         'screen_path': '/Users/tao.ding/PycharmProjects/atas-easy-test-py/screen/Login fail-1.png',
    #         'attachment_path': None,
    #         'executionId': '2'}
    # print(core.save_result(data))
    print(core.run_complete(2, 'Pass'))
