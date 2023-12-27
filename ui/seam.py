# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seam.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Seam(object):
    def setupUi(self, Seam):
        if not Seam.objectName():
            Seam.setObjectName(u"Seam")
        Seam.resize(400, 254)
        self.horizontalLayout_3 = QHBoxLayout(Seam)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_9 = QFrame(Seam)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_20 = QLabel(self.frame_9)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_2.addWidget(self.label_20)

        self.spinBox_seamThickness = QSpinBox(self.frame_9)
        self.spinBox_seamThickness.setObjectName(u"spinBox_seamThickness")
        self.spinBox_seamThickness.setMinimum(0)
        self.spinBox_seamThickness.setMaximum(11895959)
        self.spinBox_seamThickness.setValue(2)

        self.horizontalLayout_2.addWidget(self.spinBox_seamThickness)


        self.horizontalLayout_3.addWidget(self.frame_9)

        self.pushButton_generate_coalmine = QPushButton(Seam)
        self.pushButton_generate_coalmine.setObjectName(u"pushButton_generate_coalmine")
        self.pushButton_generate_coalmine.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.pushButton_generate_coalmine)


        self.retranslateUi(Seam)

        QMetaObject.connectSlotsByName(Seam)
    # setupUi

    def retranslateUi(self, Seam):
        Seam.setWindowTitle(QCoreApplication.translate("Seam", u"\u7164\u5c42\u8bbe\u7f6e", None))
        self.label_20.setText(QCoreApplication.translate("Seam", u"\u539a\u5ea6\uff1a", None))
        self.pushButton_generate_coalmine.setText(QCoreApplication.translate("Seam", u"\u751f\u6210\u7164\u5c42\uff08\u9700\u5148\u751f\u6210\u5df7\u9053\uff09", None))
    # retranslateUi

