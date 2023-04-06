import os

from core import get_root_path, get_config_file


class CoreConfig:
    @staticmethod
    def get_screen_full_path(file_name):
        if not os.path.exists(get_root_path() + get_config_file().get('result').get('screen_path')):
            os.mkdir(get_root_path() + get_config_file().get('result').get('screen_path'))
            # os.mkdir('.' + get_config_file().get('result').get('screen_path'))
        return get_root_path() + get_config_file().get('result').get('screen_path') + file_name

    @staticmethod
    def get_data_full_path():
        return get_root_path() + get_config_file().get('data').get('data_excel')

    @staticmethod
    def get_video_full_path(file_name, def_name):
        global folder_name
        file_path = get_root_path() + get_config_file().get('result').get('video_path')
        file_list = os.listdir(file_path)
        j = def_name.replace('_', '-')
        for file in file_list:
            # 读取原文件名
            i = file
            if j in i:
                folder_name = i
            else:
                return None
        return file_path + folder_name + '/' + file_name

    @staticmethod
    def if_report_portal():
        return get_config_file().get('report').get('if_report_portal')

    @staticmethod
    def if_report_atas():
        return get_config_file().get('report').get('if_report_atas')

    @staticmethod
    def get_log_info():
        res = {'file_path': get_root_path() + get_config_file().get('logs').get('path'),
               'level': get_config_file().get('logs').get('level'),
               'rotation': get_config_file().get('logs').get('rotation'),
               'backup': get_config_file().get('logs').get('backup')}
        return res

    @staticmethod
    def get_caps_by_type(type_name):
        res = get_config_file().get(type_name)
        return res

    @staticmethod
    def get_proxy(item):
        return get_config_file().get('proxy').get(item)

    @staticmethod
    def get_atas_config(item):
        return get_config_file().get('atas').get(item)

    @staticmethod
    def get_grid(item):
        return get_config_file().get('grid').get(item)
