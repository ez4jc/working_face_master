# *coding:utf-8 *
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from main_window import MainWindow
import warnings

from common.global_config import global_all_config
import common.project_memory as ProjectMemory

from loguru import logger

# 设置界面风格
from qt_material import apply_stylesheet

warnings.filterwarnings("ignore", category=DeprecationWarning)


# 程序开始
def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, 'light_blue.xml')
    # 初始化缓存
    ProjectMemory.initialize()

    # 打开界面
    ui = MainWindow(app)
    ui.showMaximized()

    ui.show()
    logger.info("current version : {}", global_all_config.version)
    ProjectMemory.set_value("version", global_all_config.version)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
