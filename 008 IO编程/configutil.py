import os
import os.path
import configparser

'''
1. 载入ini
2. 删除section
3. 删除item
4. 修改item
5. 添加section
6. 保存修改
'''


class StudentInfo:
    def __init__(self, filename):
        self.cfg_file = filename
        self.cfg = configparser.ConfigParser()

    def load_config_file(self):
        return self.cfg.read(self.cfg_file)

    def remove_section(self, section):
        return self.cfg.remove_section(section)

    def remove_item(self, section, item):
        return self.cfg.remove_option(section, item)

    def set_item(self, section, key, item):
        return self.cfg.set(section, key, item)

    def add_section(self, section):
        return self.add_section(section)

    def save(self):
        with open(self.cfg_file, 'w') as fp:
            self.cfg.write(fp)


