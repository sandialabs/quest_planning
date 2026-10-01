# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'candidate_technologies.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_CandidateTechnologiesPage(object):
    def setupUi(self, CandidateTechnologiesPage):
        if not CandidateTechnologiesPage.objectName():
            CandidateTechnologiesPage.setObjectName(u"CandidateTechnologiesPage")
        CandidateTechnologiesPage.resize(446, 618)
        self.verticalLayout = QVBoxLayout(CandidateTechnologiesPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(CandidateTechnologiesPage)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title)

        self.scrollArea_content = QScrollArea(CandidateTechnologiesPage)
        self.scrollArea_content.setObjectName(u"scrollArea_content")
        self.scrollArea_content.setMouseTracking(True)
        self.scrollArea_content.setFrameShape(QFrame.Box)
        self.scrollArea_content.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_content.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 403, 163))
        self.scrollAreaWidgetContents.setMouseTracking(True)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_default = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_default.setObjectName(u"checkBox_default")

        self.verticalLayout_2.addWidget(self.checkBox_default)

        self.checkBox_wind = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_wind.setObjectName(u"checkBox_wind")

        self.verticalLayout_2.addWidget(self.checkBox_wind)

        self.checkBox_solar = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_solar.setObjectName(u"checkBox_solar")

        self.verticalLayout_2.addWidget(self.checkBox_solar)

        self.checkBox_lion = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_lion.setObjectName(u"checkBox_lion")

        self.verticalLayout_2.addWidget(self.checkBox_lion)

        self.checkBox_flow = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_flow.setObjectName(u"checkBox_flow")

        self.verticalLayout_2.addWidget(self.checkBox_flow)

        self.checkBox_therm = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_therm.setObjectName(u"checkBox_therm")

        self.verticalLayout_2.addWidget(self.checkBox_therm)

        self.checkBox_custom = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_custom.setObjectName(u"checkBox_custom")

        self.verticalLayout_2.addWidget(self.checkBox_custom)

        self.scrollArea_content.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea_content)

        self.frame_new_tech = QFrame(CandidateTechnologiesPage)
        self.frame_new_tech.setObjectName(u"frame_new_tech")
        self.frame_new_tech.setFrameShape(QFrame.StyledPanel)
        self.frame_new_tech.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_new_tech)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_title_custom = QLabel(self.frame_new_tech)
        self.label_title_custom.setObjectName(u"label_title_custom")
        self.label_title_custom.setFont(font)

        self.verticalLayout_3.addWidget(self.label_title_custom)

        self.label_tech_name = QLabel(self.frame_new_tech)
        self.label_tech_name.setObjectName(u"label_tech_name")

        self.verticalLayout_3.addWidget(self.label_tech_name)

        self.plainTextEdit_technology = QPlainTextEdit(self.frame_new_tech)
        self.plainTextEdit_technology.setObjectName(u"plainTextEdit_technology")

        self.verticalLayout_3.addWidget(self.plainTextEdit_technology)

        self.groupBox_category = QGroupBox(self.frame_new_tech)
        self.groupBox_category.setObjectName(u"groupBox_category")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_category)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox_category = QComboBox(self.groupBox_category)
        self.comboBox_category.setObjectName(u"comboBox_category")

        self.verticalLayout_4.addWidget(self.comboBox_category)


        self.verticalLayout_3.addWidget(self.groupBox_category)

        self.groupBox_device = QGroupBox(self.frame_new_tech)
        self.groupBox_device.setObjectName(u"groupBox_device")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_device)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.comboBox_device = QComboBox(self.groupBox_device)
        self.comboBox_device.setObjectName(u"comboBox_device")

        self.verticalLayout_6.addWidget(self.comboBox_device)


        self.verticalLayout_3.addWidget(self.groupBox_device)

        self.groupBox_location = QGroupBox(self.frame_new_tech)
        self.groupBox_location.setObjectName(u"groupBox_location")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_location)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.comboBox_location = QComboBox(self.groupBox_location)
        self.comboBox_location.setObjectName(u"comboBox_location")

        self.verticalLayout_5.addWidget(self.comboBox_location)


        self.verticalLayout_3.addWidget(self.groupBox_location)

        self.btn_add_tech = QPushButton(self.frame_new_tech)
        self.btn_add_tech.setObjectName(u"btn_add_tech")

        self.verticalLayout_3.addWidget(self.btn_add_tech)


        self.verticalLayout.addWidget(self.frame_new_tech)

        self.frame_buttons = QFrame(CandidateTechnologiesPage)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setFrameShape(QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.frame_buttons)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_ok = QPushButton(self.frame_buttons)
        self.btn_ok.setObjectName(u"btn_ok")

        self.horizontalLayout.addWidget(self.btn_ok)


        self.verticalLayout.addWidget(self.frame_buttons)


        self.retranslateUi(CandidateTechnologiesPage)

        QMetaObject.connectSlotsByName(CandidateTechnologiesPage)
    # setupUi

    def retranslateUi(self, CandidateTechnologiesPage):
        CandidateTechnologiesPage.setWindowTitle(QCoreApplication.translate("CandidateTechnologiesPage", u"Candidate Technologies Page", None))
        self.label_title.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Select Candidate Technologies", None))
        self.checkBox_default.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Default", None))
        self.checkBox_wind.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Wind", None))
        self.checkBox_solar.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Solar", None))
        self.checkBox_lion.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Li-ion Battery 1", None))
        self.checkBox_flow.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Flow Battery", None))
        self.checkBox_therm.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Therm", None))
        self.checkBox_custom.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Custom", None))
        self.label_title_custom.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Add a Customized Tecnology", None))
        self.label_tech_name.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Technology Name:", None))
        self.groupBox_category.setTitle(QCoreApplication.translate("CandidateTechnologiesPage", u"Category:", None))
        self.groupBox_device.setTitle(QCoreApplication.translate("CandidateTechnologiesPage", u"Device:", None))
        self.groupBox_location.setTitle(QCoreApplication.translate("CandidateTechnologiesPage", u"Candidate Location:", None))
        self.btn_add_tech.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Add Technology", None))
        self.btn_cancel.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"Cancel", None))
        self.btn_ok.setText(QCoreApplication.translate("CandidateTechnologiesPage", u"OK", None))
    # retranslateUi

