# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_scenario.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_ViewScenarioDialog(object):
    def setupUi(self, ViewScenarioDialog):
        if not ViewScenarioDialog.objectName():
            ViewScenarioDialog.setObjectName(u"ViewScenarioDialog")
        ViewScenarioDialog.resize(780, 781)
        self.verticalLayout = QVBoxLayout(ViewScenarioDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_header = QFrame(ViewScenarioDialog)
        self.frame_header.setObjectName(u"frame_header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_header.sizePolicy().hasHeightForWidth())
        self.frame_header.setSizePolicy(sizePolicy)
        self.frame_header.setMaximumSize(QSize(16777215, 70))
        self.frame_header.setFrameShape(QFrame.NoFrame)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_header = QHBoxLayout(self.frame_header)
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.horizontalLayout_header.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_header_text = QVBoxLayout()
        self.verticalLayout_header_text.setSpacing(2)
        self.verticalLayout_header_text.setObjectName(u"verticalLayout_header_text")
        self.label_title = QLabel(self.frame_header)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout_header_text.addWidget(self.label_title)

        self.system_name_label = QLabel(self.frame_header)
        self.system_name_label.setObjectName(u"system_name_label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.system_name_label.setFont(font1)

        self.verticalLayout_header_text.addWidget(self.system_name_label)


        self.horizontalLayout_header.addLayout(self.verticalLayout_header_text)

        self.horizontalSpacer_header = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_header)

        self.pushButton = QPushButton(self.frame_header)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setFlat(True)

        self.horizontalLayout_header.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_header)

        self.frame_cards = QFrame(ViewScenarioDialog)
        self.frame_cards.setObjectName(u"frame_cards")
        self.frame_cards.setFrameShape(QFrame.NoFrame)
        self.frame_cards.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_cards = QHBoxLayout(self.frame_cards)
        self.horizontalLayout_cards.setSpacing(18)
        self.horizontalLayout_cards.setObjectName(u"horizontalLayout_cards")
        self.frame_planning_card = QFrame(self.frame_cards)
        self.frame_planning_card.setObjectName(u"frame_planning_card")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_planning_card.sizePolicy().hasHeightForWidth())
        self.frame_planning_card.setSizePolicy(sizePolicy1)
        self.frame_planning_card.setFrameShape(QFrame.NoFrame)
        self.frame_planning_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_planning = QVBoxLayout(self.frame_planning_card)
        self.verticalLayout_planning.setSpacing(10)
        self.verticalLayout_planning.setObjectName(u"verticalLayout_planning")
        self.verticalLayout_planning.setContentsMargins(18, 14, 18, 14)
        self.horizontalLayout_planning_title = QHBoxLayout()
        self.horizontalLayout_planning_title.setSpacing(8)
        self.horizontalLayout_planning_title.setObjectName(u"horizontalLayout_planning_title")
        self.label_planning_title = QLabel(self.frame_planning_card)
        self.label_planning_title.setObjectName(u"label_planning_title")
        self.label_planning_title.setFont(font1)

        self.horizontalLayout_planning_title.addWidget(self.label_planning_title)

        self.horizontalSpacer_planning_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_planning_title.addItem(self.horizontalSpacer_planning_title)


        self.verticalLayout_planning.addLayout(self.horizontalLayout_planning_title)

        self.label_planning_desc = QLabel(self.frame_planning_card)
        self.label_planning_desc.setObjectName(u"label_planning_desc")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        self.label_planning_desc.setFont(font2)
        self.label_planning_desc.setWordWrap(True)

        self.verticalLayout_planning.addWidget(self.label_planning_desc)

        self.verticalLayout_planning_rows = QVBoxLayout()
        self.verticalLayout_planning_rows.setSpacing(12)
        self.verticalLayout_planning_rows.setObjectName(u"verticalLayout_planning_rows")
        self.horizontalLayout_sim_years = QHBoxLayout()
        self.horizontalLayout_sim_years.setObjectName(u"horizontalLayout_sim_years")
        self.label_sim_years = QLabel(self.frame_planning_card)
        self.label_sim_years.setObjectName(u"label_sim_years")
        self.label_sim_years.setMinimumSize(QSize(120, 0))
        self.label_sim_years.setFont(font1)

        self.horizontalLayout_sim_years.addWidget(self.label_sim_years)

        self.sim_years_value = QLabel(self.frame_planning_card)
        self.sim_years_value.setObjectName(u"sim_years_value")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.sim_years_value.setFont(font3)
        self.sim_years_value.setWordWrap(True)

        self.horizontalLayout_sim_years.addWidget(self.sim_years_value)


        self.verticalLayout_planning_rows.addLayout(self.horizontalLayout_sim_years)

        self.horizontalLayout_trans_model = QHBoxLayout()
        self.horizontalLayout_trans_model.setObjectName(u"horizontalLayout_trans_model")
        self.label_trans_model = QLabel(self.frame_planning_card)
        self.label_trans_model.setObjectName(u"label_trans_model")
        self.label_trans_model.setMinimumSize(QSize(120, 0))
        self.label_trans_model.setFont(font1)

        self.horizontalLayout_trans_model.addWidget(self.label_trans_model)

        self.trans_model_value = QLabel(self.frame_planning_card)
        self.trans_model_value.setObjectName(u"trans_model_value")
        self.trans_model_value.setFont(font3)
        self.trans_model_value.setWordWrap(True)

        self.horizontalLayout_trans_model.addWidget(self.trans_model_value)


        self.verticalLayout_planning_rows.addLayout(self.horizontalLayout_trans_model)

        self.horizontalLayout_temporal = QHBoxLayout()
        self.horizontalLayout_temporal.setObjectName(u"horizontalLayout_temporal")
        self.label_temporal = QLabel(self.frame_planning_card)
        self.label_temporal.setObjectName(u"label_temporal")
        self.label_temporal.setMinimumSize(QSize(120, 0))
        self.label_temporal.setFont(font1)

        self.horizontalLayout_temporal.addWidget(self.label_temporal)

        self.temporal_value = QLabel(self.frame_planning_card)
        self.temporal_value.setObjectName(u"temporal_value")
        self.temporal_value.setFont(font3)
        self.temporal_value.setWordWrap(True)

        self.horizontalLayout_temporal.addWidget(self.temporal_value)


        self.verticalLayout_planning_rows.addLayout(self.horizontalLayout_temporal)

        self.horizontalLayout_discount = QHBoxLayout()
        self.horizontalLayout_discount.setObjectName(u"horizontalLayout_discount")
        self.label_discount = QLabel(self.frame_planning_card)
        self.label_discount.setObjectName(u"label_discount")
        self.label_discount.setMinimumSize(QSize(120, 0))
        self.label_discount.setFont(font1)

        self.horizontalLayout_discount.addWidget(self.label_discount)

        self.discount_value = QLabel(self.frame_planning_card)
        self.discount_value.setObjectName(u"discount_value")
        self.discount_value.setFont(font3)
        self.discount_value.setWordWrap(True)

        self.horizontalLayout_discount.addWidget(self.discount_value)


        self.verticalLayout_planning_rows.addLayout(self.horizontalLayout_discount)

        self.horizontalLayout_base_currency = QHBoxLayout()
        self.horizontalLayout_base_currency.setObjectName(u"horizontalLayout_base_currency")
        self.label_base_currency = QLabel(self.frame_planning_card)
        self.label_base_currency.setObjectName(u"label_base_currency")
        self.label_base_currency.setMinimumSize(QSize(120, 0))
        self.label_base_currency.setFont(font1)

        self.horizontalLayout_base_currency.addWidget(self.label_base_currency)

        self.base_currency_value = QLabel(self.frame_planning_card)
        self.base_currency_value.setObjectName(u"base_currency_value")
        self.base_currency_value.setFont(font3)
        self.base_currency_value.setWordWrap(True)

        self.horizontalLayout_base_currency.addWidget(self.base_currency_value)


        self.verticalLayout_planning_rows.addLayout(self.horizontalLayout_base_currency)


        self.verticalLayout_planning.addLayout(self.verticalLayout_planning_rows)

        self.verticalSpacer_planning = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_planning.addItem(self.verticalSpacer_planning)


        self.horizontalLayout_cards.addWidget(self.frame_planning_card)

        self.frame_scenario_card = QFrame(self.frame_cards)
        self.frame_scenario_card.setObjectName(u"frame_scenario_card")
        sizePolicy1.setHeightForWidth(self.frame_scenario_card.sizePolicy().hasHeightForWidth())
        self.frame_scenario_card.setSizePolicy(sizePolicy1)
        self.frame_scenario_card.setFrameShape(QFrame.NoFrame)
        self.frame_scenario_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_scenario = QVBoxLayout(self.frame_scenario_card)
        self.verticalLayout_scenario.setSpacing(10)
        self.verticalLayout_scenario.setObjectName(u"verticalLayout_scenario")
        self.verticalLayout_scenario.setContentsMargins(18, 14, 18, 14)
        self.horizontalLayout_scenario_title = QHBoxLayout()
        self.horizontalLayout_scenario_title.setSpacing(8)
        self.horizontalLayout_scenario_title.setObjectName(u"horizontalLayout_scenario_title")
        self.label_scenario_title = QLabel(self.frame_scenario_card)
        self.label_scenario_title.setObjectName(u"label_scenario_title")
        self.label_scenario_title.setFont(font1)

        self.horizontalLayout_scenario_title.addWidget(self.label_scenario_title)

        self.horizontalSpacer_scenario_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_scenario_title.addItem(self.horizontalSpacer_scenario_title)


        self.verticalLayout_scenario.addLayout(self.horizontalLayout_scenario_title)

        self.label_scenario_desc = QLabel(self.frame_scenario_card)
        self.label_scenario_desc.setObjectName(u"label_scenario_desc")
        self.label_scenario_desc.setFont(font2)
        self.label_scenario_desc.setWordWrap(True)

        self.verticalLayout_scenario.addWidget(self.label_scenario_desc)

        self.verticalLayout_scenario_rows = QVBoxLayout()
        self.verticalLayout_scenario_rows.setSpacing(10)
        self.verticalLayout_scenario_rows.setObjectName(u"verticalLayout_scenario_rows")
        self.horizontalLayout_capital_cost = QHBoxLayout()
        self.horizontalLayout_capital_cost.setObjectName(u"horizontalLayout_capital_cost")
        self.label_capital_cost = QLabel(self.frame_scenario_card)
        self.label_capital_cost.setObjectName(u"label_capital_cost")
        self.label_capital_cost.setMinimumSize(QSize(120, 0))
        self.label_capital_cost.setFont(font1)

        self.horizontalLayout_capital_cost.addWidget(self.label_capital_cost)

        self.capital_cost_value = QLabel(self.frame_scenario_card)
        self.capital_cost_value.setObjectName(u"capital_cost_value")
        self.capital_cost_value.setFont(font3)
        self.capital_cost_value.setWordWrap(True)

        self.horizontalLayout_capital_cost.addWidget(self.capital_cost_value)


        self.verticalLayout_scenario_rows.addLayout(self.horizontalLayout_capital_cost)

        self.horizontalLayout_load_forecast = QHBoxLayout()
        self.horizontalLayout_load_forecast.setObjectName(u"horizontalLayout_load_forecast")
        self.label_load_forecast = QLabel(self.frame_scenario_card)
        self.label_load_forecast.setObjectName(u"label_load_forecast")
        self.label_load_forecast.setMinimumSize(QSize(120, 0))
        self.label_load_forecast.setFont(font1)

        self.horizontalLayout_load_forecast.addWidget(self.label_load_forecast)

        self.load_forecast_value = QLabel(self.frame_scenario_card)
        self.load_forecast_value.setObjectName(u"load_forecast_value")
        self.load_forecast_value.setFont(font3)
        self.load_forecast_value.setWordWrap(True)

        self.horizontalLayout_load_forecast.addWidget(self.load_forecast_value)


        self.verticalLayout_scenario_rows.addLayout(self.horizontalLayout_load_forecast)

        self.horizontalLayout_load_growth = QHBoxLayout()
        self.horizontalLayout_load_growth.setObjectName(u"horizontalLayout_load_growth")
        self.label_load_growth = QLabel(self.frame_scenario_card)
        self.label_load_growth.setObjectName(u"label_load_growth")
        self.label_load_growth.setMinimumSize(QSize(120, 0))
        self.label_load_growth.setFont(font1)

        self.horizontalLayout_load_growth.addWidget(self.label_load_growth)

        self.annual_load_growth_value = QLabel(self.frame_scenario_card)
        self.annual_load_growth_value.setObjectName(u"annual_load_growth_value")
        self.annual_load_growth_value.setFont(font3)
        self.annual_load_growth_value.setWordWrap(True)

        self.horizontalLayout_load_growth.addWidget(self.annual_load_growth_value)


        self.verticalLayout_scenario_rows.addLayout(self.horizontalLayout_load_growth)

        self.horizontalLayout_rps = QHBoxLayout()
        self.horizontalLayout_rps.setObjectName(u"horizontalLayout_rps")
        self.label_rps = QLabel(self.frame_scenario_card)
        self.label_rps.setObjectName(u"label_rps")
        self.label_rps.setMinimumSize(QSize(120, 0))
        self.label_rps.setFont(font1)

        self.horizontalLayout_rps.addWidget(self.label_rps)

        self.rps_value = QTextBrowser(self.frame_scenario_card)
        self.rps_value.setObjectName(u"rps_value")
        self.rps_value.setMaximumSize(QSize(16777215, 48))
        self.rps_value.setFont(font3)

        self.horizontalLayout_rps.addWidget(self.rps_value)


        self.verticalLayout_scenario_rows.addLayout(self.horizontalLayout_rps)

        self.horizontalLayout_tx = QHBoxLayout()
        self.horizontalLayout_tx.setObjectName(u"horizontalLayout_tx")
        self.label_tx = QLabel(self.frame_scenario_card)
        self.label_tx.setObjectName(u"label_tx")
        self.label_tx.setMinimumSize(QSize(120, 0))
        self.label_tx.setFont(font1)

        self.horizontalLayout_tx.addWidget(self.label_tx)

        self.transmission_expansion_value = QLabel(self.frame_scenario_card)
        self.transmission_expansion_value.setObjectName(u"transmission_expansion_value")
        self.transmission_expansion_value.setFont(font3)
        self.transmission_expansion_value.setWordWrap(True)

        self.horizontalLayout_tx.addWidget(self.transmission_expansion_value)


        self.verticalLayout_scenario_rows.addLayout(self.horizontalLayout_tx)

        self.horizontalLayout_cand = QHBoxLayout()
        self.horizontalLayout_cand.setObjectName(u"horizontalLayout_cand")
        self.label_cand = QLabel(self.frame_scenario_card)
        self.label_cand.setObjectName(u"label_cand")
        self.label_cand.setMinimumSize(QSize(120, 0))
        self.label_cand.setFont(font1)

        self.horizontalLayout_cand.addWidget(self.label_cand)

        self.candidate_tech_value = QTextBrowser(self.frame_scenario_card)
        self.candidate_tech_value.setObjectName(u"candidate_tech_value")
        self.candidate_tech_value.setMaximumSize(QSize(16777215, 48))
        self.candidate_tech_value.setFont(font3)

        self.horizontalLayout_cand.addWidget(self.candidate_tech_value)


        self.verticalLayout_scenario_rows.addLayout(self.horizontalLayout_cand)

        self.horizontalLayout_retirement = QHBoxLayout()
        self.horizontalLayout_retirement.setObjectName(u"horizontalLayout_retirement")
        self.label_retirement = QLabel(self.frame_scenario_card)
        self.label_retirement.setObjectName(u"label_retirement")
        self.label_retirement.setMinimumSize(QSize(120, 0))
        self.label_retirement.setFont(font1)

        self.horizontalLayout_retirement.addWidget(self.label_retirement)

        self.retirement_value = QTextBrowser(self.frame_scenario_card)
        self.retirement_value.setObjectName(u"retirement_value")
        self.retirement_value.setMaximumSize(QSize(16777215, 48))
        self.retirement_value.setFont(font3)

        self.horizontalLayout_retirement.addWidget(self.retirement_value)


        self.verticalLayout_scenario_rows.addLayout(self.horizontalLayout_retirement)


        self.verticalLayout_scenario.addLayout(self.verticalLayout_scenario_rows)

        self.verticalSpacer_scenario = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_scenario.addItem(self.verticalSpacer_scenario)


        self.horizontalLayout_cards.addWidget(self.frame_scenario_card)


        self.verticalLayout.addWidget(self.frame_cards)

        self.frame_footer = QFrame(ViewScenarioDialog)
        self.frame_footer.setObjectName(u"frame_footer")
        sizePolicy.setHeightForWidth(self.frame_footer.sizePolicy().hasHeightForWidth())
        self.frame_footer.setSizePolicy(sizePolicy)
        self.frame_footer.setMaximumSize(QSize(16777215, 52))
        self.frame_footer.setFrameShape(QFrame.NoFrame)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_footer = QHBoxLayout(self.frame_footer)
        self.horizontalLayout_footer.setObjectName(u"horizontalLayout_footer")
        self.horizontalLayout_footer.setContentsMargins(0, 0, 0, 0)
        self.label_save_hint = QLabel(self.frame_footer)
        self.label_save_hint.setObjectName(u"label_save_hint")
        self.label_save_hint.setFont(font3)

        self.horizontalLayout_footer.addWidget(self.label_save_hint)

        self.horizontalSpacer_footer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_footer.addItem(self.horizontalSpacer_footer)

        self.close_button = QPushButton(self.frame_footer)
        self.close_button.setObjectName(u"close_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy2)
        self.close_button.setMinimumSize(QSize(110, 0))
        self.close_button.setFont(font1)

        self.horizontalLayout_footer.addWidget(self.close_button)

        self.save_scenario_button = QPushButton(self.frame_footer)
        self.save_scenario_button.setObjectName(u"save_scenario_button")
        sizePolicy2.setHeightForWidth(self.save_scenario_button.sizePolicy().hasHeightForWidth())
        self.save_scenario_button.setSizePolicy(sizePolicy2)
        self.save_scenario_button.setMinimumSize(QSize(180, 0))
        self.save_scenario_button.setFont(font1)

        self.horizontalLayout_footer.addWidget(self.save_scenario_button)


        self.verticalLayout.addWidget(self.frame_footer)


        self.retranslateUi(ViewScenarioDialog)

        QMetaObject.connectSlotsByName(ViewScenarioDialog)
    # setupUi

    def retranslateUi(self, ViewScenarioDialog):
        ViewScenarioDialog.setWindowTitle(QCoreApplication.translate("ViewScenarioDialog", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("ViewScenarioDialog", u"Scenario Summary", None))
        self.label_title.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"heading", None))
        self.system_name_label.setText(QCoreApplication.translate("ViewScenarioDialog", u"Power System: --", None))
        self.system_name_label.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"subtitle", None))
        self.pushButton.setText("")
        self.frame_planning_card.setProperty("cardType", QCoreApplication.translate("ViewScenarioDialog", u"card", None))
        self.label_planning_title.setText(QCoreApplication.translate("ViewScenarioDialog", u"PLANNING MODEL INFORMATION", None))
        self.label_planning_title.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.label_planning_desc.setText(QCoreApplication.translate("ViewScenarioDialog", u"Settings defined in the <i>Planning Model Setup</i> step.", None))
        self.label_planning_desc.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"caption", None))
        self.label_sim_years.setText(QCoreApplication.translate("ViewScenarioDialog", u"Simulation Years", None))
        self.label_sim_years.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.sim_years_value.setText(QCoreApplication.translate("ViewScenarioDialog", u"--", None))
        self.label_trans_model.setText(QCoreApplication.translate("ViewScenarioDialog", u"Transmission Model", None))
        self.label_trans_model.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.trans_model_value.setText(QCoreApplication.translate("ViewScenarioDialog", u"--", None))
        self.label_temporal.setText(QCoreApplication.translate("ViewScenarioDialog", u"Temporal Selection", None))
        self.label_temporal.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.temporal_value.setText(QCoreApplication.translate("ViewScenarioDialog", u"--", None))
        self.label_discount.setText(QCoreApplication.translate("ViewScenarioDialog", u"Discount Rate", None))
        self.label_discount.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.discount_value.setText(QCoreApplication.translate("ViewScenarioDialog", u"--", None))
        self.label_base_currency.setText(QCoreApplication.translate("ViewScenarioDialog", u"Base Currency Year", None))
        self.label_base_currency.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.base_currency_value.setText(QCoreApplication.translate("ViewScenarioDialog", u"--", None))
        self.frame_scenario_card.setProperty("cardType", QCoreApplication.translate("ViewScenarioDialog", u"card", None))
        self.label_scenario_title.setText(QCoreApplication.translate("ViewScenarioDialog", u"SCENARIO INFORMATION", None))
        self.label_scenario_title.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.label_scenario_desc.setText(QCoreApplication.translate("ViewScenarioDialog", u"Settings defined in the <i>Scenario Builder</i> step.", None))
        self.label_scenario_desc.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"caption", None))
        self.label_capital_cost.setText(QCoreApplication.translate("ViewScenarioDialog", u"Capital Costs", None))
        self.label_capital_cost.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.capital_cost_value.setText(QCoreApplication.translate("ViewScenarioDialog", u"--", None))
        self.label_load_forecast.setText(QCoreApplication.translate("ViewScenarioDialog", u"Load Forecast", None))
        self.label_load_forecast.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.load_forecast_value.setText(QCoreApplication.translate("ViewScenarioDialog", u"--", None))
        self.label_load_growth.setText(QCoreApplication.translate("ViewScenarioDialog", u"Annual Load Growth", None))
        self.label_load_growth.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.annual_load_growth_value.setText(QCoreApplication.translate("ViewScenarioDialog", u"--", None))
        self.label_rps.setText(QCoreApplication.translate("ViewScenarioDialog", u"Future Generation Mix", None))
        self.label_rps.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.label_tx.setText(QCoreApplication.translate("ViewScenarioDialog", u"Transmission Expansion", None))
        self.label_tx.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.transmission_expansion_value.setText(QCoreApplication.translate("ViewScenarioDialog", u"--", None))
        self.label_cand.setText(QCoreApplication.translate("ViewScenarioDialog", u"Candidate Technologies", None))
        self.label_cand.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.label_retirement.setText(QCoreApplication.translate("ViewScenarioDialog", u"Retirement Schedule", None))
        self.label_retirement.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"section", None))
        self.label_save_hint.setText(QCoreApplication.translate("ViewScenarioDialog", u"Save a text summary of this <i>QuESt Planning</i> scenario.", None))
        self.label_save_hint.setProperty("textRole", QCoreApplication.translate("ViewScenarioDialog", u"subtitle", None))
        self.close_button.setText(QCoreApplication.translate("ViewScenarioDialog", u"Close", None))
        self.save_scenario_button.setText(QCoreApplication.translate("ViewScenarioDialog", u"Save Scenario Info", None))
        self.save_scenario_button.setProperty("btnRole", QCoreApplication.translate("ViewScenarioDialog", u"primary", None))
    # retranslateUi

