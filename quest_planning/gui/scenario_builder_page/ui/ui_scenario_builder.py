# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scenario_builderrSWHbI.ui'
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
        scenario_builder.resize(1094, 841)
        self.verticalLayout_2 = QVBoxLayout(scenario_builder)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(scenario_builder)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"    QToolButton:hover {\n"
"        background-color: rgb(230, 230, 230);\n"
"		border-radius:5px;\n"
"    }\n"
"    QToolButton:pressed {\n"
"        background-color: rgb(180, 180, 180);		\n"
"		 border-radius:5px;\n"
"    }\n"
"QPushButton {\n"
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
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"\n"
"	background-color: rgb(208, 208, 208);\n"
"	border-radius: 25px;\n"
"\n"
"	color: black;\n"
"\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.load_profile_help_button = QToolButton(self.frame_5)
        self.load_profile_help_button.setObjectName(u"load_profile_help_button")
        self.load_profile_help_button.setStyleSheet(u"QToolButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"	border-radius:5px;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(180, 180, 180);		\n"
"	 border-radius:5px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/ainfo_24dp_5F6368_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.load_profile_help_button.setIcon(icon)
        self.load_profile_help_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.load_profile_help_button, 10, 2, 1, 1)

        self.capital_cost_trajectory_help_button = QToolButton(self.frame_5)
        self.capital_cost_trajectory_help_button.setObjectName(u"capital_cost_trajectory_help_button")
        self.capital_cost_trajectory_help_button.setStyleSheet(u"\n"
"    QToolButton:hover {\n"
"        background-color: rgb(230, 230, 230);\n"
"		border-radius:5px;\n"
"    }\n"
"    QToolButton:pressed {\n"
"        background-color: rgb(180, 180, 180);		\n"
"		 border-radius:5px;\n"
"    }")
        self.capital_cost_trajectory_help_button.setIcon(icon)
        self.capital_cost_trajectory_help_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.capital_cost_trajectory_help_button, 5, 2, 1, 1)

        self.scenario_name_help_button = QToolButton(self.frame_5)
        self.scenario_name_help_button.setObjectName(u"scenario_name_help_button")
        self.scenario_name_help_button.setStyleSheet(u"QToolButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"	border-radius:5px;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(180, 180, 180);		\n"
"	 border-radius:5px;\n"
"}")
        self.scenario_name_help_button.setIcon(icon)
        self.scenario_name_help_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.scenario_name_help_button, 1, 2, 1, 1)

        self.transmission_box = QComboBox(self.frame_5)
        self.transmission_box.addItem("")
        self.transmission_box.addItem("")
        self.transmission_box.setObjectName(u"transmission_box")
        self.transmission_box.setEnabled(False)
        self.transmission_box.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.transmission_box.setFont(font)
        self.transmission_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.transmission_box, 15, 1, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2.setWordWrap(True)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 10, 0, 1, 1)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 15, 0, 1, 1)

        self.rps_box = QComboBox(self.frame_5)
        self.rps_box.addItem("")
        self.rps_box.addItem("")
        self.rps_box.setObjectName(u"rps_box")
        self.rps_box.setMaximumSize(QSize(150, 16777215))
        self.rps_box.setFont(font)
        self.rps_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.rps_box, 14, 1, 1, 1)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.trans_expansion_help_button = QToolButton(self.frame_5)
        self.trans_expansion_help_button.setObjectName(u"trans_expansion_help_button")
        self.trans_expansion_help_button.setStyleSheet(u"QToolButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"	border-radius:5px;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(180, 180, 180);		\n"
"	 border-radius:5px;\n"
"}")
        self.trans_expansion_help_button.setIcon(icon)
        self.trans_expansion_help_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.trans_expansion_help_button, 15, 2, 1, 1)

        self.load_profile_box = QComboBox(self.frame_5)
        self.load_profile_box.setObjectName(u"load_profile_box")
        self.load_profile_box.setMaximumSize(QSize(150, 16777215))
        self.load_profile_box.setFont(font)
        self.load_profile_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.load_profile_box, 10, 1, 1, 1)

        self.scenario_name_box = QLineEdit(self.frame_5)
        self.scenario_name_box.setObjectName(u"scenario_name_box")
        self.scenario_name_box.setMaximumSize(QSize(150, 16777215))
        self.scenario_name_box.setFont(font)
        self.scenario_name_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.scenario_name_box, 1, 1, 1, 1)

        self.capital_cost_box = QComboBox(self.frame_5)
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.setObjectName(u"capital_cost_box")
        self.capital_cost_box.setMaximumSize(QSize(150, 16777215))
        self.capital_cost_box.setFont(font)
        self.capital_cost_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.capital_cost_box, 5, 1, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 14, 0, 1, 1)

        self.rps_help_button = QToolButton(self.frame_5)
        self.rps_help_button.setObjectName(u"rps_help_button")
        self.rps_help_button.setStyleSheet(u"QToolButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"	border-radius:5px;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(180, 180, 180);		\n"
"	 border-radius:5px;\n"
"}")
        self.rps_help_button.setIcon(icon)
        self.rps_help_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.rps_help_button, 14, 2, 1, 1)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)

        self.annual_load_growth_box = QLineEdit(self.frame_5)
        self.annual_load_growth_box.setObjectName(u"annual_load_growth_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.annual_load_growth_box.sizePolicy().hasHeightForWidth())
        self.annual_load_growth_box.setSizePolicy(sizePolicy1)
        self.annual_load_growth_box.setFont(font)
        self.annual_load_growth_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.annual_load_growth_box, 11, 1, 1, 1)

        self.load_growth_help_button = QToolButton(self.frame_5)
        self.load_growth_help_button.setObjectName(u"load_growth_help_button")
        self.load_growth_help_button.setStyleSheet(u"QToolButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"	border-radius:5px;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(180, 180, 180);		\n"
"	 border-radius:5px;\n"
"}")
        self.load_growth_help_button.setIcon(icon)
        self.load_growth_help_button.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.load_growth_help_button, 11, 2, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"background-color: rgb(208, 208, 208);\n"
"border-radius: 25px;\n"
"\n"
"color: black;\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"QPushButton {\n"
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
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_13, 0, 1, 1, 1)

        self.cand_tech_button = QPushButton(self.frame_6)
        self.cand_tech_button.setObjectName(u"cand_tech_button")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.cand_tech_button.setFont(font3)
        self.cand_tech_button.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.cand_tech_button, 1, 1, 1, 1)

        self.cand_technologies_help_button = QToolButton(self.frame_6)
        self.cand_technologies_help_button.setObjectName(u"cand_technologies_help_button")
        self.cand_technologies_help_button.setStyleSheet(u"QToolButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"	border-radius:5px;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(180, 180, 180);		\n"
"	 border-radius:5px;\n"
"}")
        self.cand_technologies_help_button.setIcon(icon)
        self.cand_technologies_help_button.setIconSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.cand_technologies_help_button, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 100))
        self.widget.setStyleSheet(u"")
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
        self.candidate_tech_box.setFont(font)
        self.candidate_tech_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.candidate_tech_box.setLineWidth(1)
        self.candidate_tech_box.setReadOnly(True)

        self.gridLayout_6.addWidget(self.candidate_tech_box, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.cand_tech_frame, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 10, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 4, 0, 1, 5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1, Qt.AlignTop)

        self.view_scenario_button = QPushButton(self.frame_7)
        self.view_scenario_button.setObjectName(u"view_scenario_button")
        self.view_scenario_button.setMinimumSize(QSize(150, 0))
        self.view_scenario_button.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_3.addWidget(self.view_scenario_button, 3, 0, 1, 1, Qt.AlignHCenter)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QPushButton {\n"
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
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.frame_8)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 100))
        self.widget_2.setStyleSheet(u"")
        self.gridLayout_10 = QGridLayout(self.widget_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.retirement_frame = QFrame(self.widget_2)
        self.retirement_frame.setObjectName(u"retirement_frame")
        self.retirement_frame.setStyleSheet(u"")
        self.retirement_frame.setFrameShape(QFrame.NoFrame)
        self.retirement_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.retirement_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.retirement_box = QTextEdit(self.retirement_frame)
        self.retirement_box.setObjectName(u"retirement_box")
        self.retirement_box.setFont(font)
        self.retirement_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.retirement_box.setReadOnly(True)

        self.gridLayout_7.addWidget(self.retirement_box, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.retirement_frame, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_2, 3, 1, 1, 1)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gen_retirement_help_button = QToolButton(self.frame_11)
        self.gen_retirement_help_button.setObjectName(u"gen_retirement_help_button")
        self.gen_retirement_help_button.setStyleSheet(u"QToolButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"	border-radius:5px;\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(180, 180, 180);		\n"
"	 border-radius:5px;\n"
"}")
        self.gen_retirement_help_button.setIcon(icon)
        self.gen_retirement_help_button.setIconSize(QSize(24, 24))

        self.gridLayout_8.addWidget(self.gen_retirement_help_button, 0, 3, 1, 1)

        self.gen_retirement_button = QPushButton(self.frame_11)
        self.gen_retirement_button.setObjectName(u"gen_retirement_button")
        self.gen_retirement_button.setMinimumSize(QSize(150, 0))
        self.gen_retirement_button.setFont(font3)
        self.gen_retirement_button.setStyleSheet(u"")
        self.gen_retirement_button.setFlat(True)

        self.gridLayout_8.addWidget(self.gen_retirement_button, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)


        self.gridLayout_4.addWidget(self.frame_11, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame_8, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_7)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_4 = QFrame(scenario_builder)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setStyleSheet(u"QPushButton {\n"
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
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.previous_button = QPushButton(self.frame_4)
        self.previous_button.setObjectName(u"previous_button")
        sizePolicy2.setHeightForWidth(self.previous_button.sizePolicy().hasHeightForWidth())
        self.previous_button.setSizePolicy(sizePolicy2)
        self.previous_button.setMinimumSize(QSize(100, 0))
        self.previous_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.previous_button, 0, Qt.AlignLeft)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(500, 60))
        self.label_5.setStyleSheet(u"image: url(:/logos/images/logo/scenario_icon.png);")

        self.horizontalLayout.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.next_button = QPushButton(self.frame_4)
        self.next_button.setObjectName(u"next_button")
        sizePolicy2.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy2)
        self.next_button.setMinimumSize(QSize(80, 0))
        self.next_button.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.next_button, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.retranslateUi(scenario_builder)

        QMetaObject.connectSlotsByName(scenario_builder)
    # setupUi

    def retranslateUi(self, scenario_builder):
        scenario_builder.setWindowTitle(QCoreApplication.translate("scenario_builder", u"Form", None))
        self.load_profile_help_button.setText("")
        self.capital_cost_trajectory_help_button.setText("")
        self.scenario_name_help_button.setText("")
        self.transmission_box.setItemText(0, QCoreApplication.translate("scenario_builder", u"No", None))
        self.transmission_box.setItemText(1, QCoreApplication.translate("scenario_builder", u"Yes", None))

        self.label_2.setText(QCoreApplication.translate("scenario_builder", u"Resource Capital Costs:", None))
        self.label_3.setText(QCoreApplication.translate("scenario_builder", u"Load Forecast: ", None))
        self.label.setText(QCoreApplication.translate("scenario_builder", u"Transmission Expansion (Upcoming):", None))
        self.rps_box.setItemText(0, QCoreApplication.translate("scenario_builder", u"Default", None))
        self.rps_box.setItemText(1, QCoreApplication.translate("scenario_builder", u"Create New...", None))

        self.label_6.setText(QCoreApplication.translate("scenario_builder", u"Scenario Name:", None))
        self.trans_expansion_help_button.setText("")
        self.scenario_name_box.setText(QCoreApplication.translate("scenario_builder", u"Baseline", None))
        self.capital_cost_box.setItemText(0, QCoreApplication.translate("scenario_builder", u"Moderate", None))
        self.capital_cost_box.setItemText(1, QCoreApplication.translate("scenario_builder", u"High", None))
        self.capital_cost_box.setItemText(2, QCoreApplication.translate("scenario_builder", u"Low", None))

        self.label_4.setText(QCoreApplication.translate("scenario_builder", u"<html><head/><body><p>Future Generation Mix:</p></body></html>", None))
        self.rps_help_button.setText("")
        self.label_9.setText(QCoreApplication.translate("scenario_builder", u"Annual Load Growth:", None))
        self.annual_load_growth_box.setText(QCoreApplication.translate("scenario_builder", u"1.5", None))
        self.load_growth_help_button.setText("")
        self.label_13.setText(QCoreApplication.translate("scenario_builder", u"Select candidate technologies", None))
        self.cand_tech_button.setText(QCoreApplication.translate("scenario_builder", u"Candidate Technologies", None))
        self.cand_technologies_help_button.setText("")
        self.label_7.setText(QCoreApplication.translate("scenario_builder", u"Select generation retirements schedule", None))
        self.view_scenario_button.setText(QCoreApplication.translate("scenario_builder", u"View Scenario", None))
        self.gen_retirement_help_button.setText("")
        self.gen_retirement_button.setText(QCoreApplication.translate("scenario_builder", u"Retirement Schedule", None))
        self.previous_button.setText(QCoreApplication.translate("scenario_builder", u"Previous", None))
        self.label_5.setText("")
        self.next_button.setText(QCoreApplication.translate("scenario_builder", u"Next", None))
    # retranslateUi

