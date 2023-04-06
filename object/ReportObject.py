import time

from selenium.webdriver.common.by import By


class ReportObject:
    def __init__(self, driver):
        self.driver = driver

    #  下面的def 都是Wang Zhuo编写的

    def reports_menu(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[contains(@aria-label,'nav')]//child::li[6]",
                                                 30)

    def report_search_bar(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[contains(@placeholder,'Search reports')]",
                                                 30)

    def report_search_icon(self):
        time.sleep(1)
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//i[contains(@class,'icon-search')]//parent::button",
                                                 30)

    def report_search_result_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tr[contains(@class,'next-table-row')]//child::div[contains(@class,'project-title')]")

    def report_new_report_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                "//span[text()='New Report']//parent::button",
                                                30)

    def report_report_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                "//label[text()='Report Name']//ancestor::div[2]//following-sibling::div//child::input",
                                                30)

    def report_report_summary(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                "//label[text()='Summary']//ancestor::div[2]//following-sibling::div//child::textarea[1]",
                                                30)

    def report_report_type(self, rp_type):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[contains(text(),'"+str(rp_type)+"')]//preceding-sibling::span",
                                                 30)

    def report_cal_ratio_radio(self, ratio):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='"+str(ratio)+"']//preceding-sibling::span",
                                                 30)

    def report_report_all_list_empty(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//div[@class='next-transfer-panel'][1]//div[text()='Empty' and contains(@class, 'not-found')]", 10)

    def report_report_selected_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[@class='next-transfer-panel'][2]//ul//div[contains(@class,'label-wrapper')]")

    def report_report_move_all(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@class='next-transfer-panel'][1]//child::a[text()='Move All']",
                                                 30)

    # def report_report_move_single(self, i):
    #     return self.driver.wait_and_find_element(By.XPATH,
    #                                              "//div[text()='"+str(i)+"']//ancestor::div[@class='next-box'][1]",
    #                                              30)

    def report_report_move_single(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@class='next-transfer-panel'][1]//ul//li[1]//div[@class='next-box']",
                                                 30)

    def report_report_save_button(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='"+str(option)+"']//parent::button",
                                                 30)

    def report_report_close_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Close']//parent::button",
                                                 30)

    def create_report_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//div[@role='dialog']",
                                                 10)

    def search_result_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                        "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//td[@data-next-table-col='1']//div[contains(@class,'project-title')]",
                                                        30)

    def search_result_summary(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                        "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//td[@data-next-table-col='1']//div[contains(@class,'title-desc')]",
                                                        30)

    def search_result_type(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                        "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//td[@data-next-table-col='2']//span",
                                                        30)

    def search_result_account(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                        "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//td[@data-next-table-col='4']//div",
                                                        30)

    def search_result_status(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                        "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//td[@data-next-table-col='0']//span",
                                                        30)

    def action_button_edit(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                        "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//td[@data-next-table-col='5']//button[1]",
                                                        30)

    def action_button_run(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                        "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//td[@data-next-table-col='5']//button[2]",
                                                        30)

    def action_button_delete(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                        "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//td[@data-next-table-col='5']//button[3]",
                                                        30)

    def report_delete_yes_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@role='dialog']//child::button[contains(@class,'primary')]",
                                                 30)

    def delete_report_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//div[@role='dialog']",
                                                10)

    def report_names_list(self):
        return self.driver.find_elements(By.XPATH,
                                         "//tbody//child::tr//td[@data-next-table-col='1']//div[contains(@class,'project-title')]")

    def report_view_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'content-header')]//h3",
                                                 30)

    def report_view_summary(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//pre",
                                                 30)

    def rtm_report_view_case_info_activate(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//canvas",
                                                 30)

    def rtm_report_view_case_info_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[contains(@class,'group-wrapper')][1]//div[@class='next-box']",
                                                 30)

    def rtm_report_view_case_info_name(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[contains(@class,'group-wrapper')][1]//div[@class='g2-tooltip-title']")

    def rtm_report_view_trace_info_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[contains(@class,'group-wrapper')][2]//div[@class='next-box' and contains(@style,'center')]",
                                                 30)

    def rtm_report_view_trace_info_all_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[contains(@class,'group-wrapper')][2]//tbody//tr//td[1]//span")

    def rtm_report_view_issue_info_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[contains(@class,'group-wrapper')][3]//div[@class='next-box' and contains(@style,'center')]",
                                                 30)

    def rtm_report_view_issue_info_all_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[contains(@class,'group-wrapper')][3]//tbody//tr//td[1]//span")

    def exec_report_view_test_runs_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][1]//h5",
                                                 30)

    def exec_report_view_test_runs_name_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][1]//tbody//tr//td[2]//span")

    def exec_report_view_test_runs_total_list(self, i):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][1]//tbody//tr//td[4]//div")[i-1]

    def exec_report_view_test_runs_passed_list(self, i):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][1]//tbody//tr//td[5]//div")[i-1]

    def exec_report_view_test_runs_failed_list(self, i):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][1]//tbody//tr//td[6]//div")[i-1]

    def exec_report_view_test_runs_blocked_list(self, i):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][1]//tbody//tr//td[7]//div")[i-1]

    def exec_report_view_test_runs_retested_list(self, i):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][1]//tbody//tr//td[8]//div")[i-1]

    def exec_report_view_test_runs_issues_list(self, i):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][1]//tbody//tr//td[10]//div")[i-1]

    def exec_report_view_pass_ratio_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][2]//h5",
                                                 30)

    def exec_report_pass_ratio_pass_ratio(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][2]//div[contains(@class,'MlGy6hSx')]//div[contains(@style,'items')][1]//div[2]//strong",
                                                 30)

    def exec_report_pass_ratio_test_ratio(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][2]//div[contains(@class,'MlGy6hSx')]//div[contains(@style,'items')][2]//div[2]//strong",
                                                 30)

    def exec_report_pass_ratio_total_2(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][2]//div[@role='separator']//preceding-sibling::div//canvas//following-sibling::div[2]",
                                                 30)

    def exec_report_pass_ratio_pie_chart(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][2]//div[@role='separator']//preceding-sibling::div//canvas//following-sibling::div[2]//div")

    def exec_report_view_cases_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][3]//h5",
                                                 30)

    def exec_report_view_cases_tot(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][3]//div[contains(@style, 'space-between')]//div[contains(@style, 'flex-start')][1]//div[contains(@style, 'column')][2]//strong",
                                                 30)

    def exec_report_view_cases_est(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][3]//div[contains(@style, 'space-between')]//div[contains(@style, 'flex-start')][2]//div[contains(@style, 'column')][2]//strong",
                                                 30)

    def exec_report_view_cases_eff(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][3]//div[contains(@style, 'space-between')]//div[contains(@style, 'flex-start')][3]//div[contains(@style, 'column')][2]//strong",
                                                 30)

    def exec_report_view_cases_per(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][3]//div[contains(@style, 'space-between')]//div[contains(@style, 'flex-start')][3]//div[contains(@style, 'column')][2]//following-sibling::span",
                                                 30)

    def exec_report_view_prod_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][4]//h5",
                                                 30)

    def exec_report_view_bug_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][5]//h5",
                                                 30)

    def exec_report_view_bug_rate(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][5]//div[contains(@style, 'space-between')]//div[contains(@style, 'flex-start')][2]//div[contains(@style, 'baseline')]//span[1]//strong",
                                                 30)

    def exec_report_view_bug_rate_sum_list_len(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][5]//div[contains(@class, 'mGw5QODg')]//div[contains(@style, 'center')][2]//div[3]//tbody//tr")

    def exec_report_view_bug_rate_sum_total_list(self, i):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][5]//div[contains(@class, 'mGw5QODg')]//div[contains(@style, 'center')][2]//div[3]//tbody//td[2]//div")[i-1]

    def exec_report_view_bug_rate_sum_open_list(self, i):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][5]//div[contains(@class, 'mGw5QODg')]//div[contains(@style, 'center')][2]//div[3]//tbody//td[3]//div")[i-1]

    def exec_report_view_bug_rate_info_list_len(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(@class,'report-container')]//div[@class='next-box' and contains(@style, '12px')]//div[contains(@class,'group-wrapper--KagCwEjv')][5]//div[contains(@class, 'mGw5QODg')]//div[contains(@style, 'center')][2]//div[9]//tbody//tr")

    def no_data(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                         "//div[text()='No Data']", 10)



