# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'large_load_model.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_LargeLoadModelPage(object):
    def setupUi(self, LargeLoadModelPage):
        if not LargeLoadModelPage.objectName():
            LargeLoadModelPage.setObjectName(u"LargeLoadModelPage")
        LargeLoadModelPage.resize(853, 781)
        self.verticalLayout = QVBoxLayout(LargeLoadModelPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_buttons = QFrame(LargeLoadModelPage)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setFrameShape(QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.frame_buttons)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_ok = QPushButton(self.frame_buttons)
        self.btn_ok.setObjectName(u"btn_ok")

        self.horizontalLayout.addWidget(self.btn_ok)


        self.verticalLayout.addWidget(self.frame_buttons)


        self.retranslateUi(LargeLoadModelPage)

        QMetaObject.connectSlotsByName(LargeLoadModelPage)
    # setupUi

    def retranslateUi(self, LargeLoadModelPage):
        LargeLoadModelPage.setWindowTitle(QCoreApplication.translate("LargeLoadModelPage", u"Large Load Model Page", None))
        self.btn_cancel.setText(QCoreApplication.translate("LargeLoadModelPage", u"Cancel", None))
        self.btn_ok.setText(QCoreApplication.translate("LargeLoadModelPage", u"OK", None))
    # retranslateUi

