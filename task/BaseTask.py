from distutils.util import strtobool

from business.AtasVerify import AtasVerify
from core import CoreResult
from core.CoreATASApi import CoreATASApi
from core.CoreConfig import CoreConfig


class BaseTask:
    def __init__(self, driver, data, capture, logger, atas_api):
        self.driver = driver
        self.data = data
        self.capture = capture
        self.logger = logger
        self.result = CoreResult
        self.verify = AtasVerify(self.logger)
        self.core = CoreATASApi(logger)
        self.atas_api = atas_api
        self.if_upload_rp = strtobool(CoreConfig.if_report_portal())
        self.if_upload_atas = strtobool(CoreConfig.if_report_atas())

