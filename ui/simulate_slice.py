# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulate_slice.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_SliceWin(object):
    def setupUi(self, SliceWin):
        if not SliceWin.objectName():
            SliceWin.setObjectName(u"SliceWin")
        SliceWin.resize(400, 300)
        self.pushButton_sliceSeam = QPushButton(SliceWin)
        self.pushButton_sliceSeam.setObjectName(u"pushButton_sliceSeam")
        self.pushButton_sliceSeam.setGeometry(QRect(40, 140, 75, 24))
        self.pushButton_pushCutter = QPushButton(SliceWin)
        self.pushButton_pushCutter.setObjectName(u"pushButton_pushCutter")
        self.pushButton_pushCutter.setGeometry(QRect(170, 140, 75, 24))
        self.pushButton_pushSupports = QPushButton(SliceWin)
        self.pushButton_pushSupports.setObjectName(u"pushButton_pushSupports")
        self.pushButton_pushSupports.setGeometry(QRect(310, 140, 75, 24))
        self.lineEdit_sliceThickness = QLineEdit(SliceWin)
        self.lineEdit_sliceThickness.setObjectName(u"lineEdit_sliceThickness")
        self.lineEdit_sliceThickness.setGeometry(QRect(150, 90, 113, 20))

        self.retranslateUi(SliceWin)

        QMetaObject.connectSlotsByName(SliceWin)
    # setupUi

    def retranslateUi(self, SliceWin):
        SliceWin.setWindowTitle(QCoreApplication.translate("SliceWin", u"Form", None))
        self.pushButton_sliceSeam.setText(QCoreApplication.translate("SliceWin", u"PushButton", None))
        self.pushButton_pushCutter.setText(QCoreApplication.translate("SliceWin", u"PushButton", None))
        self.pushButton_pushSupports.setText(QCoreApplication.translate("SliceWin", u"PushButton", None))
    # retranslateUi

