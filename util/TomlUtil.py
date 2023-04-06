import toml


class TomlUtil:
    @staticmethod
    def get_tml(file):
        return toml.load(file)
