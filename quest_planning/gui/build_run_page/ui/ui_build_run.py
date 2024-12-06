# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'build_runmVYhcg.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)
import quest_planning.resources_rc

class Ui_build_run(object):
    def setupUi(self, build_run):
        if not build_run.objectName():
            build_run.setObjectName(u"build_run")
        build_run.resize(849, 675)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(build_run.sizePolicy().hasHeightForWidth())
        build_run.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(build_run)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(build_run)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 250))
        self.frame_5.setMaximumSize(QSize(16777215, 250))
        self.frame_5.setStyleSheet(u"background-color: rgb(40, 84, 113);\n"
"border-radius: 25;\n"
"background-color: rgb(193, 129, 0);")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.solver_select_box = QComboBox(self.frame_5)
        self.solver_select_box.addItem("")
        self.solver_select_box.addItem("")
        self.solver_select_box.addItem("")
        self.solver_select_box.addItem("")
        self.solver_select_box.addItem("")
        self.solver_select_box.setObjectName(u"solver_select_box")
        self.solver_select_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.solver_select_box, 3, 1, 1, 1)

        self.run_button = QPushButton(self.frame_5)
        self.run_button.setObjectName(u"run_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.run_button.setFont(font)
        self.run_button.setStyleSheet(u"background-color: rgb(40, 84, 113);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.run_button, 4, 2, 1, 1)

        self.browse_folder_button = QPushButton(self.frame_5)
        self.browse_folder_button.setObjectName(u"browse_folder_button")
        self.browse_folder_button.setFont(font)
        self.browse_folder_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.browse_folder_button, 2, 2, 1, 1)

        self.build_button = QPushButton(self.frame_5)
        self.build_button.setObjectName(u"build_button")
        sizePolicy2.setHeightForWidth(self.build_button.sizePolicy().hasHeightForWidth())
        self.build_button.setSizePolicy(sizePolicy2)
        self.build_button.setFont(font)
        self.build_button.setStyleSheet(u"background-color: rgb(129, 194, 65);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.build_button, 4, 1, 1, 1)

        self.results_file_box = QComboBox(self.frame_5)
        self.results_file_box.setObjectName(u"results_file_box")
        self.results_file_box.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.results_file_box, 2, 1, 1, 1)

        self.widget = QWidget(self.frame_5)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 250))
        self.widget.setStyleSheet(u"image: url(:/pics/images/pics/custom_QP_logo.png);")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 3)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1, Qt.AlignRight)

        self.build_run_help_button = QToolButton(self.frame_5)
        self.build_run_help_button.setObjectName(u"build_run_help_button")
        self.build_run_help_button.setToolTipDuration(3)
        self.build_run_help_button.setStyleSheet(u"QToolButton{\n"
"image: url(:/icon/images/icons/info_help1.png);\n"
"	background-color: rgb(226, 226, 226);\n"
"}")

        self.gridLayout.addWidget(self.build_run_help_button, 4, 0, 1, 1, Qt.AlignRight)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1, Qt.AlignRight)


        self.gridLayout_3.addWidget(self.frame_5, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.model_status_frame = QFrame(self.widget_2)
        self.model_status_frame.setObjectName(u"model_status_frame")
        self.model_status_frame.setStyleSheet(u"background-color: rgb(40, 84, 113);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25")
        self.model_status_frame.setFrameShape(QFrame.StyledPanel)
        self.model_status_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.model_status_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.model_status_frame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_3.setFont(font2)

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.report_progress_box = QTextEdit(self.model_status_frame)
        self.report_progress_box.setObjectName(u"report_progress_box")
        self.report_progress_box.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.report_progress_box.setReadOnly(True)

        self.gridLayout_5.addWidget(self.report_progress_box, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.model_status_frame, 1, 0, 1, 1)

        self.line_top = QFrame(self.widget_2)
        self.line_top.setObjectName(u"line_top")
        self.line_top.setFrameShape(QFrame.HLine)
        self.line_top.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_top, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.line = QFrame(build_run)
        self.line.setObjectName(u"line")
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame_4 = QFrame(build_run)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.previous_button = QPushButton(self.frame_2)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setStyleSheet(u"background-color: rgb(208, 69, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.previous_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(500, 60))
        self.label_2.setStyleSheet(u"image: url(:/logos/images/logo/optimization_icon.png);")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.next_button = QPushButton(self.frame_2)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setStyleSheet(u"background-color: rgb(129, 194, 65);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.next_button)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_4)


        self.retranslateUi(build_run)

        QMetaObject.connectSlotsByName(build_run)
    # setupUi

    def retranslateUi(self, build_run):
        build_run.setWindowTitle(QCoreApplication.translate("build_run", u"Form", None))
        self.solver_select_box.setItemText(0, QCoreApplication.translate("build_run", u"Gurobi", None))
        self.solver_select_box.setItemText(1, QCoreApplication.translate("build_run", u"GLPK", None))
        self.solver_select_box.setItemText(2, QCoreApplication.translate("build_run", u"Clp", None))
        self.solver_select_box.setItemText(3, QCoreApplication.translate("build_run", u"HiGHs", None))
        self.solver_select_box.setItemText(4, QCoreApplication.translate("build_run", u"Other (Upcoming)", None))

        self.run_button.setText(QCoreApplication.translate("build_run", u"Solve", None))
        self.browse_folder_button.setText(QCoreApplication.translate("build_run", u"Browse", None))
        self.build_button.setText(QCoreApplication.translate("build_run", u"Build", None))
        self.label_5.setText(QCoreApplication.translate("build_run", u"Select Solver:", None))
        self.build_run_help_button.setText("")
        self.label.setText(QCoreApplication.translate("build_run", u"Select Results Folder:", None))
        self.label_3.setText(QCoreApplication.translate("build_run", u"Optimization Model Solve Status:", None))
        self.previous_button.setText(QCoreApplication.translate("build_run", u"Previous", None))
        self.label_2.setText("")
        self.next_button.setText(QCoreApplication.translate("build_run", u"Next", None))
    # retranslateUi

