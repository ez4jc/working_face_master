from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from ui.simulate_win import Ui_simulate_win


class SubWinSupport(QtWidgets.QWidget, Ui_simulate_win):
    def __init__(self, vtkWidget):
        super().__init__()
        self.setupUi(self)

        self.vtkWidget = vtkWidget

        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        self.bind()

    def bind(self):
        self.comboBox_supporter.currentIndexChanged.connect(self.update_selected_supporter)
        # 绑定初始支撑架，和控制按钮
        self.pushButton_pushSupport.clicked.connect(
            lambda: self.vtkWidget.move_actor(self.vtkWidget.supporter_actors[0],
                                              float(self.lineEdit_pushSupporter.text())))
        self.checkBox_supporter_model.clicked.connect(self.vtkWidget.supporter_actors[0].show_model)
        self.checkBox_label.clicked.connect(self.vtkWidget.supporter_actors[0].show_label)
        self.checkBox_wraparound_frame.clicked.connect(
            self.vtkWidget.supporter_actors[0].show_wraparound_frame)
        self.checkBox_static_wraparound_frame.clicked.connect(
            self.vtkWidget.supporter_actors[0].show_static_wraparound_frame)

    def update_selected_supporter(self):
        # 断开槽函数，控件回默认值
        self.pushButton_pushSupport.clicked.disconnect()
        self.checkBox_supporter_model.clicked.disconnect()
        self.checkBox_label.clicked.disconnect()
        self.checkBox_wraparound_frame.clicked.disconnect()
        self.checkBox_static_wraparound_frame.clicked.disconnect()

        # 同步控件和支撑架的状态，保证一致性
        self.checkBox_supporter_model.setChecked(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].model_flag)
        self.checkBox_label.setChecked(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].label_flag)
        self.checkBox_wraparound_frame.setChecked(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].wraparound_actor_flag)
        self.checkBox_static_wraparound_frame.setChecked(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].static_wraparound_actor_flag)

        # 重新绑定支撑架和相应所有按钮
        self.pushButton_pushSupport.clicked.connect(
            lambda: self.vtkWidget.move_actor(
                self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()],
                float(self.lineEdit_pushSupporter.text())))
        self.checkBox_supporter_model.clicked.connect(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].show_model)
        self.checkBox_label.clicked.connect(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].show_label)
        self.checkBox_wraparound_frame.clicked.connect(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].show_wraparound_frame)
        self.checkBox_static_wraparound_frame.clicked.connect(
            self.vtkWidget.supporter_actors[self.comboBox_supporter.currentIndex()].show_static_wraparound_frame)
