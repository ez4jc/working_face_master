# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'roadway.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_RoadwayWin(object):
    def setupUi(self, RoadwayWin):
        if not RoadwayWin.objectName():
            RoadwayWin.setObjectName(u"RoadwayWin")
        RoadwayWin.resize(547, 468)
        self.horizontalLayout_5 = QHBoxLayout(RoadwayWin)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_3 = QFrame(RoadwayWin)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_ventilationShaft_z = QSpinBox(self.groupBox_2)
        self.spinBox_ventilationShaft_z.setObjectName(u"spinBox_ventilationShaft_z")

        self.gridLayout.addWidget(self.spinBox_ventilationShaft_z, 2, 1, 1, 1)

        self.spinBox_ventilationShaft_y = QSpinBox(self.groupBox_2)
        self.spinBox_ventilationShaft_y.setObjectName(u"spinBox_ventilationShaft_y")
        self.spinBox_ventilationShaft_y.setValue(20)

        self.gridLayout.addWidget(self.spinBox_ventilationShaft_y, 1, 1, 1, 1)

        self.spinBox_ventilationShaft_x = QSpinBox(self.groupBox_2)
        self.spinBox_ventilationShaft_x.setObjectName(u"spinBox_ventilationShaft_x")
        self.spinBox_ventilationShaft_x.setEnabled(False)
        self.spinBox_ventilationShaft_x.setMaximum(5)
        self.spinBox_ventilationShaft_x.setValue(0)

        self.gridLayout.addWidget(self.spinBox_ventilationShaft_x, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setEnabled(False)

        self.gridLayout_2.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setEnabled(False)

        self.gridLayout_2.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.spinBox, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.spinBox_ventilationShaft_width = QSpinBox(self.frame_2)
        self.spinBox_ventilationShaft_width.setObjectName(u"spinBox_ventilationShaft_width")
        self.spinBox_ventilationShaft_width.setValue(3)

        self.horizontalLayout_2.addWidget(self.spinBox_ventilationShaft_width)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.spinBox_ventilationShaft_height = QSpinBox(self.frame)
        self.spinBox_ventilationShaft_height.setObjectName(u"spinBox_ventilationShaft_height")
        self.spinBox_ventilationShaft_height.setValue(3)

        self.horizontalLayout.addWidget(self.spinBox_ventilationShaft_height)


        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(RoadwayWin)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.groupBox_3 = QGroupBox(self.frame_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.spinBox_transportAlley_y = QSpinBox(self.groupBox_3)
        self.spinBox_transportAlley_y.setObjectName(u"spinBox_transportAlley_y")
        self.spinBox_transportAlley_y.setValue(20)

        self.gridLayout_3.addWidget(self.spinBox_transportAlley_y, 1, 1, 1, 1)

        self.spinBox_transportAlley_x = QSpinBox(self.groupBox_3)
        self.spinBox_transportAlley_x.setObjectName(u"spinBox_transportAlley_x")
        self.spinBox_transportAlley_x.setEnabled(False)
        self.spinBox_transportAlley_x.setMinimum(35)
        self.spinBox_transportAlley_x.setMaximum(40)
        self.spinBox_transportAlley_x.setValue(40)

        self.gridLayout_3.addWidget(self.spinBox_transportAlley_x, 0, 1, 1, 1)

        self.spinBox_transportAlley_z = QSpinBox(self.groupBox_3)
        self.spinBox_transportAlley_z.setObjectName(u"spinBox_transportAlley_z")
        self.spinBox_transportAlley_z.setEnabled(False)

        self.gridLayout_3.addWidget(self.spinBox_transportAlley_z, 2, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_15, 2, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.spinBox_10 = QSpinBox(self.groupBox_4)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setEnabled(False)
        self.spinBox_10.setValue(40)

        self.gridLayout_4.addWidget(self.spinBox_10, 0, 1, 1, 1)

        self.spinBox_11 = QSpinBox(self.groupBox_4)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setEnabled(False)

        self.gridLayout_4.addWidget(self.spinBox_11, 1, 1, 1, 1)

        self.spinBox_12 = QSpinBox(self.groupBox_4)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setEnabled(False)

        self.gridLayout_4.addWidget(self.spinBox_12, 2, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_18, 2, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.spinBox_transportAlley_width = QSpinBox(self.frame_5)
        self.spinBox_transportAlley_width.setObjectName(u"spinBox_transportAlley_width")
        self.spinBox_transportAlley_width.setValue(3)

        self.horizontalLayout_3.addWidget(self.spinBox_transportAlley_width)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.spinBox_transportAlley_height = QSpinBox(self.frame_6)
        self.spinBox_transportAlley_height.setObjectName(u"spinBox_transportAlley_height")
        self.spinBox_transportAlley_height.setEnabled(False)
        self.spinBox_transportAlley_height.setValue(3)

        self.horizontalLayout_4.addWidget(self.spinBox_transportAlley_height)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_7 = QFrame(RoadwayWin)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_generate_roadway = QPushButton(self.frame_7)
        self.pushButton_generate_roadway.setObjectName(u"pushButton_generate_roadway")

        self.verticalLayout_7.addWidget(self.pushButton_generate_roadway)

        self.pushButton_generate_coalmine = QPushButton(self.frame_7)
        self.pushButton_generate_coalmine.setObjectName(u"pushButton_generate_coalmine")
        self.pushButton_generate_coalmine.setEnabled(True)

        self.verticalLayout_7.addWidget(self.pushButton_generate_coalmine)

        self.pushButton_clear_workplace = QPushButton(self.frame_7)
        self.pushButton_clear_workplace.setObjectName(u"pushButton_clear_workplace")
        self.pushButton_clear_workplace.setEnabled(False)

        self.verticalLayout_7.addWidget(self.pushButton_clear_workplace)


        self.horizontalLayout_5.addWidget(self.frame_7)


        self.retranslateUi(RoadwayWin)

        QMetaObject.connectSlotsByName(RoadwayWin)
    # setupUi

    def retranslateUi(self, RoadwayWin):
        RoadwayWin.setWindowTitle(QCoreApplication.translate("RoadwayWin", u"\u5df7\u9053\u63a7\u5236", None))
        self.label.setText(QCoreApplication.translate("RoadwayWin", u"\u901a\u98ce\u5df7", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("RoadwayWin", u"\u7ec8\u70b9\u5750\u6807\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("RoadwayWin", u"X", None))
        self.label_8.setText(QCoreApplication.translate("RoadwayWin", u"Y", None))
        self.label_9.setText(QCoreApplication.translate("RoadwayWin", u"Z", None))
        self.groupBox.setTitle(QCoreApplication.translate("RoadwayWin", u"\u8d77\u59cb\u70b9\u5750\u6807\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("RoadwayWin", u"X", None))
        self.label_11.setText(QCoreApplication.translate("RoadwayWin", u"Y", None))
        self.label_12.setText(QCoreApplication.translate("RoadwayWin", u"Z", None))
        self.label_5.setText(QCoreApplication.translate("RoadwayWin", u"\u5bbd\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("RoadwayWin", u"\u9ad8\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("RoadwayWin", u"\u8fd0\u8f93\u5df7", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("RoadwayWin", u"\u7ec8\u70b9\u5750\u6807\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("RoadwayWin", u"X", None))
        self.label_14.setText(QCoreApplication.translate("RoadwayWin", u"Y", None))
        self.label_15.setText(QCoreApplication.translate("RoadwayWin", u"Z", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("RoadwayWin", u"\u8d77\u59cb\u70b9\u5750\u6807\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("RoadwayWin", u"X", None))
        self.label_17.setText(QCoreApplication.translate("RoadwayWin", u"Y", None))
        self.label_18.setText(QCoreApplication.translate("RoadwayWin", u"Z", None))
        self.label_6.setText(QCoreApplication.translate("RoadwayWin", u"\u5bbd\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("RoadwayWin", u"\u9ad8\uff1a", None))
        self.pushButton_generate_roadway.setText(QCoreApplication.translate("RoadwayWin", u"\u751f\u6210\u5df7\u9053\uff08\u9700\u6e05\u7a7a\u5f53\u524d\u751f\u6210\uff09", None))
        self.pushButton_generate_coalmine.setText(QCoreApplication.translate("RoadwayWin", u"\u751f\u6210\u7164\u5c42\uff08\u9700\u5148\u751f\u6210\u5df7\u9053\uff09", None))
        self.pushButton_clear_workplace.setText(QCoreApplication.translate("RoadwayWin", u"\u6e05\u7a7a\u751f\u6210", None))
    # retranslateUi

