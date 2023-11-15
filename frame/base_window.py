# -*- coding:utf-8 -*-

import os
from abc import ABCMeta

from PySide6.QtUiTools import loadUiType, QUiLoader
from PySide6.QtCore import QFile, QMetaMethod
from PySide6.QtWidgets import QWidget


class BaseWidgetMeta(ABCMeta, type(QWidget)):
    pass


# 窗口基类
class BaseWindow(QWidget):
    def __init__(self, window_name=None, parent=None):
        self.ui = self.load_ui(window_name)

    # 加载ui
    def load_ui(self, window_name):
        project_path = self.get_project_path()
        ui_path = os.path.join(project_path, "ui", window_name)
        ui_file = QFile(ui_path)
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        ui = QUiLoader().load(ui_file)
        return ui

    # 获取项目路径
    @staticmethod
    def get_project_path():
        current_abs_path = os.path.realpath(__file__)  # 脚本执行路径
        father_path = os.path.dirname(current_abs_path)
        project_path = os.path.dirname(os.path.abspath(father_path))
        return project_path

    def set_frame_ico(self):
        project_path = self.get_project_path()
        image_path = os.path.join(
            os.path.abspath(project_path), "image", "main.ico")
        return image_path

    # 添加菜单功能信号和连接去向
    def add_menu_signals(self, obj):
        for each in self._traverse_tree(self.top):
            each_meta = each.metaObject()
            if each_meta.className() == "QAction":
                slot = "on_" + each.objectName() + "_triggered"
                if hasattr(obj, slot):
                    each.triggered.connect(getattr(obj, slot))

    # 连接自定义信号
    @staticmethod
    def connect_user_defined_signal(obj, presenter):
        meta_object = obj.metaObject()
        for i in range(meta_object.methodCount()):
            method = meta_object.method(i)
            if method.methodType() != QMetaMethod.Signal:
                continue
            signature = str(method.methodSignature())
            if "signal" not in signature:
                continue
            name = signature.split("_signal")[0]
            if hasattr(presenter, name):
                slot = getattr(presenter, name)
                signal = getattr(obj, signature)
                signal.connect(slot)
            else:
                continue
