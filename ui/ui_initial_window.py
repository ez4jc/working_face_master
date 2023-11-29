# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_initial_window_new3.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QToolBar, QToolBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(933, 599)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.action_pcdScreen = QAction(MainWindow)
        self.action_pcdScreen.setObjectName(u"action_pcdScreen")
        font = QFont()
        font.setPointSize(14)
        self.action_pcdScreen.setFont(font)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_2.setFont(font)
        self.action12 = QAction(MainWindow)
        self.action12.setObjectName(u"action12")
        font1 = QFont()
        font1.setPointSize(12)
        self.action12.setFont(font1)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_3.setFont(font)
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_4.setFont(font)
        self.about_us_action = QAction(MainWindow)
        self.about_us_action.setObjectName(u"about_us_action")
        self.about_us_action.setFont(font)
        self.action_supportControler = QAction(MainWindow)
        self.action_supportControler.setObjectName(u"action_supportControler")
        self.action_supportControler.setCheckable(False)
        self.action_supportControler.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_control = QWidget(self.widget)
        self.widget_control.setObjectName(u"widget_control")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.widget_control.sizePolicy().hasHeightForWidth())
        self.widget_control.setSizePolicy(sizePolicy2)
        self.verticalLayout_9 = QVBoxLayout(self.widget_control)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.toolBox = QToolBox(self.widget_control)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setFrameShape(QFrame.StyledPanel)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 188, 115))
        self.verticalLayout_17 = QVBoxLayout(self.page_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pushButton_roadwayAndCoalmineSettings = QPushButton(self.page_2)
        self.pushButton_roadwayAndCoalmineSettings.setObjectName(u"pushButton_roadwayAndCoalmineSettings")

        self.verticalLayout_17.addWidget(self.pushButton_roadwayAndCoalmineSettings)

        self.pushButton_coalCutter = QPushButton(self.page_2)
        self.pushButton_coalCutter.setObjectName(u"pushButton_coalCutter")

        self.verticalLayout_17.addWidget(self.pushButton_coalCutter)

        self.pushButton_supporterInit = QPushButton(self.page_2)
        self.pushButton_supporterInit.setObjectName(u"pushButton_supporterInit")

        self.verticalLayout_17.addWidget(self.pushButton_supporterInit)

        self.toolBox.addItem(self.page_2, u"\u573a\u666f\u52a0\u8f7d")
        self.page_pointCloud = QWidget()
        self.page_pointCloud.setObjectName(u"page_pointCloud")
        self.page_pointCloud.setGeometry(QRect(0, 0, 98, 38))
        self.verticalLayout_11 = QVBoxLayout(self.page_pointCloud)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_pointCloudCheckBox = QWidget(self.page_pointCloud)
        self.widget_pointCloudCheckBox.setObjectName(u"widget_pointCloudCheckBox")
        self.verticalLayout_13 = QVBoxLayout(self.widget_pointCloudCheckBox)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_widget_pointCloudCheckBox = QVBoxLayout()
        self.verticalLayout_widget_pointCloudCheckBox.setObjectName(u"verticalLayout_widget_pointCloudCheckBox")

        self.verticalLayout_13.addLayout(self.verticalLayout_widget_pointCloudCheckBox)


        self.verticalLayout_11.addWidget(self.widget_pointCloudCheckBox)

        self.toolBox.addItem(self.page_pointCloud, u"\u70b9\u4e91\u5bf9\u8c61")
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.page_settings.setGeometry(QRect(0, 0, 177, 407))
        self.verticalLayout_14 = QVBoxLayout(self.page_settings)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_planeXZ = QCheckBox(self.page_settings)
        self.checkBox_planeXZ.setObjectName(u"checkBox_planeXZ")

        self.gridLayout_2.addWidget(self.checkBox_planeXZ, 0, 1, 1, 1)

        self.checkBox_planeYZ = QCheckBox(self.page_settings)
        self.checkBox_planeYZ.setObjectName(u"checkBox_planeYZ")

        self.gridLayout_2.addWidget(self.checkBox_planeYZ, 1, 0, 1, 1)

        self.checkBox_planeXY = QCheckBox(self.page_settings)
        self.checkBox_planeXY.setObjectName(u"checkBox_planeXY")

        self.gridLayout_2.addWidget(self.checkBox_planeXY, 0, 0, 1, 1)

        self.label_diffuse = QLabel(self.page_settings)
        self.label_diffuse.setObjectName(u"label_diffuse")
        self.label_diffuse.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_diffuse, 8, 0, 1, 1)

        self.label_ambient = QLabel(self.page_settings)
        self.label_ambient.setObjectName(u"label_ambient")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_ambient.sizePolicy().hasHeightForWidth())
        self.label_ambient.setSizePolicy(sizePolicy3)
        self.label_ambient.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_ambient, 6, 0, 1, 1)

        self.checkBox_axes = QCheckBox(self.page_settings)
        self.checkBox_axes.setObjectName(u"checkBox_axes")

        self.gridLayout_2.addWidget(self.checkBox_axes, 1, 1, 1, 1)

        self.checkBox_highlight_point = QCheckBox(self.page_settings)
        self.checkBox_highlight_point.setObjectName(u"checkBox_highlight_point")

        self.gridLayout_2.addWidget(self.checkBox_highlight_point, 3, 0, 1, 1)

        self.horizontalSlider_ambient = QSlider(self.page_settings)
        self.horizontalSlider_ambient.setObjectName(u"horizontalSlider_ambient")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.horizontalSlider_ambient.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_ambient.setSizePolicy(sizePolicy4)
        self.horizontalSlider_ambient.setValue(30)
        self.horizontalSlider_ambient.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_ambient, 6, 1, 1, 1)

        self.pushButton_add_ply = QPushButton(self.page_settings)
        self.pushButton_add_ply.setObjectName(u"pushButton_add_ply")

        self.gridLayout_2.addWidget(self.pushButton_add_ply, 3, 1, 1, 1)

        self.horizontalSlider_diffuse = QSlider(self.page_settings)
        self.horizontalSlider_diffuse.setObjectName(u"horizontalSlider_diffuse")
        self.horizontalSlider_diffuse.setValue(70)
        self.horizontalSlider_diffuse.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_diffuse, 8, 1, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_2)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)

        self.label_sliderHint = QLabel(self.page_settings)
        self.label_sliderHint.setObjectName(u"label_sliderHint")

        self.verticalLayout_14.addWidget(self.label_sliderHint)

        self.label_2 = QLabel(self.page_settings)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_14.addWidget(self.label_2)

        self.horizontalSlider_viewSpeed = QSlider(self.page_settings)
        self.horizontalSlider_viewSpeed.setObjectName(u"horizontalSlider_viewSpeed")
        self.horizontalSlider_viewSpeed.setValue(50)
        self.horizontalSlider_viewSpeed.setOrientation(Qt.Horizontal)

        self.verticalLayout_14.addWidget(self.horizontalSlider_viewSpeed)

        self.label_3 = QLabel(self.page_settings)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_14.addWidget(self.label_3)

        self.horizontalSlider_flySpeed = QSlider(self.page_settings)
        self.horizontalSlider_flySpeed.setObjectName(u"horizontalSlider_flySpeed")
        self.horizontalSlider_flySpeed.setEnabled(True)
        self.horizontalSlider_flySpeed.setValue(10)
        self.horizontalSlider_flySpeed.setOrientation(Qt.Horizontal)

        self.verticalLayout_14.addWidget(self.horizontalSlider_flySpeed)

        self.groupBox = QGroupBox(self.page_settings)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.radioButton_horizon_rotate = QRadioButton(self.groupBox)
        self.radioButton_horizon_rotate.setObjectName(u"radioButton_horizon_rotate")

        self.verticalLayout_10.addWidget(self.radioButton_horizon_rotate)

        self.radioButton_vertical_rotate = QRadioButton(self.groupBox)
        self.radioButton_vertical_rotate.setObjectName(u"radioButton_vertical_rotate")

        self.verticalLayout_10.addWidget(self.radioButton_vertical_rotate)

        self.radioButton_roll = QRadioButton(self.groupBox)
        self.radioButton_roll.setObjectName(u"radioButton_roll")

        self.verticalLayout_10.addWidget(self.radioButton_roll)

        self.radioButton_unlimited = QRadioButton(self.groupBox)
        self.radioButton_unlimited.setObjectName(u"radioButton_unlimited")
        self.radioButton_unlimited.setChecked(True)

        self.verticalLayout_10.addWidget(self.radioButton_unlimited)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.verticalLayout_10.addLayout(self.verticalLayout_6)


        self.verticalLayout_14.addWidget(self.groupBox)

        self.toolBox.addItem(self.page_settings, u"\u5c5e\u6027\u8bbe\u7f6e")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 216, 144))
        self.verticalLayout_15 = QVBoxLayout(self.page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton_6 = QRadioButton(self.page)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout.addWidget(self.radioButton_6, 2, 1, 1, 1)

        self.radioButton_supporterHead = QRadioButton(self.page)
        self.radioButton_supporterHead.setObjectName(u"radioButton_supporterHead")

        self.gridLayout.addWidget(self.radioButton_supporterHead, 0, 0, 1, 1)

        self.radioButton_7 = QRadioButton(self.page)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout.addWidget(self.radioButton_7, 4, 0, 1, 1)

        self.radioButton_supportertail = QRadioButton(self.page)
        self.radioButton_supportertail.setObjectName(u"radioButton_supportertail")

        self.gridLayout.addWidget(self.radioButton_supportertail, 0, 1, 1, 1)

        self.radioButton_4 = QRadioButton(self.page)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout.addWidget(self.radioButton_4, 1, 1, 1, 1)

        self.radioButton_3 = QRadioButton(self.page)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout.addWidget(self.radioButton_3, 1, 0, 1, 1)

        self.radioButton_5 = QRadioButton(self.page)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout.addWidget(self.radioButton_5, 2, 0, 1, 1)

        self.radioButton_8 = QRadioButton(self.page)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout.addWidget(self.radioButton_8, 4, 1, 1, 1)

        self.radioButton_9 = QRadioButton(self.page)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout.addWidget(self.radioButton_9, 5, 0, 1, 1)

        self.radioButton_10 = QRadioButton(self.page)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.gridLayout.addWidget(self.radioButton_10, 5, 1, 1, 1)


        self.verticalLayout_15.addLayout(self.gridLayout)

        self.toolBox.addItem(self.page, u"\u89c6\u89d2\u9009\u62e9")

        self.verticalLayout_9.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.widget_control)

        self.widget_alarm = QWidget(self.widget)
        self.widget_alarm.setObjectName(u"widget_alarm")
        sizePolicy2.setHeightForWidth(self.widget_alarm.sizePolicy().hasHeightForWidth())
        self.widget_alarm.setSizePolicy(sizePolicy2)
        self.verticalLayout_8 = QVBoxLayout(self.widget_alarm)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_getCameraPosition = QPushButton(self.widget_alarm)
        self.pushButton_getCameraPosition.setObjectName(u"pushButton_getCameraPosition")
        self.pushButton_getCameraPosition.setEnabled(False)

        self.verticalLayout_7.addWidget(self.pushButton_getCameraPosition)

        self.label = QLabel(self.widget_alarm)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.verticalLayout_2.addWidget(self.widget_alarm)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(3)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_view = QWidget(self.widget_2)
        self.widget_view.setObjectName(u"widget_view")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(5)
        sizePolicy6.setHeightForWidth(self.widget_view.sizePolicy().hasHeightForWidth())
        self.widget_view.setSizePolicy(sizePolicy6)
        self.verticalLayout_16 = QVBoxLayout(self.widget_view)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.view_layout = QVBoxLayout()
        self.view_layout.setObjectName(u"view_layout")

        self.verticalLayout_16.addLayout(self.view_layout)


        self.verticalLayout_4.addWidget(self.widget_view)

        self.widget_switchList = QWidget(self.widget_2)
        self.widget_switchList.setObjectName(u"widget_switchList")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.widget_switchList.sizePolicy().hasHeightForWidth())
        self.widget_switchList.setSizePolicy(sizePolicy7)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_switchList)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_dianyun = QRadioButton(self.widget_switchList)
        self.radioButton_dianyun.setObjectName(u"radioButton_dianyun")

        self.horizontalLayout_3.addWidget(self.radioButton_dianyun)

        self.radioButton_jiankong = QRadioButton(self.widget_switchList)
        self.radioButton_jiankong.setObjectName(u"radioButton_jiankong")

        self.horizontalLayout_3.addWidget(self.radioButton_jiankong)

        self.radioButton_clear = QRadioButton(self.widget_switchList)
        self.radioButton_clear.setObjectName(u"radioButton_clear")

        self.horizontalLayout_3.addWidget(self.radioButton_clear)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.widget_switchList)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 933, 31))
        self.menubar.setFont(font)
        self.menu_1 = QMenu(self.menubar)
        self.menu_1.setObjectName(u"menu_1")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setFont(font)
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.top_tool_bar = QToolBar(MainWindow)
        self.top_tool_bar.setObjectName(u"top_tool_bar")
        sizePolicy4.setHeightForWidth(self.top_tool_bar.sizePolicy().hasHeightForWidth())
        self.top_tool_bar.setSizePolicy(sizePolicy4)
        self.top_tool_bar.setMinimumSize(QSize(0, 0))
        self.top_tool_bar.setMaximumSize(QSize(1920, 100))
        self.top_tool_bar.setIconSize(QSize(100, 100))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.top_tool_bar)

        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu_1.addAction(self.action_pcdScreen)
        self.menu_1.addAction(self.action_2)
        self.menu_2.addAction(self.about_us_action)
        self.menu_3.addAction(self.action_supportControler)
        self.top_tool_bar.addSeparator()

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e3b\u7a97\u4f53", None))
        self.action_pcdScreen.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u4e91\u5c4f", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u76d1\u63a7\u5c4f", None))
        self.action12.setText(QCoreApplication.translate("MainWindow", u"\u83dc\u5355\u8bbe\u7f6e", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u8bbe\u7f6e", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\u8bbe\u7f6e", None))
        self.about_us_action.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_supportControler.setText(QCoreApplication.translate("MainWindow", u"\u652f\u6491\u67b6\u63a7\u5236", None))
        self.pushButton_roadwayAndCoalmineSettings.setText(QCoreApplication.translate("MainWindow", u"\u5df7\u9053\u7164\u5ca9\u5c42\u8bbe\u7f6e", None))
        self.pushButton_coalCutter.setText(QCoreApplication.translate("MainWindow", u"\u5272\u7164\u673a\u52a0\u8f7d", None))
        self.pushButton_supporterInit.setText(QCoreApplication.translate("MainWindow", u"\u652f\u6491\u67b6\u521d\u59cb\u5316", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u573a\u666f\u52a0\u8f7d", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_pointCloud), QCoreApplication.translate("MainWindow", u"\u70b9\u4e91\u5bf9\u8c61", None))
        self.checkBox_planeXZ.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u683c\u7ebfXZ", None))
        self.checkBox_planeYZ.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u683c\u7ebfYZ", None))
        self.checkBox_planeXY.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u683c\u7ebfXY", None))
        self.label_diffuse.setText(QCoreApplication.translate("MainWindow", u"\u6f2b\u53cd\u5c04", None))
        self.label_ambient.setText(QCoreApplication.translate("MainWindow", u"\u4eae\u5ea6", None))
        self.checkBox_axes.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807\u8f74", None))
        self.checkBox_highlight_point.setText(QCoreApplication.translate("MainWindow", u"\u7a81\u51fa\u70b9", None))
        self.pushButton_add_ply.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label_sliderHint.setText(QCoreApplication.translate("MainWindow", u"\uff08\u5efa\u8bae\u4eae\u5ea6\u503c\u4f4e\u4e8e\u6f2b\u53cd\u5c04\u503c\uff09", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6eda\u8f6e\u7f29\u653e\u901f\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.horizontalSlider_viewSpeed.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6444\u50cf\u5934\u901f\u5ea6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6f2b\u6e38\u901f\u5ea6", None))
#if QT_CONFIG(tooltip)
        self.horizontalSlider_flySpeed.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6f2b\u6e38\u901f\u5ea6</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.horizontalSlider_flySpeed.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u53d7\u9650\u65cb\u8f6c", None))
        self.radioButton_horizon_rotate.setText(QCoreApplication.translate("MainWindow", u"\u4ec5\u6a2a\u5411", None))
        self.radioButton_vertical_rotate.setText(QCoreApplication.translate("MainWindow", u"\u4ec5\u7ad6\u5411", None))
        self.radioButton_roll.setText(QCoreApplication.translate("MainWindow", u"\u6a2a\u6eda", None))
        self.radioButton_unlimited.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u9650\u5236", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_settings), QCoreApplication.translate("MainWindow", u"\u5c5e\u6027\u8bbe\u7f6e", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"\u7164\u5c42\u53f3\u89c6\u89d2", None))
        self.radioButton_supporterHead.setText(QCoreApplication.translate("MainWindow", u"\u652f\u6491\u67b6\u5934\u89c6\u89d2", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"\u7164\u5c42\u4fef\u89c6", None))
        self.radioButton_supportertail.setText(QCoreApplication.translate("MainWindow", u"\u652f\u6491\u67b6\u5c3e\u89c6\u89d2", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5272\u7164\u673a\u5c3e\u89c6\u89d2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5272\u7164\u673a\u5934\u89c6\u89d2", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"\u7164\u5c42\u5de6\u89c6\u89d2", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"\u7164\u5c42\u5e95\u90e8", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"\u901a\u98ce\u5df7\u89c6\u89d2", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u8f93\u5df7\u89c6\u89d2", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u89c6\u89d2\u9009\u62e9", None))
        self.pushButton_getCameraPosition.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u70b9\u4e91\u6444\u50cf\u5934\u4fe1\u606f\uff08\u5f00\u53d1\u4f7f\u7528\uff09", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9884\u8b66\u5217\u8868", None))
        self.radioButton_dianyun.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u4e91\u56fe\u50cf", None))
        self.radioButton_jiankong.setText(QCoreApplication.translate("MainWindow", u"\u76d1\u63a7\u56fe\u50cf", None))
        self.radioButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u663e\u793a\u56fe\u50cf", None))
        self.menu_1.setTitle(QCoreApplication.translate("MainWindow", u"\u5c4f\u5e55\u663e\u793a", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe\u8bbe\u7f6e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u4eff\u771f\u9762\u677f", None))
        self.top_tool_bar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

