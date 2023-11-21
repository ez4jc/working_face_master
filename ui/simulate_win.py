# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulate_win.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_simulate_win(object):
    def setupUi(self, simulate_win):
        if not simulate_win.objectName():
            simulate_win.setObjectName(u"simulate_win")
        simulate_win.resize(400, 300)
        self.gridLayout = QGridLayout(simulate_win)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_supporter = QComboBox(simulate_win)
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.addItem("")
        self.comboBox_supporter.setObjectName(u"comboBox_supporter")

        self.gridLayout.addWidget(self.comboBox_supporter, 0, 0, 1, 1)

        self.lineEdit_pushSupporter = QLineEdit(simulate_win)
        self.lineEdit_pushSupporter.setObjectName(u"lineEdit_pushSupporter")
        self.lineEdit_pushSupporter.setMaxLength(5)
        self.lineEdit_pushSupporter.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_pushSupporter, 1, 0, 1, 1)

        self.checkBox_wraparound_frame = QCheckBox(simulate_win)
        self.checkBox_wraparound_frame.setObjectName(u"checkBox_wraparound_frame")
        self.checkBox_wraparound_frame.setChecked(False)
        self.checkBox_wraparound_frame.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_wraparound_frame, 0, 1, 1, 1)

        self.pushButton_pushSupport = QPushButton(simulate_win)
        self.pushButton_pushSupport.setObjectName(u"pushButton_pushSupport")

        self.gridLayout.addWidget(self.pushButton_pushSupport, 1, 1, 1, 1)


        self.retranslateUi(simulate_win)

        self.comboBox_supporter.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(simulate_win)
    # setupUi

    def retranslateUi(self, simulate_win):
        simulate_win.setWindowTitle(QCoreApplication.translate("simulate_win", u"\u4eff\u771f\u9762\u677f", None))
        self.comboBox_supporter.setItemText(0, QCoreApplication.translate("simulate_win", u"1\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(1, QCoreApplication.translate("simulate_win", u"2\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(2, QCoreApplication.translate("simulate_win", u"3\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(3, QCoreApplication.translate("simulate_win", u"4\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(4, QCoreApplication.translate("simulate_win", u"5\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(5, QCoreApplication.translate("simulate_win", u"6\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(6, QCoreApplication.translate("simulate_win", u"7\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(7, QCoreApplication.translate("simulate_win", u"8\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(8, QCoreApplication.translate("simulate_win", u"9\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(9, QCoreApplication.translate("simulate_win", u"10\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(10, QCoreApplication.translate("simulate_win", u"11\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(11, QCoreApplication.translate("simulate_win", u"12\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(12, QCoreApplication.translate("simulate_win", u"13\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(13, QCoreApplication.translate("simulate_win", u"14\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(14, QCoreApplication.translate("simulate_win", u"15\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(15, QCoreApplication.translate("simulate_win", u"16\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(16, QCoreApplication.translate("simulate_win", u"17\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(17, QCoreApplication.translate("simulate_win", u"18\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(18, QCoreApplication.translate("simulate_win", u"19\u53f7\u652f\u6491\u67b6", None))
        self.comboBox_supporter.setItemText(19, QCoreApplication.translate("simulate_win", u"20\u53f7\u652f\u6491\u67b6", None))

        self.lineEdit_pushSupporter.setText(QCoreApplication.translate("simulate_win", u"800", None))
        self.lineEdit_pushSupporter.setPlaceholderText(QCoreApplication.translate("simulate_win", u"\u79fb\u52a8\u8ddd\u79bb\uff08\u5355\u4f4d\uff1a\u6beb\u7c73\uff09", None))
        self.checkBox_wraparound_frame.setText(QCoreApplication.translate("simulate_win", u"\u5305\u56f4\u6846", None))
        self.pushButton_pushSupport.setText(QCoreApplication.translate("simulate_win", u"\u63a8\u652f\u6491\u67b6", None))
    # retranslateUi

