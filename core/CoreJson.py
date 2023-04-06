
from core import get_root_path, get_config_file
from util.JsonUtil import JsonUtil


class CoreJson:
    @staticmethod
    def get_json(file):
        f = get_root_path() + get_config_file().get(file).get('data_json')
        try:
            d = JsonUtil.get_json(f)
        except FileNotFoundError as e:
            d = {}
        return d
