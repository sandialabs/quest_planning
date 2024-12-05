# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'build_run.ui'
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

class Ui_build_run(object):
    def setupUi(self, build_run):
        if not build_run.objectName():
            build_run.setObjectName(u"build_run")
        build_run.resize(903, 554)
        self.verticalLayout_2 = QVBoxLayout(build_run)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(build_run)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.results_file_box = QComboBox(self.frame_5)
        self.results_file_box.setObjectName(u"results_file_box")
        self.results_file_box.setStyleSheet(u"")

        self.gridLayout.addWidget(self.results_file_box, 0, 2, 1, 1)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.browse_folder_button = QPushButton(self.frame_5)
        self.browse_folder_button.setObjectName(u"browse_folder_button")
        self.browse_folder_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.browse_folder_button, 0, 3, 1, 1)

        self.open_folder_button = QPushButton(self.frame_5)
        self.open_folder_button.setObjectName(u"open_folder_button")
        self.open_folder_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.open_folder_button, 0, 4, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout.addWidget(self.frame_6)

        self.tech_frame = QFrame(self.frame_3)
        self.tech_frame.setObjectName(u"tech_frame")
        self.tech_frame.setFrameShape(QFrame.NoFrame)
        self.tech_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.tech_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.solver_text = QLineEdit(self.tech_frame)
        self.solver_text.setObjectName(u"solver_text")
        sizePolicy1.setHeightForWidth(self.solver_text.sizePolicy().hasHeightForWidth())
        self.solver_text.setSizePolicy(sizePolicy1)
        self.solver_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.solver_text, 0, 1, 1, 1)

        self.label_5 = QLabel(self.tech_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 13pt;\n"
"color: rgb(0, 0, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.run_button = QPushButton(self.tech_frame)
        self.run_button.setObjectName(u"run_button")
        sizePolicy1.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy1)
        self.run_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.run_button, 2, 1, 1, 1)

        self.build_button = QPushButton(self.tech_frame)
        self.build_button.setObjectName(u"build_button")
        sizePolicy1.setHeightForWidth(self.build_button.sizePolicy().hasHeightForWidth())
        self.build_button.setSizePolicy(sizePolicy1)
        self.build_button.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.build_button, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.tech_frame)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_4 = QFrame(build_run)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
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
"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.previous_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.next_button = QPushButton(self.frame_2)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"font: 700 12pt \"Segoe UI\";\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.next_button)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.retranslateUi(build_run)

        QMetaObject.connectSlotsByName(build_run)
    # setupUi

    def retranslateUi(self, build_run):
        build_run.setWindowTitle(QCoreApplication.translate("build_run", u"Form", None))
        self.label.setText(QCoreApplication.translate("build_run", u"Select Results Folder", None))
        self.browse_folder_button.setText(QCoreApplication.translate("build_run", u"Browse", None))
        self.open_folder_button.setText(QCoreApplication.translate("build_run", u"Open", None))
        self.label_5.setText(QCoreApplication.translate("build_run", u"Solver:", None))
        self.run_button.setText(QCoreApplication.translate("build_run", u"Run", None))
        self.build_button.setText(QCoreApplication.translate("build_run", u"Build", None))
        self.previous_button.setText(QCoreApplication.translate("build_run", u"Previous", None))
        self.next_button.setText(QCoreApplication.translate("build_run", u"Next", None))
    # retranslateUi

