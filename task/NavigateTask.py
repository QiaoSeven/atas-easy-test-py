
class NavigateTask:

    def __init__(self, driver, data):
        self.driver = driver.get_driver()
        self.data = data

    def navigate(self):
        data = self.data['url']
        self.driver.get(data)

