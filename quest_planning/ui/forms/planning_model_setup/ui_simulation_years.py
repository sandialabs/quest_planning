# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulation_years.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SimulationYearsPage(object):
    def setupUi(self, SimulationYearsPage):
        if not SimulationYearsPage.objectName():
            SimulationYearsPage.setObjectName(u"SimulationYearsPage")
        SimulationYearsPage.resize(400, 300)
        self.verticalLayout = QVBoxLayout(SimulationYearsPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_years = QFrame(SimulationYearsPage)
        self.frame_years.setObjectName(u"frame_years")
        self.frame_years.setFrameShape(QFrame.StyledPanel)
        self.frame_years.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_years)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.yeargridLayout = QGridLayout()
        self.yeargridLayout.setObjectName(u"yeargridLayout")

        self.horizontalLayout_2.addLayout(self.yeargridLayout)


        self.verticalLayout.addWidget(self.frame_years)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_years = QPushButton(SimulationYearsPage)
        self.btn_years.setObjectName(u"btn_years")
        self.btn_years.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.btn_years)

        self.btn_ok = QPushButton(SimulationYearsPage)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.btn_ok)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(SimulationYearsPage)

        QMetaObject.connectSlotsByName(SimulationYearsPage)
    # setupUi

    def retranslateUi(self, SimulationYearsPage):
        SimulationYearsPage.setWindowTitle(QCoreApplication.translate("SimulationYearsPage", u"Form", None))
        self.btn_years.setText(QCoreApplication.translate("SimulationYearsPage", u"All Years", None))
        self.btn_ok.setText(QCoreApplication.translate("SimulationYearsPage", u"OK", None))
    # retranslateUi

