# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scenario_builderUxmrad.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_scenario_builder(object):
    def setupUi(self, scenario_builder):
        if not scenario_builder.objectName():
            scenario_builder.setObjectName(u"scenario_builder")
        scenario_builder.resize(736, 584)
        self.verticalLayout_2 = QVBoxLayout(scenario_builder)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(scenario_builder)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.retirements_button = QPushButton(self.frame_5)
        self.retirements_button.setObjectName(u"retirements_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.retirements_button.sizePolicy().hasHeightForWidth())
        self.retirements_button.setSizePolicy(sizePolicy1)
        self.retirements_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.retirements_button, 7, 0, 1, 2)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.capital_cost_box = QComboBox(self.frame_5)
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.setObjectName(u"capital_cost_box")
        self.capital_cost_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.capital_cost_box, 2, 1, 1, 1)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.rps_box = QComboBox(self.frame_5)
        self.rps_box.addItem("")
        self.rps_box.addItem("")
        self.rps_box.setObjectName(u"rps_box")
        self.rps_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.rps_box, 4, 1, 1, 1)

        self.load_profile_box = QComboBox(self.frame_5)
        self.load_profile_box.setObjectName(u"load_profile_box")
        self.load_profile_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.load_profile_box, 3, 1, 1, 1)

        self.transmission_box = QComboBox(self.frame_5)
        self.transmission_box.addItem("")
        self.transmission_box.addItem("")
        self.transmission_box.setObjectName(u"transmission_box")
        self.transmission_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.transmission_box, 5, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_13)


        self.verticalLayout.addWidget(self.frame_6)

        self.tech_frame = QFrame(self.frame_3)
        self.tech_frame.setObjectName(u"tech_frame")
        self.tech_frame.setFrameShape(QFrame.NoFrame)
        self.tech_frame.setFrameShadow(QFrame.Raised)
        self.tech_frame_layout = QVBoxLayout(self.tech_frame)
        self.tech_frame_layout.setObjectName(u"tech_frame_layout")

        self.verticalLayout.addWidget(self.tech_frame)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_4 = QFrame(scenario_builder)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.previous_button = QPushButton(self.frame_4)
        self.previous_button.setObjectName(u"previous_button")
        sizePolicy1.setHeightForWidth(self.previous_button.sizePolicy().hasHeightForWidth())
        self.previous_button.setSizePolicy(sizePolicy1)
        self.previous_button.setStyleSheet(u"background-color: rgb(208, 69, 0);\n"
"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.previous_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(500, 60))
        self.label_5.setStyleSheet(u"image: url(:/logos/images/logo/scenario_icon.png);")

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.next_button = QPushButton(self.frame_4)
        self.next_button.setObjectName(u"next_button")
        sizePolicy1.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy1)
        self.next_button.setStyleSheet(u"background-color: rgb(129, 194, 65);\n"
"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.next_button)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.retranslateUi(scenario_builder)

        QMetaObject.connectSlotsByName(scenario_builder)
    # setupUi

    def retranslateUi(self, scenario_builder):
        scenario_builder.setWindowTitle(QCoreApplication.translate("scenario_builder", u"Form", None))
        self.retirements_button.setText(QCoreApplication.translate("scenario_builder", u"Retirements", None))
        self.label_4.setText(QCoreApplication.translate("scenario_builder", u"<html><head/><body><p>Renewable Portfolio Standards</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("scenario_builder", u"Scenario Name", None))
        self.label_2.setText(QCoreApplication.translate("scenario_builder", u"Capital Cost Trajectory:", None))
        self.lineEdit.setText(QCoreApplication.translate("scenario_builder", u"Test_scenario", None))
        self.capital_cost_box.setItemText(0, QCoreApplication.translate("scenario_builder", u"Moderate", None))
        self.capital_cost_box.setItemText(1, QCoreApplication.translate("scenario_builder", u"High", None))
        self.capital_cost_box.setItemText(2, QCoreApplication.translate("scenario_builder", u"Low", None))

        self.label.setText(QCoreApplication.translate("scenario_builder", u"Transmission Expansion", None))
        self.label_3.setText(QCoreApplication.translate("scenario_builder", u"Load Profile: ", None))
        self.rps_box.setItemText(0, QCoreApplication.translate("scenario_builder", u"Default RPS Policy", None))
        self.rps_box.setItemText(1, QCoreApplication.translate("scenario_builder", u"Create New...", None))

        self.transmission_box.setItemText(0, QCoreApplication.translate("scenario_builder", u"No", None))
        self.transmission_box.setItemText(1, QCoreApplication.translate("scenario_builder", u"Yes", None))

        self.label_13.setText(QCoreApplication.translate("scenario_builder", u"Please select the candidate technologies", None))
        self.previous_button.setText(QCoreApplication.translate("scenario_builder", u"Previous", None))
        self.label_5.setText("")
        self.next_button.setText(QCoreApplication.translate("scenario_builder", u"Next", None))
    # retranslateUi

