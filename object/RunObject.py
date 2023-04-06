import time

from selenium.webdriver.common.by import By


class RunObject:
    def __init__(self, driver):
        self.driver = driver

    def plan_menu(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/aside/div/div/div[2]/ul[1]/li[6]/div/span/div",
                                                 30)

    def run_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/div/form/div/div[1]/div[2]/div/div/span/input",
                                                 30)

    def run_desc(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/span/textarea",
                                                 30)

    def cal_pass_by(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/div/form/div/div[3]/div[5]/div[2]/div/div/div/label[1]/span[2]",
                                                 30)

    def save_run(self):
        return self.driver.wait_and_find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/button[1]",
                                                 30)

    def run_list_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[2]/table/tbody/tr/td[2]/div/div/div/div",
                                                 30)

    def suite_select_placeholder(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Please select a suite']//parent::span[@aria-hidden]//preceding-sibling::input", 30)

    def suite_dropdown(self):
        return self.driver.wait_and_find_element(By.XPATH, "//ul[@role='listbox' and contains(@class,'select-menu')]//li[1]", 30)

    def pass_icon_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[2]/div/div[1]/div[2]/button[1]",
                                                 30)

    def step_hover(self):
        element = self.driver.wait_and_find_element(By.XPATH,
                                                    "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[2]/div/div[1]",
                                                    30)
        self.driver.action_hover(element)

    def pass_fail_button(self, status):
        if status == 'pass':
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div/button[1]",
                                                        30)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                                        "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div/button[2]",
                                                        30)
        return element

    def submit_next(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/div/div[1]/div[6]/div[2]/div/button[1]",
                                                 30)

    def actual_case_rate(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[2]/table/tbody/tr/td[7]/div/div/span",
                                                 30)

    def edit_scope_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Edit Scope']//parent::button",
                                                 30)

    def suite_add_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h5[text()='Suites']//parent::div//child::button",
                                                 30)

    def section_item(self, which):
        if which == 'All':
            element = self.driver.wait_and_find_element(By.XPATH,
                                                 "//h5[text()='Sections']//parent::div//ul//li[1]//div[contains(@class, 'label-selectable')]",
                                                 30)
        else:
            # which == 'Last'
            element = self.driver.wait_and_find_element(By.XPATH,
                                                 "//h5[text()='Sections']//parent::div//ul//li[last()]//div[contains(@class, 'label-selectable')]",
                                                 30)
        return element

    def checkbox_case(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h5[text()='Cases']//ancestor::div[2]//following-sibling::div//tr//th[1]//label",
                                                 30)

    def scope_page_case_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//h5[text()='Cases']//ancestor::div[2]//following-sibling::div//tbody//td[3]//div")

    def run_page_case_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr[not(contains(@class,'opened'))]//td[1]//button//span")

    def expect_case_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h5[text()='Cases']//ancestor::div[2]//following-sibling::div//tr//td[last()]//div",
                                                 30)

    def section_collapse_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[contains(@class,'level-1')][last()]//div[@class='next-box']//button",
                                                 30)

    def section_if_collapse(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[contains(@class,'level-1')][last()]",
                                                 30)

    def actual_case_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[not(contains(@class,'opened'))][last()]//span[contains(@class,'title')]",
                                                 30)

    def save_case(self):
        return self.driver.wait_and_find_element(By.XPATH, "//span[text()='Save']//parent::button", 30)

    def new_test_run_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='New Test Run']//parent::button",
                                                 30)

    def run_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//div[@role='dialog']",
                                                10)

    def test_run_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Test Run Name']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//child::input",
                                                 30)

    def test_run_description(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Description']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//child::textarea",
                                                 30)

    def run_start_date(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@placeholder='Start Date']",
                                                 30)

    def run_end_date(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@placeholder='End Date']",
                                                 30)

    def run_test_level_open(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Test Level']//ancestor::div[2]//following-sibling::div//span[contains(@class,'arrow')]",
                                                 30)

    def run_test_level_dropdown(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox' and contains(@class,'select-menu')]//span[text()='"+str(option)+"']",
                                                 30)

    def run_execution_type_open(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Execution Type']//ancestor::div[2]//following-sibling::div//span[contains(@class,'arrow')]",
                                                 30)

    def run_execution_type_dropdown(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox' and contains(@class,'select-menu')]//span[text()='" + str(
                                                     option) + "']",
                                                 30)

    def run_test_env_open(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Test Environment']//ancestor::div[2]//following-sibling::div//span[contains(@class,'arrow')]",
                                                 30)

    def run_test_env_dropdown(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox' and contains(@class,'select-menu')]//span[text()='" + str(
                                                     option) + "']",
                                                 30)

    def run_cal_pass_ratio_radio(self, by):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='"+str(by)+"']//preceding-sibling::span",
                                                 30)

    def save_run_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Save']//parent::button",
                                                 30)

    def run_list_first_run(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//child::div[contains(@class,'project-title')]",
                                                 20)

    def run_list_last_run(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'next-table-row') and contains(@class,'last')]//child::div[contains(@class,'project-title')]",
                                                 30)

    def run_list_desc(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//child::div[contains(@class,'title-desc')]",
                                                 30)

    def run_list_status(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//child::td[@data-next-table-col='2']//child::span",
                                                 30)

    def run_list_test_level(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//child::td[@data-next-table-col='3']//child::span",
                                                 30)

    def run_list_exec_type(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//child::td[@data-next-table-col='4']//child::span",
                                                 30)

    def run_list_test_env(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//child::td[@data-next-table-col='5']//child::span",
                                                 30)

    def run_list_passed_ratio(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//child::td[@data-next-table-col='6']//child::span",
                                                 30)

    def run_list_dates(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//child::td[@data-next-table-col='7']//child::span",
                                                 30)

    def run_list_actions_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//child::button",
                                                 30)

    def action_edit(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[text()='Edit']",
                                                 30)

    def action_duplicate(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[text()='Duplicate']",
                                                 30)

    def action_duplicate_and_reset(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[text()='Duplicate and Reset']",
                                                 30)

    def action_delete(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[text()='Delete']",
                                                 30)

    def run_delete_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//div[@role='alertdialog']",
                                                10)

    def delete_yes_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@role,'dialog')]//child::button[contains(@class,'primary')]",
                                                 30)

    def start_test_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Continue' or text()='Start Test' or text()='Test Again']",
                                                 20)

    def start_test_arrow_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Continue' or text()='Start Test' or text()='Test Again']//parent::button//following-sibling::button",
                                                 30)

    def edit_run(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[text()='Edit Run']",
                                                 30)

    def delete_run(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[text()='Delete']",
                                                 30)

    def run_detail_cases_row(self, row):
        return self.driver.find_elements(By.XPATH,
                                         "//tbody//tr[not(contains(@class,'opened'))]//td[1]//button[@title]")[row-1]

    def run_detail_issues_list(self):
        return self.driver.find_elements(By.XPATH,
                                         "//tbody//tr[not(contains(@class,'opened'))]//td[6]//div")

    def run_detail_issues_row(self, row):
        return self.driver.find_elements(By.XPATH,
                                         "//tbody//tr[not(contains(@class,'opened'))]//td[6]//div")[row-1]

    def run_detail_run_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h2[contains(@class,'title')]",
                                                 30)

    def run_detail_start_date(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h6[text()='Start Date']//following-sibling::div",
                                                 30)

    def run_detail_end_date(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h6[text()='End Date']//following-sibling::div",
                                                 30)

    def run_detail_test_level(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h6[text()='Test Level']//following-sibling::div",
                                                 30)

    def run_detail_exec_type(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h6[text()='Exec Type']//following-sibling::div",
                                                 30)

    def run_detail_test_env(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h6[text()='Test Env']//following-sibling::div",
                                                 30)

    def run_detail_id_to_assignee(self, id):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'id-tag') and text()='"+str(id)+"']//ancestor::tr//td[4]//button//span[2]",
                                                 30)

    def run_detail_select_all_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//thead//span//i",
                                                 30)

    def run_detail_assign_to_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(),'Assign To')]//parent::button",
                                                 30)

    def run_detail_first_assign_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[not(contains(@class,'opened'))][1]//td[4]//button",
                                                 30)

    def run_detail_first_assign_text(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[not(contains(@class,'opened'))][1]//td[4]//button//span[2]",
                                                 30)

    def run_detail_assignee_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr[not(contains(@class,'opened'))]//td[4]//button//span[2]")

    def run_detail_no_assign_btn(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//i[text()='No Assignee']//parent::button")

    def run_detail_first_no_assign_btn(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//i[text()='No Assignee']//parent::button")[0]

    def run_detail_first_no_assign_id(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//i[text()='No Assignee']//ancestor::tr//div[contains(@class,'id-tag')]")[0]

    def run_detail_assign_dropdown(self, who):
        if who != 'me':
            element = self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='menu']//span[contains(text(),'"+str(who)+"')]//parent::div",
                                                30)
        else:
            element = self.driver.wait_and_find_element(By.XPATH,
                                              "//ul[@role='menu']//li[1]//div",
                                                30)
        return element

    def run_detail_first_case_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[not(contains(@class,'opened'))][1]//td[1]//button",
                                                 20)

    def run_detail_untest_case_name(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[text()='Untested']//ancestor::tr//td[1]//button")

    def run_detail_first_untest_case_name(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[text()='Untested']//ancestor::tr//td[1]//button")[0]

    def run_detail_first_case_status(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[not(contains(@class,'opened'))][1]//child::i[contains(@class,'small')]//child::*[name()='use']",
                                                 30)

    def case_list_id_match_case(self, id):
        return self.driver.wait_and_find_element(By.XPATH,
                                                "//div[text()='"+str(id)+"']//ancestor::tr",
                                                30)

    def case_list_selected_case(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                "//tr[contains(@class,'selected')]",
                                                30)

    def case_list_selected_case_id(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                "//tr[contains(@class,'selected')]//td[1]//div[contains(@class,'id-tag')]",
                                                30)

    def case_list_selected_case_status(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                "//tr[contains(@class,'selected')]//td[last()]//*[name()='use']",
                                                30)

    def case_list_above_selected_case(self):
        return self.driver.find_elements(By.XPATH,
                                                "//tr[contains(@class,'selected')]//preceding-sibling::tr[not(contains(@class,'opened'))]")[0]

    def case_list_above_selected_case_id(self):
        return self.driver.find_elements(By.XPATH,
                                                "//tr[contains(@class,'selected')]//preceding-sibling::tr[not(contains(@class,'opened'))]//td[1]//div[contains(@class,'id-tag')]")[0]

    def case_list_above_selected_case_status(self):
        return self.driver.find_elements(By.XPATH,
                                                "//tr[contains(@class,'selected')]//preceding-sibling::tr[not(contains(@class,'opened'))]//td[last()]//*[name()='use']")[0]

    def second_case_name(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//tr[not(contains(@class,'opened'))][2]",
                                                20)

    def next_case_name_from_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[not(contains(@class,'opened'))][2]",
                                                 20)

    def add_result_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div/div/div[3]/div[2]/div[2]/div[1]/button[1]",
                                                 20)

    def add_result_status_option(self, status):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='"+str(status)+"']//parent::button",
                                                 30)

    def pass_all_and_next_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Pass All and Next']//parent::button",
                                                 30)

    def pass_all_steps_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//label[text()='Steps']//ancestor::div[2]//following-sibling::div//div[contains(@class,'step-desc')]//*[name()='use']")

    def submit_and_next_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Submit & Next']//parent::button",
                                                 30)

    def submit_and_next_arrow_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Submit & Next']//parent::button//following-sibling::button",
                                                 30)

    def submit_and_raise_issue(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox' and contains(@class, 'next-overlay-inner')]//li[2]",
                                                 30)

    def submit_and_close(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox' and contains(@class, 'next-overlay-inner')]//li[1]",
                                                 30)

    def case_effort_min(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(text(), 'Effort')]//following-sibling::span//input",
                                                 30)

    def drag_file_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(),'files')]",
                                                 30)

    def add_attachment(self):
        js = "document.getElementsByName('file')[0].style.display='block';"
        self.driver.get_driver().execute_script(js)
        time.sleep(3)
        return self.driver.wait_and_find_element(By.NAME,
                                                 "file",
                                                 30)

    def upload_attachment(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@type='file']",
                                                 30)

    def link_to_issue_radio(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(),'Link')]//preceding-sibling::span",
                                                 30)

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

    # def case_page_step_status_icon(self):
    #     return self.driver.wait_and_find_element(By.XPATH,
    #                                              "//label[text()='Steps']//ancestor::div[2]//following-sibling::div//child::*[name()='use']",
    #                                              30)

    def case_page_step_status_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div/div/div[3]/div[2]/div[1]/div[1]/div/div/div/div/div/form/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/i//child::*[name()='use']",
                                                 30)

    def case_page_issue_num(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//li[@role='tab']//span[text()='Issues']//following-sibling::sup",
                                                 30)

    def case_detail_attachment_title(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//span[text()='Attachments']",
                                                10)

    def case_detail_attachment_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//span[text()='Attachments']//parent::div//div[contains(@class,'preview')]//div")

    def all_priorities_arrow_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(@class,'criteria')][1]//child::span[contains(@class,'arrow')]",
                                                 30)

    def all_priorities_dropdown(self, priority):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='"+str(priority)+"']//ancestor::li",
                                                 30)

    def all_priorities_selected(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(@class,'criteria')][1]//child::span[@class='next-tag-body']",
                                                 30)

    def all_priorities_result_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tr[not(contains(@class,'opened'))]//child::td[2]//span")

    def all_assignees_arrow_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(@class,'criteria')][2]//child::span[contains(@class,'arrow')]",
                                                 30)

    def all_assignees_none(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//span[text()='No Options']",
                                                 10)

    def all_assignees_dropdown(self, assignee):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h6[contains(text(),'"+str(assignee)+"')]",
                                                 30)

    def all_assignees_selected(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(@class,'criteria')][2]//child::span[@class='next-tag-body']",
                                                 30)

    def all_assignees_result_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tr[not(contains(@class,'opened'))]//child::td[4]//button//span[2]")

    def all_status_arrow_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(@class,'criteria')][3]//child::span[contains(@class,'arrow')]",
                                                 30)

    def all_status_dropdown(self, status):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox']//div[contains(text(),'"+str(status)+"')]",
                                                 30)

    def all_status_selected(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(@class,'criteria')][3]//child::*[name()='use']",
                                                 30)

    def all_status_result_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tr[not(contains(@class,'opened'))]//child::td[5]//div[contains(@style,'2px')]")

    def search_bar(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[contains(@placeholder,'Search')]",
                                                 30)

    def search_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[contains(@placeholder,'Search')]//parent::span//child::button[2]",
                                                 30)

    def search_result_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tr[not(contains(@class,'opened'))]//child::td[1]//button//span")

    def filter_delete_yes_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@role='alertdialog']//child::button[contains(@class,'primary')]",
                                                 30)

    def run_names_list(self):
        return self.driver.find_elements(By.XPATH,
                                         "//tbody//tr//child::div[contains(@class,'project-title')]")

    def case_details_tab(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='tablist']//li[1]//div",
                                                 30)

    def case_history_tab(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='tablist']//li[2]//div",
                                                 30)

    def case_issues_tab(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='tablist']//li[3]//div[contains(@class,'tab')]",
                                                 30)

    def case_history_find_execution(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//span[contains(@class,'exec-num')]",
                                                10)

    def case_history_count_execution(self):
        return self.driver.find_elements(By.XPATH,
                                         "//span[contains(@class,'exec-num')]")

    def case_history_find_issue(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//span[@class='next-btn-helper' and contains(text(),'Issues')]",
                                                10)

    def case_history_count_issue(self):
        return self.driver.find_elements(By.XPATH,
                                         "//span[@class='next-btn-helper' and contains(text(),'Issues')]")

    def case_history_find_attachment(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//span[@class='next-btn-helper' and contains(text(),'Attachments')]",
                                                10)

    def case_history_count_attachment(self):
        return self.driver.find_elements(By.XPATH,
                                         "//span[@class='next-btn-helper' and contains(text(),'Attachments')]")

    def case_issue_id_all(self):
        return self.driver.find_elements(By.XPATH,
                                         "//tbody[contains(@class,'table')]//tr//td[1]//span[contains(@class,'tag')]")

    def case_issue_action_all(self):
        return self.driver.find_elements(By.XPATH,
                                         "//tbody[contains(@class,'table')]//tr//td[4]//button")

    def case_issue_action_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                         "//tbody[contains(@class,'table')]//tr[1]//td[4]//button", 30)

    def no_data(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                         "//div[text()='No Data']", 10)




