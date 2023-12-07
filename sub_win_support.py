import typing

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QCoreApplication, QMutex, QMutexLocker

from ui.simulate_win import Ui_simulate_win


class SubWinSupport(QtWidgets.QWidget, Ui_simulate_win):
    def __init__(self, vtkWidget):
        super().__init__()
        self.setupUi(self)

        self.vtkWidget = vtkWidget

        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # 支撑架初始化后绑定才不会出错
        self.bind()

        # 互斥锁
        self.push_scraper_mutex = QMutex()
        self.push_scraper_is_executing = False

    def bind(self):
        self.comboBox_supporter.currentIndexChanged.connect(self.update_selected_supporter)
        # 绑定初始支撑架
        self.pushButton_pushScraper.clicked.connect(self.push_scraper)
        # 模型勾选框
        self.checkBox_supporter_model.clicked.connect(self.vtkWidget.supporter_actors[0].show_model)
        # 标签勾选框
        self.checkBox_label.clicked.connect(self.vtkWidget.supporter_actors[0].show_label)
        # 包围框勾选框
        self.checkBox_wraparound_frame.clicked.connect(
            self.vtkWidget.supporter_actors[0].show_wraparound_frame)
        # 静态包围框勾选框
        self.checkBox_static_wraparound_frame.clicked.connect(
            self.vtkWidget.supporter_actors[0].show_static_wraparound_frame)
        # 陀螺仪勾选框
        self.checkBox_gyro.clicked.connect(
            self.vtkWidget.supporter_actors[0].show_gyro)
        # xoy旋转按钮
        self.pushButton_xoy.clicked.connect(
            lambda: self.vtkWidget.supporter_actors[0].roll_xoy(float(self.lineEdit_xoy.text())))
        # yoz旋转按钮
        self.pushButton_yoz.clicked.connect(
            lambda: self.vtkWidget.supporter_actors[0].roll_yoz(float(self.lineEdit_yoz.text())))
        # zox旋转按钮
        self.pushButton_zox.clicked.connect(
            lambda: self.vtkWidget.supporter_actors[0].roll_zox(float(self.lineEdit_zox.text())))

        # 刮板机按钮勾选
        self.checkBox_scraper.clicked.connect(self.vtkWidget.scraper_actors[0].show_model)

        # 文本初始数值
        self.update_text(str("%.3f" % self.vtkWidget.supporter_actors[0].axis_theta[0]),
                         str("%.3f" % (180 - self.vtkWidget.supporter_actors[0].axis_theta[1])),
                         str("%.3f" % (180 - self.vtkWidget.supporter_actors[0].axis_theta[2])),
                         str(self.float_tupleorlist_cutter(self.vtkWidget.supporter_actors[0].GetCenter(), 3)))

    def update_selected_supporter(self):
        # 断开槽函数，控件回默认值
        # self.pushButton_pushSupport.clicked.disconnect()
        self.checkBox_supporter_model.clicked.disconnect()
        self.checkBox_label.clicked.disconnect()
        self.checkBox_wraparound_frame.clicked.disconnect()
        self.checkBox_static_wraparound_frame.clicked.disconnect()
        self.checkBox_gyro.clicked.disconnect()
        self.pushButton_xoy.clicked.disconnect()
        self.pushButton_yoz.clicked.disconnect()
        self.pushButton_zox.clicked.disconnect()
        self.checkBox_scraper.clicked.disconnect()

        # 同步控件和支撑架的状态，保证一致性
        self.checkBox_supporter_model.setChecked(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].model_flag)
        self.checkBox_label.setChecked(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].label_flag)
        self.checkBox_wraparound_frame.setChecked(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].wraparound_actor_flag)
        self.checkBox_static_wraparound_frame.setChecked(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].static_wraparound_actor_flag)
        self.checkBox_gyro.setChecked(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].gyro_flag)
        self.checkBox_supporter_model.clicked.connect(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].show_model)
        self.checkBox_label.clicked.connect(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].show_label)
        self.checkBox_wraparound_frame.clicked.connect(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].show_wraparound_frame)
        self.checkBox_static_wraparound_frame.clicked.connect(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].show_static_wraparound_frame)
        self.checkBox_gyro.clicked.connect(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].show_gyro)
        # xoy旋转按钮
        self.pushButton_xoy.clicked.connect(
            lambda: self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].roll_xoy(
                float(self.lineEdit_xoy.text())))
        # yoz旋转按钮
        self.pushButton_yoz.clicked.connect(
            lambda: self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].roll_yoz(
                float(self.lineEdit_yoz.text())))
        # zox旋转按钮
        self.pushButton_zox.clicked.connect(
            lambda: self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].roll_zox(
                float(self.lineEdit_zox.text())))
        # 刮板机按钮勾选
        self.checkBox_scraper.clicked.connect(
            self.vtkWidget.scraper_actors[self.comboBox_supporter.currentIndex()].show_model)

        # 文本切换对应支撑架的数值
        self.update_text(
            str("%.3f" % self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].axis_theta[0]),
            str("%.3f" % (180 - self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].axis_theta[1])),
            str("%.3f" % (180 - self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].axis_theta[2])),
            str(self.float_tupleorlist_cutter(
                self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].GetCenter(), 3)))

    def update_text(self, theta1: str, theta2: str, theta3: str, center):
        self.textEdit_4.setText(theta1)
        self.textEdit_5.setText(theta2)
        self.textEdit_6.setText(theta3)
        self.textEdit_centerPoint.setText(center)

    def push_scraper(self):
        with QMutexLocker(self.push_scraper_mutex):
            if self.push_scraper_is_executing:
                return
            self.push_scraper_is_executing = True

        self.pushButton_pushScraper.setEnabled(False)
        QCoreApplication.processEvents()

        # 在这里执行实际操作 move_actor
        self.vtkWidget.move_actor(self.vtkWidget.scraper_actors[self.comboBox_supporter.currentIndex()],
                                  float(self.lineEdit_pushScraper.text()))

        with QMutexLocker(self.push_scraper_mutex):
            self.push_scraper_is_executing = False
            self.pushButton_pushScraper.setEnabled(True)

    @staticmethod
    def float_tupleorlist_cutter(center: typing.Tuple, num: int):
        """
        此函数用于将浮点数类型的元组或列表中的浮点数保留3位
        :param center:
        :param num:
        :return:
        """
        return round(center[0], num), round(center[1], num), round(center[2], num)
