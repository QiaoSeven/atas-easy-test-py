import json
import logging

import pytest

from reportportal_client import RPLogger

from core import CoreResult
from core.CoreATASApi import CoreATASApi
from core.CoreCapture import CoreCapture
from core.CoreConfig import CoreConfig
from core.CoreWebDriver import CoreWebDriver
from util.ExcelUtil import ExcelUtil
from util.LogUtil import Logger


@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    yield logger


@pytest.fixture(scope="session")
def atas_api():
    atas_api = CoreATASApi(logger)
    yield atas_api


@pytest.fixture(scope='session', autouse=True)
def result_api(atas_api):
    # core = CoreATASApi(logger)
    if CoreResult.get_execution_id() == '':
        execute_id = atas_api.upload_init()
        CoreResult.set_execution_id(execute_id)
        print(execute_id)
    CoreResult.set_execution_id(CoreResult.get_execution_id())
    yield
    atas_api.upload_complete(execution_id=CoreResult.get_execution_id())


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果，返回一个result对象
    out = yield
    report = out.get_result()
    print('测试报告：%s' % report)
    print('步骤：%s' % report.when)
    print('nodeid：%s' % report.nodeid)
    print('description:%s' % str(item.function.__doc__))
    print(('运行结果: %s' % report.outcome))
    print(report.capstderr)
    if CoreConfig.if_report_atas() == "True":
        CoreResult.set_case_name(report.nodeid)
        if report.outcome != 'passed':
            core = CoreATASApi(logger)
            if CoreResult.get_execution_id() == '':
                execute_id = core.upload_init()
                CoreResult.set_execution_id(execute_id)
            data = {'caseName': CoreResult.get_case_name(),
                    'path': CoreResult.get_path(),
                    'stepStatus': report.outcome,
                    'stepDescription': report.capstderr,
                    'caseStatus': report.outcome,
                    'screen_path': None,
                    'attachment_path': None,
                    'executionId': CoreResult.get_execution_id(),
                    'startTime': '',
                    'endTime': ''}
            core.upload_result(data)


@pytest.fixture
def get_data():
    data = ExcelUtil.get_all_data_dict(CoreConfig.get_data_full_path())
    yield data


@pytest.fixture
def driver(request, logger):
    driver = CoreWebDriver(request.param['browser_type'], request.param['if_head'], logger)
    yield driver


@pytest.fixture
def close(driver):
    driver.get_driver().quit()


@pytest.fixture
def capture(driver, rp_logger):
    capture = CoreCapture(driver, rp_logger)
    yield capture


@pytest.fixture(scope='session')
def logger():
    logger = Logger(CoreConfig.get_log_info().get('file_path'), CoreConfig.get_log_info().get('level'),
                    CoreConfig.get_log_info().get('rotation'), CoreConfig.get_log_info().get('backup')).logger
    yield logger


def pytest_collection_modifyitems(items):
    # 期望用例顺序按照.py文件执行
    appoint_classes = {"TestLogin": [], "TestProject": [], "TestSuite": [], "TestCase": [], "TestRequirement": [],
                       "TestRun": [], "TestReport": [], "TestIssue": [],
                       "TestAndroid": [], "TestIos": [], "TestAndroidLogin": [],
                       "TestAndroidKobiton": [], "TestIosKobiton": [], "TestLogout": [],
                       "TestProjects": [], "TestRequirements": [], "TestIssues": [], "TestSuites": [], "TestCases": [],
                       "TestRuns": [], "TestReports": [], "TestCaseApi": []}

    for item in items:
        for cls_name in appoint_classes:
            if item.parent.name == cls_name:
                appoint_classes[cls_name].append(item)
    items.clear()
    for cases in appoint_classes.values():
        items.extend(cases)
