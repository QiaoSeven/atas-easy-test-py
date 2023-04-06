import time

from selenium.webdriver.common.by import By


class ProjectObject:
    def __init__(self, driver):
        self.driver = driver

    def members_tab(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='tablist']//li[1]//div",
                                                 30)

    def roles_tab(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='tablist']//li[2]//div",
                                                 30)

    def members_name_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr//div[@title]")

    def members_name_new(self, i):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr["+str(i)+"]//div[@title]",
                                                 30)

    def members_email_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr//div[contains(@class, 'title-desc')]")

    def members_email_new(self, i):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[last()]//td[4]//div[contains(@class, 'Action')]//button[2]",30)

    def members_tab(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='tablist']//li[1]//div",
                                                 30)

    def roles_tab(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='tablist']//li[2]//div",
                                                 30)

    def members_name_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr//div[@title]")

    def members_name_new(self, i):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr["+str(i)+"]//div[@title]",
                                                 30)

    def members_email_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr//div[contains(@class, 'title-desc')]")

    def members_email_new(self, i):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr["+str(i)+"]//div[contains(@class, 'title-desc')]",
                                                 30)

    def members_list_role_target(self, email):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[contains(text(),'"+str(email)+"')]//ancestor::tr[1]//td[3]//span")

    def members_role_news(self, i):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr["+str(i)+"]//td[3]//span")

    def members_assign_target(self, email):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(text(),'"+str(email)+"')]//ancestor::tr[1]//td[4]//div[contains(@class, 'Action')]//button[1]",
                                                 30)

    def members_assign_new(self, i):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr["+str(i)+"]//td[4]//div[contains(@class, 'Action')]//button[1]",
                                                 30)

    def members_delete_new(self, i):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr["+str(i)+"]//td[4]//div[contains(@class, 'Action')]//button[2]",
                                                 30)

    def members_assign_btn_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//tbody//tr[1]//td[4]//div[contains(@class, 'Action')]//button[1]",
                                                 5)

    def members_delete_btn_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//tbody//tr[1]//td[4]//div[contains(@class, 'Action')]//button[2]",
                                                 5)

    def delete_modal_window(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                "//div[@role='dialog']",
                                                10)

    def delete_ok_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@role,'dialog')]//child::button[contains(@class,'primary')]",
                                                 30)

    def members_invite_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Invite']//parent::button",
                                                 30)

    def members_invite_btn_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//span[text()='Invite']//parent::button",
                                                 10)

    def members_invite_modal(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//div[@role='dialog']",
                                                 10)

    def members_invite_email(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Email']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input",
                                                 30)

    def members_invite_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Display Name']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input",
                                                 30)

    def members_invite_role_arrow(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@role='dialog']//i[contains(@class,'arrow')]",
                                                 30)

    def members_invite_role_dropdown(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox' and contains(@class, 'multiple')]//span[text()='"+str(option)+"']",
                                                 30)

    def members_invite_submit_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Submit']//parent::button",
                                                 30)

    def members_assign_modal(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//div[@role='dialog']",
                                                 10)

    def members_assign_checkbox(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@role='dialog']//thead//span[@class='next-checkbox']",
                                                 30)

    def members_role_admin(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@class='next-box' and contains(text(),'Organization Admin')]//ancestor::td[1]//preceding-sibling::td//span[@class='next-checkbox']",
                                                 30)

    def members_role_target(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[text()='"+str(option)+"']//parent::td//preceding-sibling::td//span[@class='next-checkbox']",
                                                 30)

    def members_assign_list_1(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[@role='dialog']//tbody//tr//td[2]//div[@class='next-box']")

    def members_assign_list_2(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[@role='dialog']//tbody//tr//td[2]//div[@class='next-table-cell-wrapper' and text()]")

    def members_assign_ok_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='OK']//parent::button",
                                                 30)

    def custom_role_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//li[@title='Custom Roles']//following-sibling::li//div[contains(@class,'role-item') and not(contains(@class,'actions'))]")

    def custom_role_name(self, name):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//li[@title='Custom Roles']//following-sibling::li//div[contains(text(), '"+str(name)+"')]", 30)

    def add_role_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h2[text()='Roles']//following-sibling::button",
                                                 30)

    def add_role_btn_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//h2[text()='Roles']//following-sibling::button",
                                                 10)

    def add_role_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h2[text()='Roles']//parent::div//following-sibling::ul//li[last()]//input",
                                                 30)

    def add_role_v(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h2[text()='Roles']//parent::div//following-sibling::ul//li[last()]//button[1]",
                                                 30)

    def roles_name_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//div[text()='Custom Roles']//parent::li//following-sibling::li//div[contains(@style, 'relative')]")

    def role_custom_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//li[@title='Custom Roles']//following-sibling::li[1]//div[contains(@style, 'relative')]",
                                                 30)

    def role_rename_btn_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//li[@title='Custom Roles']//following-sibling::li[1]//button[1]",
                                                 5)

    def custom_role_delete_btn(self, name):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(text(), '"+str(name)+"')]//ancestor::li[1]//button[2]", 30)

    def role_delete_btn_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//li[@title='Custom Roles']//following-sibling::li[1]//button[2]",
                                                 5)

    def role_ops_invite_click(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[2]//td[2]//label[2]//span[@class='next-checkbox']",
                                                 30)

    def role_ops_assign_click(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[2]//td[2]//label[3]//span[@class='next-checkbox']",
                                                 30)

    def role_ops_delete_click(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[2]//td[2]//label[4]//span[@class='next-checkbox']",
                                                 30)

    def role_ops_create_click(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[3]//td[2]//label[2]//span[@class='next-checkbox']",
                                                 30)

    def role_ops_edit_click(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[3]//td[2]//label[3]//span[@class='next-checkbox']",
                                                 30)

    def role_ops_checkall_click(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[3]//td[3]//label//span[@class='next-checkbox']",
                                                 30)

    def role_ops_view_click(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[6]//td[2]//label[1]//span[@class='next-checkbox']",
                                                 30)

    def role_ops_member_check(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[2]//td[3]//label",
                                                 30)

    def role_ops_role_check(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[3]//td[3]//label",
                                                 30)

    def role_ops_project_check(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[6]//td[2]//label[1]",
                                                 30)

    def role_ops_save(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Save']//parent::button",
                                                 30)

    def field_search_bar(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@placeholder]", 30)

    def field_list_name(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr//td[2]//span")

    def field_list_name_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//td[2]//span", 30)

    def field_list_type_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//td[5]//div", 30)

    def new_field_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='New Field']//parent::button",
                                                 30)

    def field_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Field Name']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input",
                                                 30)

    def field_type_arrow_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Field Type']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//span[contains(@class,'arrow')]",
                                                 30)

    def field_type_dropdown(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox']//span[text()='"+str(option)+"']//parent::div",
                                                 30)

    def field_help_text(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Help Text']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input",
                                                 30)

    def field_require_switch(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Is Required']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//div[@role='switch']",
                                                 30)

    def field_message_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Message']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input",
                                                 30)

    def field_number_default(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Default Value']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input",
                                                 30)

    def field_radio_btn(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='"+str(option)+"']//preceding-sibling::span",
                                                 30)

    def field_add_option(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Add Option']//parent::button",
                                                 30)

    def field_option_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[last()]//td[3]//input",
                                                 30)

    def field_option_default_radio(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[last()]//td[2]//span[@class='next-radio ']",
                                                 30)

    def field_option_default_checkbox(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[last()]//td[2]//span[@class='next-checkbox']",
                                                 30)

    def field_save_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Save']//parent::button",
                                                 30)

    def field_preview_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//div[contains(@class,'label-content')]//label",
                                                 30)

    def field_preview_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//span[contains(@class,'next-input')]//*",
                                                 30)

    def field_preview_textbox(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[@role='textbox']",
                                                 30)

    def field_preview_number(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//span[contains(@class,'next-input')]//input",
                                                 30)

    def field_preview_number_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//span[@class='next-number-picker-handler']//button[1]",
                                                 30)

    def field_preview_dropdown_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//em",
                                                 30)

    def field_preview_dropdown_tag(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//div[contains(@class,'tag')]//span[contains(@class,'body')]",
                                                 30)

    def field_preview_dropdown_arrow(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//span[@class='next-input-control']",
                                                 30)

    def field_preview_dropdown_option(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'opened')]//ul[@role='listbox']//li[1]//div[@class='next-menu-item-inner']",
                                                 30)

    def field_preview_radio_option(self, i):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//*[contains(@class,'group')]//label["+str(i)+"]",
                                                 30)

    def field_preview_checkbox_option(self, i):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//*[contains(@class,'group')]//label["+str(i)+"]",
                                                 30)

    def field_preview_helptext(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//div[contains(@class,'extra')]",
                                                 30)

    def field_preview_required_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//div[contains(@class,'label-content')]//span",
                                                 30)

    def field_preview_switch(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Preview: ']//following-sibling::div[@role='switch']",
                                                 30)

    def field_preview_message(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//div[contains(@class,'error-help')]",
                                                 30)

    def field_pre_msg_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//div[contains(@class,'error-help')]",
                                                 5)

    def field_reset_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Reset']//parent::button",
                                                 30)

    def field_validate_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Validate']//parent::button",
                                                 30)

    def field_validate_message(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'preview-wireframe')]//div[contains(@class,'src-components')]//div[contains(@class,'pass')]//div",
                                                 30)

    def template_list_name(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr//td[2]//div[@title]")

    def template_list_name_first(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//td[2]//div[@title]",
                                                 30)

    def new_template_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='New Organization Template']//parent::button",
                                                 30)

    def template_base_dropdown_arrow(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[@class='next-input-control']",
                                                 30)

    def template_base_dropdown_option(self, option):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class,'opened')]//ul[@role='listbox']//span[text()='"+str(option)+"']//parent::div",
                                                 30)

    def template_name_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='Name']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input",
                                                 30)

    def template_first_field(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//h4[text()='Custom Fields']//following-sibling::div//div[contains(@style,'row wrap')]//div[contains(@class, 'next-box')][1]//div[contains(@class,'next-tag')]",
                                                 30)

    def template_last_row(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class, 'grid-wrapper')][last()]//div[contains(@class, 'DropArea-__hoz')]",
                                                 30)

    def template_save_btn(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Save']//parent::button",
                                                 30)

    def new_project_bt_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//span[text()='New Project']//parent::button",
                                                 5)

    def new_project_bt(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div[3]/div[1]/div[2]/button",
                                                 30)

    def project_title(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/div/form/div/div[1]/div[2]/div/div/span/input",
                                                 30)

    def project_desc(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/span/textarea[1]",
                                                 30)

    def pro_url_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='JIRA URL']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input",
                                                 30)

    def pro_key_input(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//label[text()='JIRA Project Key']//ancestor::div[@class='next-formily-item-label']//following-sibling::div//input",
                                                 30)

    def project_save(self):
        return self.driver.wait_and_find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/button[1]",
                                                 30)

    def project_name_in_list(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//div[contains(@class, 'project-title')]",
                                                 30)

    def switch_pro_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class, 'project-selector')]//em",
                                                 30)

    def switch_pro_arrow(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class, 'project-selector')]//span[@class='next-input-control']",
                                                 30)

    def switch_pro_dropdown(self, i):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@class='next-menu-content']//li["+str(i)+"]//span",
                                                 30)

    def switch_pro_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//ul[@class='next-menu-content']//li")

    def get_setting_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class, 'config-tab') and text()='Settings']",
                                                 30)

    def get_members_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='menu']//div[text()='Members']",
                                                 30)

    def get_roles_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='menu']//div[text()='Roles']",
                                                 30)

    def get_fields_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='menu']//div[text()='Fields']",
                                                 30)

    def get_templates_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='menu']//div[text()='Templates']",
                                                 30)

    def members_option_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//ul[@role='menu']//div[text()='Members']",
                                                 10)

    def roles_option_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//ul[@role='menu']//div[text()='Roles']",
                                                 10)

    def fields_option_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//ul[@role='menu']//div[text()='Fields']",
                                                 5)

    def templates_option_exist(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                                 "//ul[@role='menu']//div[text()='Templates']",
                                                 5)

    def get_members_link(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/button",
                                                 30)

    def get_add_members_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/button",
                                                 30)

    def get_search_members(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//input[@role='combobox' and @placeholder]",
                                                 30)

    def get_members_items(self):
        return self.driver.wait_and_find_element(By.XPATH, "//li[@role='option']//div[contains(@class, 'project-title')]", 30)

    def get_ok_button(self):
        return self.driver.wait_and_find_element(By.XPATH, "//span[text()='OK']//parent::button", 30)

    def get_members_list(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[last()]//td[2]//div[contains(@class, project-title) and @title]",
                                                 30)

    def get_search_project(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div[3]/div[1]/div[2]/span/input",
                                                 30)

    def get_search_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div[3]/div[1]/div[2]/span/span/div/button[2]",
                                                 30)

    def search_result_list(self):
        return self.driver.find_elements(By.XPATH,
                                                 "//tbody//tr//div[contains(@class, 'project-title')]")

    def get_search_result(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "/html/body/div/section/section/section/div/div/div/div[3]/div[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[1]/div/div/div",
                                                 30)

    def get_delete_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[text()='Delete Project']//preceding-sibling::button",
                                                 30)

    def get_delete_ok_button(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='OK']//parent::button",
                                                 30)

    def get_list_page_no(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div[3]/div[2]/div/div[2]/div/div[2]/span[1]",
                                                 30)

    def get_list_one_page(self):
        return self.driver.find_elements(By.CLASS_NAME,
                                         "next-table-row")

    def get_pagination_button(self):
        return self.driver.find_elements(By.XPATH,
                                         "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div[3]/div[2]/div/div[2]/div/div[2]/div/button")

    def get_one_page_number(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//*[@id=\"ice-container\"]/section/section/section/div/div/div/div[3]/div[2]/div/div[2]/div/div[1]/span[2]/span[1]/span[1]/em",
                                                 30)

    def get_first_project(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                    "//tr[contains(@class,'next-table-row') and contains(@class,'first')]//child::div[contains(@class,'project-title')]",
                                                    30)

    def project_to_rqm_btn(self):
        time.sleep(1)
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'first')]//td[@data-next-table-col='1']//button[2]",
                                                 30)

    def project_to_case_btn(self):
        time.sleep(1)
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'first')]//td[@data-next-table-col='1']//button[3]",
                                                 30)

    def project_to_run_btn(self):
        time.sleep(1)
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'first')]//td[@data-next-table-col='1']//button[4]",
                                                 30)

    def project_to_report_btn(self):
        time.sleep(1)
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'first')]//td[@data-next-table-col='1']//button[5]",
                                                 30)

    def project_to_issue_btn(self):
        time.sleep(1)
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'first')]//td[@data-next-table-col='1']//button[6]",
                                                 30)

    def project_to_job_btn(self):
        time.sleep(1)
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'first')]//td[@data-next-table-col='1']//button[7]",
                                                 30)

    def project_to_module_btn(self, i):
        time.sleep(1)
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tr[contains(@class,'first')]//td[@data-next-table-col='1']//button["+str(i)+"]",
                                                 30)

    def module_menu(self, i):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//ul[@role='listbox'][1]//li["+str(i+2)+"]//span[contains(@class,'label')]",
                                                 20)

    def project_menu(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//span[text()='Projects']//ancestor::div[contains(@class,'inner')]",
                                                 20)

    def star_icon(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//tbody//tr[1]//td[3]//button",
                                                 30)

    def starred_project_name(self):
        return self.driver.wait_and_find_element(By.XPATH,
                                                 "//div[contains(@class, 'container--REgHHs3K')]//div[contains(@class, 'header--TOSKNwzR')]//following-sibling::div[@class='next-box']//div[not(@class) and not(@style)][last()]//div[contains(@class,'project-card')]//span[contains(@class,'helper')]",
                                                 30)

    def no_data(self):
        return self.driver.ensure_element_exist(By.XPATH,
                                         "//div[text()='No Data']", 10)

