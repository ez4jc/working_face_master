# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QSizePolicy,
    QTextEdit, QWidget)

class Ui_LoadingDialog(object):
    def setupUi(self, LoadingDialog):
        if not LoadingDialog.objectName():
            LoadingDialog.setObjectName(u"LoadingDialog")
        LoadingDialog.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(LoadingDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit = QTextEdit(LoadingDialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setLayoutDirection(Qt.LeftToRight)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.textEdit)


        self.retranslateUi(LoadingDialog)

        QMetaObject.connectSlotsByName(LoadingDialog)
    # setupUi

    def retranslateUi(self, LoadingDialog):
        LoadingDialog.setWindowTitle(QCoreApplication.translate("LoadingDialog", u"Dialog", None))
        self.textEdit.setHtml(QCoreApplication.translate("LoadingDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt;\"><br />\u52a0\u8f7d\u4e2d...<br />\uff08\u9884\u8ba1\u5341\u79d2\uff09</span></p></body></html>", None))
    # retranslateUi

