import datetime
import re
import time
import platform

from selenium.webdriver import Keys

from object.ProjectObject import ProjectObject
from task.BaseTask import BaseTask
from util.TimeUtil import TimeUtil


class ProjectTask(BaseTask):

    def __init__(self, driver, data, capture, logger, atas_api):
        BaseTask.__init__(self, driver, data, capture, logger, atas_api)
        self.project = ProjectObject(self.driver)

    def invite_member(self, if_verify, not_delete):
        # 一、准备数据
        case_desc = self.data['case_desc']
        email = self.data['email']
        name = self.data['name']
        role = self.data['role']
        # 二、开始操作。创建新的project
        time.sleep(1)
        self.project.get_setting_button().click()
        time.sleep(0.5)
        self.project.get_members_button().click()
        time.sleep(3)
        email_list = []
        emails = self.project.members_email_list()
        for emall in emails:
            email_list.append(emall.text.split("\n")[1])
        new_member = self.verify.check_member_email(email_list, email)

        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if not new_member:
            self.project.members_invite_btn().click()
            time.sleep(0.5)
            self.project.members_invite_email().send_keys(email)
            self.project.members_invite_name().send_keys(name)
            self.project.members_invite_role_arrow().click()
            time.sleep(0.5)
            self.project.members_invite_role_dropdown(role).click()
            self.project.members_invite_role_arrow().click()

            self.capture.capture_all(case_desc + "-1.png")
            if self.if_upload_rp:
                self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Invite new member")

            if self.if_upload_atas:
                self.atas_api.upload_result(self.result.get_upload_result('Invite new member',
                                                                          self.capture.get_full_path(
                                                                              case_desc + "-1.png"),
                                                                          None, start_time,
                                                                          end_time))

            self.project.members_invite_submit_btn().click()
            # time.sleep(1)
            # self.driver.page_refresh()
            time.sleep(5)
            # self.verify.verify_member_email(self.project.members_email_last().text, email)
        # 三、校验结果
        if if_verify:
            # 校验点1：modal window关闭
            invite_modal_window = self.project.members_invite_modal()
            self.verify.verify_modal_window(invite_modal_window)
            # 校验点2：member列表的email成功更新
            e_num = len(self.project.members_email_list())
            global i
            i = 1
            actual_email = self.project.members_email_new(i).text.split("\n")[1]
            expect_email = email
            while expect_email != actual_email:
                i += 1
                actual_email = self.project.members_email_new(i).text.split("\n")[1]
                if i > e_num:
                    self.logger.error('New member is not added')
                    assert False
            # 校验点3：member列表的name成功更新
            actual_name = self.project.members_name_new(i).text
            expect_name = name
            self.verify.verify_member_name(actual_name, expect_name)
            if not_delete:
                # 校验点4：member列表的role成功更新
                actual_role = []
                role_list = self.project.members_role_news(i)
                for a_role in role_list:
                    actual_role.append(a_role.text)
                expect_role = role
                self.verify.verify_member_role(actual_role, expect_role)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "New member is invited")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('New member is invited',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def assign_role(self, if_project, if_verify):
        # 一、准备数据
        global i
        case_desc = self.data['case_desc']
        # 二、开始操作。创建新的project
        if if_project:
            time.sleep(1)
            self.project.get_setting_button().click()
            time.sleep(0.5)
            self.project.get_members_button().click()
        self.driver.scroll_to_element(self.project.members_assign_new(i))
        self.project.members_assign_new(i).click()
        expect_roles = []
        list_1 = self.project.members_assign_list_1()
        list_2 = self.project.members_assign_list_2()
        for l1 in list_1:
            # expect_roles.append(l1.text)
            l1_real = re.sub('\nDEFAULT', "", l1.text)
            expect_roles.append(l1_real)
        for l2 in list_2:
            expect_roles.append(l2.text)
        self.project.members_assign_checkbox().click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Assign roles to new member")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Assign roles to new member',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.project.members_assign_ok_btn().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：modal window关闭
            assign_modal_window = self.project.members_assign_modal()
            self.verify.verify_modal_window(assign_modal_window)
            # 校验点2：roles成功更新
            actual_roles = []
            m_list = self.project.members_role_news(i)
            for m_l in m_list:
                actual_roles.append(m_l.text)
            self.verify.verify_member_assign(actual_roles, expect_roles)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Roles are assigned to new member")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Roles are assigned to new member',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def delete_member(self, if_project, if_verify):
        # 一、准备数据
        global i
        case_desc = self.data['case_desc']
        name = self.data['name']
        # 二、开始操作。删除新添加的member
        if if_project:
            time.sleep(1)
            self.project.get_setting_button().click()
            time.sleep(0.5)
            self.project.get_members_button().click()
        self.driver.scroll_to_element(self.project.members_delete_new(i))
        self.project.members_delete_new(i).click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Delete invited member")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Delete invited member',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.project.delete_ok_button().click()
        time.sleep(1)
        self.driver.page_refresh()
        time.sleep(5)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            delete_modal_window = self.project.delete_modal_window()
            self.verify.verify_modal_window(delete_modal_window)
            # 校验点2：确认member被删除
            names = []
            members = self.project.members_name_list()
            for member_list in members:
                member = member_list.text
                names.append(member)
            self.verify.verify_delete(names, name)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Invited member is deleted")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Invited member is deleted',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def add_role(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        role_name = self.data['role_name']
        # 二、开始操作。创建新的project
        if if_project:
            time.sleep(1)
            self.project.get_setting_button().click()
            time.sleep(0.5)
            self.project.get_roles_button().click()
            time.sleep(3)
        p_names = []
        p_roles = self.project.custom_role_list()
        for p_role in p_roles:
            p_names.append(p_role.text)
        new_role = self.verify.check_add_role(p_names, role_name)
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if not new_role:
            self.project.add_role_btn().click()
            time.sleep(0.5)
            self.project.add_role_input().send_keys(role_name)

            self.capture.capture_all(case_desc + "-1.png")
            if self.if_upload_rp:
                self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Add new role")
            if self.if_upload_atas:
                self.atas_api.upload_result(self.result.get_upload_result('Add new role',
                                                                          self.capture.get_full_path(
                                                                              case_desc + "-1.png"),
                                                                          None, start_time,
                                                                          end_time))

            self.project.add_role_v().click()
            time.sleep(3)
            # 三、校验结果
            if if_verify:
                # 校验点1：列表生成新的role
                names = []
                roles = self.project.custom_role_list()
                for role in roles:
                    names.append(role.text)
                self.verify.verify_add_role(names, role_name)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "New role is added")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('New role is added',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def set_permission(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        user_name = self.data['user_name']
        role_name = self.data['role_name']
        # 二、开始操作。创建新的project
        if if_project:
            time.sleep(1)
            self.project.get_setting_button().click()
            time.sleep(0.5)
            self.project.get_roles_button().click()
        time.sleep(1)
        self.project.custom_role_name(role_name).click()
        self.project.role_ops_invite_click().click()
        self.project.role_ops_assign_click().click()
        self.project.role_ops_delete_click().click()
        self.project.role_ops_create_click().click()
        self.project.role_ops_edit_click().click()
        self.project.role_ops_checkall_click().click()
        self.project.role_ops_view_click().click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Set permission for new role")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Set permission for new role',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.project.role_ops_save().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：确认被选中
            member_checkbox = self.project.role_ops_member_check().get_attribute("class")
            role_checkbox = self.project.role_ops_role_check().get_attribute("class")
            project_checkbox = self.project.role_ops_project_check().get_attribute("class")
            self.verify.verify_set_permission('checked', member_checkbox)
            self.verify.verify_set_permission('checked', role_checkbox)
            self.verify.verify_set_permission('checked', project_checkbox)
            # 校验点2：有/没有对应的权限
            self.project.members_tab().click()
            self.driver.scroll_to_element(self.project.members_assign_target(user_name))
            self.project.members_assign_target(user_name).click()
            self.project.members_assign_checkbox().click()
            time.sleep(0.5)
            self.project.members_assign_checkbox().click()
            self.project.members_role_target(role_name).click()
            self.project.members_assign_ok_btn().click()
            time.sleep(3)
            actual_roles = []
            m_list = self.project.members_list_role_target(user_name)
            for m_l in m_list:
                actual_roles.append(m_l.text)
            self.verify.verify_member_role(actual_roles, role_name)
            self.project.project_menu().click()
            time.sleep(1)
            self.driver.page_refresh()
            time.sleep(5)
            self.verify.verify_permission_disabled(self.project.new_project_bt_exist())
            self.project.get_setting_button().click()
            time.sleep(2)
            self.verify.verify_permission_enabled(self.project.members_option_exist())
            self.verify.verify_permission_enabled(self.project.roles_option_exist())
            self.verify.verify_permission_disabled(self.project.fields_option_exist())
            self.verify.verify_permission_disabled(self.project.templates_option_exist())
            self.project.get_members_button().click()
            time.sleep(3)
            self.verify.verify_permission_enabled(self.project.members_invite_btn_exist())
            self.verify.verify_permission_enabled(self.project.members_assign_btn_exist())
            self.verify.verify_permission_enabled(self.project.members_delete_btn_exist())
            self.project.roles_tab().click()
            time.sleep(3)
            self.verify.verify_permission_enabled(self.project.add_role_btn_exist())
            self.driver.action_hover(self.project.role_custom_first())
            self.verify.verify_permission_enabled(self.project.role_rename_btn_exist())
            self.verify.verify_permission_enabled(self.project.role_delete_btn_exist())
            # 校验通过，将member的role改回admin，否则下一条case删除role会出问题
            self.project.members_tab().click()
            self.driver.scroll_to_element(self.project.members_assign_target(user_name))
            self.project.members_assign_target(user_name).click()
            self.project.members_assign_checkbox().click()
            time.sleep(0.5)
            self.project.members_assign_checkbox().click()
            self.project.members_role_admin().click()
            self.project.members_assign_ok_btn().click()
            time.sleep(3)
            actual_role = []
            a_list = self.project.members_list_role_target(user_name)
            for a_l in a_list:
                actual_role.append(a_l.text)
            self.verify.verify_member_role(actual_role, 'Organization Admin')

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Permission is set")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Permission is set',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def delete_role(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        role_name = self.data['role_name']
        # 二、开始操作。删除新添加的role
        if if_project:
            time.sleep(1)
            self.project.get_setting_button().click()
            time.sleep(0.5)
            self.project.get_roles_button().click()
        time.sleep(1)
        self.driver.action_hover(self.project.custom_role_name(role_name))
        self.project.custom_role_delete_btn(role_name).click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Delete created role")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Delete created role',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.project.delete_ok_button().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：Modal window关闭
            delete_modal_window = self.project.delete_modal_window()
            self.verify.verify_modal_window(delete_modal_window)
            # 校验点2：确认role被删除
            names = []
            roles = self.project.roles_name_list()
            for role_list in roles:
                role = role_list.text
                names.append(role)
            self.verify.verify_delete(names, role_name)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Role is deleted")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Role is deleted',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def add_field(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        field_name = self.data['field_name']
        field_type = self.data['field_type']
        help_text = self.data['help_text']
        component_type = self.data['component_type']
        select_mode = self.data['select_mode']
        direction = self.data['direction']
        option_name = self.data['option_name']
        data_resource_type = self.data['data_resource_type']
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        # 二、开始操作。创建新的field
        if if_project:
            time.sleep(1)
            self.project.get_setting_button().click()
            time.sleep(0.5)
            self.project.get_fields_button().click()
        time.sleep(1)
        self.project.new_field_btn().click()
        self.project.field_name().send_keys(field_name + suffix_time)
        self.project.field_type_arrow_icon().click()
        time.sleep(0.5)
        self.project.field_type_dropdown(field_type).click()
        self.project.field_help_text().send_keys(help_text)
        self.project.field_require_switch().click()
        if field_type == 'Text':
            self.project.field_radio_btn(component_type).click()
        elif field_type == 'Select':
            self.project.field_radio_btn(component_type).click()
            if component_type == 'Dropdown':
                self.project.field_radio_btn(select_mode).click()
            else:
                # component_type == 'Radio/Checkbox'
                self.project.field_radio_btn(direction).click()
            i = 1
            while i <= 3:
                self.project.field_add_option().click()
                self.project.field_option_name().send_keys(option_name + '-' + str(i))
                time.sleep(0.5)
                i += 1
            if component_type == 'Checkbox':
                self.project.field_option_default_checkbox().click()
            else:
                self.project.field_option_default_radio().click()
        elif field_type == 'User Picker':
            self.project.field_radio_btn(data_resource_type).click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Add new field")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Add new field',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        if if_verify:
            # 校验点1：preview的名称正确
            actual_pre_name = self.project.field_preview_name().text
            expect_pre_name = field_name + suffix_time
            self.verify.verify_field_preview_same(actual_pre_name, expect_pre_name)
            # 校验点2：preview的helptext正确
            actual_pre_help = self.project.field_preview_helptext().text
            expect_pre_help = help_text
            self.verify.verify_field_preview_same(actual_pre_help, expect_pre_help)
            # 校验点3：preview有必填符号*
            actual_pre_required = self.project.field_preview_required_icon().text
            expect_pre_required = '*'
            self.verify.verify_field_preview_same(actual_pre_required, expect_pre_required)
            # 校验点4：preview的field显示正确
            if field_type == 'Select':
                if component_type == 'Dropdown':
                    if select_mode == 'Single':
                        actual_option = self.project.field_preview_dropdown_name().text
                    else:
                        # select_mode == 'Multiple'
                        actual_option = self.project.field_preview_dropdown_tag().text
                    expect_option = option_name + '-3'
                    self.verify.verify_field_preview_same(actual_option, expect_option)
                elif component_type == 'Radio':
                    actual_option = self.project.field_preview_radio_option('3').get_attribute('aria-checked')
                    expect_option = 'true'
                    self.verify.verify_field_preview_same(actual_option, expect_option)
                else:
                    # component_type == 'Checkbox'
                    actual_option = self.project.field_preview_checkbox_option('3').get_attribute('class')
                    expect_option = 'checked'
                    self.verify.verify_field_preview_contain(actual_option, expect_option)
            elif field_type == 'Number Picker':
                actual_num = self.project.field_preview_number().get_attribute('value')
                expect_num = self.project.field_number_default().get_attribute('value')
                self.verify.verify_field_preview_same(actual_num, expect_num)
            # 校验点4：preview的preview可正常使用
            if field_type == 'Text' or field_type == 'Rich Text' or field_type == 'User Picker':
                self.project.field_preview_switch().click()
                time.sleep(1)
                actual_pre_msg = self.project.field_preview_message().text
                expect_pre_msg = self.project.field_message_input().get_attribute('value')
                self.verify.verify_field_preview_same(actual_pre_msg, expect_pre_msg)
            # 校验点5：preview的reset可正常使用
            if field_type == 'Text' or field_type == 'Rich Text' or field_type == 'User Picker':
                self.project.field_reset_btn().click()
                pre_msg = self.project.field_pre_msg_exist()
                self.verify.verify_field_preview_disappear(pre_msg)
            elif field_type == 'Select':
                if component_type == 'Dropdown':
                    self.project.field_preview_dropdown_arrow().click()
                    self.project.field_preview_dropdown_option().click()
                    if select_mode == 'Multiple':
                        self.project.field_preview_dropdown_arrow().click()
                    self.project.field_reset_btn().click()
                    if select_mode == 'Single':
                        actual_option = self.project.field_preview_dropdown_name().text
                    else:
                        # select_mode == 'Multiple'
                        actual_option = self.project.field_preview_dropdown_tag().text
                    expect_option = option_name + '-3'
                    self.verify.verify_field_preview_same(actual_option, expect_option)
                elif component_type == 'Radio':
                    self.project.field_preview_radio_option('1').click()
                    self.project.field_reset_btn().click()
                    time.sleep(1)
                    actual_option = self.project.field_preview_radio_option('3').get_attribute('aria-checked')
                    expect_option = 'true'
                    self.verify.verify_field_preview_same(actual_option, expect_option)
                else:
                    # component_type == 'Checkbox'
                    self.project.field_preview_checkbox_option('1').click()
                    self.project.field_reset_btn().click()
                    time.sleep(1)
                    actual_option = self.project.field_preview_checkbox_option('3').get_attribute('class')
                    expect_option = 'checked'
                    self.verify.verify_field_preview_contain(actual_option, expect_option)
            elif field_type == 'Number Picker':
                self.project.field_preview_number_btn().click()
                self.project.field_reset_btn().click()
                time.sleep(1)
                actual_num = self.project.field_preview_number().get_attribute('value')
                expect_num = self.project.field_number_default().get_attribute('value')
                self.verify.verify_field_preview_same(actual_num, expect_num)
            # 校验点6：preview的validate可正常使用
            if field_type == 'Text':
                self.project.field_preview_input().send_keys('auto-text')
            elif field_type == 'Rich Text':
                self.project.field_preview_textbox().send_keys('auto-text')
            elif field_type == 'User Picker':
                self.project.field_preview_dropdown_arrow().click()
                self.project.field_preview_dropdown_option().click()
            self.project.field_validate_btn().click()
            actual_vld_msg = self.project.field_validate_message().text
            expect_vld_msg = 'The field value is valid.'
            self.verify.verify_field_preview_same(actual_vld_msg, expect_vld_msg)
        self.project.field_save_btn().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点：列表中name正确
            self.project.field_search_bar().send_keys(field_name + suffix_time)
            self.project.field_search_bar().send_keys(Keys.ENTER)
            time.sleep(2)
            actual_name = self.project.field_list_name_first().text
            expect_name = field_name + suffix_time
            self.verify.verify_field_list_same(actual_name, expect_name)
            # 校验点：列表中type正确
            actual_type = self.project.field_list_type_first().text
            if field_type == 'Text' or field_type == 'Select':
                expect_type = component_type
            elif field_type == 'User Picker':
                expect_type = re.sub(re.compile(r'\s+'), '', field_type)
            else:
                expect_type = field_type
            self.verify.verify_field_list_similar(actual_type, expect_type)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "New field is added")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('New field is added',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def search_field(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        search_key = self.data['search_keyword']
        # 二、开始操作。搜索requirement
        if if_project:
            time.sleep(1)
            self.project.get_setting_button().click()
            time.sleep(0.5)
            self.project.get_fields_button().click()
        time.sleep(1)
        self.project.field_search_bar().send_keys(search_key)
        time.sleep(0.5)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png",
                                                         "Search field by " + str(search_key) + "")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Search field by " + str(search_key) + "",
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.project.field_search_bar().send_keys(Keys.ENTER)
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：搜索结果都包含搜索关键字
            result = []
            names = self.project.field_list_name()
            for name in names:
                result.append(name.text)
            self.verify.verify_field_search(result, search_key)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Field is searched")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Field is searched",
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def add_template(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        tpt_name = self.data['tpt_name']
        base_tpt_name = self.data['base_tpt_name']
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        # 二、开始操作。创建新的template
        if if_project:
            time.sleep(1)
            self.project.get_setting_button().click()
            time.sleep(0.5)
            self.project.get_templates_button().click()
        time.sleep(1)
        self.project.new_template_btn().click()
        self.project.template_base_dropdown_arrow().click()
        time.sleep(0.5)
        self.project.template_base_dropdown_option(base_tpt_name).click()
        time.sleep(0.5)
        self.project.template_name_input().send_keys(tpt_name + suffix_time)
        time.sleep(0.5)
        self.project.template_first_field().click()
        self.project.template_last_row().click()

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png", "Add new template")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Add new template",
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.project.template_save_btn().click()
        time.sleep(2)
        # 三、校验结果
        if if_verify:
            # 校验点1：列表中template名称正确
            self.project.field_search_bar().send_keys(tpt_name + suffix_time)
            self.project.field_search_bar().send_keys(Keys.ENTER)
            time.sleep(2)
            actual_name = self.project.template_list_name_first().text
            expect_name = tpt_name + suffix_time
            self.verify.verify_template_add(actual_name, expect_name)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Template is added")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Template is added",
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def search_template(self, if_project, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        search_key = self.data['search_keyword']
        # 二、开始操作。搜索requirement
        if if_project:
            time.sleep(1)
            self.project.get_setting_button().click()
            time.sleep(0.5)
            self.project.get_templates_button().click()
        time.sleep(1)
        self.project.field_search_bar().send_keys(search_key)
        time.sleep(0.5)

        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png",
                                                         "Search template by " + str(search_key) + "")
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Search template by " + str(search_key) + "",
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.project.field_search_bar().send_keys(Keys.ENTER)
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            # 校验点1：搜索结果都包含搜索关键字
            result = []
            names = self.project.template_list_name()
            for name in names:
                result.append(name.text)
            self.verify.verify_field_search(result, search_key)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png", "Template is searched")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result("Template is searched",
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def create_project(self, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        title = self.data['title']
        desc = self.data['description']
        suffix_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        # 二、开始操作。创建新的project
        time.sleep(3)
        self.project.new_project_bt().click()
        time.sleep(1)

        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "create-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "create-1.png", "Click New Project button")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Click New Project button',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "create-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.project.project_title().send_keys(title + suffix_time)
        self.project.project_desc().send_keys(desc)
        self.project.pro_key_input().send_keys('CNTDAP')

        self.capture.capture_all(case_desc + "create-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "create-2.png",
                                                         "Fill title and description, then click save button")
        if self.if_upload_atas:
            self.atas_api.upload_result(
                self.result.get_upload_result('Fill title and description, then click save button',
                                              self.capture.get_full_path(
                                                  case_desc + "create-2.png"),
                                              None, start_time,
                                              end_time))
        self.project.project_save().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            actual_project_name = self.project.project_name_in_list().text
            expect_project_name = title + suffix_time
            self.verify.verify_project_name(actual_project_name, expect_project_name)

        self.capture.capture_all(case_desc + "create-3.png")
        end_time = TimeUtil.get_current_time()
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "create-3.png",
                                                         "Project is created success and navigate to all projects page")
        if self.if_upload_atas:
            self.atas_api.upload_result(
                self.result.get_upload_result('Project is created success and navigate to all projects page',
                                              self.capture.get_full_path(
                                                  case_desc + "create-3.png"),
                                              None, start_time,
                                              end_time))

    def star_project(self, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        # 二、开始操作。收藏project
        time.sleep(2)
        self.project.star_icon().click()

        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png",
                                                         "Star created project")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Star created project',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        time.sleep(3)
        # 三、校验结果
        if if_verify:
            actual_starred_project = self.project.starred_project_name().text
            expect_starred_project = self.project.get_first_project().text
            self.verify.verify_star_project(actual_starred_project, expect_starred_project)

        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png",
                                                         "Created project is starred")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Created project is starred',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def search_project(self, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        project_name = self.data['project_name']
        # 二、开始操作。搜索project
        self.project.get_search_project().send_keys(project_name)

        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "search-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "search-1.png",
                                                         "Input project name and search")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Input project name and search',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "search-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        self.project.get_search_project().send_keys(Keys.ENTER)
        time.sleep(5)
        # 三、校验结果
        if if_verify:
            names = []
            rows = self.project.search_result_list()
            for row in rows:
                name = row.text
                names.append(name)
            self.verify.verify_project_search(names, project_name)

        self.capture.capture_all(case_desc + "search-2.png")
        end_time = TimeUtil.get_current_time()
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "search-2.png",
                                                         "Search project successfully")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Search project successfully',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "search-2.png"),
                                                                      None, start_time,
                                                                      end_time))

    def delete_project(self, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        # 二、开始操作。搜索project
        deleted_name = self.project.project_name_in_list().text
        project_element = self.project.project_to_run_btn()
        project_element.click()
        start_time = TimeUtil.get_current_time()
        self.project.get_setting_button().click()
        self.project.get_delete_button().click()
        self.project.get_delete_ok_button().click()
        # 三、校验结果
        if if_verify:
            self.project.get_search_project().send_keys(deleted_name)
            self.project.get_search_project().send_keys(Keys.ENTER)
            time.sleep(3)
            no_data = self.project.no_data()
            self.verify.verify_issue_unlinked(no_data)

        self.capture.capture_all(case_desc + "delete-4.png")
        end_time = TimeUtil.get_current_time()
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "delete-4.png",
                                                         "Delete project successfully")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Delete project successfully',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "delete-4.png"),
                                                                      None, start_time,
                                                                      end_time))

    def list_project(self):
        case_desc = self.data['case_desc']
        start_time = TimeUtil.get_current_time()
        temp = self.project.get_list_page_no().text
        total_page = int(temp[temp.index("/") + 1:])
        one_page_count = len(self.project.get_list_one_page())
        max_page = int(self.project.get_pagination_button()[len(self.project.get_pagination_button()) - 1].text)
        max_page_count = int(self.project.get_one_page_number().text)
        self.verify.verify_project_list_page(total_page, one_page_count, max_page, max_page_count)
        self.capture.capture_all(case_desc + "search-1.png")
        end_time = TimeUtil.get_current_time()
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "search-1.png",
                                                         "Project list page is correct")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Project list page is correct',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "search-1.png"),
                                                                      None, start_time,
                                                                      end_time))

    def navigate_to_modules(self, which, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        # 二、开始操作。点击icon进入子层级
        time.sleep(3)
        self.project.project_to_module_btn(which).click()
        start_time = TimeUtil.get_current_time()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            actual_module_menu = self.project.module_menu(which).text
            if which == 2:
                expect_module_menu = "Requirements"
            elif which == 3:
                expect_module_menu = "Cases"
            elif which == 4:
                expect_module_menu = "Runs"
            elif which == 5:
                expect_module_menu = "Reports"
            elif which == 6:
                expect_module_menu = "Issues"
            else:
                # which == 7
                expect_module_menu = "Jobs"
            self.verify.verify_consistent_display(actual_module_menu, expect_module_menu)

        self.capture.capture_all(case_desc + "-1.png")
        end_time = TimeUtil.get_current_time()
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png",
                                                         "Navigate to module menu")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Navigate to module menu',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

    def add_member(self, if_verify, browser_data):
        # 一、准备数据
        case_desc = self.data['case_desc']
        member = self.data['member']
        verify = self.data['verify']
        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        plat = platform.system().lower()
        # 二、开始操作。添加member
        project_element = self.project.project_to_run_btn()
        project_element.click()
        time.sleep(2)
        self.project.get_setting_button().click()
        time.sleep(0.5)
        self.project.get_members_button().click()
        self.project.get_setting_button().click()

        self.capture.capture_all(case_desc + "starred-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "starred-1.png",
                                                         "Navigate to members list")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Navigate to members list',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "starred-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        time.sleep(2)
        self.project.get_add_members_button().click()
        time.sleep(2)
        if plat == "darwin" and ('remote' not in str(browser_data)):
            self.project.get_search_members().send_keys(Keys.COMMAND, "a")
        else:
            self.project.get_search_members().send_keys(Keys.CONTROL, "a")
        self.project.get_search_members().send_keys(Keys.DELETE)
        self.project.get_search_members().send_keys(member)
        time.sleep(2)
        self.project.get_members_items().click()

        self.capture.capture_all(case_desc + "starred-2.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "starred-2.png",
                                                         "Add new user to this project")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Add new user to this project',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "starred-2.png"),
                                                                      None, start_time,
                                                                      end_time))

        time.sleep(1)
        self.project.get_ok_button().click()
        time.sleep(3)
        # 三、校验结果
        if if_verify:
            actual = self.project.get_members_list().text
            self.verify.verify_add_members(actual, verify)

        self.capture.capture_all(case_desc + "starred-3.png")
        end_time = TimeUtil.get_current_time()
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "starred-3.png",
                                                         "Add members for project successfully")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Add members for project successfully',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "starred-3.png"),
                                                                      None, start_time,
                                                                      end_time))

    def switch_project(self, if_verify):
        # 一、准备数据
        case_desc = self.data['case_desc']
        # 二、开始操作。搜索project
        time.sleep(3)
        project_element = self.project.project_to_run_btn()
        project_element.click()
        time.sleep(1)
        self.project.switch_pro_arrow().click()
        time.sleep(1)

        start_time = TimeUtil.get_current_time()
        end_time = TimeUtil.get_current_time()
        self.capture.capture_all(case_desc + "-1.png")
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-1.png",
                                                         "Switch to another project")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Switch to another project',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-1.png"),
                                                                      None, start_time,
                                                                      end_time))

        count = len(self.project.switch_pro_list())
        time.sleep(1)
        expect_new_pro = self.project.switch_pro_dropdown(count).text
        self.driver.scroll_to_element(self.project.switch_pro_dropdown(count))
        self.project.switch_pro_dropdown(count).click()
        time.sleep(6)
        # 三、校验结果
        if if_verify:
            actual_new_pro = self.project.switch_pro_name().text
            self.verify.verify_switch_project(actual_new_pro, expect_new_pro)

        self.capture.capture_all(case_desc + "-2.png")
        end_time = TimeUtil.get_current_time()
        if self.if_upload_rp:
            self.capture.upload_capture_to_report_portal(case_desc + "-2.png",
                                                         "Project is switched")
        if self.if_upload_atas:
            self.atas_api.upload_result(self.result.get_upload_result('Project is switched',
                                                                      self.capture.get_full_path(
                                                                          case_desc + "-2.png"),
                                                                      None, start_time,
                                                                      end_time))
