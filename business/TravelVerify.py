

class TravelVerify:
    def __init__(self, logger):
        self.logger = logger

    def verify_search_no_result(self, actual_result, expect_result):
        if actual_result == expect_result:
            assert True
        else:
            self.logger.error('Search fail')
            assert False

    def verify_login_fail(self, actual_result, expect_result):
        if actual_result in expect_result:
            assert True
        else:
            self.logger.error('Login fail message is incorrect')
            assert False

    def verify_login_fail_bt(self, element):
        if element is not None:
            assert element.is_enabled()
        else:
            self.logger.error('Login success')
            assert False
