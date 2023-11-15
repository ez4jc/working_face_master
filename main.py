# *coding:utf-8 *
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from main_window import MainWindow
import warnings

from common.global_config import global_all_config
import common.project_memory as ProjectMemory

# from qt_material import apply_stylesheet

from loguru import logger

warnings.filterwarnings("ignore", category=DeprecationWarning)


# 程序开始
def main():
    app = QApplication(sys.argv)

    # 初始化缓存
    ProjectMemory.initialize()

    ui = MainWindow(app)
    ui.showMaximized()

    ui.show()
    logger.info("current version : {}", global_all_config.version)
    ProjectMemory.set_value("version", global_all_config.version)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
