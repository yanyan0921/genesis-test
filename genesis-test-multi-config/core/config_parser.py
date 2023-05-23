import configparser


class ConfigLoader:

    def __init__(self, name):
        self.parser = configparser.ConfigParser()
        self.config_file = "./conf/" + name + ".cfg"
        self.parser.read(self.config_file)

    def get_sections(self):
        return self.parser.sections()

    def get_setting_test(self):
        return self.parser.items("test")

    def get_setting_db(self):
        return self.parser.items("db")

    def get_setting_selenium(self):
        return self.parser.items("selenium")

    def get_setting(self, section, item):
        return self.parser.get(section, item)
