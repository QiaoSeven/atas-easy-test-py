from selenium.webdriver.common.by import By


class CaseObject:
    def __init__(self, driver):
        self.driver = driver

    def new_section(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(@class, 'next-search')]//following-sibling::div//button",
                                                 30)

    def add_section(self):
        return self.driver.wait_and_find_element(By.XPATH, "//ul[@role='menu']//span[text()='Add Section']", 30)

    def parent_section_item(self):
        return self.driver.wait_and_find_element(By.XPATH, "/html/body/div[3]/div/div/ul/li/div/div/div", 30)

    def parent_section(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div/div/form/div/div[1]/div[1]/div[2]/div/div/span/span[1]",
                                                 30)

    def section_name(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div/form/div/div[1]/div[2]/div[2]/div[1]/div/span/input")

    def section_desc(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div/form/div/div[2]/div[2]/div/div/span/textarea")

    def save_section(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/button[1]")

    def save_close(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/button[1]")

    def new_case(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div[2]/div/div[3]/div[1]/div/div/div[1]/div/button",
                                                 30)

    def section_select(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Section']//parent::span//preceding-sibling::input",
                                                 30)

    def section_select_item(self, text):
        return self.driver.wait_and_find_element(By.XPATH, "//*[contains(text(), " + text + ")]", 30)

    # def section_select_last_item(self):
    #     return self.driver.wait_and_find_element(By.XPATH, "/html/body/div[3]/div/div/ul/li/ul/li/div/div/div", 30)

    def case_template(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/form/div/div[2]/div/div[2]/div[2]/div/div/div/span/span[1]/span[1]/span",
                                                 30)

    def case_template_item(self):
        return self.driver.wait_and_find_element(By.XPATH, "/html/body/div[4]/ul/li[11]/div", 30)

    def case_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/form/div/div[1]/div/div/div/div/span/input",
                                                 30)

    def execute_js_precondition(self, text):
        test_js = 'document.getElementClassName("editor-container--U87rRgcD rdw-editor-wrapper").contentWindow.document.body.innerText="%s"' % text
        self.driver.get_driver().execute_script(test_js)

    def switch_to_precondition(self):
        self.driver.get_driver().switch_to.frame(
            self.driver.find_element(By.CLASS_NAME, "editor-container--U87rRgcD rdw-editor-wrapper"))

    def case_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH, "//div[contains(@role,'dialog')]", 10)

    def case_priority_open(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//form//span[contains(@class, 'next-select-values')]")[1]

    def case_priority_dropdown(self, priority):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox']//span[text()='"+str(priority)+"']//parent::div",
                                                 30)

    def case_estimation(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(),'min')]//preceding-sibling::input",
                                                 30)

    def precondition(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div",
                                                 30)

    def add_step(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div/form/div/div[3]/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div[3]/div/div/div/div/div/button[1]",
                                                 30)

    def steps(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody[@class='next-table-body']//tr[last()]//textarea[contains(@placeholder,'steps')]",
                                                 30)

    def expect(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody[@class='next-table-body']//tr[last()]//textarea[contains(@placeholder,'results')]",
                                                 30)

    def list_case_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[not(contains(@class,'opened'))][last()]//span[contains(@class,'title')]",
                                                 30)

    def list_case_priority(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[not(contains(@class,'opened'))][last()]//td[2]//span",
                                                 30)

    def list_case_estimation(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[not(contains(@class,'opened'))][last()]//td[3]//span",
                                                 30)

    def case_names_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr[not(contains(@class,'opened'))]//span[contains(@class,'title')]")

    def case_name_line(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div/section/section/section/div/div/div/div[2]/div[3]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[1]/div",
                                                 30)

    def section_delete_check_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[contains(@class,'opened')][last()]//td[1]",
                                                 30)

    def section_delete_icon_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[contains(@class,'opened')][last()]//div[contains(@class,'action-group')]//button[4]",
                                                 30)

    def case_action_more(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div/section/section/section/div/div/div/div[2]/div[3]/div[1]/button",
                                                 30)

    def case_delete_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div/ul/li[8]/div/span/div/button",
                                                 30)

    def section_delete_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH, "//div[contains(@role,'dialog')]", 10)

    def section_delete_yes_button(self):
        return self.driver.wait_and_find_element(By.XPATH, "//div[contains(@role,'dialog')]//button[1]", 30)

    def case_delete_yes_button(self):
        return self.driver.wait_and_find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[3]/button[1]", 30)

    def case_delete_item(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "/html/body/div/section/section/section/div/div/div/div[2]/div[3]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[1]/div/div/div[2]/div[1]/div[2]",
                                                10)

    def section_collapse_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[contains(@class,'level-0')][last()]//div[@class='next-box']//button",
                                                 30)

    def section_if_collapse(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[contains(@class,'level-0')][last()]",
                                                 30)

    def section_select_last_item(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='tree' and contains(@class,'dropdown')]//ul//li[last()]//div[contains(@class,'select')]",
                                                 30)

    def filter_view(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[text()='Filter View']",
                                                 20)

    def new_test_case_filter_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='New Test Case Filter']//parent::button",
                                                 30)

    def filter_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//div[contains(@class,'filter-container--wRy_8b9U')]",
                                                10)

    def filter_information_filter_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@placeholder='Filter name']",
                                                 30)

    def filter_criteria_column_name_arrow_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@placeholder='Column Name']",
                                                 30)

    def filter_criteria_column_name_dropdown(self, name):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@role='option' and @title='"+str(name)+"']",
                                                 30)

    def filter_criteria_condition_arrow_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@placeholder='Condition']",
                                                 30)

    def filter_criteria_condition_dropdown(self, condition):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@role='option' and @title='"+str(condition)+"']",
                                                 30)

    def filter_criteria_criteria_textbox(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@placeholder='Criteria']",
                                                 30)

    def filter_criteria_criteria_dropdown(self, cri):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox']//li//span[text()='"+str(cri)+"']//parent::div",
                                                 30)

    def filter_criteria_criteria_arrow_icon(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//input[@placeholder='Criteria']//ancestor::span[contains(@class,'value')]//following-sibling::span[@class]",
                                                 10)

    def filter_columns_select_single(self, columns):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//p[text()='"+str(columns)+"']//parent::div//following-sibling::button",
                                                 30)

    def filter_columns_select_all(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                "//div[contains(@style,'justify-content') and contains(@style,'padding: 0px 10px')]//child::button[last()]",
                                                30)

    def filter_save_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Save']//parent::button",
                                                 30)

    def filter_names_list(self):
        return self.driver.find_elements(By.XPATH,
                                         "//ul[@class='next-list-items']//child::li//child::span")

    def last_filter_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//li[@device][last()]//child::span",
                                                 30)

    def filter_action_check_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//li[last()][contains(@class,'list')]//child::div[2]",
                                                 30)

    def filter_edit_icon_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//li[last()][contains(@class,'list')]//child::div[2]//child::button[1]",
                                                 30)

    def filter_delete_icon_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//li[last()][contains(@class,'list')]//child::div[2]//child::button[2]",
                                                 30)

    def delete_filter_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//div[@role='dialog']",
                                                10)

    def filter_delete_yes_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@role='dialog']//child::button[contains(@class,'primary')]",
                                                 30)

    def filter_results_list_new_column(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//thead//child::th[last()]//child::div",
                                                 30)

    def filter_results_list_first_column(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//thead//child::th[3]//child::div",
                                                 30)

