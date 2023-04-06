import datetime
import json

global global_list
global_list = []
global global_execution_id
global_execution_id = ''
global global_run_data
global_run_data = {}
global global_case_name
global_case_name = ''
global global_path
global_path = ''


def get_list():
    return global_list


def set_case_name(node_id):
    global global_case_name
    global_case_name = node_id[node_id.rindex('::') + 2:node_id.rindex('[')]
    global global_path
    global_path = node_id[node_id.index('::') + 2:node_id.rindex('::')]


def get_path():
    return global_path


def get_case_name():
    return global_case_name


def set_run_data(data):
    global global_run_data
    global_run_data = data


def get_run_data():
    return global_run_data


def set_execution_id(execution_id):
    global global_execution_id
    global_execution_id = execution_id


def get_execution_id():
    return global_execution_id


def get_upload_result(step_description, screen_path,
                      attachment_path, start_time, end_time, case_status='pass', step_status='pass'):
    data = {'caseName': get_case_name(),
            'path': get_path(),
            'stepStatus': step_status,
            'stepDescription': step_description,
            'caseStatus': case_status,
            'screen_path': screen_path,
            'attachment_path': attachment_path,
            'executionId': get_execution_id(),
            'startTime': start_time,
            'endTime': end_time}
    return data


def update_result(atas_api, case_name, path, step_status, case_status, step_description, screen_path,
                  attachment_path, start_time, end_time):
    data = {'caseName': case_name,
            'path': path,
            'stepStatus': step_status,
            'stepDescription': step_description,
            'caseStatus': case_status,
            'screen_path': screen_path,
            'attachment_path': attachment_path,
            'executionId': get_execution_id(),
            'startTime': start_time,
            'endTime': end_time}
    atas_api.save_result(data)


def append_list(global_list, desc, screen, screen_thumbnail, status):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ind = False
    for item in global_list:
        if item.get('case_name') == '':
            ind = True
            break
    if ind:
        for item in global_list:
            if item.get('case_name') == '':
                value = '{\"step\": \"' + desc + '\", \"screen\": \"' + screen + '\", \"screen_thumbnail\": \"' + screen_thumbnail + '\", \"status\": \"' + status + '\"}'
                item.get('steps').append(json.loads(value))
                item['status'] = status
    else:
        value = '{\"case_name\": \"''\", \"complete_time\": \"' + time + '\", \"steps\": [{\"step\": \"' + desc + '\", \"screen\": \"' + screen + '\", \"screen_thumbnail\": \"' + screen_thumbnail + '\", \"status\": \"' + status + '\"}], \"log_file\": \"\", \"status\": \"' + status + '\"}'
        global_list.append(json.loads(value))


def update_status(global_list, case_name, status):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ind = False
    for item in global_list:
        if item.get('case_name') == '':
            ind = True
            break
    if ind:
        for item in global_list:
            if item.get('case_name') == '':
                item['status'] = status
                item['case_name'] = case_name
    else:
        value = '{\"case_name\": \"' + case_name + '\", \"complete_time\": \"' + time + '\", \"steps\": [{\"step\": \"\", \"screen\": \"\", \"screen_thumbnail\": \"\", \"status\": \"' + status + '\"}], \"log_file\": \"\", \"status\": \"' + status + '\"}'
        global_list.append(json.loads(value))

# def append_list(global_list, case_name, desc, screen, screen_thumbnail, status):
#     time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     ind = False
#     for item in global_list:
#         if item.get('case_name') == case_name:
#             ind = True
#             break
#     if ind:
#         for item in global_list:
#             if item.get('case_name') == case_name:
#                 value = '{\"step\": \"' + desc + '\", \"screen\": \"' + screen + '\", \"screen_thumbnail\": \"' + screen_thumbnail + '\"}'
#                 item.get('steps').append(json.loads(value))
#                 item['status'] = status
#     else:
#         value = '{\"case_name\": \"' + case_name + '\", \"complete_time\": \"' + time + '\", \"steps\": [{\"step\": \"' + desc + '\", \"screen\": \"' + screen + '\", \"screen_thumbnail\": \"' + screen_thumbnail + '\"}], \"log_file\": \"\", \"status\": \"' + status + '\"}'
#         global_list.append(json.loads(value))
#
#
# def update_status(global_list, status):
#     time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     ind = False
#     for item in global_list:
#         if item.get('case_name') == global_case_name:
#             ind = True
#             break
#     if ind:
#         for item in global_list:
#             if item.get('case_name') == global_case_name:
#                 item['status'] = status
#     else:
#         value = '{\"case_name\": \"' + global_case_name + '\", \"complete_time\": \"' + time + '\", \"steps\": [{\"step\": \"\", \"screen\": \"\", \"screen_thumbnail\": \"\"}], \"log_file\": \"\", \"status\": \"' + status + '\"}'
#         global_list.append(json.loads(value))
