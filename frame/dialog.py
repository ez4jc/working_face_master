# -*- coding:utf-8 -*-

import re

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

from .base_window import BaseWindow
import os


# 对话框基类
class Dialog(BaseWindow, QMainWindow):
    def __init__(self, window_name):
        super(Dialog, self).__init__(window_name)
        if hasattr(self.ui, "quit_button"):
            self.ui.quit_button.clicked.connect(self.quit)  # 关闭信号按钮连接
        else:
            pass
        if hasattr(self.ui, "ok_button"):
            self.ui.ok_button.clicked.connect(self.on_ok_button_clicked)  # ok按钮信号连接
        else:
            pass
        if hasattr(self.ui, "retry_Button"):
            self.ui.retry_Button.clicked.connect(self.on_retry_Button_clicked)
        else:
            pass
        # self.top.setWindowFlags(Qt.FramelessWindowHint)
        # 去除显示？的内容
        self.ui.setWindowFlags(Qt.WindowCloseButtonHint)

    # 显示
    def show(self):
        return self.ui.exec_()

    # 退出
    def quit(self):
        self.ui.hide()

    # 点击ok按钮功能
    def on_ok_button_clicked(self):
        pass

    # 点击重试按钮功能
    def on_retry_Button_clicked(self):
        pass

    # 获取项目路径
    @staticmethod
    def get_project_path():
        current_abs_path = os.path.realpath(__file__)  # 脚本执行路径
        father_path = os.path.dirname(current_abs_path)
        project_path = os.path.dirname(os.path.abspath(father_path))
        return project_path

    # 设置图标
    def set_frame_ico(self):
        project_path = self.get_project_path()
        image_path = os.path.join(
            os.path.abspath(project_path), "static/images", "main.ico")
        return image_path

    # 判断是否为数字
    @staticmethod
    def is_number(num):
        if not num:
            return True
        if isinstance(num, int):
            return True
        if isinstance(num, float):
            return True

        try:
            eval(num)  # 计算
            return True
        except Exception:
            return False

    # 检查并格式化数据
    def format_cell(self, data):
        if data is None:
            return True
        if self.is_number(data):
            return True
        if re.match(r"[_]", data[0]):  # 正则表达式
            return False
        for character in data:
            if re.match(r"\s", character):
                return True

            result = re.findall(r"[^0-9A-Za-z_=\+\-\*/\.]", character)
            if result:
                return False
        last_ch = re.match(r"[^0-9a-zA-Z]", data[-1])
        if last_ch:
            return False
        return True



