# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_screenrNVtHP.ui'
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
    QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_start_screen(object):
    def setupUi(self, start_screen):
        if not start_screen.objectName():
            start_screen.setObjectName(u"start_screen")
        start_screen.resize(1427, 725)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(start_screen.sizePolicy().hasHeightForWidth())
        start_screen.setSizePolicy(sizePolicy)
        start_screen.setStyleSheet(u"#label {\n"
"	font: 13pt;\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.horizontalLayout = QHBoxLayout(start_screen)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(start_screen)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"\n"
"image: url(:/logos/images/logo/new_logo.png);")

        self.verticalLayout_3.addWidget(self.label_3)


        self.gridLayout.addWidget(self.frame_6, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setLineWidth(5)
        self.label.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setItalic(True)
        self.label_8.setFont(font1)
        self.label_8.setTextFormat(Qt.RichText)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_7)

        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setInputMethodHints(Qt.ImhNoTextHandles)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.frame_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_5.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_5, 0, 7, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"image: url(:/logos/images/logo/DOE_Logo_Color.png);")

        self.gridLayout_2.addWidget(self.label_6, 0, 5, 1, 1)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"image: url(:/logos/images/logo/Sandia_National_Laboratories_logo.svg);")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.line_3 = QFrame(self.frame_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 0, 6, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignVCenter)

        self.line_4 = QFrame(self.frame_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.start_button = QPushButton(self.frame)
        self.start_button.setObjectName(u"start_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy3)
        self.start_button.setMaximumSize(QSize(200, 16777215))
        self.start_button.setAutoFillBackground(False)
        self.start_button.setStyleSheet(u"QPushButton {\n"
"        border: 2px solid rgb(40, 84, 113);\n"
"        border-radius: 15px;\n"
"        background-color: rgb(40, 84, 113);\n"
"        color: white;\n"
"		 font: 700 12pt \"Segoe UI\";\n"
"        padding: 4px;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(60, 120, 150);\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: rgb(20, 60, 80);\n"
"    }")
        self.start_button.setFlat(True)

        self.gridLayout_3.addWidget(self.start_button, 0, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(500, 60))
        self.label_7.setStyleSheet(u"image: url(:/logos/images/logo/start_icons.png);")

        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)

        self.doc_button = QPushButton(self.frame)
        self.doc_button.setObjectName(u"doc_button")
        sizePolicy3.setHeightForWidth(self.doc_button.sizePolicy().hasHeightForWidth())
        self.doc_button.setSizePolicy(sizePolicy3)
        self.doc_button.setMaximumSize(QSize(300, 16777215))
        self.doc_button.setStyleSheet(u"QPushButton {\n"
"        border: 2px solid rgb(40, 84, 113);\n"
"        border-radius: 15px;\n"
"        background-color: rgb(40, 84, 113);\n"
"        color: white;\n"
"		 font: 700 12pt \"Segoe UI\";\n"
"        padding: 4px;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(60, 120, 150);\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: rgb(20, 60, 80);\n"
"    }")
        self.doc_button.setFlat(True)

        self.gridLayout_3.addWidget(self.doc_button, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(0, 1)

        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(start_screen)

        QMetaObject.connectSlotsByName(start_screen)
    # setupUi

    def retranslateUi(self, start_screen):
        start_screen.setWindowTitle(QCoreApplication.translate("start_screen", u"Form", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("start_screen", u"<html><head/><body><p>The <span style=\" font-weight:700; font-style:italic; color:#285471;\">QuESt Planning</span> tool, developed by Sandia National Laboratories, is a long-term capacity expansion planning model that examines the role of energy storage technologies on optimal generation and transmission expansion. </p><p><span style=\" font-weight:700; font-style:italic; color:#285471;\">Key features include:</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Identification of cost-optimal energy storage, generation, and transmission investments</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sizing and siting of energy storage resources &amp; generation </li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\">Scenario-based planning and model flexibility</li></ul></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("start_screen", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To run advanced simulations, proceed to the <a href=\"https://github.com/sandialabs/quest_planning\"><span style=\" text-decoration: underline; color:#0000ff;\">QuESt Planning GitHub</span></a><a href=\"https://github.com/sandialabs/quest_planning\"><span style=\" font-style:normal; color:#0000ff;\"> </span></a>page for further instructions.</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("start_screen", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Acknowledgement</span></p><p><span style=\" font-family:'Calibri'; font-size:11pt; font-style:italic; color:#000000;\">This material is based upon work supported by the U.S. Department of Energy, Office of Electricity (OE), Energy Storage Division.</span><span style=\" font-family:'Calibri'; font-size:18pt; font-style:italic; color:#000000;\"/></p></body></html>", None))
        self.label_6.setText("")
        self.label_2.setText("")
        self.start_button.setText(QCoreApplication.translate("start_screen", u"START", None))
        self.label_7.setText("")
        self.doc_button.setText(QCoreApplication.translate("start_screen", u"Documentation", None))
    # retranslateUi

