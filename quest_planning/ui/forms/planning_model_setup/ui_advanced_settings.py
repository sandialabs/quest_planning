# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advanced_settings.ui'
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
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_AdvancedSettingsPage(object):
    def setupUi(self, AdvancedSettingsPage):
        if not AdvancedSettingsPage.objectName():
            AdvancedSettingsPage.setObjectName(u"AdvancedSettingsPage")
        AdvancedSettingsPage.resize(500, 350)
        AdvancedSettingsPage.setMaximumSize(QSize(500, 350))
        self.verticalLayout = QVBoxLayout(AdvancedSettingsPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(AdvancedSettingsPage)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title)

        self.scrollArea_content = QScrollArea(AdvancedSettingsPage)
        self.scrollArea_content.setObjectName(u"scrollArea_content")
        self.scrollArea_content.setMouseTracking(True)
        self.scrollArea_content.setFrameShape(QFrame.Box)
        self.scrollArea_content.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_content.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 457, 398))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_labels = QFrame(self.scrollAreaWidgetContents)
        self.frame_labels.setObjectName(u"frame_labels")
        self.frame_labels.setFrameShape(QFrame.NoFrame)
        self.frame_labels.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_labels)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.label_planning = QLabel(self.frame_labels)
        self.label_planning.setObjectName(u"label_planning")
        font1 = QFont()
        font1.setBold(True)
        self.label_planning.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_planning)

        self.label_regulating = QLabel(self.frame_labels)
        self.label_regulating.setObjectName(u"label_regulating")
        self.label_regulating.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_regulating)

        self.label_spinning = QLabel(self.frame_labels)
        self.label_spinning.setObjectName(u"label_spinning")
        self.label_spinning.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_spinning)

        self.label_flex_reserve_solar = QLabel(self.frame_labels)
        self.label_flex_reserve_solar.setObjectName(u"label_flex_reserve_solar")
        self.label_flex_reserve_solar.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_flex_reserve_solar)

        self.label_flex_reserve_wind = QLabel(self.frame_labels)
        self.label_flex_reserve_wind.setObjectName(u"label_flex_reserve_wind")
        self.label_flex_reserve_wind.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_flex_reserve_wind)

        self.label_sys_wind_max = QLabel(self.frame_labels)
        self.label_sys_wind_max.setObjectName(u"label_sys_wind_max")
        self.label_sys_wind_max.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_sys_wind_max)

        self.label_sys_solar_max = QLabel(self.frame_labels)
        self.label_sys_solar_max.setObjectName(u"label_sys_solar_max")
        self.label_sys_solar_max.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_sys_solar_max)

        self.label_sys_gas_max = QLabel(self.frame_labels)
        self.label_sys_gas_max.setObjectName(u"label_sys_gas_max")
        self.label_sys_gas_max.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_sys_gas_max)

        self.label_sys_trans_max = QLabel(self.frame_labels)
        self.label_sys_trans_max.setObjectName(u"label_sys_trans_max")
        self.label_sys_trans_max.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_sys_trans_max)

        self.label_tax_cred = QLabel(self.frame_labels)
        self.label_tax_cred.setObjectName(u"label_tax_cred")
        self.label_tax_cred.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_tax_cred)

        self.label_tax_cred_end_year = QLabel(self.frame_labels)
        self.label_tax_cred_end_year.setObjectName(u"label_tax_cred_end_year")
        self.label_tax_cred_end_year.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_tax_cred_end_year)

        self.label_end_effects = QLabel(self.frame_labels)
        self.label_end_effects.setObjectName(u"label_end_effects")
        self.label_end_effects.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_end_effects)


        self.horizontalLayout_2.addWidget(self.frame_labels)

        self.frame_inputs = QFrame(self.scrollAreaWidgetContents)
        self.frame_inputs.setObjectName(u"frame_inputs")
        self.frame_inputs.setFrameShape(QFrame.NoFrame)
        self.frame_inputs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_inputs)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.lineEdit_planning = QLineEdit(self.frame_inputs)
        self.lineEdit_planning.setObjectName(u"lineEdit_planning")

        self.verticalLayout_3.addWidget(self.lineEdit_planning)

        self.lineEdit_reserve = QLineEdit(self.frame_inputs)
        self.lineEdit_reserve.setObjectName(u"lineEdit_reserve")

        self.verticalLayout_3.addWidget(self.lineEdit_reserve)

        self.lineEdit_spinning = QLineEdit(self.frame_inputs)
        self.lineEdit_spinning.setObjectName(u"lineEdit_spinning")

        self.verticalLayout_3.addWidget(self.lineEdit_spinning)

        self.lineEdit_flex_solar = QLineEdit(self.frame_inputs)
        self.lineEdit_flex_solar.setObjectName(u"lineEdit_flex_solar")

        self.verticalLayout_3.addWidget(self.lineEdit_flex_solar)

        self.lineEdit_flex_wind = QLineEdit(self.frame_inputs)
        self.lineEdit_flex_wind.setObjectName(u"lineEdit_flex_wind")

        self.verticalLayout_3.addWidget(self.lineEdit_flex_wind)

        self.lineEdit_sys_wind_max = QLineEdit(self.frame_inputs)
        self.lineEdit_sys_wind_max.setObjectName(u"lineEdit_sys_wind_max")

        self.verticalLayout_3.addWidget(self.lineEdit_sys_wind_max)

        self.lineEdit_sys_solar_max = QLineEdit(self.frame_inputs)
        self.lineEdit_sys_solar_max.setObjectName(u"lineEdit_sys_solar_max")

        self.verticalLayout_3.addWidget(self.lineEdit_sys_solar_max)

        self.lineEdit_sys_gas_max = QLineEdit(self.frame_inputs)
        self.lineEdit_sys_gas_max.setObjectName(u"lineEdit_sys_gas_max")

        self.verticalLayout_3.addWidget(self.lineEdit_sys_gas_max)

        self.lineEdit_sys_trans_max = QLineEdit(self.frame_inputs)
        self.lineEdit_sys_trans_max.setObjectName(u"lineEdit_sys_trans_max")

        self.verticalLayout_3.addWidget(self.lineEdit_sys_trans_max)

        self.lineEdit_tax_cred = QLineEdit(self.frame_inputs)
        self.lineEdit_tax_cred.setObjectName(u"lineEdit_tax_cred")

        self.verticalLayout_3.addWidget(self.lineEdit_tax_cred)

        self.lineEdit_tax_cred_end_year = QLineEdit(self.frame_inputs)
        self.lineEdit_tax_cred_end_year.setObjectName(u"lineEdit_tax_cred_end_year")

        self.verticalLayout_3.addWidget(self.lineEdit_tax_cred_end_year)

        self.lineEdit_end_effects = QLineEdit(self.frame_inputs)
        self.lineEdit_end_effects.setObjectName(u"lineEdit_end_effects")

        self.verticalLayout_3.addWidget(self.lineEdit_end_effects)


        self.horizontalLayout_2.addWidget(self.frame_inputs)

        self.scrollArea_content.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea_content)

        self.frame_buttons = QFrame(AdvancedSettingsPage)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setFrameShape(QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.frame_buttons)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_ok = QPushButton(self.frame_buttons)
        self.btn_ok.setObjectName(u"btn_ok")

        self.horizontalLayout.addWidget(self.btn_ok)


        self.verticalLayout.addWidget(self.frame_buttons)


        self.retranslateUi(AdvancedSettingsPage)

        QMetaObject.connectSlotsByName(AdvancedSettingsPage)
    # setupUi

    def retranslateUi(self, AdvancedSettingsPage):
        AdvancedSettingsPage.setWindowTitle(QCoreApplication.translate("AdvancedSettingsPage", u"Advanced Planning Model Settings", None))
        self.label_title.setText(QCoreApplication.translate("AdvancedSettingsPage", u"Advanced Settings ", None))
        self.label_planning.setText(QCoreApplication.translate("AdvancedSettingsPage", u"Planning Reserve Margin", None))
        self.label_regulating.setText(QCoreApplication.translate("AdvancedSettingsPage", u"Regulating Reserve Requirement", None))
        self.label_spinning.setText(QCoreApplication.translate("AdvancedSettingsPage", u"Spinning Reserve Requirement", None))
        self.label_flex_reserve_solar.setText(QCoreApplication.translate("AdvancedSettingsPage", u"Flexibility Reserve Requirement (Solar)", None))
        self.label_flex_reserve_wind.setText(QCoreApplication.translate("AdvancedSettingsPage", u"Flexibility Reserve Requirement (Wind)", None))
        self.label_sys_wind_max.setText(QCoreApplication.translate("AdvancedSettingsPage", u"System-wide Wind Maximum Investment", None))
        self.label_sys_solar_max.setText(QCoreApplication.translate("AdvancedSettingsPage", u"System-wide Solar Maximum Investment", None))
        self.label_sys_gas_max.setText(QCoreApplication.translate("AdvancedSettingsPage", u"System-wide Gas Maximum Investment", None))
        self.label_sys_trans_max.setText(QCoreApplication.translate("AdvancedSettingsPage", u"System-wide Transmission Maximum Investment", None))
        self.label_tax_cred.setText(QCoreApplication.translate("AdvancedSettingsPage", u"Tax Credits Option", None))
        self.label_tax_cred_end_year.setText(QCoreApplication.translate("AdvancedSettingsPage", u"Tax Credits End Year", None))
        self.label_end_effects.setText(QCoreApplication.translate("AdvancedSettingsPage", u"End Effects", None))
        self.btn_cancel.setText(QCoreApplication.translate("AdvancedSettingsPage", u"Cancel", None))
        self.btn_ok.setText(QCoreApplication.translate("AdvancedSettingsPage", u"OK", None))
    # retranslateUi

