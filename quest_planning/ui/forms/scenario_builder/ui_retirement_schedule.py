# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retirement_schedule.ui'
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
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_RetirementSchedulePage(object):
    def setupUi(self, RetirementSchedulePage):
        if not RetirementSchedulePage.objectName():
            RetirementSchedulePage.setObjectName(u"RetirementSchedulePage")
        RetirementSchedulePage.resize(586, 665)
        self.verticalLayout = QVBoxLayout(RetirementSchedulePage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(RetirementSchedulePage)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title)

        self.frame_default = QFrame(RetirementSchedulePage)
        self.frame_default.setObjectName(u"frame_default")
        self.frame_default.setFrameShape(QFrame.Box)
        self.frame_default.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame_default)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_default = QRadioButton(self.frame_default)
        self.radioButton_default.setObjectName(u"radioButton_default")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.radioButton_default.setFont(font1)
        self.radioButton_default.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioButton_default)

        self.label_capital_cost_desc = QLabel(self.frame_default)
        self.label_capital_cost_desc.setObjectName(u"label_capital_cost_desc")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.label_capital_cost_desc.setFont(font2)
        self.label_capital_cost_desc.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_capital_cost_desc)


        self.verticalLayout.addWidget(self.frame_default)

        self.radioButton_tech = QRadioButton(RetirementSchedulePage)
        self.radioButton_tech.setObjectName(u"radioButton_tech")
        self.radioButton_tech.setFont(font1)

        self.verticalLayout.addWidget(self.radioButton_tech)

        self.frame_custom_tech = QFrame(RetirementSchedulePage)
        self.frame_custom_tech.setObjectName(u"frame_custom_tech")
        self.frame_custom_tech.setFrameShape(QFrame.Box)
        self.frame_custom_tech.setFrameShadow(QFrame.Sunken)
        self.gridLayout = QGridLayout(self.frame_custom_tech)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_coal = QFrame(self.frame_custom_tech)
        self.frame_coal.setObjectName(u"frame_coal")
        self.frame_coal.setFrameShape(QFrame.NoFrame)
        self.frame_coal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_coal)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_coal = QLabel(self.frame_coal)
        self.label_coal.setObjectName(u"label_coal")

        self.verticalLayout_4.addWidget(self.label_coal)

        self.comboBox_coal = QComboBox(self.frame_coal)
        self.comboBox_coal.setObjectName(u"comboBox_coal")

        self.verticalLayout_4.addWidget(self.comboBox_coal)


        self.gridLayout.addWidget(self.frame_coal, 2, 1, 1, 1)

        self.frame_ngas = QFrame(self.frame_custom_tech)
        self.frame_ngas.setObjectName(u"frame_ngas")
        self.frame_ngas.setFrameShape(QFrame.NoFrame)
        self.frame_ngas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_ngas)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_ngas = QLabel(self.frame_ngas)
        self.label_ngas.setObjectName(u"label_ngas")

        self.verticalLayout_3.addWidget(self.label_ngas)

        self.comboBox_ngas = QComboBox(self.frame_ngas)
        self.comboBox_ngas.setObjectName(u"comboBox_ngas")

        self.verticalLayout_3.addWidget(self.comboBox_ngas)


        self.gridLayout.addWidget(self.frame_ngas, 2, 0, 1, 1)

        self.frame_nuclear = QFrame(self.frame_custom_tech)
        self.frame_nuclear.setObjectName(u"frame_nuclear")
        self.frame_nuclear.setFrameShape(QFrame.NoFrame)
        self.frame_nuclear.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_nuclear)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_nuclear = QLabel(self.frame_nuclear)
        self.label_nuclear.setObjectName(u"label_nuclear")

        self.verticalLayout_6.addWidget(self.label_nuclear)

        self.comboBox_nuclear = QComboBox(self.frame_nuclear)
        self.comboBox_nuclear.setObjectName(u"comboBox_nuclear")

        self.verticalLayout_6.addWidget(self.comboBox_nuclear)


        self.gridLayout.addWidget(self.frame_nuclear, 3, 0, 1, 1)

        self.frame_oil = QFrame(self.frame_custom_tech)
        self.frame_oil.setObjectName(u"frame_oil")
        self.frame_oil.setFrameShape(QFrame.NoFrame)
        self.frame_oil.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_oil)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_oil = QLabel(self.frame_oil)
        self.label_oil.setObjectName(u"label_oil")

        self.verticalLayout_5.addWidget(self.label_oil)

        self.comboBox_oil = QComboBox(self.frame_oil)
        self.comboBox_oil.setObjectName(u"comboBox_oil")

        self.verticalLayout_5.addWidget(self.comboBox_oil)


        self.gridLayout.addWidget(self.frame_oil, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_custom_tech)

        self.radioButton_gen = QRadioButton(RetirementSchedulePage)
        self.radioButton_gen.setObjectName(u"radioButton_gen")
        self.radioButton_gen.setFont(font1)

        self.verticalLayout.addWidget(self.radioButton_gen)

        self.frame_custom_gen = QFrame(RetirementSchedulePage)
        self.frame_custom_gen.setObjectName(u"frame_custom_gen")
        self.frame_custom_gen.setFrameShape(QFrame.Box)
        self.frame_custom_gen.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_9 = QVBoxLayout(self.frame_custom_gen)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_5 = QFrame(self.frame_custom_gen)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_generator = QLabel(self.frame_5)
        self.label_generator.setObjectName(u"label_generator")

        self.verticalLayout_7.addWidget(self.label_generator)

        self.comboBox_generator = QComboBox(self.frame_5)
        self.comboBox_generator.setObjectName(u"comboBox_generator")

        self.verticalLayout_7.addWidget(self.comboBox_generator)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_custom_gen)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_retirement_year = QLabel(self.frame_6)
        self.label_retirement_year.setObjectName(u"label_retirement_year")

        self.verticalLayout_8.addWidget(self.label_retirement_year)

        self.comboBox_retirement_year = QComboBox(self.frame_6)
        self.comboBox_retirement_year.setObjectName(u"comboBox_retirement_year")

        self.verticalLayout_8.addWidget(self.comboBox_retirement_year)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.frame_add_retirement = QFrame(self.frame_custom_gen)
        self.frame_add_retirement.setObjectName(u"frame_add_retirement")
        self.frame_add_retirement.setFrameShape(QFrame.NoFrame)
        self.frame_add_retirement.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_add_retirement)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(386, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_add_retirement = QPushButton(self.frame_add_retirement)
        self.btn_add_retirement.setObjectName(u"btn_add_retirement")

        self.horizontalLayout_2.addWidget(self.btn_add_retirement)


        self.verticalLayout_9.addWidget(self.frame_add_retirement)


        self.verticalLayout.addWidget(self.frame_custom_gen)

        self.frame_buttons = QFrame(RetirementSchedulePage)
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


        self.retranslateUi(RetirementSchedulePage)

        QMetaObject.connectSlotsByName(RetirementSchedulePage)
    # setupUi

    def retranslateUi(self, RetirementSchedulePage):
        RetirementSchedulePage.setWindowTitle(QCoreApplication.translate("RetirementSchedulePage", u"Retirement Schedule Page", None))
        self.label_title.setText(QCoreApplication.translate("RetirementSchedulePage", u"Generation Retirement Schedule", None))
        self.radioButton_default.setText(QCoreApplication.translate("RetirementSchedulePage", u"Default retirement schedule", None))
        self.label_capital_cost_desc.setText(QCoreApplication.translate("RetirementSchedulePage", u"<html><head/><body><p>Use the model's default retirement assumptions.</p></body></html>", None))
        self.label_capital_cost_desc.setProperty("textRole", QCoreApplication.translate("RetirementSchedulePage", u"body", None))
        self.radioButton_tech.setText(QCoreApplication.translate("RetirementSchedulePage", u"Custom retirement by technology", None))
        self.label_coal.setText(QCoreApplication.translate("RetirementSchedulePage", u"Coal", None))
        self.label_ngas.setText(QCoreApplication.translate("RetirementSchedulePage", u"Natural Gas", None))
        self.label_nuclear.setText(QCoreApplication.translate("RetirementSchedulePage", u"Nuclear", None))
        self.label_oil.setText(QCoreApplication.translate("RetirementSchedulePage", u"Oil", None))
        self.radioButton_gen.setText(QCoreApplication.translate("RetirementSchedulePage", u"Custom retirement by generator", None))
        self.label_generator.setText(QCoreApplication.translate("RetirementSchedulePage", u"Generator", None))
        self.label_retirement_year.setText(QCoreApplication.translate("RetirementSchedulePage", u"Retirement Year", None))
        self.btn_add_retirement.setText(QCoreApplication.translate("RetirementSchedulePage", u"Add Retirement", None))
        self.btn_cancel.setText(QCoreApplication.translate("RetirementSchedulePage", u"Cancel", None))
        self.btn_ok.setText(QCoreApplication.translate("RetirementSchedulePage", u"OK", None))
    # retranslateUi

