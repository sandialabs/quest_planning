# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'large_load_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_LargeLoadDialog(object):
    def setupUi(self, LargeLoadDialog):
        if not LargeLoadDialog.objectName():
            LargeLoadDialog.setObjectName(u"LargeLoadDialog")
        LargeLoadDialog.resize(409, 763)
        self.verticalLayout = QVBoxLayout(LargeLoadDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(LargeLoadDialog)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title)

        self.frame_params = QFrame(LargeLoadDialog)
        self.frame_params.setObjectName(u"frame_params")
        self.frame_params.setFrameShape(QFrame.Box)
        self.frame_params.setFrameShadow(QFrame.Sunken)
        self.gridLayout = QGridLayout(self.frame_params)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_bus = QLabel(self.frame_params)
        self.label_bus.setObjectName(u"label_bus")

        self.gridLayout.addWidget(self.label_bus, 1, 0, 1, 1)

        self.lineEdit_id = QLineEdit(self.frame_params)
        self.lineEdit_id.setObjectName(u"lineEdit_id")

        self.gridLayout.addWidget(self.lineEdit_id, 0, 2, 1, 1)

        self.label_id = QLabel(self.frame_params)
        self.label_id.setObjectName(u"label_id")

        self.gridLayout.addWidget(self.label_id, 0, 0, 1, 1)

        self.label_cap = QLabel(self.frame_params)
        self.label_cap.setObjectName(u"label_cap")

        self.gridLayout.addWidget(self.label_cap, 3, 0, 1, 1)

        self.lineEdit_cap = QLineEdit(self.frame_params)
        self.lineEdit_cap.setObjectName(u"lineEdit_cap")

        self.gridLayout.addWidget(self.lineEdit_cap, 3, 2, 1, 1)

        self.label_deploy = QLabel(self.frame_params)
        self.label_deploy.setObjectName(u"label_deploy")

        self.gridLayout.addWidget(self.label_deploy, 4, 0, 1, 1)

        self.lineEdit_deploy = QLineEdit(self.frame_params)
        self.lineEdit_deploy.setObjectName(u"lineEdit_deploy")

        self.gridLayout.addWidget(self.lineEdit_deploy, 4, 2, 1, 1)

        self.lineEdit_bus = QLineEdit(self.frame_params)
        self.lineEdit_bus.setObjectName(u"lineEdit_bus")

        self.gridLayout.addWidget(self.lineEdit_bus, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_params)

        self.frame_profile = QFrame(LargeLoadDialog)
        self.frame_profile.setObjectName(u"frame_profile")
        self.frame_profile.setFrameShape(QFrame.Box)
        self.frame_profile.setFrameShadow(QFrame.Sunken)
        self.gridLayout_4 = QGridLayout(self.frame_profile)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_file = QLineEdit(self.frame_profile)
        self.lineEdit_file.setObjectName(u"lineEdit_file")

        self.gridLayout_4.addWidget(self.lineEdit_file, 1, 1, 1, 1)

        self.label_file = QLabel(self.frame_profile)
        self.label_file.setObjectName(u"label_file")

        self.gridLayout_4.addWidget(self.label_file, 1, 0, 1, 1)

        self.label_type = QLabel(self.frame_profile)
        self.label_type.setObjectName(u"label_type")

        self.gridLayout_4.addWidget(self.label_type, 2, 0, 1, 1)

        self.label_profile = QLabel(self.frame_profile)
        self.label_profile.setObjectName(u"label_profile")
        self.label_profile.setFont(font)

        self.gridLayout_4.addWidget(self.label_profile, 0, 0, 1, 1)

        self.btn_file = QPushButton(self.frame_profile)
        self.btn_file.setObjectName(u"btn_file")

        self.gridLayout_4.addWidget(self.btn_file, 1, 2, 1, 1)

        self.comboBox_type = QComboBox(self.frame_profile)
        self.comboBox_type.setObjectName(u"comboBox_type")

        self.gridLayout_4.addWidget(self.comboBox_type, 2, 1, 1, 2)


        self.verticalLayout.addWidget(self.frame_profile)

        self.frame_onsite = QFrame(LargeLoadDialog)
        self.frame_onsite.setObjectName(u"frame_onsite")
        self.frame_onsite.setFrameShape(QFrame.Box)
        self.frame_onsite.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.frame_onsite)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_onsite = QLabel(self.frame_onsite)
        self.label_onsite.setObjectName(u"label_onsite")
        self.label_onsite.setFont(font)

        self.verticalLayout_3.addWidget(self.label_onsite)

        self.frame_ngas = QFrame(self.frame_onsite)
        self.frame_ngas.setObjectName(u"frame_ngas")
        self.frame_ngas.setFrameShape(QFrame.NoFrame)
        self.frame_ngas.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_ngas)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_11 = QLabel(self.frame_ngas)
        self.label_11.setObjectName(u"label_11")
        font1 = QFont()
        font1.setBold(True)
        self.label_11.setFont(font1)

        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)

        self.checkBox_ngas_cand = QCheckBox(self.frame_ngas)
        self.checkBox_ngas_cand.setObjectName(u"checkBox_ngas_cand")

        self.gridLayout_3.addWidget(self.checkBox_ngas_cand, 1, 0, 1, 1)

        self.label_max_cap = QLabel(self.frame_ngas)
        self.label_max_cap.setObjectName(u"label_max_cap")

        self.gridLayout_3.addWidget(self.label_max_cap, 2, 0, 1, 1)

        self.lineEdit_max_cap = QLineEdit(self.frame_ngas)
        self.lineEdit_max_cap.setObjectName(u"lineEdit_max_cap")

        self.gridLayout_3.addWidget(self.lineEdit_max_cap, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_ngas)

        self.frame_bess = QFrame(self.frame_onsite)
        self.frame_bess.setObjectName(u"frame_bess")
        self.frame_bess.setFrameShape(QFrame.NoFrame)
        self.frame_bess.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_bess)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_bess = QLabel(self.frame_bess)
        self.label_bess.setObjectName(u"label_bess")
        self.label_bess.setFont(font1)

        self.gridLayout_2.addWidget(self.label_bess, 0, 0, 1, 1)

        self.lineEdit_power = QLineEdit(self.frame_bess)
        self.lineEdit_power.setObjectName(u"lineEdit_power")

        self.gridLayout_2.addWidget(self.lineEdit_power, 4, 1, 1, 1)

        self.label_power = QLabel(self.frame_bess)
        self.label_power.setObjectName(u"label_power")

        self.gridLayout_2.addWidget(self.label_power, 4, 0, 1, 1)

        self.checkBox_bess = QCheckBox(self.frame_bess)
        self.checkBox_bess.setObjectName(u"checkBox_bess")

        self.gridLayout_2.addWidget(self.checkBox_bess, 1, 0, 1, 1)

        self.label_max_energy = QLabel(self.frame_bess)
        self.label_max_energy.setObjectName(u"label_max_energy")

        self.gridLayout_2.addWidget(self.label_max_energy, 2, 0, 1, 1)

        self.lineEdit_max_energy = QLineEdit(self.frame_bess)
        self.lineEdit_max_energy.setObjectName(u"lineEdit_max_energy")

        self.gridLayout_2.addWidget(self.lineEdit_max_energy, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_bess)


        self.verticalLayout.addWidget(self.frame_onsite)

        self.frame_buttons = QFrame(LargeLoadDialog)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setFrameShape(QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.frame_buttons)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_3.addWidget(self.btn_cancel)

        self.btn_add = QPushButton(self.frame_buttons)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout_3.addWidget(self.btn_add)


        self.verticalLayout.addWidget(self.frame_buttons)


        self.retranslateUi(LargeLoadDialog)

        QMetaObject.connectSlotsByName(LargeLoadDialog)
    # setupUi

    def retranslateUi(self, LargeLoadDialog):
        LargeLoadDialog.setWindowTitle(QCoreApplication.translate("LargeLoadDialog", u"Add Large Load ", None))
        self.label_title.setText(QCoreApplication.translate("LargeLoadDialog", u"Add Large Load", None))
        self.label_bus.setText(QCoreApplication.translate("LargeLoadDialog", u"Bus", None))
        self.label_id.setText(QCoreApplication.translate("LargeLoadDialog", u"ID", None))
        self.label_cap.setText(QCoreApplication.translate("LargeLoadDialog", u"Capacity (MW)", None))
        self.label_deploy.setText(QCoreApplication.translate("LargeLoadDialog", u"Deploy Year", None))
        self.label_file.setText(QCoreApplication.translate("LargeLoadDialog", u"File", None))
        self.label_type.setText(QCoreApplication.translate("LargeLoadDialog", u"Type", None))
        self.label_profile.setText(QCoreApplication.translate("LargeLoadDialog", u"Profile", None))
        self.btn_file.setText(QCoreApplication.translate("LargeLoadDialog", u"Browse", None))
        self.label_onsite.setText(QCoreApplication.translate("LargeLoadDialog", u"Onsite Resources", None))
        self.label_11.setText(QCoreApplication.translate("LargeLoadDialog", u"Natural Gas", None))
        self.checkBox_ngas_cand.setText(QCoreApplication.translate("LargeLoadDialog", u"Candidate", None))
        self.label_max_cap.setText(QCoreApplication.translate("LargeLoadDialog", u" Max Capacity (MW):", None))
        self.label_bess.setText(QCoreApplication.translate("LargeLoadDialog", u"BESS", None))
        self.label_power.setText(QCoreApplication.translate("LargeLoadDialog", u" Max Power (MW):", None))
        self.checkBox_bess.setText(QCoreApplication.translate("LargeLoadDialog", u"Candidate", None))
        self.label_max_energy.setText(QCoreApplication.translate("LargeLoadDialog", u" Max Energy (MWh):", None))
        self.btn_cancel.setText(QCoreApplication.translate("LargeLoadDialog", u"Cancel", None))
        self.btn_add.setText(QCoreApplication.translate("LargeLoadDialog", u"Add Large Load", None))
    # retranslateUi

