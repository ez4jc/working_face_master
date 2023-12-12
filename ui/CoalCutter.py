# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CoalCutter.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_CoalCutter(object):
    def setupUi(self, CoalCutter):
        if not CoalCutter.objectName():
            CoalCutter.setObjectName(u"CoalCutter")
        CoalCutter.resize(400, 300)
        self.gridLayout = QGridLayout(CoalCutter)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(CoalCutter)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.pushButton_translateCoalCutter = QPushButton(CoalCutter)
        self.pushButton_translateCoalCutter.setObjectName(u"pushButton_translateCoalCutter")

        self.gridLayout.addWidget(self.pushButton_translateCoalCutter, 2, 2, 1, 1)

        self.lineEdit_translateDis = QLineEdit(CoalCutter)
        self.lineEdit_translateDis.setObjectName(u"lineEdit_translateDis")
        self.lineEdit_translateDis.setMaxLength(5)

        self.gridLayout.addWidget(self.lineEdit_translateDis, 2, 1, 1, 1)

        self.checkBox_showCoalCutter = QCheckBox(CoalCutter)
        self.checkBox_showCoalCutter.setObjectName(u"checkBox_showCoalCutter")
        self.checkBox_showCoalCutter.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_showCoalCutter, 1, 2, 1, 1)

        self.pushButton_loadCoalCutter = QPushButton(CoalCutter)
        self.pushButton_loadCoalCutter.setObjectName(u"pushButton_loadCoalCutter")

        self.gridLayout.addWidget(self.pushButton_loadCoalCutter, 1, 1, 1, 1)

        self.pushButton_fitSeamSurface = QPushButton(CoalCutter)
        self.pushButton_fitSeamSurface.setObjectName(u"pushButton_fitSeamSurface")

        self.gridLayout.addWidget(self.pushButton_fitSeamSurface, 3, 2, 1, 1)


        self.retranslateUi(CoalCutter)

        QMetaObject.connectSlotsByName(CoalCutter)
    # setupUi

    def retranslateUi(self, CoalCutter):
        CoalCutter.setWindowTitle(QCoreApplication.translate("CoalCutter", u"\u5272\u7164\u673a\u52a0\u8f7d/\u63a7\u5236", None))
        self.label.setText(QCoreApplication.translate("CoalCutter", u"\u5355\u4f4d\uff1amm", None))
        self.pushButton_translateCoalCutter.setText(QCoreApplication.translate("CoalCutter", u"\u8d34\u7164\u58c1\u9762\u5e73\u79fb", None))
        self.checkBox_showCoalCutter.setText(QCoreApplication.translate("CoalCutter", u"\u6a21\u578b", None))
        self.pushButton_loadCoalCutter.setText(QCoreApplication.translate("CoalCutter", u"\u52a0\u8f7d\u6a21\u578b", None))
        self.pushButton_fitSeamSurface.setText(QCoreApplication.translate("CoalCutter", u"\u8d34\u4f4f\u7164\u58c1\u9762", None))
    # retranslateUi

