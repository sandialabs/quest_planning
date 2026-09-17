# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'landing.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import quest_planning.resources_rc

class Ui_LandingPage(object):
    def setupUi(self, LandingPage):
        if not LandingPage.objectName():
            LandingPage.setObjectName(u"LandingPage")
        LandingPage.resize(739, 761)
        self.verticalLayout = QVBoxLayout(LandingPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 18, 18, 18)
        self.frame_logo = QFrame(LandingPage)
        self.frame_logo.setObjectName(u"frame_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_logo.sizePolicy().hasHeightForWidth())
        self.frame_logo.setSizePolicy(sizePolicy)
        self.frame_logo.setFrameShape(QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_logo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 12, -1, -1)
        self.label_logo = QLabel(self.frame_logo)
        self.label_logo.setObjectName(u"label_logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy1)
        self.label_logo.setMaximumSize(QSize(900, 500))
        self.label_logo.setPixmap(QPixmap(u":/logos/images/logo/Quest_Planning_Logo_RGB.png"))
        self.label_logo.setScaledContents(False)
        self.label_logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_logo)


        self.verticalLayout.addWidget(self.frame_logo)

        self.frame_btns = QFrame(LandingPage)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(16777215, 30))
        self.frame_btns.setFrameShape(QFrame.NoFrame)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.pushButton = QPushButton(self.frame_btns)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_btns)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.frame_btns)

        self.frame = QFrame(LandingPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_8 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addWidget(self.frame)

        self.frame_footer = QFrame(LandingPage)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setFrameShape(QFrame.NoFrame)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_footer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_quest = QLabel(self.frame_footer)
        self.label_quest.setObjectName(u"label_quest")
        self.label_quest.setMaximumSize(QSize(160, 80))
        self.label_quest.setPixmap(QPixmap(u":/logos/images/logo/footer/Quest_Logo_RGB.png"))
        self.label_quest.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_quest)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_doe = QLabel(self.frame_footer)
        self.label_doe.setObjectName(u"label_doe")
        self.label_doe.setMaximumSize(QSize(150, 150))
        self.label_doe.setPixmap(QPixmap(u":/logos/images/logo/footer/DOE_transparent.png"))
        self.label_doe.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_doe)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_snl = QLabel(self.frame_footer)
        self.label_snl.setObjectName(u"label_snl")
        self.label_snl.setMaximumSize(QSize(180, 100))
        self.label_snl.setPixmap(QPixmap(u":/logos/images/logo/footer/SNL_logo.png"))
        self.label_snl.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_snl)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.frame_footer)


        self.retranslateUi(LandingPage)

        QMetaObject.connectSlotsByName(LandingPage)
    # setupUi

    def retranslateUi(self, LandingPage):
        LandingPage.setWindowTitle(QCoreApplication.translate("LandingPage", u"Form", None))
        self.label_logo.setText("")
        self.pushButton.setText(QCoreApplication.translate("LandingPage", u"Documentation", None))
        self.pushButton_2.setText(QCoreApplication.translate("LandingPage", u"Start", None))
        self.pushButton_2.setProperty("btnRole", u"primary")
        self.label.setText(QCoreApplication.translate("LandingPage", u"<html><head/><body><p>The <span style=\" font-weight:696; font-style:italic; color:#285471;\">QuESt Planning</span> tool, developed by Sandia National Laboratories, is a long-term capacity expansion planning model that examines the role of energy storage technologies on optimal generation and transmission expansion. </p><p><span style=\" font-weight:696; font-style:italic; color:#285471;\">Key features include:</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Identification of cost-optimal energy storage, generation, and transmission investments</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sizing and siting of energy storage resources &amp; generation </li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\">Scenario-based planning and model flexibility</li></ul><p><span style=\" font-family:'Segoe UI'; font-style:italic;\">To run advanced simulations, proceed to the </span><a href=\"https://github.com/sandialabs/quest_planning\"><span style=\" font-family:'Segoe UI'; font-style:italic; text-decoration: underline; color:#0000ff;\">QuESt Planning GitHub</span></a><span style=\" font-family:'Segoe UI'; font-style:italic;\">page for further instructions.</span></p><p><span style=\" font-weight:600;\">Acknowledgement</span>: This material is based upon work supported by the U.S. Department of Energy, Office of Electricity (OE), Energy Storage Division.</p></body></html>", None))
        self.label_quest.setText("")
        self.label_doe.setText("")
        self.label_snl.setText("")
    # retranslateUi

