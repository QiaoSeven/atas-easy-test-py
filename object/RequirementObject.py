import time

from selenium.webdriver.common.by import By


class RequirementObject:
    def __init__(self, driver):
        self.driver = driver

    def create_rqm_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(), 'Create')]//parent::button", 30)

    def create_rqm_arrow(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(), 'Create')]//parent::button//following-sibling::button", 30)

    def dropdown_link_rqm(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(), 'Link')]//parent::div", 30)

    def rqm_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//div[@role='dialog']", 10)

    def rqm_modal_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Title']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input", 30)

    def rqm_modal_type_arrow(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Type']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//span[@class='next-input-control']", 30)

    def rqm_modal_type_dropdown(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='"+str(option)+"']//parent::div", 30)

    def rqm_modal_pri_arrow(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Priority']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//span[@class='next-input-control']", 30)

    def rqm_modal_pri_dropdown(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='"+str(option)+"']//parent::div[contains(@class, 'inner')]", 30)

    def rqm_modal_status_arrow(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Testing Status']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//span[@class='next-input-control']", 30)

    def rqm_modal_status_dropdown(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='"+str(option)+"']//parent::div", 30)

    def rqm_modal_dropdown_null(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//ul[@aria-hidden='false']//span[text()='No Options']", 10)

    def rqm_modal_dropdown_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@aria-hidden='false']//input", 30)

    def rqm_modal_dropdown_add_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@aria-hidden='false']//button", 30)

    def rqm_modal_dropdown_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@aria-hidden='false']//ul//li[1]//div[contains(@class, 'next-box')]//span", 30)

    def rqm_modal_feature_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Feature']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input", 30)

    def rqm_modal_release_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Release']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input", 30)

    def rqm_modal_version_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Version']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input", 30)

    def rqm_modal_sprint_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Sprint']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input", 30)

    def rqm_modal_tags_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Tags']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input", 30)

    def rqm_modal_sum_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@role='textbox']", 30)

    def rqm_modal_save_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Save']//parent::button", 20)

    def link_modal_ticket_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@role='dialog']//input", 30)

    def link_modal_search_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@role='dialog']//button", 30)

    def link_modal_priority(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@role='dialog']//div[contains(text(),'Priority')]//following-sibling::div", 20)

    def link_modal_add_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(),'Add')]//parent::button", 20)

    def edit_modal_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h2", 30)

    def edit_modal_attachments(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//i[contains(@class,'next-icon-attachment')]",
                                                10)

    def edit_modal_attachment_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'preview')]//div[contains(@class, 'FileUploader')]")

    def edit_modal_edit_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Edit']//parent::button", 30)

    def edit_modal_save_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Save']//parent::button", 30)

    def edit_modal_cases_tab(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//li[@role='tab'][2]//div", 30)

    def edit_modal_link_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Link Case']//parent::button", 30)

    def edit_modal_case_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@role and @placeholder]", 30)

    def edit_modal_attachment_add(self):
        js = "document.getElementsByName('file')[0].style.display='block';"
        self.driver.get_driver().execute_script(js)
        time.sleep(3)
        return self.driver.wait_and_find_element(By.NAME,
                                                 "file",
                                                 30)

    def edit_modal_dropdown_first_case(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox' and contains(@class, 'next-select-menu')]//li[1]//span[@style]", 30)

    def edit_modal_list_first_case(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//td[3]//span", 30)

    def search_bar(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@placeholder]", 30)

    def no_data(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                         "//div[text()='No Data']", 10)

    def rqm_name_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr//div[@title]")

    def rqm_name_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//div[@title]", 30)

    def rqm_pri_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//td[3]//span", 30)

    def rqm_feature_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//td[4]//div", 30)

    def rqm_release_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//td[5]//div", 30)

