import time

from selenium.webdriver.common.by import By


class LoginObject:
    def __init__(self, driver):
        self.driver = driver

    def account_tab(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[text()='Account']",
                                                 20)

    def user_name(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@placeholder='Username']")

    def user_pwd(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@placeholder='Password']")

    def login_bt(self):
        return self.driver.find_element(By.XPATH,
                                        "//span[text()='Login']//parent::button")

    def login_bt_exist(self):
        time.sleep(3)
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//span[text()='Login']//parent::button",
                                                 20)

    def new_project_bt(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='New Project']//parent::button",
                                                 10)

    def login_fail_pop(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[3]/div/div",
                                                 30)

    def logout_label(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(@class, 'avatar-circle')]",
                                                 30)

    def logout_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div/div[2]/ul/li[2]/div",
                                                 10)

    def login_sso_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/button",
                                                 10)

    def login_sso_input(self):
        return self.driver.wait_and_find_element(By.ID, "idp-discovery-username", 10)

    def login_okta_input(self):
        return self.driver.wait_and_find_element(By.ID, "okta-signin-username", 10)

    def login_okta_password(self):
        return self.driver.wait_and_find_element(By.ID, "input72", 10)
