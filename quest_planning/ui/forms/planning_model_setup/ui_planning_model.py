# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'planning_model.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_PlanningModelPage(object):
    def setupUi(self, PlanningModelPage):
        if not PlanningModelPage.objectName():
            PlanningModelPage.setObjectName(u"PlanningModelPage")
        PlanningModelPage.resize(740, 733)
        self.verticalLayout = QVBoxLayout(PlanningModelPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_header = QFrame(PlanningModelPage)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setFrameShape(QFrame.NoFrame)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_header)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_title = QLabel(self.frame_header)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout_8.addWidget(self.label_title)

        self.label_subtitle = QLabel(self.frame_header)
        self.label_subtitle.setObjectName(u"label_subtitle")

        self.verticalLayout_8.addWidget(self.label_subtitle)


        self.verticalLayout.addWidget(self.frame_header)

        self.groupBox_model = QGroupBox(PlanningModelPage)
        self.groupBox_model.setObjectName(u"groupBox_model")
        self.gridLayout = QGridLayout(self.groupBox_model)
        self.gridLayout.setObjectName(u"gridLayout")
        self.base_currency_year = QLineEdit(self.groupBox_model)
        self.base_currency_year.setObjectName(u"base_currency_year")

        self.gridLayout.addWidget(self.base_currency_year, 5, 1, 1, 1)

        self.label_temporal = QLabel(self.groupBox_model)
        self.label_temporal.setObjectName(u"label_temporal")

        self.gridLayout.addWidget(self.label_temporal, 3, 0, 1, 1)

        self.label_base_currency = QLabel(self.groupBox_model)
        self.label_base_currency.setObjectName(u"label_base_currency")

        self.gridLayout.addWidget(self.label_base_currency, 5, 0, 1, 1)

        self.label_annual_discount = QLabel(self.groupBox_model)
        self.label_annual_discount.setObjectName(u"label_annual_discount")

        self.gridLayout.addWidget(self.label_annual_discount, 4, 0, 1, 1)

        self.transmission_box = QComboBox(self.groupBox_model)
        self.transmission_box.addItem("")
        self.transmission_box.addItem("")
        self.transmission_box.addItem("")
        self.transmission_box.setObjectName(u"transmission_box")

        self.gridLayout.addWidget(self.transmission_box, 2, 1, 1, 1)

        self.annual_discount_factor = QDoubleSpinBox(self.groupBox_model)
        self.annual_discount_factor.setObjectName(u"annual_discount_factor")

        self.gridLayout.addWidget(self.annual_discount_factor, 4, 1, 1, 1)

        self.button_trans_help = QPushButton(self.groupBox_model)
        self.button_trans_help.setObjectName(u"button_trans_help")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_trans_help.sizePolicy().hasHeightForWidth())
        self.button_trans_help.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_trans_help.setIcon(icon)
        self.button_trans_help.setIconSize(QSize(30, 30))
        self.button_trans_help.setFlat(True)

        self.gridLayout.addWidget(self.button_trans_help, 2, 2, 1, 1)

        self.button_temporal_help = QPushButton(self.groupBox_model)
        self.button_temporal_help.setObjectName(u"button_temporal_help")
        sizePolicy.setHeightForWidth(self.button_temporal_help.sizePolicy().hasHeightForWidth())
        self.button_temporal_help.setSizePolicy(sizePolicy)
        self.button_temporal_help.setIcon(icon)
        self.button_temporal_help.setIconSize(QSize(30, 30))
        self.button_temporal_help.setFlat(True)

        self.gridLayout.addWidget(self.button_temporal_help, 3, 2, 1, 1)

        self.frame_8 = QFrame(self.groupBox_model)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.frame_dates = QFrame(self.frame_8)
        self.frame_dates.setObjectName(u"frame_dates")
        self.frame_dates.setFrameShape(QFrame.NoFrame)
        self.frame_dates.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_dates)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.dateEdit_start = QDateEdit(self.frame_dates)
        self.dateEdit_start.setObjectName(u"dateEdit_start")

        self.gridLayout_2.addWidget(self.dateEdit_start, 0, 1, 1, 1)

        self.label_start = QLabel(self.frame_dates)
        self.label_start.setObjectName(u"label_start")

        self.gridLayout_2.addWidget(self.label_start, 0, 0, 1, 1)

        self.label_end = QLabel(self.frame_dates)
        self.label_end.setObjectName(u"label_end")

        self.gridLayout_2.addWidget(self.label_end, 1, 0, 1, 1)

        self.dateEdit_end = QDateEdit(self.frame_dates)
        self.dateEdit_end.setObjectName(u"dateEdit_end")
        self.dateEdit_end.setCurrentSection(QDateTimeEdit.YearSection)

        self.gridLayout_2.addWidget(self.dateEdit_end, 1, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_dates)

        self.button_years_select = QPushButton(self.frame_8)
        self.button_years_select.setObjectName(u"button_years_select")

        self.horizontalLayout_4.addWidget(self.button_years_select)

        self.button_sim_help = QPushButton(self.frame_8)
        self.button_sim_help.setObjectName(u"button_sim_help")
        sizePolicy.setHeightForWidth(self.button_sim_help.sizePolicy().hasHeightForWidth())
        self.button_sim_help.setSizePolicy(sizePolicy)
        self.button_sim_help.setIcon(icon)
        self.button_sim_help.setIconSize(QSize(30, 30))
        self.button_sim_help.setFlat(True)

        self.horizontalLayout_4.addWidget(self.button_sim_help)


        self.gridLayout.addWidget(self.frame_8, 0, 0, 1, 3)

        self.button_discount_help = QPushButton(self.groupBox_model)
        self.button_discount_help.setObjectName(u"button_discount_help")
        sizePolicy.setHeightForWidth(self.button_discount_help.sizePolicy().hasHeightForWidth())
        self.button_discount_help.setSizePolicy(sizePolicy)
        self.button_discount_help.setIcon(icon)
        self.button_discount_help.setIconSize(QSize(30, 30))
        self.button_discount_help.setFlat(True)

        self.gridLayout.addWidget(self.button_discount_help, 4, 2, 1, 1)

        self.button_base_help = QPushButton(self.groupBox_model)
        self.button_base_help.setObjectName(u"button_base_help")
        sizePolicy.setHeightForWidth(self.button_base_help.sizePolicy().hasHeightForWidth())
        self.button_base_help.setSizePolicy(sizePolicy)
        self.button_base_help.setIcon(icon)
        self.button_base_help.setIconSize(QSize(30, 30))
        self.button_base_help.setFlat(True)

        self.gridLayout.addWidget(self.button_base_help, 5, 2, 1, 1)

        self.hline1 = QFrame(self.groupBox_model)
        self.hline1.setObjectName(u"hline1")
        self.hline1.setFrameShape(QFrame.HLine)
        self.hline1.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.hline1, 6, 1, 1, 1)

        self.temporal_box = QComboBox(self.groupBox_model)
        self.temporal_box.addItem("")
        self.temporal_box.addItem("")
        self.temporal_box.addItem("")
        self.temporal_box.setObjectName(u"temporal_box")

        self.gridLayout.addWidget(self.temporal_box, 3, 1, 1, 1)

        self.label_transmission = QLabel(self.groupBox_model)
        self.label_transmission.setObjectName(u"label_transmission")

        self.gridLayout.addWidget(self.label_transmission, 2, 0, 1, 1)

        self.advanced_settings_button = QPushButton(self.groupBox_model)
        self.advanced_settings_button.setObjectName(u"advanced_settings_button")

        self.gridLayout.addWidget(self.advanced_settings_button, 7, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_model)

        self.groupBox_summary = QGroupBox(PlanningModelPage)
        self.groupBox_summary.setObjectName(u"groupBox_summary")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.groupBox_summary.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.groupBox_summary)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_sim = QFrame(self.groupBox_summary)
        self.frame_sim.setObjectName(u"frame_sim")
        self.frame_sim.setFrameShape(QFrame.StyledPanel)
        self.frame_sim.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_sim)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_years = QLabel(self.frame_sim)
        self.label_years.setObjectName(u"label_years")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_years.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_years)

        self.label_years_input = QLabel(self.frame_sim)
        self.label_years_input.setObjectName(u"label_years_input")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.label_years_input.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_years_input)


        self.horizontalLayout.addWidget(self.frame_sim)

        self.frame_transmission = QFrame(self.groupBox_summary)
        self.frame_transmission.setObjectName(u"frame_transmission")
        self.frame_transmission.setFrameShape(QFrame.StyledPanel)
        self.frame_transmission.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_transmission)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_trans = QLabel(self.frame_transmission)
        self.label_trans.setObjectName(u"label_trans")
        self.label_trans.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_trans)

        self.label_trans_input = QLabel(self.frame_transmission)
        self.label_trans_input.setObjectName(u"label_trans_input")
        self.label_trans_input.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_trans_input)


        self.horizontalLayout.addWidget(self.frame_transmission)

        self.frame_temporal = QFrame(self.groupBox_summary)
        self.frame_temporal.setObjectName(u"frame_temporal")
        self.frame_temporal.setFrameShape(QFrame.StyledPanel)
        self.frame_temporal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_temporal)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_temp = QLabel(self.frame_temporal)
        self.label_temp.setObjectName(u"label_temp")
        self.label_temp.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_temp)

        self.label_temp_input = QLabel(self.frame_temporal)
        self.label_temp_input.setObjectName(u"label_temp_input")
        self.label_temp_input.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_temp_input)


        self.horizontalLayout.addWidget(self.frame_temporal)

        self.frame_discount = QFrame(self.groupBox_summary)
        self.frame_discount.setObjectName(u"frame_discount")
        self.frame_discount.setFrameShape(QFrame.StyledPanel)
        self.frame_discount.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_discount)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_discount = QLabel(self.frame_discount)
        self.label_discount.setObjectName(u"label_discount")
        self.label_discount.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_discount)

        self.label_discount_input = QLabel(self.frame_discount)
        self.label_discount_input.setObjectName(u"label_discount_input")
        self.label_discount_input.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_discount_input)


        self.horizontalLayout.addWidget(self.frame_discount)

        self.frame_currency = QFrame(self.groupBox_summary)
        self.frame_currency.setObjectName(u"frame_currency")
        self.frame_currency.setFrameShape(QFrame.StyledPanel)
        self.frame_currency.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_currency)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_currency = QLabel(self.frame_currency)
        self.label_currency.setObjectName(u"label_currency")
        self.label_currency.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_currency)

        self.label_currency_input = QLabel(self.frame_currency)
        self.label_currency_input.setObjectName(u"label_currency_input")
        self.label_currency_input.setFont(font3)

        self.verticalLayout_7.addWidget(self.label_currency_input)


        self.horizontalLayout.addWidget(self.frame_currency)


        self.verticalLayout.addWidget(self.groupBox_summary)


        self.retranslateUi(PlanningModelPage)

        QMetaObject.connectSlotsByName(PlanningModelPage)
    # setupUi

    def retranslateUi(self, PlanningModelPage):
        PlanningModelPage.setWindowTitle(QCoreApplication.translate("PlanningModelPage", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("PlanningModelPage", u"Planning Model Setup", None))
        self.label_subtitle.setText(QCoreApplication.translate("PlanningModelPage", u"Configure the simulation years, transmission model, temporal resolution, and economic parameters.", None))
        self.groupBox_model.setTitle(QCoreApplication.translate("PlanningModelPage", u"Model Configuration", None))
        self.base_currency_year.setText(QCoreApplication.translate("PlanningModelPage", u"2000", None))
        self.label_temporal.setText(QCoreApplication.translate("PlanningModelPage", u"Temporal Selection", None))
        self.label_base_currency.setText(QCoreApplication.translate("PlanningModelPage", u"Base Currency Year", None))
        self.label_annual_discount.setText(QCoreApplication.translate("PlanningModelPage", u"Annual Discount Rate", None))
        self.transmission_box.setItemText(0, QCoreApplication.translate("PlanningModelPage", u"Transportation (Pipe & Bubble)", None))
        self.transmission_box.setItemText(1, QCoreApplication.translate("PlanningModelPage", u"Copper Sheet", None))
        self.transmission_box.setItemText(2, QCoreApplication.translate("PlanningModelPage", u"DC Power Flow (Upcoming)", None))

        self.button_trans_help.setText("")
        self.button_temporal_help.setText("")
        self.dateEdit_start.setDisplayFormat(QCoreApplication.translate("PlanningModelPage", u"yyyy", None))
        self.label_start.setText(QCoreApplication.translate("PlanningModelPage", u"Start Year", None))
        self.label_end.setText(QCoreApplication.translate("PlanningModelPage", u"End Year", None))
        self.dateEdit_end.setDisplayFormat(QCoreApplication.translate("PlanningModelPage", u"yyyy", None))
        self.button_years_select.setText(QCoreApplication.translate("PlanningModelPage", u"Select Simulation Years", None))
        self.button_sim_help.setText("")
        self.button_discount_help.setText("")
        self.button_base_help.setText("")
        self.temporal_box.setItemText(0, QCoreApplication.translate("PlanningModelPage", u"Representative Weeks", None))
        self.temporal_box.setItemText(1, QCoreApplication.translate("PlanningModelPage", u"Seasonal Blocks", None))
        self.temporal_box.setItemText(2, QCoreApplication.translate("PlanningModelPage", u"8760 Analysis (Upcoming)", None))

        self.label_transmission.setText(QCoreApplication.translate("PlanningModelPage", u"Transmission Model", None))
        self.advanced_settings_button.setText(QCoreApplication.translate("PlanningModelPage", u"Advanced Settings", None))
        self.groupBox_summary.setTitle(QCoreApplication.translate("PlanningModelPage", u"Selection Summary", None))
        self.label_years.setText(QCoreApplication.translate("PlanningModelPage", u"Simulation Years", None))
        self.label_years_input.setText(QCoreApplication.translate("PlanningModelPage", u"----", None))
        self.label_trans.setText(QCoreApplication.translate("PlanningModelPage", u"Transmission Model", None))
        self.label_trans_input.setText(QCoreApplication.translate("PlanningModelPage", u"----", None))
        self.label_temp.setText(QCoreApplication.translate("PlanningModelPage", u"Temporal Selection", None))
        self.label_temp_input.setText(QCoreApplication.translate("PlanningModelPage", u"----", None))
        self.label_discount.setText(QCoreApplication.translate("PlanningModelPage", u"Discount Rate", None))
        self.label_discount_input.setText(QCoreApplication.translate("PlanningModelPage", u"----", None))
        self.label_currency.setText(QCoreApplication.translate("PlanningModelPage", u"Base Currency Year", None))
        self.label_currency_input.setText(QCoreApplication.translate("PlanningModelPage", u"----", None))
    # retranslateUi

