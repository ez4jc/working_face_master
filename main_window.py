import os
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from loguru import logger

import win32gui

import open3d as o3d

import vtkmodules.all as vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

import cv2

import numpy as np

from frame.frame_dialog import InformationDialog
from ui.ui_initial_window import Ui_MainWindow
from sub_win_support import SubWinSupport
from roadway_win import RoadWayWin

import common.project_memory as ProjectMemory

# 导入项目模块
from point_cloud_module import CustomQVTKRenderWindowInteractor
from video_module import CustomCameraLabel


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, app, parent=None):
        self.app = app
        self.image_parent_path = self.get_images_path()

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("煤矿软件（版本0.1）")
        self.setWindowIcon(QIcon(self.set_frame_ico()))

        # 点云模块实例
        self.vtkWidget = CustomQVTKRenderWindowInteractor(self)

        # 巷道窗口实例
        self.roadway_win = RoadWayWin(self.vtkWidget)

        # 摄像头模块实例
        self.videoWidget = CustomCameraLabel(self)

        # 按钮初始化、绑定
        self.button_init()
        self.bind()

        # 正在显示某信息则设置为True,此标志用来帮助释放资源
        self.showVideo = False
        self.showPointCloud = False

        # 工具栏模块
        self._create_actions()

        # 固定视角的摄像头位置
        self.camera_fixed_position = [(-7.3, 2.2, 0.9)]

    def simulate_win_init(self):
        # 点云模块实例后，支撑架窗口实例才不会出错
        self.simulate_win = SubWinSupport(self.vtkWidget)
        # 菜单栏绑定
        self.action_supportControler.triggered.connect(self.simulate_win.show)
        self.simulate_win_init_flag = True

    def button_init(self):
        self.widget_control.setEnabled(False)
        self.checkBox_planeXY.setChecked(True)

    def bind(self):
        # view下方的按钮
        self.radioButton_dianyun.clicked.connect(self.vtkWidget.show_point_cloud)
        self.radioButton_jiankong.clicked.connect(self.videoWidget.show_video)
        self.radioButton_clear.clicked.connect(self.show_blank)
        # 控制面板的按钮
        # 加载场景选项卡
        self.pushButton_roadwayAndCoalmineSettings.clicked.connect(self.roadway_win.show)
        self.pushButton_coalCutter.clicked.connect(self.vtkWidget.coal_cutter_actor.show_model)
        self.pushButton_supporterInit.clicked.connect(self.vtkWidget.support_init)
        ##############################
        self.checkBox_planeXY.toggled.connect(self.vtkWidget.toggled_planeXY)
        self.checkBox_planeYZ.toggled.connect(self.vtkWidget.toggled_planeYZ)
        self.checkBox_planeXZ.toggled.connect(self.vtkWidget.toggled_planeXZ)
        self.checkBox_axes.toggled.connect(self.vtkWidget.toggled_axes)
        self.checkBox_highlight_point.toggled.connect(self.vtkWidget.toggled_highlight_point)
        self.pushButton_add_ply.clicked.connect(self.vtkWidget.load_dianyun_module)
        self.horizontalSlider_ambient.valueChanged.connect(self.vtkWidget.change_property)
        self.horizontalSlider_diffuse.valueChanged.connect(self.vtkWidget.change_property)
        self.horizontalSlider_viewSpeed.valueChanged.connect(self.vtkWidget.change_viewSpeed_intermediary)
        self.horizontalSlider_flySpeed.valueChanged.connect(self.vtkWidget.change_flySpeed_intermediary)
        self.radioButton_horizon_rotate.clicked.connect(self.vtkWidget.camera_controller.switch_limitedX)
        self.radioButton_vertical_rotate.clicked.connect(self.vtkWidget.camera_controller.switch_limitedY)
        self.radioButton_roll.clicked.connect(self.vtkWidget.camera_controller.switch_limitedRoll)
        self.radioButton_unlimited.clicked.connect(self.vtkWidget.camera_controller.switch_unlimited)
        # 视角设置按钮
        self.radioButton_supporterHead.clicked.connect(lambda: self.vtkWidget.load_camera_info(0))
        self.radioButton_supportertail.clicked.connect(lambda: self.vtkWidget.load_camera_info(1))
        self.radioButton_3.clicked.connect(lambda: self.vtkWidget.load_camera_info(2))
        self.radioButton_4.clicked.connect(lambda: self.vtkWidget.load_camera_info(3))
        self.radioButton_5.clicked.connect(lambda: self.vtkWidget.load_camera_info(4))
        self.radioButton_6.clicked.connect(lambda: self.vtkWidget.load_camera_info(5))
        self.radioButton_7.clicked.connect(lambda: self.vtkWidget.load_camera_info(6))
        self.radioButton_8.clicked.connect(lambda: self.vtkWidget.load_camera_info(7))
        self.radioButton_9.clicked.connect(lambda: self.vtkWidget.load_camera_info(8))
        self.radioButton_10.clicked.connect(lambda: self.vtkWidget.load_camera_info(9))

        # 开发按钮
        self.pushButton_getCameraPosition.clicked.connect(self.vtkWidget.camera_controller.save_camera_info)

    def viewer_show(self, item):
        if item == "Video":
            # 清空
            if self.showPointCloud:
                self.show_blank()
            # 显示
            self.view_layout.addWidget(self.videoWidget)
            self.widget_control.setEnabled(False)  # 点云控制面板失效
        elif item == "PointCloud":
            # 清空
            if self.showVideo:
                self.show_blank()
            # 显示
            self.view_layout.addWidget(self.vtkWidget)
            self.widget_control.setEnabled(True)  # 使控制面板生效

    def add_check_box(self, file_name, actor, checkBoxs):
        # 添加点云对象的可选框
        point_actor_check_box = QCheckBox(self)
        point_actor_check_box.setText(file_name.split('/')[-1])
        point_actor_check_box.setChecked(True)
        point_actor_check_box.clicked.connect(lambda: self.vtkWidget.show_actor(actor))
        checkBoxs.append(point_actor_check_box)  # 更新CustomQVTKRenderWindowInteractor的数据结构
        self.verticalLayout_widget_pointCloudCheckBox.addWidget(point_actor_check_box)

    def show_blank(self):
        # 移除控件前需释放资源
        if self.showPointCloud:
            self.vtkWidget.setParent(None)
            self.view_layout.removeWidget(self.vtkWidget)
            self.showPointCloud = False  # 释放点云计算资源
        elif self.showVideo:  # 释放摄像头资源
            self.videoWidget.cap.release()
            self.videoWidget.clockForVideo.stop()
            self.videoWidget.setParent(None)
            self.view_layout.removeWidget(self.videoWidget)
            self.showVideo = False
        self.widget_view.setLayout(None)
        self.widget_control.setEnabled(False)  # 使控制面板失效

    @Slot()
    def on_about_us_action_triggered(self):
        self.about_us_operator()

    @Slot()
    def trigger_about_us(self):
        logger.info("关于我们！ ")

    def _create_actions(self):
        open_file_action = self.create_action(
            slot=self.on_open_file_triggered,
            icon="open.png",
            tip="打开文件",
        )

        bracket_action = self.create_action(
            slot=self.on_bracket_triggered,
            icon="bracket.png",
            tip="支架",
        )

        tunnel_action = self.create_action(
            slot=self.on_tunnel_triggered,
            icon="tunnel.png",
            tip="巷道",
        )

        buttock_action = self.create_action(
            slot=self.on_buttock_triggered,
            icon="buttock.png",
            tip="割煤机",
        )

        radio_action = self.create_action(
            slot=self.on_radio_triggered,
            icon="radio.png",
            tip="雷达",
        )

        information_action = self.create_action(
            slot=self.on_information_triggered,
            icon="information.png",
            tip="数据",
        )

        settings_action = self.create_action(
            slot=self.on_settings_triggered,
            icon="settings.png",
            tip="设置",
        )

        about_us_action = self.create_action(
            slot=self.on_about_us_triggered,
            icon="about_us.png",
            tip="关于",
        )

        exit_action = self.create_action(
            slot=self.on_exit_triggered,
            icon="exit.png",
            tip="退出",
        )

        self.top_tool_bar.addWidget(open_file_action)
        self.top_tool_bar.addWidget(bracket_action)
        self.top_tool_bar.addWidget(tunnel_action)
        self.top_tool_bar.addWidget(buttock_action)
        self.top_tool_bar.addWidget(radio_action)
        self.top_tool_bar.addWidget(information_action)
        self.top_tool_bar.addWidget(settings_action)
        self.top_tool_bar.addWidget(about_us_action)
        self.top_tool_bar.addWidget(exit_action)
        logger.info(self.top_tool_bar.width())

    def create_action(
            self,
            text=None,
            slot=None,
            shortcut=None,
            icon=None,
            tip=None,
            checkable=False,
            signal="triggered",
    ):
        # 创建表格工具栏和action
        action = QToolButton()
        action.setFixedWidth(60)
        action.setFixedHeight(60)
        if text:
            action.setText(text)
        if icon:
            image_path = os.path.join(
                os.path.abspath(self.image_parent_path), "static\\images", icon)
            action.setIcon(QIcon(image_path))
            logger.info("图标路径 ： {}", image_path)
        if shortcut:
            action.setShortcut(shortcut)
        if tip:
            action.setToolTip(tip)
        if slot:
            action.clicked.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action

    @Slot()
    def on_open_file_triggered(self, test_mode=False):
        logger.info("打开文件！")
        pass

    @Slot()
    def on_bracket_triggered(self, test_mode=False):
        logger.info("支架视角！")

    @Slot()
    def on_tunnel_triggered(self, test_mode=False):
        logger.info("巷道视角！")

    @Slot()
    def on_buttock_triggered(self, test_mode=False):
        logger.info("割煤机视角！")

    @Slot()
    def on_radio_triggered(self, test_mode=False):
        logger.info("雷达视角！")

    @Slot()
    def on_information_triggered(self, test_mode=False):
        logger.info("查看距离信息！")

    @Slot()
    def on_settings_triggered(self, test_mode=False):
        logger.info("设置参数！")

    @Slot()
    def on_about_us_triggered(self, test_mode=False):
        self.about_us_operator()

    @Slot()
    def on_exit_triggered(self, test_mode=False):
        logger.info("退出！")
        self.closeWindow()

    @staticmethod
    def about_us_operator():
        information_dialog = InformationDialog()
        information_dialog.change_text("版本号：" + str(ProjectMemory.get_value("version")))
        information_dialog.change_title("关于我们")
        information_dialog.show()
        logger.info("关于我们！")

    @staticmethod
    def get_images_path():
        current_abs_path = os.path.realpath(__file__)  # 脚本执行路径
        father_path = os.path.dirname(current_abs_path)
        return father_path

    def set_frame_ico(self):
        project_path = self.get_project_path()
        image_path = os.path.join(
            os.path.abspath(project_path), "static/images", "main.ico")
        return image_path

    # 获取项目路径
    @staticmethod
    def get_project_path():
        current_abs_path = os.path.realpath(__file__)  # 脚本执行路径
        father_path = os.path.dirname(current_abs_path)
        project_path = os.path.dirname(os.path.abspath(father_path))
        return project_path

    def closeEvent(self, event):
        result = QMessageBox.question(self, "确定", "确定退出?", QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            event.accept()
            logger.info("退出程序!")
            # sys.exit(0)
            try:
                sys.exit(1)
            except:
                os._exit(1)
            finally:
                os._exit(1)
        else:
            event.ignore()

    def closeWindow(self):
        result = QMessageBox.question(self, "确定", "确定退出?", QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            logger.info("退出程序!")
            # sys.exit(0)
            try:
                sys.exit(1)
            except:
                os._exit(1)
            finally:
                os._exit(1)
