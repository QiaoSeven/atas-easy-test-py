import json

import json_tools


class JsonUtil:
    @staticmethod
    def get_json(file):
        with open(file, 'r', encoding="utf-8") as fp:
            dict_json = json.load(fp)
        return dict_json

    @staticmethod
    def diff_json(expect, actual):
        result = json_tools.diff(expect, actual)
        print(expect)
        print(actual)
        return result
