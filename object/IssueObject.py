from selenium.webdriver.common.by import By


class IssueObject:
    def __init__(self, driver):
        self.driver = driver

    def settings_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class, 'SettingMenu') and text()='Settings']", 30)

    def edit_pro_option(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[text()='Edit Project']//preceding-sibling::button", 30)

    def edit_pro_url_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='JIRA URL']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input", 30)

    def edit_pro_key_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='JIRA Project Key']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input", 30)

    def edit_pro_save_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Save']//parent::button", 20)

    def create_jira_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(), 'Create')]//parent::button", 30)

    def create_jira_arrow(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(), 'Create')]//parent::button//following-sibling::button", 30)

    def dropdown_link_jira(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(), 'Link')]//parent::div", 30)

    def jira_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//div[@role='dialog']", 10)

    def jira_modal_summary(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Summary']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input", 30)

    def jira_modal_pri_arrow(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Priority']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//span[@class='next-input-control']", 30)

    def jira_modal_pri_dropdown(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='"+str(option)+"']//parent::div[contains(@class, 'inner')]", 30)

    def jira_modal_assignee(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Assignee']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input", 30)

    def jira_modal_save_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Save']//parent::button", 20)

    def link_to_issue_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(),'http')]//following-sibling::span//input",
                                                 30)

    def link_to_issue_search(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(),'Search')]//parent::button",
                                                 30)

    def link_to_issue_link(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Link']//parent::button",
                                                 30)

    def search_bar(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@placeholder]", 30)

    def no_data(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                         "//div[text()='No Data']", 10)

    def jira_id_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr//div[@title]//span[contains(@class, 'tag')]", 30)

    def jira_id_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//div[@title]//span[contains(@class, 'tag')]", 30)

    def jira_name_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr//div[@title]//span[contains(@class, 'title')]")

    def jira_name_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//div[@title]//span[contains(@class, 'title')]", 30)

    def jira_status_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//td[2]//span", 30)

    def jira_pri_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//td[3]//span", 30)

    def jira_refresh_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//td[4]//div[contains(@class, 'Action')]//button[1]", 30)



