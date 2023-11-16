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
        # 绑定初始支撑架
        self.pushButton_pushSupport.clicked.connect(
            lambda: self.vtkWidget.move_actor(self.vtkWidget.point_cloud_actors[0],
                                              float(self.lineEdit_pushSupporter.text())))

    def update_selected_supporter(self):
        self.pushButton_pushSupport.clicked.disconnect()
        # 重新绑定支撑架
        self.pushButton_pushSupport.clicked.connect(
            lambda: self.vtkWidget.move_actor(
                self.vtkWidget.point_cloud_actors[self.comboBox_supporter.currentIndex()],
                float(self.lineEdit_pushSupporter.text())))
