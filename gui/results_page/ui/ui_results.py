# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resultsSenaEi.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

from quest_planning.matplotlibwidget import MatplotlibWidget
import quest_planning.resources_rc

class Ui_results(object):
    def setupUi(self, results):
        if not results.objectName():
            results.setObjectName(u"results")
        results.resize(831, 607)
        results.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(results)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(results)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.results_frame = QFrame(self.frame)
        self.results_frame.setObjectName(u"results_frame")
        self.results_frame.setStyleSheet(u"background-color: rgb(226, 226, 226);\n"
"border-radius:20")
        self.results_frame.setFrameShape(QFrame.StyledPanel)
        self.results_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.results_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.quest_planning_label = QLabel(self.results_frame)
        self.quest_planning_label.setObjectName(u"quest_planning_label")
        self.quest_planning_label.setStyleSheet(u"image: url(:/pics/images/pics/custom_QP_logo.png);\n"
"")

        self.gridLayout_2.addWidget(self.quest_planning_label, 0, 0, 1, 2)

        self.table_frame = QFrame(self.results_frame)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setMaximumSize(QSize(250, 16777215))
        self.table_frame.setFrameShape(QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.results_table_layout = QHBoxLayout(self.table_frame)
        self.results_table_layout.setObjectName(u"results_table_layout")
        self.results_table_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.results_table_layout.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.results_table_layout.addItem(self.horizontalSpacer_9)


        self.gridLayout_2.addWidget(self.table_frame, 2, 1, 3, 1)

        self.frame_2 = QFrame(self.results_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.es_capacity = MatplotlibWidget(self.frame_2)
        self.es_capacity.setObjectName(u"es_capacity")
        self.es_capacity.setMinimumSize(QSize(350, 200))
        self.es_capacity.setMaximumSize(QSize(650, 600))
        self.es_capacity.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.es_capacity, 1, 1, 1, 1)

        self.installed_capacity = MatplotlibWidget(self.frame_2)
        self.installed_capacity.setObjectName(u"installed_capacity")
        self.installed_capacity.setMinimumSize(QSize(350, 200))
        self.installed_capacity.setMaximumSize(QSize(650, 500))
        self.installed_capacity.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.installed_capacity, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 2, 5, 1)

        self.system_name_label = QLabel(self.results_frame)
        self.system_name_label.setObjectName(u"system_name_label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.system_name_label.setFont(font)
        self.system_name_label.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.system_name_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.system_name_label, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.results_frame, 0, 0, 1, 8)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_5 = QFrame(results)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.gen_plots_button = QPushButton(self.frame_5)
        self.gen_plots_button.setObjectName(u"gen_plots_button")
        self.gen_plots_button.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.gen_plots_button.setFont(font1)
        self.gen_plots_button.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.gen_plots_button, 0, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 0, 6, 1, 1)

        self.collect_results_button = QPushButton(self.frame_5)
        self.collect_results_button.setObjectName(u"collect_results_button")
        self.collect_results_button.setMaximumSize(QSize(200, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.collect_results_button.setFont(font2)
        self.collect_results_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(129, 194, 65);")

        self.gridLayout_6.addWidget(self.collect_results_button, 0, 1, 1, 1)

        self.open_maps_button = QPushButton(self.frame_5)
        self.open_maps_button.setObjectName(u"open_maps_button")
        self.open_maps_button.setMaximumSize(QSize(200, 16777215))
        self.open_maps_button.setFont(font2)
        self.open_maps_button.setStyleSheet(u"background-color: rgb(55, 165, 81);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.open_maps_button, 0, 7, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.open_results_folder_button = QPushButton(self.frame_5)
        self.open_results_folder_button.setObjectName(u"open_results_folder_button")
        self.open_results_folder_button.setMaximumSize(QSize(200, 16777215))
        self.open_results_folder_button.setFont(font2)
        self.open_results_folder_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(209, 139, 0);")

        self.gridLayout_6.addWidget(self.open_results_folder_button, 0, 5, 1, 1)

        self.results_help_button = QToolButton(self.frame_5)
        self.results_help_button.setObjectName(u"results_help_button")
        self.results_help_button.setStyleSheet(u"QToolButton{\n"
"image: url(:/icon/images/icons/info_help1.png);\n"
"	background-color: rgb(226, 226, 226);\n"
"}")

        self.gridLayout_6.addWidget(self.results_help_button, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.line = QFrame(results)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.frame_4 = QFrame(results)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(500, 60))
        self.label_2.setStyleSheet(u"image: url(:/logos/images/logo/results_icon.png);")

        self.gridLayout_5.addWidget(self.label_2, 0, 2, 1, 1)

        self.save_results_button = QPushButton(self.frame_4)
        self.save_results_button.setObjectName(u"save_results_button")
        self.save_results_button.setStyleSheet(u"background-color: rgb(129, 194, 65);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 12pt \"Segoe UI\";")

        self.gridLayout_5.addWidget(self.save_results_button, 0, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.previous_button = QPushButton(self.frame_4)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setStyleSheet(u"background-color: rgb(208, 69, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 12pt \"Segoe UI\";")

        self.gridLayout_5.addWidget(self.previous_button, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.retranslateUi(results)

        QMetaObject.connectSlotsByName(results)
    # setupUi

    def retranslateUi(self, results):
        results.setWindowTitle(QCoreApplication.translate("results", u"Form", None))
        self.quest_planning_label.setText("")
        self.system_name_label.setText("")
        self.gen_plots_button.setText(QCoreApplication.translate("results", u"Generate Plots", None))
        self.collect_results_button.setText(QCoreApplication.translate("results", u"Collect Results", None))
        self.open_maps_button.setText(QCoreApplication.translate("results", u"Open Maps", None))
        self.open_results_folder_button.setText(QCoreApplication.translate("results", u"Open Results Folder", None))
        self.results_help_button.setText("")
        self.label_2.setText("")
        self.save_results_button.setText(QCoreApplication.translate("results", u"Save Results", None))
        self.previous_button.setText(QCoreApplication.translate("results", u"Previous", None))
    # retranslateUi

