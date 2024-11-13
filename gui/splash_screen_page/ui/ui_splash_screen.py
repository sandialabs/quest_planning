# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen_pageSZsXnR.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)
import quest_planning.resources_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(500, 500)
        SplashScreen.setMinimumSize(QSize(500, 500))
        SplashScreen.setMaximumSize(QSize(500, 500))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.base = QFrame(self.centralwidget)
        self.base.setObjectName(u"base")
        self.base.setStyleSheet(u"QFrame {\n"
"	background-color: #26495c;\n"
"	\n"
"	background-color: rgb(40, 84, 113);\n"
"	border-radius: 55px;\n"
"	border-color: rgb(129, 194, 65);\n"
"}")
        self.base.setFrameShape(QFrame.StyledPanel)
        self.base.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.base)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.base)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"image: url(:/pics/images/pics/custom_QP_logo.png);\n"
"background-color: rgb(217, 217, 217);\n"
"border-color: rgb(129, 194, 65);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(11)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.base)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.load_status_graphic = QFrame(self.frame_3)
        self.load_status_graphic.setObjectName(u"load_status_graphic")
        self.load_status_graphic.setMinimumSize(QSize(250, 250))
        self.load_status_graphic.setMaximumSize(QSize(250, 250))
        self.load_status_graphic.setStyleSheet(u"QFrame {\n"
"	border-radius: 125px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.748 rgba(0, 0, 0, 0), stop:0.75 rgba(229, 229, 220, 255));\n"
"	color: rgb(255, 255, 0);\n"
"}")
        self.load_status_graphic.setFrameShape(QFrame.StyledPanel)
        self.load_status_graphic.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.load_status_graphic)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.load_status_graphic)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(230, 230))
        self.frame.setMaximumSize(QSize(230, 230))
        self.frame.setStyleSheet(u"QFrame {\n"
"	border-radius: 115px;\n"
"	background-color: #26495c;	\n"
"	background-color: rgb(40, 84, 113);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 100))
        self.label.setMaximumSize(QSize(200, 100))
        font = QFont()
        font.setFamilies([u"Product Sans"])
        font.setPointSize(48)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"	\n"
"	color: rgb(129, 194, 64);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame)


        self.gridLayout.addWidget(self.load_status_graphic, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: rgb(129, 194, 64);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.base)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SplashScreen", u"0 %", None))
        self.label_2.setText(QCoreApplication.translate("SplashScreen", u"Loading...", None))
    # retranslateUi

