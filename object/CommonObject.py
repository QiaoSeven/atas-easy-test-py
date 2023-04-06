from selenium.webdriver.common.by import By


class CommonObject:
    def __init__(self, driver):
        self.driver = driver

    def get_element_by_text(self, text):
        return self.driver.wait_and_find_element(By.XPATH, "//*[text()='"+text+"']", 10)


