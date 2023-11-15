# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'initial_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QRadioButton, QSizePolicy, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(839, 605)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        font = QFont()
        font.setPointSize(14)
        self.action.setFont(font)
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
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.widget_control.sizePolicy().hasHeightForWidth())
        self.widget_control.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.widget_control)

        self.widget_alarm = QWidget(self.widget)
        self.widget_alarm.setObjectName(u"widget_alarm")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.widget_alarm.sizePolicy().hasHeightForWidth())
        self.widget_alarm.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.widget_alarm)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(4)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_view = QWidget(self.widget_2)
        self.widget_view.setObjectName(u"widget_view")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(5)
        sizePolicy5.setHeightForWidth(self.widget_view.sizePolicy().hasHeightForWidth())
        self.widget_view.setSizePolicy(sizePolicy5)

        self.verticalLayout_4.addWidget(self.widget_view)

        self.widget_switchList = QWidget(self.widget_2)
        self.widget_switchList.setObjectName(u"widget_switchList")
        sizePolicy2.setHeightForWidth(self.widget_switchList.sizePolicy().hasHeightForWidth())
        self.widget_switchList.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_switchList)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_2 = QRadioButton(self.widget_switchList)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_3.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.widget_switchList)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_3.addWidget(self.radioButton)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.widget_switchList)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 839, 31))
        self.menubar.setFont(font)
        self.menu_1 = QMenu(self.menubar)
        self.menu_1.setObjectName(u"menu_1")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setFont(font)
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.top_tool_bar = QToolBar(MainWindow)
        self.top_tool_bar.setObjectName(u"top_tool_bar")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.top_tool_bar.sizePolicy().hasHeightForWidth())
        self.top_tool_bar.setSizePolicy(sizePolicy6)
        self.top_tool_bar.setMinimumSize(QSize(0, 0))
        self.top_tool_bar.setMaximumSize(QSize(1920, 100))
        self.top_tool_bar.setIconSize(QSize(100, 100))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.top_tool_bar)

        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu_1.addAction(self.action)
        self.menu_1.addAction(self.action_2)
        self.menu_2.addAction(self.about_us_action)
        self.top_tool_bar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e3b\u7a97\u4f53", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u4e91\u5c4f", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u76d1\u63a7\u5c4f", None))
        self.action12.setText(QCoreApplication.translate("MainWindow", u"\u83dc\u5355\u8bbe\u7f6e", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u8bbe\u7f6e", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\u8bbe\u7f6e", None))
        self.about_us_action.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u4e91\u56fe\u50cf", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u76d1\u63a7\u56fe\u50cf", None))
        self.menu_1.setTitle(QCoreApplication.translate("MainWindow", u"\u5c4f\u5e55\u663e\u793a", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe\u8bbe\u7f6e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.top_tool_bar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

