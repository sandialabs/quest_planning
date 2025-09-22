# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scenario_widgetWSyHVg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_scenario_view_widget(object):
    def setupUi(self, scenario_view_widget):
        if not scenario_view_widget.objectName():
            scenario_view_widget.setObjectName(u"scenario_view_widget")
        scenario_view_widget.resize(1617, 979)
        scenario_view_widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(scenario_view_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(scenario_view_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.scenario_help = QPushButton(self.frame_5)
        self.scenario_help.setObjectName(u"scenario_help")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/ainfo_24dp_5F6368_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scenario_help.setIcon(icon)
        self.scenario_help.setIconSize(QSize(32, 32))
        self.scenario_help.setFlat(True)

        self.horizontalLayout_3.addWidget(self.scenario_help, 0, Qt.AlignLeft)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"\n"
"	background-color: rgb(208, 208, 208);\n"
"	border-radius: 25px;\n"
"\n"
"	color: black;\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_excel = QVBoxLayout()
        self.verticalLayout_excel.setObjectName(u"verticalLayout_excel")
        self.load_button = QPushButton(self.frame_2)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setStyleSheet(u"QPushButton {\n"
"        border: 1px solid rgb(40, 84, 113);\n"
"        border-radius: 7px;\n"
"        background-color: rgb(40, 84, 113);\n"
"        color: white;\n"
"		 font: 700 10pt \"Segoe UI\";\n"
"        padding: 1px;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(60, 120, 150);\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: rgb(20, 60, 80);\n"
"    }")
        self.load_button.setFlat(True)

        self.verticalLayout_excel.addWidget(self.load_button, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_2.addLayout(self.verticalLayout_excel)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"\n"
"	background-color: rgb(208, 208, 208);\n"
"	border-radius: 25px;\n"
"\n"
"	color: black;\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_select = QVBoxLayout()
        self.verticalLayout_select.setObjectName(u"verticalLayout_select")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_select.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_3.addLayout(self.verticalLayout_select)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"\n"
"	background-color: rgb(208, 208, 208);\n"
"	border-radius: 25px;\n"
"\n"
"	color: black;\n"
"\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_selected = QVBoxLayout()
        self.verticalLayout_selected.setObjectName(u"verticalLayout_selected")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_selected.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_4.addLayout(self.verticalLayout_selected)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.graph_type_combo = QComboBox(self.frame)
        self.graph_type_combo.addItem("")
        self.graph_type_combo.addItem("")
        self.graph_type_combo.addItem("")
        self.graph_type_combo.setObjectName(u"graph_type_combo")
        self.graph_type_combo.setMinimumSize(QSize(250, 0))
        self.graph_type_combo.setStyleSheet(u"background-color:rgb(255,255,255);")

        self.horizontalLayout_2.addWidget(self.graph_type_combo)

        self.plot_button = QPushButton(self.frame)
        self.plot_button.setObjectName(u"plot_button")
        self.plot_button.setMinimumSize(QSize(250, 0))
        self.plot_button.setStyleSheet(u"QPushButton {\n"
"        border: 1px solid rgb(40, 84, 113);\n"
"        border-radius: 7px;\n"
"        background-color: rgb(40, 84, 113);\n"
"        color: white;\n"
"		 font: 700 10pt \"Segoe UI\";\n"
"        padding: 1px;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(60, 120, 150);\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: rgb(20, 60, 80);\n"
"    }")
        self.plot_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.plot_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.progbar = QProgressBar(self.frame)
        self.progbar.setObjectName(u"progbar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progbar.sizePolicy().hasHeightForWidth())
        self.progbar.setSizePolicy(sizePolicy)
        self.progbar.setStyleSheet(u"QProgressBar{\n"
"	border: 1px solid#cfcfcf;\n"
"	border-radius:8px;\n"
"	background-color: transparent;\n"
"	text-align: center;\n"
"	font: bold 10pt \"Segoe UI\";\n"
"	color: #444;\n"
"	height:16px;\n"
"}\n"
"QProgressBar::chunk {\n"
"	border-radius:8px;\n"
"	background:qlineargradient(\n"
"	spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"	stop:0 #6aa9ff,\n"
"	stop:1 #005bea\n"
");\n"
"}")
        self.progbar.setValue(10)
        self.progbar.setInvertedAppearance(False)

        self.verticalLayout_5.addWidget(self.progbar)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_6.setStretch(1, 3)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(scenario_view_widget)

        QMetaObject.connectSlotsByName(scenario_view_widget)
    # setupUi

    def retranslateUi(self, scenario_view_widget):
        scenario_view_widget.setWindowTitle(QCoreApplication.translate("scenario_view_widget", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("scenario_view_widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Scenario Viewer</span></p></body></html>", None))
        self.scenario_help.setText("")
        self.load_button.setText(QCoreApplication.translate("scenario_view_widget", u"Load Excel Files", None))
        self.label.setText(QCoreApplication.translate("scenario_view_widget", u"Select Scenarios", None))
        self.label_2.setText(QCoreApplication.translate("scenario_view_widget", u"Selected", None))
        self.graph_type_combo.setItemText(0, QCoreApplication.translate("scenario_view_widget", u"Generation Capacity", None))
        self.graph_type_combo.setItemText(1, QCoreApplication.translate("scenario_view_widget", u"ESS Capacity", None))
        self.graph_type_combo.setItemText(2, QCoreApplication.translate("scenario_view_widget", u"Capacity Investments", None))

        self.plot_button.setText(QCoreApplication.translate("scenario_view_widget", u"Plot", None))
        self.progbar.setFormat("")
    # retranslateUi

