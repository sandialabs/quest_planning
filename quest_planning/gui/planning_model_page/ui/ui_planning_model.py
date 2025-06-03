# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'planning_modelwleKJM.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDateTimeEdit, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)
import quest_planning.resources_rc

class Ui_planning_model(object):
    def setupUi(self, planning_model):
        if not planning_model.objectName():
            planning_model.setObjectName(u"planning_model")
        planning_model.resize(944, 678)
        planning_model.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(planning_model)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 15, 0, 0)
        self.frame_2 = QFrame(planning_model)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setBold(False)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(208, 208, 208);\n"
"border-radius: 25px;\n"
"\n"
"color: black;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 6, 2, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(500, 0))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"\n"
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
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(35)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_7, 7, 1, 1, 1)

        self.transmission_model_help_button = QToolButton(self.frame_4)
        self.transmission_model_help_button.setObjectName(u"transmission_model_help_button")
        self.transmission_model_help_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/ainfo_24dp_5F6368_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.transmission_model_help_button.setIcon(icon)
        self.transmission_model_help_button.setIconSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.transmission_model_help_button, 4, 3, 1, 1)

        self.advanced_settings_button = QPushButton(self.frame_4)
        self.advanced_settings_button.setObjectName(u"advanced_settings_button")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.advanced_settings_button.setFont(font2)
        self.advanced_settings_button.setStyleSheet(u"")
        self.advanced_settings_button.setFlat(True)

        self.gridLayout_5.addWidget(self.advanced_settings_button, 8, 2, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"\n"
"font: 700 12pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_5, 5, 1, 1, 1)

        self.transmission_box = QComboBox(self.frame_4)
        self.transmission_box.addItem("")
        self.transmission_box.addItem("")
        self.transmission_box.addItem("")
        self.transmission_box.setObjectName(u"transmission_box")
        font4 = QFont()
        font4.setPointSize(11)
        self.transmission_box.setFont(font4)
        self.transmission_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.transmission_box, 4, 2, 1, 1)

        self.select_years_button = QPushButton(self.frame_4)
        self.select_years_button.setObjectName(u"select_years_button")
        self.select_years_button.setMaximumSize(QSize(250, 16777215))
        self.select_years_button.setFont(font2)
        self.select_years_button.setStyleSheet(u"")
        self.select_years_button.setFlat(True)

        self.gridLayout_5.addWidget(self.select_years_button, 2, 2, 1, 1)

        self.temporal_box = QComboBox(self.frame_4)
        self.temporal_box.addItem("")
        self.temporal_box.addItem("")
        self.temporal_box.addItem("")
        self.temporal_box.setObjectName(u"temporal_box")
        self.temporal_box.setFont(font4)
        self.temporal_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.temporal_box, 5, 2, 1, 1)

        self.discount_rate_help_button = QToolButton(self.frame_4)
        self.discount_rate_help_button.setObjectName(u"discount_rate_help_button")
        self.discount_rate_help_button.setStyleSheet(u"")
        self.discount_rate_help_button.setIcon(icon)
        self.discount_rate_help_button.setIconSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.discount_rate_help_button, 6, 3, 1, 1)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_3, 4, 1, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_4, 0, 1, 1, 1)

        self.temporal_selection_help_button = QToolButton(self.frame_4)
        self.temporal_selection_help_button.setObjectName(u"temporal_selection_help_button")
        self.temporal_selection_help_button.setStyleSheet(u"")
        self.temporal_selection_help_button.setIcon(icon)
        self.temporal_selection_help_button.setIconSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.temporal_selection_help_button, 5, 3, 1, 1)

        self.begin_date = QDateEdit(self.frame_4)
        self.begin_date.setObjectName(u"begin_date")
        self.begin_date.setFont(font4)
        self.begin_date.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.begin_date.setDate(QDate(2022, 1, 1))

        self.gridLayout_5.addWidget(self.begin_date, 0, 2, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label, 6, 1, 1, 1)

        self.annual_discount_factor = QDoubleSpinBox(self.frame_4)
        self.annual_discount_factor.setObjectName(u"annual_discount_factor")
        self.annual_discount_factor.setFont(font4)
        self.annual_discount_factor.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.annual_discount_factor.setMinimum(0.500000000000000)
        self.annual_discount_factor.setMaximum(50.000000000000000)
        self.annual_discount_factor.setStepType(QAbstractSpinBox.DefaultStepType)
        self.annual_discount_factor.setValue(5.000000000000000)

        self.gridLayout_5.addWidget(self.annual_discount_factor, 6, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 3, 2, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_6, 1, 1, 1, 1)

        self.base_currency_year = QLineEdit(self.frame_4)
        self.base_currency_year.setObjectName(u"base_currency_year")
        self.base_currency_year.setFont(font4)
        self.base_currency_year.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.base_currency_year, 7, 2, 1, 1)

        self.select_simulation_years_help_button = QToolButton(self.frame_4)
        self.select_simulation_years_help_button.setObjectName(u"select_simulation_years_help_button")
        self.select_simulation_years_help_button.setStyleSheet(u"")
        self.select_simulation_years_help_button.setIcon(icon)
        self.select_simulation_years_help_button.setIconSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.select_simulation_years_help_button, 2, 3, 1, 1)

        self.end_date = QDateEdit(self.frame_4)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setFont(font4)
        self.end_date.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.end_date.setCurrentSection(QDateTimeEdit.YearSection)
        self.end_date.setDate(QDate(2042, 1, 1))

        self.gridLayout_5.addWidget(self.end_date, 1, 2, 1, 1)

        self.base_currency_help_button = QToolButton(self.frame_4)
        self.base_currency_help_button.setObjectName(u"base_currency_help_button")
        self.base_currency_help_button.setStyleSheet(u"")
        self.base_currency_help_button.setIcon(icon)
        self.base_currency_help_button.setIconSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.base_currency_help_button, 7, 3, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.gridLayout_2.addWidget(self.frame_3, 6, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 6, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.planning_model_widget = QWidget(self.frame_2)
        self.planning_model_widget.setObjectName(u"planning_model_widget")
        self.gridLayout = QGridLayout(self.planning_model_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.planning_model_info_frame = QFrame(self.planning_model_widget)
        self.planning_model_info_frame.setObjectName(u"planning_model_info_frame")
        self.planning_model_info_frame.setStyleSheet(u"background-color: rgb(208, 208, 208);\n"
"border-radius: 25px;\n"
"\n"
"color: black;")
        self.planning_model_info_frame.setFrameShape(QFrame.NoFrame)
        self.planning_model_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.planning_model_info_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 20, 0)
        self.label_13 = QLabel(self.planning_model_info_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"\n"
"text-decoration: underline;\n"
"font: 700 italic 16pt \"Segoe UI\";\n"
"")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_9 = QLabel(self.planning_model_info_frame)
        self.label_9.setObjectName(u"label_9")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setItalic(True)
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1, Qt.AlignHCenter)

        self.label_10 = QLabel(self.planning_model_info_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 1, Qt.AlignHCenter)

        self.trans_model_label = QLabel(self.planning_model_info_frame)
        self.trans_model_label.setObjectName(u"trans_model_label")
        font6 = QFont()
        font6.setPointSize(12)
        self.trans_model_label.setFont(font6)
        self.trans_model_label.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.trans_model_label, 2, 1, 1, 1)

        self.temporal_selection_label = QLabel(self.planning_model_info_frame)
        self.temporal_selection_label.setObjectName(u"temporal_selection_label")
        self.temporal_selection_label.setFont(font6)
        self.temporal_selection_label.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.temporal_selection_label, 3, 1, 1, 1)

        self.sim_years_label = QLabel(self.planning_model_info_frame)
        self.sim_years_label.setObjectName(u"sim_years_label")
        self.sim_years_label.setFont(font6)
        self.sim_years_label.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.sim_years_label, 1, 1, 1, 1)

        self.label_8 = QLabel(self.planning_model_info_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.planning_model_info_frame, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.planning_model_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.previous_button = QPushButton(self.frame_5)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setMinimumSize(QSize(100, 0))
        self.previous_button.setStyleSheet(u"QPushButton {\n"
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
        self.previous_button.setFlat(True)

        self.horizontalLayout.addWidget(self.previous_button, 0, Qt.AlignLeft)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(500, 60))
        self.label_2.setMaximumSize(QSize(16777211, 16777215))
        self.label_2.setStyleSheet(u"image: url(:/logos/images/logo/planning_model_icon.png);")

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.next_button = QPushButton(self.frame_5)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setMinimumSize(QSize(80, 0))
        self.next_button.setStyleSheet(u"QPushButton {\n"
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
        self.next_button.setFlat(True)

        self.horizontalLayout.addWidget(self.next_button, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(planning_model)

        QMetaObject.connectSlotsByName(planning_model)
    # setupUi

    def retranslateUi(self, planning_model):
        planning_model.setWindowTitle(QCoreApplication.translate("planning_model", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("planning_model", u"Base Currency Year:", None))
        self.transmission_model_help_button.setText("")
        self.advanced_settings_button.setText(QCoreApplication.translate("planning_model", u"Advanced Settings", None))
        self.label_5.setText(QCoreApplication.translate("planning_model", u"Temporal Selection:", None))
        self.transmission_box.setItemText(0, QCoreApplication.translate("planning_model", u"Transportation (Pipe & Bubble)", None))
        self.transmission_box.setItemText(1, QCoreApplication.translate("planning_model", u"Copper Sheet", None))
        self.transmission_box.setItemText(2, QCoreApplication.translate("planning_model", u"DC Power Flow (Upcoming)", None))

        self.select_years_button.setText(QCoreApplication.translate("planning_model", u"Select Simulation Years", None))
        self.temporal_box.setItemText(0, QCoreApplication.translate("planning_model", u"Seasonal Blocks", None))
        self.temporal_box.setItemText(1, QCoreApplication.translate("planning_model", u"Representative Weeks", None))
        self.temporal_box.setItemText(2, QCoreApplication.translate("planning_model", u"8760 Analysis (Upcoming)", None))

        self.discount_rate_help_button.setText("")
        self.label_3.setText(QCoreApplication.translate("planning_model", u"Transmission Model:", None))
        self.label_4.setText(QCoreApplication.translate("planning_model", u"Begin Year:", None))
        self.temporal_selection_help_button.setText("")
        self.begin_date.setDisplayFormat(QCoreApplication.translate("planning_model", u"yyyy", None))
        self.label.setText(QCoreApplication.translate("planning_model", u"Annual Discount Rate:", None))
        self.label_6.setText(QCoreApplication.translate("planning_model", u"End Year:", None))
        self.base_currency_year.setText(QCoreApplication.translate("planning_model", u"2021", None))
        self.select_simulation_years_help_button.setText("")
        self.end_date.setDisplayFormat(QCoreApplication.translate("planning_model", u"yyyy", None))
        self.base_currency_help_button.setText("")
        self.label_13.setText(QCoreApplication.translate("planning_model", u"Planning Model Setup", None))
        self.label_9.setText(QCoreApplication.translate("planning_model", u"Transmission Model:", None))
        self.label_10.setText(QCoreApplication.translate("planning_model", u"Temporal Selection:", None))
        self.trans_model_label.setText(QCoreApplication.translate("planning_model", u"--", None))
        self.temporal_selection_label.setText(QCoreApplication.translate("planning_model", u"--", None))
        self.sim_years_label.setText(QCoreApplication.translate("planning_model", u"--", None))
        self.label_8.setText(QCoreApplication.translate("planning_model", u"Simulation Years:", None))
        self.previous_button.setText(QCoreApplication.translate("planning_model", u"Previous", None))
        self.label_2.setText("")
        self.next_button.setText(QCoreApplication.translate("planning_model", u"Next", None))
    # retranslateUi

