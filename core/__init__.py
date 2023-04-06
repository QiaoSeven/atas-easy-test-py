import os

from util.TomlUtil import TomlUtil


def get_root_path():
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("atas-easy-test-py") + len("atas-easy-test-py")]
    return rootPath


def get_config_file():
    if os.getenv('ATAS_CONF') != '' and os.getenv('ATAS_CONF') is not None:
        conf_path = get_root_path() + '/config/conf_' + os.getenv('ATAS_CONF') + '.tml'
    else:
        conf_path = get_root_path() + '/config/conf.tml'
    conf_file = TomlUtil.get_tml(conf_path)
    return conf_file
