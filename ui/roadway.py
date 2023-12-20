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
        RoadwayWin.resize(601, 468)
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
        self.spinBox_ez1 = QSpinBox(self.groupBox_2)
        self.spinBox_ez1.setObjectName(u"spinBox_ez1")
        self.spinBox_ez1.setMinimum(-10000)
        self.spinBox_ez1.setMaximum(10000)

        self.gridLayout.addWidget(self.spinBox_ez1, 2, 1, 1, 1)

        self.spinBox_ey1 = QSpinBox(self.groupBox_2)
        self.spinBox_ey1.setObjectName(u"spinBox_ey1")
        self.spinBox_ey1.setMinimum(-10000)
        self.spinBox_ey1.setMaximum(10000)
        self.spinBox_ey1.setValue(20)

        self.gridLayout.addWidget(self.spinBox_ey1, 1, 1, 1, 1)

        self.spinBox_ex1 = QSpinBox(self.groupBox_2)
        self.spinBox_ex1.setObjectName(u"spinBox_ex1")
        self.spinBox_ex1.setEnabled(True)
        self.spinBox_ex1.setMinimum(-10000)
        self.spinBox_ex1.setMaximum(10000)
        self.spinBox_ex1.setValue(0)

        self.gridLayout.addWidget(self.spinBox_ex1, 0, 1, 1, 1)

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
        self.spinBox_sz1 = QSpinBox(self.groupBox)
        self.spinBox_sz1.setObjectName(u"spinBox_sz1")
        self.spinBox_sz1.setEnabled(True)
        self.spinBox_sz1.setMinimum(-10000)
        self.spinBox_sz1.setMaximum(10000)

        self.gridLayout_2.addWidget(self.spinBox_sz1, 2, 1, 1, 1)

        self.spinBox_sy1 = QSpinBox(self.groupBox)
        self.spinBox_sy1.setObjectName(u"spinBox_sy1")
        self.spinBox_sy1.setEnabled(True)
        self.spinBox_sy1.setMinimum(-10000)
        self.spinBox_sy1.setMaximum(10000)

        self.gridLayout_2.addWidget(self.spinBox_sy1, 1, 1, 1, 1)

        self.spinBox_sx1 = QSpinBox(self.groupBox)
        self.spinBox_sx1.setObjectName(u"spinBox_sx1")
        self.spinBox_sx1.setEnabled(True)
        self.spinBox_sx1.setMinimum(-10000)
        self.spinBox_sx1.setMaximum(10000)

        self.gridLayout_2.addWidget(self.spinBox_sx1, 0, 1, 1, 1)

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
        self.spinBox_ey2 = QSpinBox(self.groupBox_3)
        self.spinBox_ey2.setObjectName(u"spinBox_ey2")
        self.spinBox_ey2.setEnabled(True)
        self.spinBox_ey2.setMinimum(-10000)
        self.spinBox_ey2.setMaximum(10000)
        self.spinBox_ey2.setValue(20)

        self.gridLayout_3.addWidget(self.spinBox_ey2, 1, 1, 1, 1)

        self.spinBox_ex2 = QSpinBox(self.groupBox_3)
        self.spinBox_ex2.setObjectName(u"spinBox_ex2")
        self.spinBox_ex2.setEnabled(True)
        self.spinBox_ex2.setMinimum(-10000)
        self.spinBox_ex2.setMaximum(10000)
        self.spinBox_ex2.setValue(40)

        self.gridLayout_3.addWidget(self.spinBox_ex2, 0, 1, 1, 1)

        self.spinBox_ez2 = QSpinBox(self.groupBox_3)
        self.spinBox_ez2.setObjectName(u"spinBox_ez2")
        self.spinBox_ez2.setEnabled(True)
        self.spinBox_ez2.setMinimum(-10000)
        self.spinBox_ez2.setMaximum(10000)

        self.gridLayout_3.addWidget(self.spinBox_ez2, 2, 1, 1, 1)

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
        self.spinBox_sx2 = QSpinBox(self.groupBox_4)
        self.spinBox_sx2.setObjectName(u"spinBox_sx2")
        self.spinBox_sx2.setEnabled(True)
        self.spinBox_sx2.setMinimum(-10000)
        self.spinBox_sx2.setMaximum(10000)
        self.spinBox_sx2.setValue(40)

        self.gridLayout_4.addWidget(self.spinBox_sx2, 0, 1, 1, 1)

        self.spinBox_sy2 = QSpinBox(self.groupBox_4)
        self.spinBox_sy2.setObjectName(u"spinBox_sy2")
        self.spinBox_sy2.setEnabled(True)
        self.spinBox_sy2.setMinimum(-10000)
        self.spinBox_sy2.setMaximum(10000)

        self.gridLayout_4.addWidget(self.spinBox_sy2, 1, 1, 1, 1)

        self.spinBox_sz2 = QSpinBox(self.groupBox_4)
        self.spinBox_sz2.setObjectName(u"spinBox_sz2")
        self.spinBox_sz2.setEnabled(True)
        self.spinBox_sz2.setMinimum(-10000)
        self.spinBox_sz2.setMaximum(10000)

        self.gridLayout_4.addWidget(self.spinBox_sz2, 2, 1, 1, 1)

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
        self.spinBox_transportAlley_height.setEnabled(True)
        self.spinBox_transportAlley_height.setValue(3)

        self.horizontalLayout_4.addWidget(self.spinBox_transportAlley_height)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_8 = QFrame(RoadwayWin)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_19)

        self.groupBox_5 = QGroupBox(self.frame_8)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.spinBox_ey3 = QSpinBox(self.groupBox_5)
        self.spinBox_ey3.setObjectName(u"spinBox_ey3")
        self.spinBox_ey3.setEnabled(True)
        self.spinBox_ey3.setMinimum(-10000)
        self.spinBox_ey3.setMaximum(10000)
        self.spinBox_ey3.setValue(0)

        self.gridLayout_5.addWidget(self.spinBox_ey3, 1, 1, 1, 1)

        self.spinBox_ex3 = QSpinBox(self.groupBox_5)
        self.spinBox_ex3.setObjectName(u"spinBox_ex3")
        self.spinBox_ex3.setEnabled(True)
        self.spinBox_ex3.setMinimum(-10000)
        self.spinBox_ex3.setMaximum(10000)
        self.spinBox_ex3.setValue(40)

        self.gridLayout_5.addWidget(self.spinBox_ex3, 0, 1, 1, 1)

        self.spinBox_ez3 = QSpinBox(self.groupBox_5)
        self.spinBox_ez3.setObjectName(u"spinBox_ez3")
        self.spinBox_ez3.setEnabled(True)
        self.spinBox_ez3.setMinimum(-10000)
        self.spinBox_ez3.setMaximum(10000)

        self.gridLayout_5.addWidget(self.spinBox_ez3, 2, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_22, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.frame_8)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.spinBox_sx3 = QSpinBox(self.groupBox_6)
        self.spinBox_sx3.setObjectName(u"spinBox_sx3")
        self.spinBox_sx3.setEnabled(True)
        self.spinBox_sx3.setMinimum(-10000)
        self.spinBox_sx3.setMaximum(10000)
        self.spinBox_sx3.setValue(0)

        self.gridLayout_6.addWidget(self.spinBox_sx3, 0, 1, 1, 1)

        self.spinBox_sy3 = QSpinBox(self.groupBox_6)
        self.spinBox_sy3.setObjectName(u"spinBox_sy3")
        self.spinBox_sy3.setEnabled(True)
        self.spinBox_sy3.setMinimum(-10000)
        self.spinBox_sy3.setMaximum(10000)

        self.gridLayout_6.addWidget(self.spinBox_sy3, 1, 1, 1, 1)

        self.spinBox_sz3 = QSpinBox(self.groupBox_6)
        self.spinBox_sz3.setObjectName(u"spinBox_sz3")
        self.spinBox_sz3.setEnabled(True)
        self.spinBox_sz3.setMinimum(-10000)
        self.spinBox_sz3.setMaximum(10000)

        self.gridLayout_6.addWidget(self.spinBox_sz3, 2, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_24 = QLabel(self.groupBox_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_24, 1, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_25, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_6)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_26 = QLabel(self.frame_9)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_26)

        self.spinBox_transportAlley_width_2 = QSpinBox(self.frame_9)
        self.spinBox_transportAlley_width_2.setObjectName(u"spinBox_transportAlley_width_2")
        self.spinBox_transportAlley_width_2.setValue(3)

        self.horizontalLayout_6.addWidget(self.spinBox_transportAlley_width_2)


        self.verticalLayout.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_27 = QLabel(self.frame_10)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_27)

        self.spinBox_transportAlley_height_2 = QSpinBox(self.frame_10)
        self.spinBox_transportAlley_height_2.setObjectName(u"spinBox_transportAlley_height_2")
        self.spinBox_transportAlley_height_2.setEnabled(True)
        self.spinBox_transportAlley_height_2.setValue(3)

        self.horizontalLayout_7.addWidget(self.spinBox_transportAlley_height_2)


        self.verticalLayout.addWidget(self.frame_10)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.frame_7 = QFrame(RoadwayWin)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_generate_roadway = QPushButton(self.frame_7)
        self.pushButton_generate_roadway.setObjectName(u"pushButton_generate_roadway")

        self.verticalLayout_7.addWidget(self.pushButton_generate_roadway)


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
        self.label_19.setText(QCoreApplication.translate("RoadwayWin", u"\u8fd0\u8f93\u5df7", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("RoadwayWin", u"\u7ec8\u70b9\u5750\u6807\uff1a", None))
        self.label_20.setText(QCoreApplication.translate("RoadwayWin", u"X", None))
        self.label_21.setText(QCoreApplication.translate("RoadwayWin", u"Y", None))
        self.label_22.setText(QCoreApplication.translate("RoadwayWin", u"Z", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("RoadwayWin", u"\u8d77\u59cb\u70b9\u5750\u6807\uff1a", None))
        self.label_23.setText(QCoreApplication.translate("RoadwayWin", u"X", None))
        self.label_24.setText(QCoreApplication.translate("RoadwayWin", u"Y", None))
        self.label_25.setText(QCoreApplication.translate("RoadwayWin", u"Z", None))
        self.label_26.setText(QCoreApplication.translate("RoadwayWin", u"\u5bbd\uff1a", None))
        self.label_27.setText(QCoreApplication.translate("RoadwayWin", u"\u9ad8\uff1a", None))
        self.pushButton_generate_roadway.setText(QCoreApplication.translate("RoadwayWin", u"\u751f\u6210\u5df7\u9053\uff08\u9700\u6e05\u7a7a\u5f53\u524d\u751f\u6210\uff09", None))
    # retranslateUi

