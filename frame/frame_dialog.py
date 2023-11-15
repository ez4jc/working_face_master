# -*- coding:utf-8 -*-
import os
import shutil

from PySide6.QtGui import QIcon
from loguru import logger
from pathlib import Path

from frame.dialog import Dialog


#  信息弹窗
class InformationDialog(Dialog):
    def __init__(self):
        super(InformationDialog, self).__init__("information_dialog.ui")
        self.ui.setWindowIcon(QIcon(self.set_frame_ico()))
        project_path = self.get_project_path()
        # 暂时不限时界面中图片
        # warning_path = os.path.join(
        #     os.path.abspath(project_path), "image", "information.png")
        # self.label_icon.setPixmap(QPixmap(warning_path))

    def change_text(self, text):
        self.ui.text_label.setText(text)

    def change_title(self, title):
        self.ui.setWindowTitle(title)
