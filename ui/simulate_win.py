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
        simulate_win.resize(400, 314)
        self.gridLayout = QGridLayout(simulate_win)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit_2 = QTextEdit(simulate_win)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setAcceptDrops(True)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.textEdit_2, 0, 1, 1, 1)

        self.checkBox_wraparound_frame = QCheckBox(simulate_win)
        self.checkBox_wraparound_frame.setObjectName(u"checkBox_wraparound_frame")
        self.checkBox_wraparound_frame.setChecked(False)
        self.checkBox_wraparound_frame.setTristate(False)

        self.gridLayout.addWidget(self.checkBox_wraparound_frame, 3, 3, 1, 1)

        self.checkBox_supporter_model = QCheckBox(simulate_win)
        self.checkBox_supporter_model.setObjectName(u"checkBox_supporter_model")
        self.checkBox_supporter_model.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_supporter_model, 3, 0, 1, 1)

        self.lineEdit_zox = QLineEdit(simulate_win)
        self.lineEdit_zox.setObjectName(u"lineEdit_zox")
        self.lineEdit_zox.setMaxLength(3)
        self.lineEdit_zox.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_zox, 9, 0, 1, 2)

        self.checkBox_label = QCheckBox(simulate_win)
        self.checkBox_label.setObjectName(u"checkBox_label")

        self.gridLayout.addWidget(self.checkBox_label, 4, 0, 1, 1)

        self.pushButton_xoy = QPushButton(simulate_win)
        self.pushButton_xoy.setObjectName(u"pushButton_xoy")

        self.gridLayout.addWidget(self.pushButton_xoy, 7, 3, 1, 1)

        self.checkBox_scraper = QCheckBox(simulate_win)
        self.checkBox_scraper.setObjectName(u"checkBox_scraper")
        self.checkBox_scraper.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_scraper, 10, 0, 1, 1)

        self.pushButton_zox = QPushButton(simulate_win)
        self.pushButton_zox.setObjectName(u"pushButton_zox")

        self.gridLayout.addWidget(self.pushButton_zox, 9, 3, 1, 1)

        self.pushButton_pushScraper = QPushButton(simulate_win)
        self.pushButton_pushScraper.setObjectName(u"pushButton_pushScraper")

        self.gridLayout.addWidget(self.pushButton_pushScraper, 11, 3, 1, 1)

        self.checkBox_static_wraparound_frame = QCheckBox(simulate_win)
        self.checkBox_static_wraparound_frame.setObjectName(u"checkBox_static_wraparound_frame")

        self.gridLayout.addWidget(self.checkBox_static_wraparound_frame, 4, 3, 1, 1)

        self.textEdit_1 = QTextEdit(simulate_win)
        self.textEdit_1.setObjectName(u"textEdit_1")
        self.textEdit_1.setAcceptDrops(True)
        self.textEdit_1.setReadOnly(True)
        self.textEdit_1.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.textEdit_1, 0, 0, 1, 1)

        self.lineEdit_yoz = QLineEdit(simulate_win)
        self.lineEdit_yoz.setObjectName(u"lineEdit_yoz")
        self.lineEdit_yoz.setMaxLength(3)
        self.lineEdit_yoz.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_yoz, 8, 0, 1, 2)

        self.lineEdit_xoy = QLineEdit(simulate_win)
        self.lineEdit_xoy.setObjectName(u"lineEdit_xoy")
        self.lineEdit_xoy.setMaxLength(3)
        self.lineEdit_xoy.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_xoy, 7, 0, 1, 2)

        self.checkBox_gyro = QCheckBox(simulate_win)
        self.checkBox_gyro.setObjectName(u"checkBox_gyro")

        self.gridLayout.addWidget(self.checkBox_gyro, 3, 1, 1, 1)

        self.lineEdit_pushScraper = QLineEdit(simulate_win)
        self.lineEdit_pushScraper.setObjectName(u"lineEdit_pushScraper")
        self.lineEdit_pushScraper.setMaxLength(5)
        self.lineEdit_pushScraper.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit_pushScraper, 11, 0, 1, 2)

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

        self.gridLayout.addWidget(self.comboBox_supporter, 2, 0, 1, 4)

        self.checkBox_static_gyro = QCheckBox(simulate_win)
        self.checkBox_static_gyro.setObjectName(u"checkBox_static_gyro")

        self.gridLayout.addWidget(self.checkBox_static_gyro, 4, 1, 1, 1)

        self.textEdit_3 = QTextEdit(simulate_win)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setAcceptDrops(True)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.textEdit_3, 0, 3, 1, 1)

        self.pushButton_yoz = QPushButton(simulate_win)
        self.pushButton_yoz.setObjectName(u"pushButton_yoz")

        self.gridLayout.addWidget(self.pushButton_yoz, 8, 3, 1, 1)

        self.textEdit_4 = QTextEdit(simulate_win)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setAcceptDrops(True)
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setOverwriteMode(False)
        self.textEdit_4.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.textEdit_4, 1, 0, 1, 1)

        self.textEdit_5 = QTextEdit(simulate_win)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setAcceptDrops(True)
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setOverwriteMode(False)
        self.textEdit_5.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.textEdit_5, 1, 1, 1, 1)

        self.textEdit_6 = QTextEdit(simulate_win)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setEnabled(True)
        self.textEdit_6.setAcceptDrops(True)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setOverwriteMode(False)
        self.textEdit_6.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.textEdit_6, 1, 3, 1, 1)


        self.retranslateUi(simulate_win)

        self.comboBox_supporter.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(simulate_win)
    # setupUi

    def retranslateUi(self, simulate_win):
        simulate_win.setWindowTitle(QCoreApplication.translate("simulate_win", u"\u4eff\u771f\u9762\u677f", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("simulate_win", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u503e\u659c\u89d2\uff1a(\u5355\u4f4d\uff1a\u5ea6)</p></body></html>", None))
        self.checkBox_wraparound_frame.setText(QCoreApplication.translate("simulate_win", u"\u5305\u56f4\u6846", None))
        self.checkBox_supporter_model.setText(QCoreApplication.translate("simulate_win", u"\u6a21\u578b", None))
        self.lineEdit_zox.setText(QCoreApplication.translate("simulate_win", u"-60", None))
        self.checkBox_label.setText(QCoreApplication.translate("simulate_win", u"\u6807\u7b7e", None))
        self.pushButton_xoy.setText(QCoreApplication.translate("simulate_win", u"xoy\u65cb\u8f6c", None))
        self.checkBox_scraper.setText(QCoreApplication.translate("simulate_win", u"\u522e\u677f\u673a", None))
        self.pushButton_zox.setText(QCoreApplication.translate("simulate_win", u"zox\u65cb\u8f6c", None))
        self.pushButton_pushScraper.setText(QCoreApplication.translate("simulate_win", u"\u63a8\u522e\u677f\u673a", None))
        self.checkBox_static_wraparound_frame.setText(QCoreApplication.translate("simulate_win", u"\u7edd\u5bf9\u5305\u56f4\u6846", None))
        self.textEdit_1.setHtml(QCoreApplication.translate("simulate_win", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4fef\u4ef0\u89d2\uff1a(\u5355\u4f4d\uff1a\u5ea6)</p></body></html>", None))
        self.lineEdit_yoz.setText(QCoreApplication.translate("simulate_win", u"60", None))
        self.lineEdit_xoy.setText(QCoreApplication.translate("simulate_win", u"60", None))
        self.checkBox_gyro.setText(QCoreApplication.translate("simulate_win", u"\u9640\u87ba\u4eea", None))
        self.lineEdit_pushScraper.setText(QCoreApplication.translate("simulate_win", u"800", None))
        self.lineEdit_pushScraper.setPlaceholderText(QCoreApplication.translate("simulate_win", u"\u79fb\u52a8\u8ddd\u79bb\uff08\u5355\u4f4d\uff1a\u6beb\u7c73\uff09", None))
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

        self.checkBox_static_gyro.setText(QCoreApplication.translate("simulate_win", u"\u7edd\u5bf9\u9640\u87ba\u4eea", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("simulate_win", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u65cb\u8f6c\u89d2\uff1a(\u5355\u4f4d\uff1a\u5ea6)</p></body></html>", None))
        self.pushButton_yoz.setText(QCoreApplication.translate("simulate_win", u"yoz\u65cb\u8f6c", None))
    # retranslateUi

