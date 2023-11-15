# *coding:utf-8 *
import yaml


# 需要定义全局变量的放在这里，最好定义一个初始值
class GlobalConfig:
    def __init__(self):
        self.io_model = 'mock'
        # 读取配置文件
        with open("global_config.yml", 'r', encoding='utf-8') as ymlfile:
            config_data = yaml.load(ymlfile, Loader=yaml.FullLoader)
            # 获取版本号
            self.remote_port = config_data["other"]["remote_port"]
            # 获取版本号
            self.version = config_data["other"]["version"]


global_all_config = GlobalConfig()
