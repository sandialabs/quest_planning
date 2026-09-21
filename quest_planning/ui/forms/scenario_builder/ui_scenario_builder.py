# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scenario_builder.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_ScenarioBuilderPage(object):
    def setupUi(self, ScenarioBuilderPage):
        if not ScenarioBuilderPage.objectName():
            ScenarioBuilderPage.setObjectName(u"ScenarioBuilderPage")
        ScenarioBuilderPage.resize(780, 781)
        self.verticalLayout = QVBoxLayout(ScenarioBuilderPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_title = QFrame(ScenarioBuilderPage)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout_2.addWidget(self.label_title)

        self.label_subtitle = QLabel(self.frame_title)
        self.label_subtitle.setObjectName(u"label_subtitle")

        self.verticalLayout_2.addWidget(self.label_subtitle)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(62, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_title_help = QPushButton(self.frame_title)
        self.btn_title_help.setObjectName(u"btn_title_help")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_title_help.setIcon(icon)
        self.btn_title_help.setIconSize(QSize(30, 30))
        self.btn_title_help.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_title_help)


        self.verticalLayout.addWidget(self.frame_title)

        self.frame_options = QFrame(ScenarioBuilderPage)
        self.frame_options.setObjectName(u"frame_options")
        self.frame_options.setFrameShape(QFrame.NoFrame)
        self.frame_options.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_options)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_panel_1 = QFrame(self.frame_options)
        self.frame_panel_1.setObjectName(u"frame_panel_1")
        self.frame_panel_1.setFrameShape(QFrame.NoFrame)
        self.frame_panel_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_panel_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_scenario = QFrame(self.frame_panel_1)
        self.frame_scenario.setObjectName(u"frame_scenario")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_scenario.sizePolicy().hasHeightForWidth())
        self.frame_scenario.setSizePolicy(sizePolicy)
        self.frame_scenario.setMaximumSize(QSize(16777215, 150))
        self.frame_scenario.setFrameShape(QFrame.NoFrame)
        self.frame_scenario.setFrameShadow(QFrame.Raised)
        self.verticalLayout_scenario = QVBoxLayout(self.frame_scenario)
        self.verticalLayout_scenario.setSpacing(10)
        self.verticalLayout_scenario.setObjectName(u"verticalLayout_scenario")
        self.verticalLayout_scenario.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_scenario_title = QHBoxLayout()
        self.horizontalLayout_scenario_title.setSpacing(8)
        self.horizontalLayout_scenario_title.setObjectName(u"horizontalLayout_scenario_title")
        self.label_scenario_title = QLabel(self.frame_scenario)
        self.label_scenario_title.setObjectName(u"label_scenario_title")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_scenario_title.setFont(font1)

        self.horizontalLayout_scenario_title.addWidget(self.label_scenario_title)

        self.horizontalSpacer_scenario_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_scenario_title.addItem(self.horizontalSpacer_scenario_title)

        self.btn_scenario_help = QPushButton(self.frame_scenario)
        self.btn_scenario_help.setObjectName(u"btn_scenario_help")
        self.btn_scenario_help.setIcon(icon)
        self.btn_scenario_help.setIconSize(QSize(30, 30))
        self.btn_scenario_help.setFlat(True)

        self.horizontalLayout_scenario_title.addWidget(self.btn_scenario_help)


        self.verticalLayout_scenario.addLayout(self.horizontalLayout_scenario_title)

        self.label_scenario_desc = QLabel(self.frame_scenario)
        self.label_scenario_desc.setObjectName(u"label_scenario_desc")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.label_scenario_desc.setFont(font2)
        self.label_scenario_desc.setWordWrap(True)

        self.verticalLayout_scenario.addWidget(self.label_scenario_desc)

        self.scenario_name_box = QLineEdit(self.frame_scenario)
        self.scenario_name_box.setObjectName(u"scenario_name_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scenario_name_box.sizePolicy().hasHeightForWidth())
        self.scenario_name_box.setSizePolicy(sizePolicy1)
        self.scenario_name_box.setMaximumSize(QSize(420, 16777215))
        self.scenario_name_box.setFont(font2)

        self.verticalLayout_scenario.addWidget(self.scenario_name_box)


        self.verticalLayout_3.addWidget(self.frame_scenario)

        self.frame_capital_cost = QFrame(self.frame_panel_1)
        self.frame_capital_cost.setObjectName(u"frame_capital_cost")
        sizePolicy.setHeightForWidth(self.frame_capital_cost.sizePolicy().hasHeightForWidth())
        self.frame_capital_cost.setSizePolicy(sizePolicy)
        self.frame_capital_cost.setMaximumSize(QSize(16777215, 150))
        self.frame_capital_cost.setFrameShape(QFrame.NoFrame)
        self.frame_capital_cost.setFrameShadow(QFrame.Raised)
        self.verticalLayout_capital_cost = QVBoxLayout(self.frame_capital_cost)
        self.verticalLayout_capital_cost.setSpacing(10)
        self.verticalLayout_capital_cost.setObjectName(u"verticalLayout_capital_cost")
        self.verticalLayout_capital_cost.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_capital_cost_title = QHBoxLayout()
        self.horizontalLayout_capital_cost_title.setSpacing(8)
        self.horizontalLayout_capital_cost_title.setObjectName(u"horizontalLayout_capital_cost_title")
        self.label_capital_cost_title = QLabel(self.frame_capital_cost)
        self.label_capital_cost_title.setObjectName(u"label_capital_cost_title")
        self.label_capital_cost_title.setFont(font1)

        self.horizontalLayout_capital_cost_title.addWidget(self.label_capital_cost_title)

        self.horizontalSpacer_capital_cost_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_capital_cost_title.addItem(self.horizontalSpacer_capital_cost_title)

        self.btn_capita_help = QPushButton(self.frame_capital_cost)
        self.btn_capita_help.setObjectName(u"btn_capita_help")
        self.btn_capita_help.setIcon(icon)
        self.btn_capita_help.setIconSize(QSize(30, 30))
        self.btn_capita_help.setFlat(True)

        self.horizontalLayout_capital_cost_title.addWidget(self.btn_capita_help)


        self.verticalLayout_capital_cost.addLayout(self.horizontalLayout_capital_cost_title)

        self.label_capital_cost_desc = QLabel(self.frame_capital_cost)
        self.label_capital_cost_desc.setObjectName(u"label_capital_cost_desc")
        self.label_capital_cost_desc.setFont(font2)
        self.label_capital_cost_desc.setWordWrap(True)

        self.verticalLayout_capital_cost.addWidget(self.label_capital_cost_desc)

        self.capital_cost_box = QComboBox(self.frame_capital_cost)
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.setObjectName(u"capital_cost_box")
        sizePolicy1.setHeightForWidth(self.capital_cost_box.sizePolicy().hasHeightForWidth())
        self.capital_cost_box.setSizePolicy(sizePolicy1)
        self.capital_cost_box.setMaximumSize(QSize(300, 16777215))
        self.capital_cost_box.setFont(font2)

        self.verticalLayout_capital_cost.addWidget(self.capital_cost_box)


        self.verticalLayout_3.addWidget(self.frame_capital_cost)

        self.frame_load = QFrame(self.frame_panel_1)
        self.frame_load.setObjectName(u"frame_load")
        sizePolicy.setHeightForWidth(self.frame_load.sizePolicy().hasHeightForWidth())
        self.frame_load.setSizePolicy(sizePolicy)
        self.frame_load.setMaximumSize(QSize(16777215, 200))
        self.frame_load.setFrameShape(QFrame.NoFrame)
        self.frame_load.setFrameShadow(QFrame.Raised)
        self.verticalLayout_load = QVBoxLayout(self.frame_load)
        self.verticalLayout_load.setSpacing(8)
        self.verticalLayout_load.setObjectName(u"verticalLayout_load")
        self.verticalLayout_load.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_load_title = QHBoxLayout()
        self.horizontalLayout_load_title.setSpacing(8)
        self.horizontalLayout_load_title.setObjectName(u"horizontalLayout_load_title")
        self.label_load_title = QLabel(self.frame_load)
        self.label_load_title.setObjectName(u"label_load_title")
        self.label_load_title.setFont(font1)

        self.horizontalLayout_load_title.addWidget(self.label_load_title)

        self.horizontalSpacer_load_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_load_title.addItem(self.horizontalSpacer_load_title)

        self.btn_load_help = QPushButton(self.frame_load)
        self.btn_load_help.setObjectName(u"btn_load_help")
        self.btn_load_help.setIcon(icon)
        self.btn_load_help.setIconSize(QSize(30, 30))
        self.btn_load_help.setFlat(True)

        self.horizontalLayout_load_title.addWidget(self.btn_load_help)


        self.verticalLayout_load.addLayout(self.horizontalLayout_load_title)

        self.label_load_desc = QLabel(self.frame_load)
        self.label_load_desc.setObjectName(u"label_load_desc")
        self.label_load_desc.setFont(font2)
        self.label_load_desc.setWordWrap(True)

        self.verticalLayout_load.addWidget(self.label_load_desc)

        self.horizontalLayout_load_profile = QHBoxLayout()
        self.horizontalLayout_load_profile.setSpacing(10)
        self.horizontalLayout_load_profile.setObjectName(u"horizontalLayout_load_profile")
        self.label_load_profile_text = QLabel(self.frame_load)
        self.label_load_profile_text.setObjectName(u"label_load_profile_text")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_load_profile_text.setFont(font3)

        self.horizontalLayout_load_profile.addWidget(self.label_load_profile_text)

        self.load_profile_box = QComboBox(self.frame_load)
        self.load_profile_box.setObjectName(u"load_profile_box")
        sizePolicy1.setHeightForWidth(self.load_profile_box.sizePolicy().hasHeightForWidth())
        self.load_profile_box.setSizePolicy(sizePolicy1)
        self.load_profile_box.setMaximumSize(QSize(300, 16777215))
        self.load_profile_box.setFont(font2)

        self.horizontalLayout_load_profile.addWidget(self.load_profile_box)

        self.horizontalSpacer_load_profile = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_load_profile.addItem(self.horizontalSpacer_load_profile)


        self.verticalLayout_load.addLayout(self.horizontalLayout_load_profile)

        self.horizontalLayout_load_growth = QHBoxLayout()
        self.horizontalLayout_load_growth.setSpacing(10)
        self.horizontalLayout_load_growth.setObjectName(u"horizontalLayout_load_growth")
        self.label_load_growth_text = QLabel(self.frame_load)
        self.label_load_growth_text.setObjectName(u"label_load_growth_text")
        self.label_load_growth_text.setFont(font3)

        self.horizontalLayout_load_growth.addWidget(self.label_load_growth_text)

        self.annual_load_growth_box = QLineEdit(self.frame_load)
        self.annual_load_growth_box.setObjectName(u"annual_load_growth_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.annual_load_growth_box.sizePolicy().hasHeightForWidth())
        self.annual_load_growth_box.setSizePolicy(sizePolicy2)
        self.annual_load_growth_box.setMaximumSize(QSize(140, 16777215))
        self.annual_load_growth_box.setFont(font2)

        self.horizontalLayout_load_growth.addWidget(self.annual_load_growth_box)

        self.horizontalSpacer_load_growth = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_load_growth.addItem(self.horizontalSpacer_load_growth)

        self.btn_growth_help = QPushButton(self.frame_load)
        self.btn_growth_help.setObjectName(u"btn_growth_help")
        self.btn_growth_help.setIcon(icon)
        self.btn_growth_help.setIconSize(QSize(25, 25))
        self.btn_growth_help.setFlat(True)

        self.horizontalLayout_load_growth.addWidget(self.btn_growth_help)


        self.verticalLayout_load.addLayout(self.horizontalLayout_load_growth)


        self.verticalLayout_3.addWidget(self.frame_load)

        self.frame_transmission = QFrame(self.frame_panel_1)
        self.frame_transmission.setObjectName(u"frame_transmission")
        sizePolicy.setHeightForWidth(self.frame_transmission.sizePolicy().hasHeightForWidth())
        self.frame_transmission.setSizePolicy(sizePolicy)
        self.frame_transmission.setMaximumSize(QSize(16777215, 150))
        self.frame_transmission.setFrameShape(QFrame.NoFrame)
        self.frame_transmission.setFrameShadow(QFrame.Raised)
        self.verticalLayout_transmission = QVBoxLayout(self.frame_transmission)
        self.verticalLayout_transmission.setSpacing(10)
        self.verticalLayout_transmission.setObjectName(u"verticalLayout_transmission")
        self.verticalLayout_transmission.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_transmission_title = QHBoxLayout()
        self.horizontalLayout_transmission_title.setSpacing(8)
        self.horizontalLayout_transmission_title.setObjectName(u"horizontalLayout_transmission_title")
        self.label_transmission_title = QLabel(self.frame_transmission)
        self.label_transmission_title.setObjectName(u"label_transmission_title")
        self.label_transmission_title.setFont(font1)

        self.horizontalLayout_transmission_title.addWidget(self.label_transmission_title)

        self.horizontalSpacer_transmission_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_transmission_title.addItem(self.horizontalSpacer_transmission_title)

        self.btn_trans_help = QPushButton(self.frame_transmission)
        self.btn_trans_help.setObjectName(u"btn_trans_help")
        self.btn_trans_help.setIcon(icon)
        self.btn_trans_help.setIconSize(QSize(30, 30))
        self.btn_trans_help.setFlat(True)

        self.horizontalLayout_transmission_title.addWidget(self.btn_trans_help)


        self.verticalLayout_transmission.addLayout(self.horizontalLayout_transmission_title)

        self.label_transmission_desc = QLabel(self.frame_transmission)
        self.label_transmission_desc.setObjectName(u"label_transmission_desc")
        self.label_transmission_desc.setFont(font2)
        self.label_transmission_desc.setWordWrap(True)

        self.verticalLayout_transmission.addWidget(self.label_transmission_desc)

        self.transmission_box = QComboBox(self.frame_transmission)
        self.transmission_box.addItem("")
        self.transmission_box.addItem("")
        self.transmission_box.setObjectName(u"transmission_box")
        sizePolicy1.setHeightForWidth(self.transmission_box.sizePolicy().hasHeightForWidth())
        self.transmission_box.setSizePolicy(sizePolicy1)
        self.transmission_box.setMaximumSize(QSize(300, 16777215))
        self.transmission_box.setFont(font2)

        self.verticalLayout_transmission.addWidget(self.transmission_box)


        self.verticalLayout_3.addWidget(self.frame_transmission)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_panel_1)

        self.frame_panel_2 = QFrame(self.frame_options)
        self.frame_panel_2.setObjectName(u"frame_panel_2")
        self.frame_panel_2.setFrameShape(QFrame.NoFrame)
        self.frame_panel_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_panel_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_policy = QFrame(self.frame_panel_2)
        self.frame_policy.setObjectName(u"frame_policy")
        sizePolicy.setHeightForWidth(self.frame_policy.sizePolicy().hasHeightForWidth())
        self.frame_policy.setSizePolicy(sizePolicy)
        self.frame_policy.setMaximumSize(QSize(16777215, 150))
        self.frame_policy.setFrameShape(QFrame.NoFrame)
        self.frame_policy.setFrameShadow(QFrame.Raised)
        self.verticalLayout_policy = QVBoxLayout(self.frame_policy)
        self.verticalLayout_policy.setSpacing(10)
        self.verticalLayout_policy.setObjectName(u"verticalLayout_policy")
        self.verticalLayout_policy.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_policy_title = QHBoxLayout()
        self.horizontalLayout_policy_title.setSpacing(8)
        self.horizontalLayout_policy_title.setObjectName(u"horizontalLayout_policy_title")
        self.label_policy_title = QLabel(self.frame_policy)
        self.label_policy_title.setObjectName(u"label_policy_title")
        self.label_policy_title.setFont(font1)

        self.horizontalLayout_policy_title.addWidget(self.label_policy_title)

        self.horizontalSpacer_policy_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_policy_title.addItem(self.horizontalSpacer_policy_title)

        self.btn_generation_help = QPushButton(self.frame_policy)
        self.btn_generation_help.setObjectName(u"btn_generation_help")
        self.btn_generation_help.setIcon(icon)
        self.btn_generation_help.setIconSize(QSize(30, 30))
        self.btn_generation_help.setFlat(True)

        self.horizontalLayout_policy_title.addWidget(self.btn_generation_help)


        self.verticalLayout_policy.addLayout(self.horizontalLayout_policy_title)

        self.label_policy_desc = QLabel(self.frame_policy)
        self.label_policy_desc.setObjectName(u"label_policy_desc")
        self.label_policy_desc.setFont(font2)
        self.label_policy_desc.setWordWrap(True)

        self.verticalLayout_policy.addWidget(self.label_policy_desc)

        self.rps_box = QComboBox(self.frame_policy)
        self.rps_box.addItem("")
        self.rps_box.addItem("")
        self.rps_box.setObjectName(u"rps_box")
        sizePolicy1.setHeightForWidth(self.rps_box.sizePolicy().hasHeightForWidth())
        self.rps_box.setSizePolicy(sizePolicy1)
        self.rps_box.setMaximumSize(QSize(300, 16777215))
        self.rps_box.setFont(font2)

        self.verticalLayout_policy.addWidget(self.rps_box)


        self.verticalLayout_4.addWidget(self.frame_policy)

        self.frame_candidates = QFrame(self.frame_panel_2)
        self.frame_candidates.setObjectName(u"frame_candidates")
        sizePolicy.setHeightForWidth(self.frame_candidates.sizePolicy().hasHeightForWidth())
        self.frame_candidates.setSizePolicy(sizePolicy)
        self.frame_candidates.setMaximumSize(QSize(16777215, 230))
        self.frame_candidates.setFrameShape(QFrame.NoFrame)
        self.frame_candidates.setFrameShadow(QFrame.Raised)
        self.verticalLayout_candidates = QVBoxLayout(self.frame_candidates)
        self.verticalLayout_candidates.setSpacing(10)
        self.verticalLayout_candidates.setObjectName(u"verticalLayout_candidates")
        self.verticalLayout_candidates.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_candidates_title = QHBoxLayout()
        self.horizontalLayout_candidates_title.setSpacing(8)
        self.horizontalLayout_candidates_title.setObjectName(u"horizontalLayout_candidates_title")
        self.label_candidates_title = QLabel(self.frame_candidates)
        self.label_candidates_title.setObjectName(u"label_candidates_title")
        self.label_candidates_title.setFont(font1)

        self.horizontalLayout_candidates_title.addWidget(self.label_candidates_title)

        self.horizontalSpacer_candidates_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_candidates_title.addItem(self.horizontalSpacer_candidates_title)

        self.btn_candidates_help = QPushButton(self.frame_candidates)
        self.btn_candidates_help.setObjectName(u"btn_candidates_help")
        self.btn_candidates_help.setIcon(icon)
        self.btn_candidates_help.setIconSize(QSize(30, 30))
        self.btn_candidates_help.setFlat(True)

        self.horizontalLayout_candidates_title.addWidget(self.btn_candidates_help)


        self.verticalLayout_candidates.addLayout(self.horizontalLayout_candidates_title)

        self.label_candidates_desc = QLabel(self.frame_candidates)
        self.label_candidates_desc.setObjectName(u"label_candidates_desc")
        self.label_candidates_desc.setFont(font2)
        self.label_candidates_desc.setWordWrap(True)

        self.verticalLayout_candidates.addWidget(self.label_candidates_desc)

        self.horizontalLayout_cand_button = QHBoxLayout()
        self.horizontalLayout_cand_button.setSpacing(10)
        self.horizontalLayout_cand_button.setObjectName(u"horizontalLayout_cand_button")
        self.cand_tech_button = QPushButton(self.frame_candidates)
        self.cand_tech_button.setObjectName(u"cand_tech_button")
        sizePolicy2.setHeightForWidth(self.cand_tech_button.sizePolicy().hasHeightForWidth())
        self.cand_tech_button.setSizePolicy(sizePolicy2)
        self.cand_tech_button.setMinimumSize(QSize(220, 0))
        self.cand_tech_button.setFont(font3)

        self.horizontalLayout_cand_button.addWidget(self.cand_tech_button)

        self.horizontalSpacer_cand_button = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_cand_button.addItem(self.horizontalSpacer_cand_button)


        self.verticalLayout_candidates.addLayout(self.horizontalLayout_cand_button)

        self.cand_tech_frame = QFrame(self.frame_candidates)
        self.cand_tech_frame.setObjectName(u"cand_tech_frame")
        sizePolicy.setHeightForWidth(self.cand_tech_frame.sizePolicy().hasHeightForWidth())
        self.cand_tech_frame.setSizePolicy(sizePolicy)
        self.cand_tech_frame.setMaximumSize(QSize(16777215, 150))
        self.cand_tech_frame.setFrameShape(QFrame.NoFrame)
        self.cand_tech_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_cand_tech = QVBoxLayout(self.cand_tech_frame)
        self.verticalLayout_cand_tech.setSpacing(6)
        self.verticalLayout_cand_tech.setObjectName(u"verticalLayout_cand_tech")
        self.verticalLayout_cand_tech.setContentsMargins(12, 10, 12, 10)
        self.label_cand_tech_list_title = QLabel(self.cand_tech_frame)
        self.label_cand_tech_list_title.setObjectName(u"label_cand_tech_list_title")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(9)
        font4.setBold(True)
        self.label_cand_tech_list_title.setFont(font4)

        self.verticalLayout_cand_tech.addWidget(self.label_cand_tech_list_title)

        self.candidate_tech_box = QTextBrowser(self.cand_tech_frame)
        self.candidate_tech_box.setObjectName(u"candidate_tech_box")
        self.candidate_tech_box.setMinimumSize(QSize(0, 70))
        self.candidate_tech_box.setFont(font2)
        self.candidate_tech_box.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_cand_tech.addWidget(self.candidate_tech_box)


        self.verticalLayout_candidates.addWidget(self.cand_tech_frame)


        self.verticalLayout_4.addWidget(self.frame_candidates)

        self.frame_candidates_2 = QFrame(self.frame_panel_2)
        self.frame_candidates_2.setObjectName(u"frame_candidates_2")
        sizePolicy.setHeightForWidth(self.frame_candidates_2.sizePolicy().hasHeightForWidth())
        self.frame_candidates_2.setSizePolicy(sizePolicy)
        self.frame_candidates_2.setMaximumSize(QSize(16777215, 230))
        self.frame_candidates_2.setFrameShape(QFrame.NoFrame)
        self.frame_candidates_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_candidates_2 = QVBoxLayout(self.frame_candidates_2)
        self.verticalLayout_candidates_2.setSpacing(10)
        self.verticalLayout_candidates_2.setObjectName(u"verticalLayout_candidates_2")
        self.verticalLayout_candidates_2.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_candidates_title_2 = QHBoxLayout()
        self.horizontalLayout_candidates_title_2.setSpacing(8)
        self.horizontalLayout_candidates_title_2.setObjectName(u"horizontalLayout_candidates_title_2")
        self.label_candidates_title_2 = QLabel(self.frame_candidates_2)
        self.label_candidates_title_2.setObjectName(u"label_candidates_title_2")
        self.label_candidates_title_2.setFont(font1)

        self.horizontalLayout_candidates_title_2.addWidget(self.label_candidates_title_2)

        self.horizontalSpacer_candidates_title_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_candidates_title_2.addItem(self.horizontalSpacer_candidates_title_2)

        self.btn_model_help = QPushButton(self.frame_candidates_2)
        self.btn_model_help.setObjectName(u"btn_model_help")
        sizePolicy2.setHeightForWidth(self.btn_model_help.sizePolicy().hasHeightForWidth())
        self.btn_model_help.setSizePolicy(sizePolicy2)
        self.btn_model_help.setIcon(icon)
        self.btn_model_help.setIconSize(QSize(30, 30))
        self.btn_model_help.setFlat(True)

        self.horizontalLayout_candidates_title_2.addWidget(self.btn_model_help)


        self.verticalLayout_candidates_2.addLayout(self.horizontalLayout_candidates_title_2)

        self.label_candidates_desc_2 = QLabel(self.frame_candidates_2)
        self.label_candidates_desc_2.setObjectName(u"label_candidates_desc_2")
        self.label_candidates_desc_2.setFont(font2)
        self.label_candidates_desc_2.setWordWrap(True)

        self.verticalLayout_candidates_2.addWidget(self.label_candidates_desc_2)

        self.horizontalLayout_cand_button_2 = QHBoxLayout()
        self.horizontalLayout_cand_button_2.setSpacing(10)
        self.horizontalLayout_cand_button_2.setObjectName(u"horizontalLayout_cand_button_2")
        self.cand_tech_button_2 = QPushButton(self.frame_candidates_2)
        self.cand_tech_button_2.setObjectName(u"cand_tech_button_2")
        sizePolicy2.setHeightForWidth(self.cand_tech_button_2.sizePolicy().hasHeightForWidth())
        self.cand_tech_button_2.setSizePolicy(sizePolicy2)
        self.cand_tech_button_2.setMinimumSize(QSize(220, 0))
        self.cand_tech_button_2.setFont(font3)

        self.horizontalLayout_cand_button_2.addWidget(self.cand_tech_button_2)

        self.horizontalSpacer_cand_button_2 = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_cand_button_2.addItem(self.horizontalSpacer_cand_button_2)


        self.verticalLayout_candidates_2.addLayout(self.horizontalLayout_cand_button_2)

        self.cand_tech_frame_2 = QFrame(self.frame_candidates_2)
        self.cand_tech_frame_2.setObjectName(u"cand_tech_frame_2")
        sizePolicy.setHeightForWidth(self.cand_tech_frame_2.sizePolicy().hasHeightForWidth())
        self.cand_tech_frame_2.setSizePolicy(sizePolicy)
        self.cand_tech_frame_2.setMaximumSize(QSize(16777215, 150))
        self.cand_tech_frame_2.setFrameShape(QFrame.NoFrame)
        self.cand_tech_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_cand_tech_2 = QVBoxLayout(self.cand_tech_frame_2)
        self.verticalLayout_cand_tech_2.setSpacing(6)
        self.verticalLayout_cand_tech_2.setObjectName(u"verticalLayout_cand_tech_2")
        self.verticalLayout_cand_tech_2.setContentsMargins(12, 10, 12, 10)
        self.label_cand_tech_list_title_2 = QLabel(self.cand_tech_frame_2)
        self.label_cand_tech_list_title_2.setObjectName(u"label_cand_tech_list_title_2")
        self.label_cand_tech_list_title_2.setFont(font4)

        self.verticalLayout_cand_tech_2.addWidget(self.label_cand_tech_list_title_2)

        self.candidate_tech_box_2 = QTextBrowser(self.cand_tech_frame_2)
        self.candidate_tech_box_2.setObjectName(u"candidate_tech_box_2")
        self.candidate_tech_box_2.setMinimumSize(QSize(0, 70))
        self.candidate_tech_box_2.setFont(font2)
        self.candidate_tech_box_2.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_cand_tech_2.addWidget(self.candidate_tech_box_2)


        self.verticalLayout_candidates_2.addWidget(self.cand_tech_frame_2)


        self.verticalLayout_4.addWidget(self.frame_candidates_2)

        self.frame_retirements = QFrame(self.frame_panel_2)
        self.frame_retirements.setObjectName(u"frame_retirements")
        sizePolicy.setHeightForWidth(self.frame_retirements.sizePolicy().hasHeightForWidth())
        self.frame_retirements.setSizePolicy(sizePolicy)
        self.frame_retirements.setMaximumSize(QSize(16777215, 230))
        self.frame_retirements.setFrameShape(QFrame.NoFrame)
        self.frame_retirements.setFrameShadow(QFrame.Raised)
        self.verticalLayout_retirements = QVBoxLayout(self.frame_retirements)
        self.verticalLayout_retirements.setSpacing(10)
        self.verticalLayout_retirements.setObjectName(u"verticalLayout_retirements")
        self.verticalLayout_retirements.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_retirements_title = QHBoxLayout()
        self.horizontalLayout_retirements_title.setSpacing(8)
        self.horizontalLayout_retirements_title.setObjectName(u"horizontalLayout_retirements_title")
        self.label_retirements_title = QLabel(self.frame_retirements)
        self.label_retirements_title.setObjectName(u"label_retirements_title")
        self.label_retirements_title.setFont(font1)

        self.horizontalLayout_retirements_title.addWidget(self.label_retirements_title)

        self.horizontalSpacer_retirements_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_retirements_title.addItem(self.horizontalSpacer_retirements_title)

        self.btn_generatio_help = QPushButton(self.frame_retirements)
        self.btn_generatio_help.setObjectName(u"btn_generatio_help")
        self.btn_generatio_help.setIcon(icon)
        self.btn_generatio_help.setIconSize(QSize(30, 30))
        self.btn_generatio_help.setFlat(True)

        self.horizontalLayout_retirements_title.addWidget(self.btn_generatio_help)


        self.verticalLayout_retirements.addLayout(self.horizontalLayout_retirements_title)

        self.label_retirements_desc = QLabel(self.frame_retirements)
        self.label_retirements_desc.setObjectName(u"label_retirements_desc")
        self.label_retirements_desc.setFont(font2)
        self.label_retirements_desc.setWordWrap(True)

        self.verticalLayout_retirements.addWidget(self.label_retirements_desc)

        self.horizontalLayout_retirement_button = QHBoxLayout()
        self.horizontalLayout_retirement_button.setSpacing(10)
        self.horizontalLayout_retirement_button.setObjectName(u"horizontalLayout_retirement_button")
        self.gen_retirement_button = QPushButton(self.frame_retirements)
        self.gen_retirement_button.setObjectName(u"gen_retirement_button")
        sizePolicy2.setHeightForWidth(self.gen_retirement_button.sizePolicy().hasHeightForWidth())
        self.gen_retirement_button.setSizePolicy(sizePolicy2)
        self.gen_retirement_button.setMinimumSize(QSize(200, 0))
        self.gen_retirement_button.setFont(font3)

        self.horizontalLayout_retirement_button.addWidget(self.gen_retirement_button)

        self.horizontalSpacer_retirement_button = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_retirement_button.addItem(self.horizontalSpacer_retirement_button)


        self.verticalLayout_retirements.addLayout(self.horizontalLayout_retirement_button)

        self.retirement_frame = QFrame(self.frame_retirements)
        self.retirement_frame.setObjectName(u"retirement_frame")
        sizePolicy.setHeightForWidth(self.retirement_frame.sizePolicy().hasHeightForWidth())
        self.retirement_frame.setSizePolicy(sizePolicy)
        self.retirement_frame.setMaximumSize(QSize(16777215, 150))
        self.retirement_frame.setFrameShape(QFrame.NoFrame)
        self.retirement_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_retirement = QVBoxLayout(self.retirement_frame)
        self.verticalLayout_retirement.setSpacing(6)
        self.verticalLayout_retirement.setObjectName(u"verticalLayout_retirement")
        self.verticalLayout_retirement.setContentsMargins(12, 10, 12, 10)
        self.label_retirement_list_title = QLabel(self.retirement_frame)
        self.label_retirement_list_title.setObjectName(u"label_retirement_list_title")
        self.label_retirement_list_title.setFont(font4)

        self.verticalLayout_retirement.addWidget(self.label_retirement_list_title)

        self.retirement_box = QTextBrowser(self.retirement_frame)
        self.retirement_box.setObjectName(u"retirement_box")
        self.retirement_box.setMinimumSize(QSize(0, 70))
        self.retirement_box.setFont(font2)
        self.retirement_box.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_retirement.addWidget(self.retirement_box)


        self.verticalLayout_retirements.addWidget(self.retirement_frame)


        self.verticalLayout_4.addWidget(self.frame_retirements)


        self.horizontalLayout.addWidget(self.frame_panel_2)


        self.verticalLayout.addWidget(self.frame_options)


        self.retranslateUi(ScenarioBuilderPage)

        QMetaObject.connectSlotsByName(ScenarioBuilderPage)
    # setupUi

    def retranslateUi(self, ScenarioBuilderPage):
        ScenarioBuilderPage.setWindowTitle(QCoreApplication.translate("ScenarioBuilderPage", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Scenario Builder", None))
        self.label_subtitle.setText(QCoreApplication.translate("ScenarioBuilderPage", u"The QuESt Planning scenario builder turns your model configuration into a runnable scenario.", None))
        self.btn_title_help.setText("")
        self.frame_scenario.setProperty("cardType", QCoreApplication.translate("ScenarioBuilderPage", u"card", None))
        self.label_scenario_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"SCENARIO NAME", None))
        self.label_scenario_title.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.btn_scenario_help.setText("")
        self.label_scenario_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"The <b><i>Scenario Name</i></b> you provide should be unique to this <i>QuESt Planning</i> scenario, as it will be used to save the print results.", None))
        self.label_scenario_desc.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"body", None))
        self.scenario_name_box.setPlaceholderText(QCoreApplication.translate("ScenarioBuilderPage", u"Base Scenario", None))
        self.frame_capital_cost.setProperty("cardType", QCoreApplication.translate("ScenarioBuilderPage", u"card", None))
        self.label_capital_cost_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"RESOURCE CAPITAL COSTS", None))
        self.label_capital_cost_title.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.btn_capita_help.setText("")
        self.label_capital_cost_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Select the <b><i>capital cost trajectory</i></b> that <i>QuESt Planning</i> will use for the energy storage technologies. The cost trajectories are defined in the input csv data.", None))
        self.label_capital_cost_desc.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"body", None))
        self.capital_cost_box.setItemText(0, QCoreApplication.translate("ScenarioBuilderPage", u"Baseline", None))
        self.capital_cost_box.setItemText(1, QCoreApplication.translate("ScenarioBuilderPage", u"Low", None))
        self.capital_cost_box.setItemText(2, QCoreApplication.translate("ScenarioBuilderPage", u"Moderate", None))
        self.capital_cost_box.setItemText(3, QCoreApplication.translate("ScenarioBuilderPage", u"High", None))

        self.frame_load.setProperty("cardType", QCoreApplication.translate("ScenarioBuilderPage", u"card", None))
        self.label_load_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"LOAD FORECASTS", None))
        self.label_load_title.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.btn_load_help.setText("")
        self.label_load_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Select the <b><i>load forecast</i></b> used by <i>QuESt Planning</i>. The forecasts are defined in the csv data.", None))
        self.label_load_desc.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"body", None))
        self.label_load_profile_text.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Load Forecast", None))
        self.label_load_profile_text.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.label_load_growth_text.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Annual Load Growth", None))
        self.label_load_growth_text.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.annual_load_growth_box.setText(QCoreApplication.translate("ScenarioBuilderPage", u"1.5", None))
        self.annual_load_growth_box.setPlaceholderText(QCoreApplication.translate("ScenarioBuilderPage", u"%", None))
        self.btn_growth_help.setText("")
        self.frame_transmission.setProperty("cardType", QCoreApplication.translate("ScenarioBuilderPage", u"card", None))
        self.label_transmission_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"TRANSMISSION EXPANSION", None))
        self.label_transmission_title.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.btn_trans_help.setText("")
        self.label_transmission_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Choose whether <i>QuESt Planning</i> may expand the transmission network. Transmission expansion is a feature that will be added in a later release.", None))
        self.label_transmission_desc.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"body", None))
        self.transmission_box.setItemText(0, QCoreApplication.translate("ScenarioBuilderPage", u"Yes", None))
        self.transmission_box.setItemText(1, QCoreApplication.translate("ScenarioBuilderPage", u"No", None))

        self.frame_policy.setProperty("cardType", QCoreApplication.translate("ScenarioBuilderPage", u"card", None))
        self.label_policy_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"FUTURE GENERATION MIX", None))
        self.label_policy_title.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.btn_generation_help.setText("")
        self.label_policy_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Select the <b><i>Future Generation Mix</i></b> to be used in the scenario. The schedule can be defined in the csv data, or select <i>Create New...</i> to define custom targets.", None))
        self.label_policy_desc.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"body", None))
        self.rps_box.setItemText(0, QCoreApplication.translate("ScenarioBuilderPage", u"Default", None))
        self.rps_box.setItemText(1, QCoreApplication.translate("ScenarioBuilderPage", u"Create New...", None))

        self.frame_candidates.setProperty("cardType", QCoreApplication.translate("ScenarioBuilderPage", u"tile", None))
        self.label_candidates_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"CANDIDATE TECHNOLOGIES", None))
        self.label_candidates_title.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.btn_candidates_help.setText("")
        self.label_candidates_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Click the <b><i>Candidate Technologies</i></b> button to select the candidate technologies to be considered in the <i>QuESt Planning</i> optimization.", None))
        self.label_candidates_desc.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"body", None))
        self.cand_tech_button.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Candidate Technologies", None))
        self.cand_tech_button.setProperty("btnRole", QCoreApplication.translate("ScenarioBuilderPage", u"primary", None))
        self.cand_tech_frame.setProperty("cardType", QCoreApplication.translate("ScenarioBuilderPage", u"tile", None))
        self.label_cand_tech_list_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"SELECTED CANDIDATE TECHNOLOGIES", None))
        self.label_cand_tech_list_title.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.frame_candidates_2.setProperty("cardType", QCoreApplication.translate("ScenarioBuilderPage", u"tile", None))
        self.label_candidates_title_2.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Large Load Model", None))
        self.label_candidates_title_2.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.btn_model_help.setText("")
        self.label_candidates_desc_2.setText(QCoreApplication.translate("ScenarioBuilderPage", u"<html><head/><body><p>Click the <span style=\" font-weight:600; font-style:italic;\">Large Load Model</span> button to select the large load model to be considered in the <span style=\" font-style:italic;\">QuESt Planning</span> optimization.</p></body></html>", None))
        self.label_candidates_desc_2.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"body", None))
        self.cand_tech_button_2.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Large Load Model", None))
        self.cand_tech_button_2.setProperty("btnRole", QCoreApplication.translate("ScenarioBuilderPage", u"primary", None))
        self.cand_tech_frame_2.setProperty("cardType", QCoreApplication.translate("ScenarioBuilderPage", u"tile", None))
        self.label_cand_tech_list_title_2.setText(QCoreApplication.translate("ScenarioBuilderPage", u"SELECTED CANDIDATE TECHNOLOGIES", None))
        self.label_cand_tech_list_title_2.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.frame_retirements.setProperty("cardType", QCoreApplication.translate("ScenarioBuilderPage", u"tile", None))
        self.label_retirements_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"GENERATION RETIREMENTS", None))
        self.label_retirements_title.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
        self.btn_generatio_help.setText("")
        self.label_retirements_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Click the <b><i>Retirement Schedule</i></b> button to select the retirement schedule enforced in the <i>QuESt Planning</i> optimization. The <i>Default</i> option uses the schedule detailed in the csv data.", None))
        self.label_retirements_desc.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"body", None))
        self.gen_retirement_button.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Retirement Schedule", None))
        self.gen_retirement_button.setProperty("btnRole", QCoreApplication.translate("ScenarioBuilderPage", u"primary", None))
        self.retirement_frame.setProperty("cardType", QCoreApplication.translate("ScenarioBuilderPage", u"tile", None))
        self.label_retirement_list_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"SELECTED RETIREMENT SCHEDULE", None))
        self.label_retirement_list_title.setProperty("textRole", QCoreApplication.translate("ScenarioBuilderPage", u"section", None))
    # retranslateUi

