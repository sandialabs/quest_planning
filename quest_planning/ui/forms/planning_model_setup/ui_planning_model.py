# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'planning_model.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_PlanningModelPage(object):
    def setupUi(self, PlanningModelPage):
        if not PlanningModelPage.objectName():
            PlanningModelPage.setObjectName(u"PlanningModelPage")
        PlanningModelPage.resize(760, 781)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlanningModelPage.sizePolicy().hasHeightForWidth())
        PlanningModelPage.setSizePolicy(sizePolicy)
        self.verticalLayout_main = QVBoxLayout(PlanningModelPage)
        self.verticalLayout_main.setSpacing(18)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(24, 24, 24, 24)
        self.frame_header = QFrame(PlanningModelPage)
        self.frame_header.setObjectName(u"frame_header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_header.sizePolicy().hasHeightForWidth())
        self.frame_header.setSizePolicy(sizePolicy1)
        self.frame_header.setMaximumSize(QSize(16777215, 80))
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

        self.label_subtitle = QLabel(self.frame_header)
        self.label_subtitle.setObjectName(u"label_subtitle")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.label_subtitle.setFont(font1)

        self.verticalLayout_header_text.addWidget(self.label_subtitle)


        self.horizontalLayout_header.addLayout(self.verticalLayout_header_text)

        self.horizontalSpacer_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_header)

        self.planning_model_help_button = QToolButton(self.frame_header)
        self.planning_model_help_button.setObjectName(u"planning_model_help_button")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/help_FILL0_wght200_GRAD0_opsz48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.planning_model_help_button.setIcon(icon)
        self.planning_model_help_button.setIconSize(QSize(24, 24))
        self.planning_model_help_button.setAutoRaise(True)

        self.horizontalLayout_header.addWidget(self.planning_model_help_button)


        self.verticalLayout_main.addWidget(self.frame_header)

        self.frame_config = QFrame(PlanningModelPage)
        self.frame_config.setObjectName(u"frame_config")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_config.sizePolicy().hasHeightForWidth())
        self.frame_config.setSizePolicy(sizePolicy2)
        self.frame_config.setMaximumSize(QSize(16777215, 430))
        self.frame_config.setFrameShape(QFrame.NoFrame)
        self.frame_config.setFrameShadow(QFrame.Raised)
        self.verticalLayout_config = QVBoxLayout(self.frame_config)
        self.verticalLayout_config.setSpacing(12)
        self.verticalLayout_config.setObjectName(u"verticalLayout_config")
        self.verticalLayout_config.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_config_title = QHBoxLayout()
        self.horizontalLayout_config_title.setSpacing(8)
        self.horizontalLayout_config_title.setObjectName(u"horizontalLayout_config_title")
        self.label_config_icon = QLabel(self.frame_config)
        self.label_config_icon.setObjectName(u"label_config_icon")
        self.label_config_icon.setMaximumSize(QSize(22, 22))
        self.label_config_icon.setPixmap(QPixmap(u":/icon/images/icons/token_FILL0_wght200_GRAD0_opsz48.png"))
        self.label_config_icon.setScaledContents(True)

        self.horizontalLayout_config_title.addWidget(self.label_config_icon)

        self.label_config_title = QLabel(self.frame_config)
        self.label_config_title.setObjectName(u"label_config_title")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_config_title.setFont(font2)

        self.horizontalLayout_config_title.addWidget(self.label_config_title)

        self.horizontalSpacer_config_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_config_title.addItem(self.horizontalSpacer_config_title)


        self.verticalLayout_config.addLayout(self.horizontalLayout_config_title)

        self.gridLayout_config = QGridLayout()
        self.gridLayout_config.setObjectName(u"gridLayout_config")
        self.gridLayout_config.setHorizontalSpacing(14)
        self.gridLayout_config.setVerticalSpacing(12)
        self.label_begin = QLabel(self.frame_config)
        self.label_begin.setObjectName(u"label_begin")
        self.label_begin.setMinimumSize(QSize(160, 0))
        self.label_begin.setFont(font2)
        self.label_begin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_config.addWidget(self.label_begin, 0, 0, 1, 1)

        self.begin_date = QDateEdit(self.frame_config)
        self.begin_date.setObjectName(u"begin_date")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.begin_date.sizePolicy().hasHeightForWidth())
        self.begin_date.setSizePolicy(sizePolicy3)
        self.begin_date.setMaximumSize(QSize(220, 16777215))
        self.begin_date.setFont(font1)
        self.begin_date.setDate(QDate(2022, 1, 1))

        self.gridLayout_config.addWidget(self.begin_date, 0, 1, 1, 1)

        self.label_end = QLabel(self.frame_config)
        self.label_end.setObjectName(u"label_end")
        self.label_end.setMinimumSize(QSize(160, 0))
        self.label_end.setFont(font2)
        self.label_end.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_config.addWidget(self.label_end, 0, 2, 1, 1)

        self.end_date = QDateEdit(self.frame_config)
        self.end_date.setObjectName(u"end_date")
        sizePolicy3.setHeightForWidth(self.end_date.sizePolicy().hasHeightForWidth())
        self.end_date.setSizePolicy(sizePolicy3)
        self.end_date.setMaximumSize(QSize(220, 16777215))
        self.end_date.setFont(font1)
        self.end_date.setCurrentSection(QDateTimeEdit.YearSection)
        self.end_date.setDate(QDate(2042, 1, 1))

        self.gridLayout_config.addWidget(self.end_date, 0, 3, 1, 1)

        self.horizontalSpacer_years = QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_config.addItem(self.horizontalSpacer_years, 1, 0, 1, 1)

        self.select_years_button = QPushButton(self.frame_config)
        self.select_years_button.setObjectName(u"select_years_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.select_years_button.sizePolicy().hasHeightForWidth())
        self.select_years_button.setSizePolicy(sizePolicy4)
        self.select_years_button.setMinimumSize(QSize(200, 0))
        self.select_years_button.setFont(font2)

        self.gridLayout_config.addWidget(self.select_years_button, 1, 1, 1, 1)

        self.select_simulation_years_help_button = QToolButton(self.frame_config)
        self.select_simulation_years_help_button.setObjectName(u"select_simulation_years_help_button")
        self.select_simulation_years_help_button.setIcon(icon)
        self.select_simulation_years_help_button.setIconSize(QSize(20, 20))
        self.select_simulation_years_help_button.setAutoRaise(True)

        self.gridLayout_config.addWidget(self.select_simulation_years_help_button, 1, 3, 1, 1)

        self.label_3 = QLabel(self.frame_config)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_config.addWidget(self.label_3, 2, 0, 1, 1)

        self.transmission_box = QComboBox(self.frame_config)
        self.transmission_box.addItem("")
        self.transmission_box.addItem("")
        self.transmission_box.addItem("")
        self.transmission_box.setObjectName(u"transmission_box")
        sizePolicy3.setHeightForWidth(self.transmission_box.sizePolicy().hasHeightForWidth())
        self.transmission_box.setSizePolicy(sizePolicy3)
        self.transmission_box.setMaximumSize(QSize(500, 16777215))
        self.transmission_box.setFont(font1)

        self.gridLayout_config.addWidget(self.transmission_box, 2, 1, 1, 1)

        self.transmission_model_help_button = QToolButton(self.frame_config)
        self.transmission_model_help_button.setObjectName(u"transmission_model_help_button")
        self.transmission_model_help_button.setIcon(icon)
        self.transmission_model_help_button.setIconSize(QSize(20, 20))
        self.transmission_model_help_button.setAutoRaise(True)

        self.gridLayout_config.addWidget(self.transmission_model_help_button, 2, 3, 1, 1)

        self.label_5 = QLabel(self.frame_config)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_config.addWidget(self.label_5, 3, 0, 1, 1)

        self.temporal_box = QComboBox(self.frame_config)
        self.temporal_box.addItem("")
        self.temporal_box.addItem("")
        self.temporal_box.addItem("")
        self.temporal_box.setObjectName(u"temporal_box")
        sizePolicy3.setHeightForWidth(self.temporal_box.sizePolicy().hasHeightForWidth())
        self.temporal_box.setSizePolicy(sizePolicy3)
        self.temporal_box.setMaximumSize(QSize(500, 16777215))
        self.temporal_box.setFont(font1)

        self.gridLayout_config.addWidget(self.temporal_box, 3, 1, 1, 1)

        self.temporal_selection_help_button = QToolButton(self.frame_config)
        self.temporal_selection_help_button.setObjectName(u"temporal_selection_help_button")
        self.temporal_selection_help_button.setIcon(icon)
        self.temporal_selection_help_button.setIconSize(QSize(20, 20))
        self.temporal_selection_help_button.setAutoRaise(True)

        self.gridLayout_config.addWidget(self.temporal_selection_help_button, 3, 3, 1, 1)

        self.label = QLabel(self.frame_config)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_config.addWidget(self.label, 4, 0, 1, 1)

        self.annual_discount_factor = QDoubleSpinBox(self.frame_config)
        self.annual_discount_factor.setObjectName(u"annual_discount_factor")
        sizePolicy3.setHeightForWidth(self.annual_discount_factor.sizePolicy().hasHeightForWidth())
        self.annual_discount_factor.setSizePolicy(sizePolicy3)
        self.annual_discount_factor.setMaximumSize(QSize(220, 16777215))
        self.annual_discount_factor.setFont(font1)
        self.annual_discount_factor.setDecimals(2)
        self.annual_discount_factor.setMinimum(0.500000000000000)
        self.annual_discount_factor.setMaximum(50.000000000000000)
        self.annual_discount_factor.setValue(5.000000000000000)

        self.gridLayout_config.addWidget(self.annual_discount_factor, 4, 1, 1, 1)

        self.discount_rate_help_button = QToolButton(self.frame_config)
        self.discount_rate_help_button.setObjectName(u"discount_rate_help_button")
        self.discount_rate_help_button.setIcon(icon)
        self.discount_rate_help_button.setIconSize(QSize(20, 20))
        self.discount_rate_help_button.setAutoRaise(True)

        self.gridLayout_config.addWidget(self.discount_rate_help_button, 4, 3, 1, 1)

        self.label_7 = QLabel(self.frame_config)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_config.addWidget(self.label_7, 5, 0, 1, 1)

        self.base_currency_year = QLineEdit(self.frame_config)
        self.base_currency_year.setObjectName(u"base_currency_year")
        sizePolicy3.setHeightForWidth(self.base_currency_year.sizePolicy().hasHeightForWidth())
        self.base_currency_year.setSizePolicy(sizePolicy3)
        self.base_currency_year.setMaximumSize(QSize(220, 16777215))
        self.base_currency_year.setFont(font1)

        self.gridLayout_config.addWidget(self.base_currency_year, 5, 1, 1, 1)

        self.base_currency_help_button = QToolButton(self.frame_config)
        self.base_currency_help_button.setObjectName(u"base_currency_help_button")
        self.base_currency_help_button.setIcon(icon)
        self.base_currency_help_button.setIconSize(QSize(20, 20))
        self.base_currency_help_button.setAutoRaise(True)

        self.gridLayout_config.addWidget(self.base_currency_help_button, 5, 3, 1, 1)


        self.verticalLayout_config.addLayout(self.gridLayout_config)

        self.line_divider = QFrame(self.frame_config)
        self.line_divider.setObjectName(u"line_divider")
        self.line_divider.setMaximumSize(QSize(16777215, 1))
        self.line_divider.setFrameShape(QFrame.Shape.HLine)
        self.line_divider.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_config.addWidget(self.line_divider)

        self.horizontalLayout_advanced = QHBoxLayout()
        self.horizontalLayout_advanced.setSpacing(10)
        self.horizontalLayout_advanced.setObjectName(u"horizontalLayout_advanced")
        self.horizontalSpacer_advanced = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_advanced.addItem(self.horizontalSpacer_advanced)

        self.advanced_settings_button = QPushButton(self.frame_config)
        self.advanced_settings_button.setObjectName(u"advanced_settings_button")
        sizePolicy4.setHeightForWidth(self.advanced_settings_button.sizePolicy().hasHeightForWidth())
        self.advanced_settings_button.setSizePolicy(sizePolicy4)
        self.advanced_settings_button.setMinimumSize(QSize(190, 0))
        self.advanced_settings_button.setFont(font2)

        self.horizontalLayout_advanced.addWidget(self.advanced_settings_button)


        self.verticalLayout_config.addLayout(self.horizontalLayout_advanced)


        self.verticalLayout_main.addWidget(self.frame_config)

        self.planning_model_info_frame = QFrame(PlanningModelPage)
        self.planning_model_info_frame.setObjectName(u"planning_model_info_frame")
        sizePolicy2.setHeightForWidth(self.planning_model_info_frame.sizePolicy().hasHeightForWidth())
        self.planning_model_info_frame.setSizePolicy(sizePolicy2)
        self.planning_model_info_frame.setMaximumSize(QSize(16777215, 170))
        self.planning_model_info_frame.setFrameShape(QFrame.NoFrame)
        self.planning_model_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_summary = QVBoxLayout(self.planning_model_info_frame)
        self.verticalLayout_summary.setSpacing(10)
        self.verticalLayout_summary.setObjectName(u"verticalLayout_summary")
        self.verticalLayout_summary.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_summary_title = QHBoxLayout()
        self.horizontalLayout_summary_title.setSpacing(8)
        self.horizontalLayout_summary_title.setObjectName(u"horizontalLayout_summary_title")
        self.label_summary_icon = QLabel(self.planning_model_info_frame)
        self.label_summary_icon.setObjectName(u"label_summary_icon")
        self.label_summary_icon.setMaximumSize(QSize(22, 22))
        self.label_summary_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-check-circle.png"))
        self.label_summary_icon.setScaledContents(True)

        self.horizontalLayout_summary_title.addWidget(self.label_summary_icon)

        self.label_summary_title = QLabel(self.planning_model_info_frame)
        self.label_summary_title.setObjectName(u"label_summary_title")
        self.label_summary_title.setFont(font2)

        self.horizontalLayout_summary_title.addWidget(self.label_summary_title)

        self.horizontalSpacer_summary_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_summary_title.addItem(self.horizontalSpacer_summary_title)


        self.verticalLayout_summary.addLayout(self.horizontalLayout_summary_title)

        self.horizontalLayout_summary_rows = QHBoxLayout()
        self.horizontalLayout_summary_rows.setSpacing(14)
        self.horizontalLayout_summary_rows.setObjectName(u"horizontalLayout_summary_rows")
        self.frame_tile_summary = QFrame(self.planning_model_info_frame)
        self.frame_tile_summary.setObjectName(u"frame_tile_summary")
        self.frame_tile_summary.setFrameShape(QFrame.NoFrame)
        self.frame_tile_summary.setFrameShadow(QFrame.Raised)
        self.verticalLayout_tile_years = QVBoxLayout(self.frame_tile_summary)
        self.verticalLayout_tile_years.setSpacing(0)
        self.verticalLayout_tile_years.setObjectName(u"verticalLayout_tile_years")
        self.label_years_term = QLabel(self.frame_tile_summary)
        self.label_years_term.setObjectName(u"label_years_term")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        self.label_years_term.setFont(font3)

        self.verticalLayout_tile_years.addWidget(self.label_years_term)

        self.sim_years_label = QLabel(self.frame_tile_summary)
        self.sim_years_label.setObjectName(u"sim_years_label")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.sim_years_label.setFont(font4)

        self.verticalLayout_tile_years.addWidget(self.sim_years_label)


        self.horizontalLayout_summary_rows.addWidget(self.frame_tile_summary)

        self.frame_tile_summary_2 = QFrame(self.planning_model_info_frame)
        self.frame_tile_summary_2.setObjectName(u"frame_tile_summary_2")
        self.frame_tile_summary_2.setFrameShape(QFrame.NoFrame)
        self.frame_tile_summary_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_tile_trans = QVBoxLayout(self.frame_tile_summary_2)
        self.verticalLayout_tile_trans.setSpacing(0)
        self.verticalLayout_tile_trans.setObjectName(u"verticalLayout_tile_trans")
        self.label_trans_term = QLabel(self.frame_tile_summary_2)
        self.label_trans_term.setObjectName(u"label_trans_term")
        self.label_trans_term.setFont(font3)

        self.verticalLayout_tile_trans.addWidget(self.label_trans_term)

        self.trans_model_label = QLabel(self.frame_tile_summary_2)
        self.trans_model_label.setObjectName(u"trans_model_label")
        self.trans_model_label.setFont(font4)

        self.verticalLayout_tile_trans.addWidget(self.trans_model_label)


        self.horizontalLayout_summary_rows.addWidget(self.frame_tile_summary_2)

        self.frame_tile_summary_3 = QFrame(self.planning_model_info_frame)
        self.frame_tile_summary_3.setObjectName(u"frame_tile_summary_3")
        self.frame_tile_summary_3.setFrameShape(QFrame.NoFrame)
        self.frame_tile_summary_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_tile_temporal = QVBoxLayout(self.frame_tile_summary_3)
        self.verticalLayout_tile_temporal.setSpacing(0)
        self.verticalLayout_tile_temporal.setObjectName(u"verticalLayout_tile_temporal")
        self.label_temporal_term = QLabel(self.frame_tile_summary_3)
        self.label_temporal_term.setObjectName(u"label_temporal_term")
        self.label_temporal_term.setFont(font3)

        self.verticalLayout_tile_temporal.addWidget(self.label_temporal_term)

        self.temporal_selection_label = QLabel(self.frame_tile_summary_3)
        self.temporal_selection_label.setObjectName(u"temporal_selection_label")
        self.temporal_selection_label.setFont(font4)

        self.verticalLayout_tile_temporal.addWidget(self.temporal_selection_label)


        self.horizontalLayout_summary_rows.addWidget(self.frame_tile_summary_3)

        self.frame_tile_summary_4 = QFrame(self.planning_model_info_frame)
        self.frame_tile_summary_4.setObjectName(u"frame_tile_summary_4")
        self.frame_tile_summary_4.setFrameShape(QFrame.NoFrame)
        self.frame_tile_summary_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_tile_discount = QVBoxLayout(self.frame_tile_summary_4)
        self.verticalLayout_tile_discount.setSpacing(0)
        self.verticalLayout_tile_discount.setObjectName(u"verticalLayout_tile_discount")
        self.label_discount_term = QLabel(self.frame_tile_summary_4)
        self.label_discount_term.setObjectName(u"label_discount_term")
        self.label_discount_term.setFont(font3)

        self.verticalLayout_tile_discount.addWidget(self.label_discount_term)

        self.discount_rate_label = QLabel(self.frame_tile_summary_4)
        self.discount_rate_label.setObjectName(u"discount_rate_label")
        self.discount_rate_label.setFont(font4)

        self.verticalLayout_tile_discount.addWidget(self.discount_rate_label)


        self.horizontalLayout_summary_rows.addWidget(self.frame_tile_summary_4)

        self.frame_tile_summary_5 = QFrame(self.planning_model_info_frame)
        self.frame_tile_summary_5.setObjectName(u"frame_tile_summary_5")
        self.frame_tile_summary_5.setFrameShape(QFrame.NoFrame)
        self.frame_tile_summary_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_tile_currency = QVBoxLayout(self.frame_tile_summary_5)
        self.verticalLayout_tile_currency.setSpacing(0)
        self.verticalLayout_tile_currency.setObjectName(u"verticalLayout_tile_currency")
        self.label_currency_term = QLabel(self.frame_tile_summary_5)
        self.label_currency_term.setObjectName(u"label_currency_term")
        self.label_currency_term.setFont(font3)

        self.verticalLayout_tile_currency.addWidget(self.label_currency_term)

        self.base_currency_label = QLabel(self.frame_tile_summary_5)
        self.base_currency_label.setObjectName(u"base_currency_label")
        self.base_currency_label.setFont(font4)

        self.verticalLayout_tile_currency.addWidget(self.base_currency_label)


        self.horizontalLayout_summary_rows.addWidget(self.frame_tile_summary_5)


        self.verticalLayout_summary.addLayout(self.horizontalLayout_summary_rows)


        self.verticalLayout_main.addWidget(self.planning_model_info_frame)


        self.retranslateUi(PlanningModelPage)

        QMetaObject.connectSlotsByName(PlanningModelPage)
    # setupUi

    def retranslateUi(self, PlanningModelPage):
        PlanningModelPage.setWindowTitle(QCoreApplication.translate("PlanningModelPage", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("PlanningModelPage", u"Planning Model Setup", None))
        self.label_title.setProperty("textRole", u"heading")
        self.label_subtitle.setText(QCoreApplication.translate("PlanningModelPage", u"Configure the simulation years, transmission model, temporal resolution, and economic parameters.", None))
        self.label_subtitle.setProperty("textRole", u"subtitle")
        self.planning_model_help_button.setText("")
        self.planning_model_help_button.setProperty("btnRole", u"icon")
        self.frame_config.setProperty("cardType", u"card")
        self.label_config_icon.setText("")
        self.label_config_title.setText(QCoreApplication.translate("PlanningModelPage", u"MODEL CONFIGURATION", None))
        self.label_config_title.setProperty("textRole", u"section")
        self.label_begin.setText(QCoreApplication.translate("PlanningModelPage", u"Begin Year", None))
        self.begin_date.setDisplayFormat(QCoreApplication.translate("PlanningModelPage", u"yyyy", None))
        self.label_end.setText(QCoreApplication.translate("PlanningModelPage", u"End Year", None))
        self.end_date.setDisplayFormat(QCoreApplication.translate("PlanningModelPage", u"yyyy", None))
        self.select_years_button.setText(QCoreApplication.translate("PlanningModelPage", u"Select Simulation Years", None))
        self.select_simulation_years_help_button.setText("")
        self.select_simulation_years_help_button.setProperty("btnRole", u"icon")
        self.label_3.setText(QCoreApplication.translate("PlanningModelPage", u"Transmission Model", None))
        self.transmission_box.setItemText(0, QCoreApplication.translate("PlanningModelPage", u"Transportation (Pipe & Bubble)", None))
        self.transmission_box.setItemText(1, QCoreApplication.translate("PlanningModelPage", u"Copper Sheet", None))
        self.transmission_box.setItemText(2, QCoreApplication.translate("PlanningModelPage", u"DC Power Flow (Upcoming)", None))

        self.transmission_model_help_button.setText("")
        self.transmission_model_help_button.setProperty("btnRole", u"icon")
        self.label_5.setText(QCoreApplication.translate("PlanningModelPage", u"Temporal Selection", None))
        self.temporal_box.setItemText(0, QCoreApplication.translate("PlanningModelPage", u"Representative Weeks", None))
        self.temporal_box.setItemText(1, QCoreApplication.translate("PlanningModelPage", u"Seasonal Blocks", None))
        self.temporal_box.setItemText(2, QCoreApplication.translate("PlanningModelPage", u"8760 Analysis (Upcoming)", None))

        self.temporal_selection_help_button.setText("")
        self.temporal_selection_help_button.setProperty("btnRole", u"icon")
        self.label.setText(QCoreApplication.translate("PlanningModelPage", u"Annual Discount Rate", None))
        self.discount_rate_help_button.setText("")
        self.discount_rate_help_button.setProperty("btnRole", u"icon")
        self.label_7.setText(QCoreApplication.translate("PlanningModelPage", u"Base Currency Year", None))
        self.base_currency_year.setText(QCoreApplication.translate("PlanningModelPage", u"2021", None))
        self.base_currency_help_button.setText("")
        self.base_currency_help_button.setProperty("btnRole", u"icon")
        self.advanced_settings_button.setText(QCoreApplication.translate("PlanningModelPage", u"Advanced Settings", None))
        self.advanced_settings_button.setProperty("btnRole", u"primary")
        self.planning_model_info_frame.setProperty("cardType", u"tile")
        self.label_summary_icon.setText("")
        self.label_summary_title.setText(QCoreApplication.translate("PlanningModelPage", u"SELECTION SUMMARY", None))
        self.label_summary_title.setProperty("textRole", u"section")
        self.frame_tile_summary.setProperty("cardType", u"tile")
        self.label_years_term.setText(QCoreApplication.translate("PlanningModelPage", u"Simulation Years", None))
        self.label_years_term.setProperty("textRole", u"caption")
        self.sim_years_label.setText(QCoreApplication.translate("PlanningModelPage", u"--", None))
        self.sim_years_label.setProperty("textRole", u"section")
        self.label_trans_term.setText(QCoreApplication.translate("PlanningModelPage", u"Transmission Model", None))
        self.label_trans_term.setProperty("textRole", u"caption")
        self.trans_model_label.setText(QCoreApplication.translate("PlanningModelPage", u"--", None))
        self.trans_model_label.setProperty("textRole", u"section")
        self.label_temporal_term.setText(QCoreApplication.translate("PlanningModelPage", u"Temporal Selection", None))
        self.label_temporal_term.setProperty("textRole", u"caption")
        self.temporal_selection_label.setText(QCoreApplication.translate("PlanningModelPage", u"--", None))
        self.temporal_selection_label.setProperty("textRole", u"section")
        self.label_discount_term.setText(QCoreApplication.translate("PlanningModelPage", u"Discount Rate", None))
        self.label_discount_term.setProperty("textRole", u"caption")
        self.discount_rate_label.setText(QCoreApplication.translate("PlanningModelPage", u"--", None))
        self.discount_rate_label.setProperty("textRole", u"section")
        self.label_currency_term.setText(QCoreApplication.translate("PlanningModelPage", u"Base Currency Year", None))
        self.label_currency_term.setProperty("textRole", u"caption")
        self.base_currency_label.setText(QCoreApplication.translate("PlanningModelPage", u"--", None))
        self.base_currency_label.setProperty("textRole", u"section")
    # retranslateUi

