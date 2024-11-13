# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scenario_builderjmopEH.ui'
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
    QSizePolicy, QSpacerItem, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_scenario_builder(object):
    def setupUi(self, scenario_builder):
        if not scenario_builder.objectName():
            scenario_builder.setObjectName(u"scenario_builder")
        scenario_builder.resize(822, 605)
        self.verticalLayout_2 = QVBoxLayout(scenario_builder)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_8 = QLabel(scenario_builder)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QSize(16777215, 293))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_8.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_8)

        self.frame = QFrame(scenario_builder)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QToolButton{\n"
"image: url(:/icon/images/icons/info_help1.png);\n"
"	background-color: rgb(226, 226, 226);\n"
"}\n"
"QFrame{background-color: rgb(40, 84, 113);border-radius: 20px;}\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 255, 255)}\n"
"QFrame{\n"
"	\n"
"	background-color: rgb(96, 191, 0);\n"
"	background-color: rgb(193, 129, 0);\n"
"}\n"
"QCombBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.load_profile_help_button = QToolButton(self.frame_5)
        self.load_profile_help_button.setObjectName(u"load_profile_help_button")

        self.gridLayout.addWidget(self.load_profile_help_button, 10, 2, 1, 1)

        self.capital_cost_trajectory_help_button = QToolButton(self.frame_5)
        self.capital_cost_trajectory_help_button.setObjectName(u"capital_cost_trajectory_help_button")

        self.gridLayout.addWidget(self.capital_cost_trajectory_help_button, 5, 2, 1, 1)

        self.scenario_name_help_button = QToolButton(self.frame_5)
        self.scenario_name_help_button.setObjectName(u"scenario_name_help_button")

        self.gridLayout.addWidget(self.scenario_name_help_button, 1, 2, 1, 1)

        self.transmission_box = QComboBox(self.frame_5)
        self.transmission_box.addItem("")
        self.transmission_box.addItem("")
        self.transmission_box.setObjectName(u"transmission_box")
        self.transmission_box.setEnabled(False)
        self.transmission_box.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        self.transmission_box.setFont(font1)
        self.transmission_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.transmission_box, 15, 1, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2.setWordWrap(True)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 10, 0, 1, 1)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 15, 0, 1, 1)

        self.rps_box = QComboBox(self.frame_5)
        self.rps_box.addItem("")
        self.rps_box.addItem("")
        self.rps_box.setObjectName(u"rps_box")
        self.rps_box.setMaximumSize(QSize(150, 16777215))
        self.rps_box.setFont(font1)
        self.rps_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.rps_box, 14, 1, 1, 1)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.trans_expansion_help_button = QToolButton(self.frame_5)
        self.trans_expansion_help_button.setObjectName(u"trans_expansion_help_button")

        self.gridLayout.addWidget(self.trans_expansion_help_button, 15, 2, 1, 1)

        self.load_profile_box = QComboBox(self.frame_5)
        self.load_profile_box.setObjectName(u"load_profile_box")
        self.load_profile_box.setMaximumSize(QSize(150, 16777215))
        self.load_profile_box.setFont(font1)
        self.load_profile_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.load_profile_box, 10, 1, 1, 1)

        self.scenario_name_box = QLineEdit(self.frame_5)
        self.scenario_name_box.setObjectName(u"scenario_name_box")
        self.scenario_name_box.setMaximumSize(QSize(150, 16777215))
        self.scenario_name_box.setFont(font1)
        self.scenario_name_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.scenario_name_box, 1, 1, 1, 1)

        self.capital_cost_box = QComboBox(self.frame_5)
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.setObjectName(u"capital_cost_box")
        self.capital_cost_box.setMaximumSize(QSize(150, 16777215))
        self.capital_cost_box.setFont(font1)
        self.capital_cost_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.capital_cost_box, 5, 1, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 14, 0, 1, 1)

        self.rps_help_button = QToolButton(self.frame_5)
        self.rps_help_button.setObjectName(u"rps_help_button")

        self.gridLayout.addWidget(self.rps_help_button, 14, 2, 1, 1)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)

        self.annual_load_growth_box = QLineEdit(self.frame_5)
        self.annual_load_growth_box.setObjectName(u"annual_load_growth_box")
        self.annual_load_growth_box.setFont(font1)
        self.annual_load_growth_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.annual_load_growth_box, 11, 1, 1, 1)

        self.load_growth_help_button = QToolButton(self.frame_5)
        self.load_growth_help_button.setObjectName(u"load_growth_help_button")

        self.gridLayout.addWidget(self.load_growth_help_button, 11, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{background-color: rgb(93, 186, 0);}\n"
"\n"
"QLabel{color:rgb(255,255,255)}\n"
"QCheckBox{\n"
"background-color: rgb(93, 186, 0);\n"
"color:rgb(255,255,255)\n"
"}\n"
"QRadioButton{\n"
"background-color: rgb(93, 186, 0);\n"
"color:rgb(255,255,255)\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 100))
        self.widget.setStyleSheet(u"background-color: rgb(93, 186, 0);")
        self.gridLayout_9 = QGridLayout(self.widget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.cand_tech_frame = QFrame(self.widget)
        self.cand_tech_frame.setObjectName(u"cand_tech_frame")
        self.cand_tech_frame.setFrameShape(QFrame.NoFrame)
        self.cand_tech_frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_6 = QGridLayout(self.cand_tech_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.candidate_tech_box = QTextEdit(self.cand_tech_frame)
        self.candidate_tech_box.setObjectName(u"candidate_tech_box")
        self.candidate_tech_box.setMinimumSize(QSize(0, 70))
        self.candidate_tech_box.setFont(font1)
        self.candidate_tech_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.candidate_tech_box.setLineWidth(1)
        self.candidate_tech_box.setReadOnly(True)

        self.gridLayout_6.addWidget(self.candidate_tech_box, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.cand_tech_frame, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 10, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 4, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_13, 0, 1, 1, 1)

        self.cand_tech_button = QPushButton(self.frame_6)
        self.cand_tech_button.setObjectName(u"cand_tech_button")
        self.cand_tech_button.setFont(font3)
        self.cand_tech_button.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.cand_tech_button, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.cand_technologies_help_button = QToolButton(self.frame_6)
        self.cand_technologies_help_button.setObjectName(u"cand_technologies_help_button")

        self.gridLayout_5.addWidget(self.cand_technologies_help_button, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_2 = QWidget(self.frame_8)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 100))
        self.widget_2.setStyleSheet(u"background-color: rgb(93, 186, 0);")
        self.gridLayout_10 = QGridLayout(self.widget_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.retirement_frame = QFrame(self.widget_2)
        self.retirement_frame.setObjectName(u"retirement_frame")
        self.retirement_frame.setFrameShape(QFrame.StyledPanel)
        self.retirement_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.retirement_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.retirement_box = QTextEdit(self.retirement_frame)
        self.retirement_box.setObjectName(u"retirement_box")
        self.retirement_box.setFont(font1)
        self.retirement_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.retirement_box.setReadOnly(True)

        self.gridLayout_7.addWidget(self.retirement_box, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.retirement_frame, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_2, 3, 1, 1, 1)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gen_retirement_button = QPushButton(self.frame_11)
        self.gen_retirement_button.setObjectName(u"gen_retirement_button")
        self.gen_retirement_button.setFont(font3)
        self.gen_retirement_button.setStyleSheet(u"background-color: rgb(127, 127, 127);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_8.addWidget(self.gen_retirement_button, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 0, 4, 1, 1)

        self.gen_retirement_help_button = QToolButton(self.frame_11)
        self.gen_retirement_help_button.setObjectName(u"gen_retirement_help_button")

        self.gridLayout_8.addWidget(self.gen_retirement_help_button, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame_11, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_8, 3, 0, 1, 1)

        self.line_3 = QFrame(self.frame_7)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1, Qt.AlignTop)

        self.view_scenario_button = QPushButton(self.frame_7)
        self.view_scenario_button.setObjectName(u"view_scenario_button")
        self.view_scenario_button.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_3.addWidget(self.view_scenario_button, 4, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_7)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.line_2 = QFrame(scenario_builder)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.frame_4 = QFrame(scenario_builder)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
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
"color: rgb(255, 255, 255);\n"
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
"color: rgb(255, 255, 255);\n"
"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.next_button)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.retranslateUi(scenario_builder)

        QMetaObject.connectSlotsByName(scenario_builder)
    # setupUi

    def retranslateUi(self, scenario_builder):
        scenario_builder.setWindowTitle(QCoreApplication.translate("scenario_builder", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("scenario_builder", u"Build Planning Scenario", None))
        self.load_profile_help_button.setText("")
        self.capital_cost_trajectory_help_button.setText("")
        self.scenario_name_help_button.setText("")
        self.transmission_box.setItemText(0, QCoreApplication.translate("scenario_builder", u"No", None))
        self.transmission_box.setItemText(1, QCoreApplication.translate("scenario_builder", u"Yes", None))

        self.label_2.setText(QCoreApplication.translate("scenario_builder", u"Resource Capital Costs:", None))
        self.label_3.setText(QCoreApplication.translate("scenario_builder", u"Load Forecast: ", None))
        self.label.setText(QCoreApplication.translate("scenario_builder", u"Transmission Expansion (Upcoming):", None))
        self.rps_box.setItemText(0, QCoreApplication.translate("scenario_builder", u"Default RPS Policy", None))
        self.rps_box.setItemText(1, QCoreApplication.translate("scenario_builder", u"Create New...", None))

        self.label_6.setText(QCoreApplication.translate("scenario_builder", u"Scenario Name:", None))
        self.trans_expansion_help_button.setText("")
        self.scenario_name_box.setText(QCoreApplication.translate("scenario_builder", u"Baseline", None))
        self.capital_cost_box.setItemText(0, QCoreApplication.translate("scenario_builder", u"Moderate", None))
        self.capital_cost_box.setItemText(1, QCoreApplication.translate("scenario_builder", u"High", None))
        self.capital_cost_box.setItemText(2, QCoreApplication.translate("scenario_builder", u"Low", None))

        self.label_4.setText(QCoreApplication.translate("scenario_builder", u"<html><head/><body><p>Renewable Portfolio Standard:</p></body></html>", None))
        self.rps_help_button.setText("")
        self.label_9.setText(QCoreApplication.translate("scenario_builder", u"Annual Load Growth:", None))
        self.annual_load_growth_box.setText(QCoreApplication.translate("scenario_builder", u"1.5", None))
        self.load_growth_help_button.setText(QCoreApplication.translate("scenario_builder", u"...", None))
        self.label_13.setText(QCoreApplication.translate("scenario_builder", u"Select candidate technologies", None))
        self.cand_tech_button.setText(QCoreApplication.translate("scenario_builder", u"Candidate Technologies", None))
        self.cand_technologies_help_button.setText("")
        self.gen_retirement_button.setText(QCoreApplication.translate("scenario_builder", u"Retirement Schedule", None))
        self.gen_retirement_help_button.setText("")
        self.label_7.setText(QCoreApplication.translate("scenario_builder", u"Select generation retirements schedule", None))
        self.view_scenario_button.setText(QCoreApplication.translate("scenario_builder", u"View Scenario", None))
        self.previous_button.setText(QCoreApplication.translate("scenario_builder", u"Previous", None))
        self.label_5.setText("")
        self.next_button.setText(QCoreApplication.translate("scenario_builder", u"Next", None))
    # retranslateUi

