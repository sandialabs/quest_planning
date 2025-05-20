# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'power_system_dataFPupKK.ui'
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
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

from quest_planning.matplotlibwidget import MatplotlibWidget
import quest_planning.resources_rc

class Ui_power_system_data(object):
    def setupUi(self, power_system_data):
        if not power_system_data.objectName():
            power_system_data.setObjectName(u"power_system_data")
        power_system_data.resize(1093, 636)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(power_system_data.sizePolicy().hasHeightForWidth())
        power_system_data.setSizePolicy(sizePolicy)
        power_system_data.setMinimumSize(QSize(0, 0))
        power_system_data.setMaximumSize(QSize(1000000, 1000000))
        power_system_data.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(power_system_data)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(power_system_data)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.power_system_data_widget = QWidget(self.frame_2)
        self.power_system_data_widget.setObjectName(u"power_system_data_widget")
        self.power_system_data_widget.setMinimumSize(QSize(0, 0))
        self.power_system_data_widget.setAutoFillBackground(False)
        self.gridLayout_4 = QGridLayout(self.power_system_data_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)

        self.verticalLayout_5.addWidget(self.power_system_data_widget)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 150))
        self.frame_3.setStyleSheet(u"background-color: rgb(208, 208, 208);\n"
"border-radius: 25px;\n"
"\n"
"color: black;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(25, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(10000000, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(45)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.open_file_button = QPushButton(self.frame_5)
        self.open_file_button.setObjectName(u"open_file_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.open_file_button.sizePolicy().hasHeightForWidth())
        self.open_file_button.setSizePolicy(sizePolicy2)
        self.open_file_button.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.open_file_button.setFont(font)
        self.open_file_button.setStyleSheet(u"QPushButton {\n"
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
        self.open_file_button.setIconSize(QSize(16, 16))
        self.open_file_button.setFlat(True)

        self.gridLayout_3.addWidget(self.open_file_button, 3, 3, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.file_combo_box = QComboBox(self.frame_5)
        self.file_combo_box.setObjectName(u"file_combo_box")
        self.file_combo_box.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.file_combo_box, 2, 1, 1, 3)

        self.system_name_input = QLineEdit(self.frame_5)
        self.system_name_input.setObjectName(u"system_name_input")
        sizePolicy2.setHeightForWidth(self.system_name_input.sizePolicy().hasHeightForWidth())
        self.system_name_input.setSizePolicy(sizePolicy2)
        self.system_name_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.system_name_input, 1, 1, 1, 3)

        self.file_button = QPushButton(self.frame_5)
        self.file_button.setObjectName(u"file_button")
        sizePolicy2.setHeightForWidth(self.file_button.sizePolicy().hasHeightForWidth())
        self.file_button.setSizePolicy(sizePolicy2)
        self.file_button.setMaximumSize(QSize(100, 16777215))
        self.file_button.setFont(font)
        self.file_button.setStyleSheet(u"QPushButton {\n"
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
        self.file_button.setIconSize(QSize(16, 16))
        self.file_button.setFlat(True)

        self.gridLayout_3.addWidget(self.file_button, 3, 2, 1, 1)

        self.power_system_help_button = QToolButton(self.frame_5)
        self.power_system_help_button.setObjectName(u"power_system_help_button")
        self.power_system_help_button.setStyleSheet(u"\n"
"    QToolButton:hover {\n"
"        background-color: rgb(230, 230, 230);\n"
"		border-radius:5px;\n"
"    }\n"
"    QToolButton:pressed {\n"
"        background-color: rgb(180, 180, 180);		\n"
"		 border-radius:5px;\n"
"    }")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/ainfo_24dp_5F6368_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.power_system_help_button.setIcon(icon)
        self.power_system_help_button.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.power_system_help_button, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 1)

        self.power_system_info_frame = QFrame(self.frame_3)
        self.power_system_info_frame.setObjectName(u"power_system_info_frame")
        self.power_system_info_frame.setStyleSheet(u"\n"
"border-color: rgb(129, 194, 65);")
        self.power_system_info_frame.setFrameShape(QFrame.StyledPanel)
        self.power_system_info_frame.setFrameShadow(QFrame.Raised)
        self.power_system_info_frame.setLineWidth(7)
        self.verticalLayout_4 = QVBoxLayout(self.power_system_info_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.bus_label = QLabel(self.power_system_info_frame)
        self.bus_label.setObjectName(u"bus_label")
        font3 = QFont()
        font3.setPointSize(12)
        self.bus_label.setFont(font3)

        self.verticalLayout_4.addWidget(self.bus_label)

        self.line_label = QLabel(self.power_system_info_frame)
        self.line_label.setObjectName(u"line_label")
        self.line_label.setFont(font3)

        self.verticalLayout_4.addWidget(self.line_label)

        self.gen_label = QLabel(self.power_system_info_frame)
        self.gen_label.setObjectName(u"gen_label")
        self.gen_label.setFont(font3)
        self.gen_label.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.gen_label)

        self.sys_label = QLabel(self.power_system_info_frame)
        self.sys_label.setObjectName(u"sys_label")
        self.sys_label.setFont(font3)

        self.verticalLayout_4.addWidget(self.sys_label)


        self.gridLayout_2.addWidget(self.power_system_info_frame, 2, 2, 1, 1)

        self.line_3 = QFrame(self.frame_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 2, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.power_system_data_frame = QFrame(self.frame_2)
        self.power_system_data_frame.setObjectName(u"power_system_data_frame")
        sizePolicy1.setHeightForWidth(self.power_system_data_frame.sizePolicy().hasHeightForWidth())
        self.power_system_data_frame.setSizePolicy(sizePolicy1)
        self.power_system_data_frame.setMinimumSize(QSize(0, 0))
        self.power_system_data_frame.setStyleSheet(u"background-color: rgb(208, 208, 208);\n"
"border-radius: 25px;\n"
"")
        self.power_system_data_frame.setFrameShape(QFrame.StyledPanel)
        self.power_system_data_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.power_system_data_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.network_map_widget = MatplotlibWidget(self.power_system_data_frame)
        self.network_map_widget.setObjectName(u"network_map_widget")
        self.network_map_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.network_map_widget, 0, 1, 2, 1)

        self.generation_mix = MatplotlibWidget(self.power_system_data_frame)
        self.generation_mix.setObjectName(u"generation_mix")
        sizePolicy1.setHeightForWidth(self.generation_mix.sizePolicy().hasHeightForWidth())
        self.generation_mix.setSizePolicy(sizePolicy1)
        self.generation_mix.setMinimumSize(QSize(0, 0))
        self.generation_mix.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.generation_mix, 0, 3, 2, 1)


        self.verticalLayout_5.addWidget(self.power_system_data_frame)

        self.verticalLayout_5.setStretch(3, 1)

        self.verticalLayout_3.addWidget(self.frame_2)

        self.line_bottom = QFrame(power_system_data)
        self.line_bottom.setObjectName(u"line_bottom")
        self.line_bottom.setFrameShape(QFrame.HLine)
        self.line_bottom.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_bottom)

        self.frame = QFrame(power_system_data)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMaximumSize(QSize(16777215, 10000000))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.previous_button = QPushButton(self.frame_6)
        self.previous_button.setObjectName(u"previous_button")
        sizePolicy2.setHeightForWidth(self.previous_button.sizePolicy().hasHeightForWidth())
        self.previous_button.setSizePolicy(sizePolicy2)
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

        self.horizontalLayout_3.addWidget(self.previous_button, 0, Qt.AlignLeft)

        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(500, 60))
        self.label_3.setStyleSheet(u"image: url(:/logos/images/logo/power_system_icon.png);")

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.next_button = QPushButton(self.frame_6)
        self.next_button.setObjectName(u"next_button")
        sizePolicy2.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy2)
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

        self.horizontalLayout_3.addWidget(self.next_button, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignBottom)

        self.verticalLayout_3.setStretch(0, 1)

        self.retranslateUi(power_system_data)

        QMetaObject.connectSlotsByName(power_system_data)
    # setupUi

    def retranslateUi(self, power_system_data):
        power_system_data.setWindowTitle(QCoreApplication.translate("power_system_data", u"Form", None))
        self.open_file_button.setText(QCoreApplication.translate("power_system_data", u"Open", None))
        self.label_2.setText(QCoreApplication.translate("power_system_data", u"System Name", None))
        self.label.setText(QCoreApplication.translate("power_system_data", u"Data Folder", None))
        self.file_combo_box.setCurrentText("")
        self.system_name_input.setText(QCoreApplication.translate("power_system_data", u"Default System Name", None))
        self.file_button.setText(QCoreApplication.translate("power_system_data", u"Browse", None))
        self.power_system_help_button.setText("")
        self.bus_label.setText(QCoreApplication.translate("power_system_data", u"Buses (Zones): --", None))
        self.line_label.setText(QCoreApplication.translate("power_system_data", u"Branches: --", None))
        self.gen_label.setText(QCoreApplication.translate("power_system_data", u"Generators:  --", None))
        self.sys_label.setText(QCoreApplication.translate("power_system_data", u"System Name: --", None))
        self.previous_button.setText(QCoreApplication.translate("power_system_data", u"Previous", None))
        self.label_3.setText("")
        self.next_button.setText(QCoreApplication.translate("power_system_data", u"Next", None))
    # retranslateUi

