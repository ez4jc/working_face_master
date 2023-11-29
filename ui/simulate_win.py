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
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_simulate_win(object):
    def setupUi(self, simulate_win):
        if not simulate_win.objectName():
            simulate_win.setObjectName(u"simulate_win")
        simulate_win.resize(400, 300)
        self.gridLayout = QGridLayout(simulate_win)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_xoy = QLineEdit(simulate_win)
        self.lineEdit_xoy.setObjectName(u"lineEdit_xoy")
        self.lineEdit_xoy.setMaxLength(3)
        self.lineEdit_xoy.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_xoy, 6, 0, 1, 2)

        self.textEdit_2 = QTextEdit(simulate_win)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout.addWidget(self.textEdit_2, 0, 1, 1, 1)

        self.lineEdit_pushSupporter = QLineEdit(simulate_win)
        self.lineEdit_pushSupporter.setObjectName(u"lineEdit_pushSupporter")
        self.lineEdit_pushSupporter.setMaxLength(5)
        self.lineEdit_pushSupporter.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_pushSupporter, 5, 0, 1, 2)

        self.pushButton_pushSupport = QPushButton(simulate_win)
        self.pushButton_pushSupport.setObjectName(u"pushButton_pushSupport")

        self.gridLayout.addWidget(self.pushButton_pushSupport, 5, 3, 1, 1)

        self.pushButton_zox = QPushButton(simulate_win)
        self.pushButton_zox.setObjectName(u"pushButton_zox")

        self.gridLayout.addWidget(self.pushButton_zox, 8, 3, 1, 1)

        self.pushButton_yoz = QPushButton(simulate_win)
        self.pushButton_yoz.setObjectName(u"pushButton_yoz")

        self.gridLayout.addWidget(self.pushButton_yoz, 7, 3, 1, 1)

        self.pushButton_xoy = QPushButton(simulate_win)
        self.pushButton_xoy.setObjectName(u"pushButton_xoy")

        self.gridLayout.addWidget(self.pushButton_xoy, 6, 3, 1, 1)

        self.checkBox_wraparound_frame = QCheckBox(simulate_win)
        self.checkBox_wraparound_frame.setObjectName(u"checkBox_wraparound_frame")
        self.checkBox_wraparound_frame.setChecked(False)
        self.checkBox_wraparound_frame.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_wraparound_frame, 2, 3, 1, 1)

        self.lineEdit_zox = QLineEdit(simulate_win)
        self.lineEdit_zox.setObjectName(u"lineEdit_zox")
        self.lineEdit_zox.setMaxLength(3)
        self.lineEdit_zox.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_zox, 8, 0, 1, 2)

        self.textEdit_3 = QTextEdit(simulate_win)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.gridLayout.addWidget(self.textEdit_3, 0, 3, 1, 1)

        self.textEdit = QTextEdit(simulate_win)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.lineEdit_yoz = QLineEdit(simulate_win)
        self.lineEdit_yoz.setObjectName(u"lineEdit_yoz")
        self.lineEdit_yoz.setMaxLength(3)
        self.lineEdit_yoz.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_yoz, 7, 0, 1, 2)

        self.checkBox_static_wraparound_frame = QCheckBox(simulate_win)
        self.checkBox_static_wraparound_frame.setObjectName(u"checkBox_static_wraparound_frame")

        self.gridLayout.addWidget(self.checkBox_static_wraparound_frame, 3, 3, 1, 1)

        self.checkBox_gyro = QCheckBox(simulate_win)
        self.checkBox_gyro.setObjectName(u"checkBox_gyro")

        self.gridLayout.addWidget(self.checkBox_gyro, 2, 1, 1, 1)

        self.checkBox_static_gyro = QCheckBox(simulate_win)
        self.checkBox_static_gyro.setObjectName(u"checkBox_static_gyro")

        self.gridLayout.addWidget(self.checkBox_static_gyro, 3, 1, 1, 1)

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

        self.gridLayout.addWidget(self.comboBox_supporter, 1, 0, 1, 4)

        self.checkBox_supporter_model = QCheckBox(simulate_win)
        self.checkBox_supporter_model.setObjectName(u"checkBox_supporter_model")
        self.checkBox_supporter_model.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_supporter_model, 2, 0, 1, 1)

        self.checkBox_label = QCheckBox(simulate_win)
        self.checkBox_label.setObjectName(u"checkBox_label")

        self.gridLayout.addWidget(self.checkBox_label, 3, 0, 1, 1)

        self.checkBox_scraper = QCheckBox(simulate_win)
        self.checkBox_scraper.setObjectName(u"checkBox_scraper")
        self.checkBox_scraper.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_scraper, 4, 0, 1, 1)


        self.retranslateUi(simulate_win)

        self.comboBox_supporter.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(simulate_win)
    # setupUi

    def retranslateUi(self, simulate_win):
        simulate_win.setWindowTitle(QCoreApplication.translate("simulate_win", u"\u4eff\u771f\u9762\u677f", None))
        self.lineEdit_xoy.setText(QCoreApplication.translate("simulate_win", u"60", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("simulate_win", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u503e\u659c\u89d2\uff1a</p></body></html>", None))
        self.lineEdit_pushSupporter.setText(QCoreApplication.translate("simulate_win", u"800", None))
        self.lineEdit_pushSupporter.setPlaceholderText(QCoreApplication.translate("simulate_win", u"\u79fb\u52a8\u8ddd\u79bb\uff08\u5355\u4f4d\uff1a\u6beb\u7c73\uff09", None))
        self.pushButton_pushSupport.setText(QCoreApplication.translate("simulate_win", u"\u63a8\u652f\u6491\u67b6", None))
        self.pushButton_zox.setText(QCoreApplication.translate("simulate_win", u"zox\u65cb\u8f6c", None))
        self.pushButton_yoz.setText(QCoreApplication.translate("simulate_win", u"yoz\u65cb\u8f6c", None))
        self.pushButton_xoy.setText(QCoreApplication.translate("simulate_win", u"xoy\u65cb\u8f6c", None))
        self.checkBox_wraparound_frame.setText(QCoreApplication.translate("simulate_win", u"\u5305\u56f4\u6846", None))
        self.lineEdit_zox.setText(QCoreApplication.translate("simulate_win", u"-60", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("simulate_win", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u65cb\u8f6c\u89d2\uff1a</p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("simulate_win", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4fef\u4ef0\u89d2\uff1a</p></body></html>", None))
        self.lineEdit_yoz.setText(QCoreApplication.translate("simulate_win", u"60", None))
        self.checkBox_static_wraparound_frame.setText(QCoreApplication.translate("simulate_win", u"\u7edd\u5bf9\u5305\u56f4\u6846", None))
        self.checkBox_gyro.setText(QCoreApplication.translate("simulate_win", u"\u9640\u87ba\u4eea", None))
        self.checkBox_static_gyro.setText(QCoreApplication.translate("simulate_win", u"\u7edd\u5bf9\u9640\u87ba\u4eea", None))
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

        self.checkBox_supporter_model.setText(QCoreApplication.translate("simulate_win", u"\u6a21\u578b", None))
        self.checkBox_label.setText(QCoreApplication.translate("simulate_win", u"\u6807\u7b7e", None))
        self.checkBox_scraper.setText(QCoreApplication.translate("simulate_win", u"\u522e\u677f\u673a", None))
    # retranslateUi

