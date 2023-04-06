import time

from selenium.webdriver.common.by import By


class SuiteObject:
    def __init__(self, driver):
        self.driver = driver

    def case_menu(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div/section/section/aside/div/div/div[2]/ul[1]/li[5]/div/span/div/span",
                                                 30)

    def new_suite_bt(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div[2]/div/div[1]/div[2]/button",
                                                 30)

    def suite_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/div/form/div/div[1]/div[2]/div/div/span/input",
                                                 30)

    def suite_desc(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/span/textarea")

    def suite_save(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/button[1]")

    def suite_in_list(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//div[contains(@class, 'project-title')]",
                                                 30)

    def suite_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH, "//div[contains(@role,'dialog')]", 10)

    def get_first_suite(self):
        time.sleep(1)
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//div[contains(@class,'project-title')]",
                                                 30)
