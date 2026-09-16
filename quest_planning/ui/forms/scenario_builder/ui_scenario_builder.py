# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scenario_builder.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_ScenarioBuilderPage(object):
    def setupUi(self, ScenarioBuilderPage):
        if not ScenarioBuilderPage.objectName():
            ScenarioBuilderPage.setObjectName(u"ScenarioBuilderPage")
        ScenarioBuilderPage.resize(1118, 928)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScenarioBuilderPage.sizePolicy().hasHeightForWidth())
        ScenarioBuilderPage.setSizePolicy(sizePolicy)
        self.verticalLayout_main = QVBoxLayout(ScenarioBuilderPage)
        self.verticalLayout_main.setSpacing(18)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(24, 24, 24, 24)
        self.frame_header = QFrame(ScenarioBuilderPage)
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
        self.label_title.setStyleSheet(u"color: rgb(40, 84, 113);\n"
"background-color: transparent;")

        self.verticalLayout_header_text.addWidget(self.label_title)

        self.label_subtitle = QLabel(self.frame_header)
        self.label_subtitle.setObjectName(u"label_subtitle")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.label_subtitle.setFont(font1)
        self.label_subtitle.setStyleSheet(u"color: rgb(100, 100, 100);\n"
"background-color: transparent;")

        self.verticalLayout_header_text.addWidget(self.label_subtitle)


        self.horizontalLayout_header.addLayout(self.verticalLayout_header_text)

        self.horizontalSpacer_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_header)

        self.scenario_builder_help_button = QToolButton(self.frame_header)
        self.scenario_builder_help_button.setObjectName(u"scenario_builder_help_button")
        self.scenario_builder_help_button.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(230, 235, 240);\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210, 218, 225);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/help_FILL0_wght200_GRAD0_opsz48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.scenario_builder_help_button.setIcon(icon)
        self.scenario_builder_help_button.setIconSize(QSize(24, 24))
        self.scenario_builder_help_button.setAutoRaise(True)

        self.horizontalLayout_header.addWidget(self.scenario_builder_help_button)


        self.verticalLayout_main.addWidget(self.frame_header)

        self.frame_columns = QFrame(ScenarioBuilderPage)
        self.frame_columns.setObjectName(u"frame_columns")
        self.frame_columns.setFrameShape(QFrame.NoFrame)
        self.frame_columns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_columns = QHBoxLayout(self.frame_columns)
        self.horizontalLayout_columns.setSpacing(18)
        self.horizontalLayout_columns.setObjectName(u"horizontalLayout_columns")
        self.frame_column_left = QFrame(self.frame_columns)
        self.frame_column_left.setObjectName(u"frame_column_left")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_column_left.sizePolicy().hasHeightForWidth())
        self.frame_column_left.setSizePolicy(sizePolicy2)
        self.frame_column_left.setFrameShape(QFrame.NoFrame)
        self.frame_column_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_column_left = QVBoxLayout(self.frame_column_left)
        self.verticalLayout_column_left.setSpacing(18)
        self.verticalLayout_column_left.setObjectName(u"verticalLayout_column_left")
        self.verticalLayout_column_left.setContentsMargins(0, 0, 0, 0)
        self.frame_scenario = QFrame(self.frame_column_left)
        self.frame_scenario.setObjectName(u"frame_scenario")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_scenario.sizePolicy().hasHeightForWidth())
        self.frame_scenario.setSizePolicy(sizePolicy3)
        self.frame_scenario.setMaximumSize(QSize(16777215, 150))
        self.frame_scenario.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(216, 216, 216);\n"
"    border-radius: 12px;\n"
"}\n"
"QFrame QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"QFrame QLineEdit, QFrame QComboBox, QFrame QDoubleSpinBox, QFrame QTextBrowser {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 6px;\n"
"    padding: 6px 8px;\n"
"    selection-background-color: rgb(40, 84, 113);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.frame_scenario.setFrameShape(QFrame.NoFrame)
        self.frame_scenario.setFrameShadow(QFrame.Raised)
        self.verticalLayout_scenario = QVBoxLayout(self.frame_scenario)
        self.verticalLayout_scenario.setSpacing(10)
        self.verticalLayout_scenario.setObjectName(u"verticalLayout_scenario")
        self.verticalLayout_scenario.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_scenario_title = QHBoxLayout()
        self.horizontalLayout_scenario_title.setSpacing(8)
        self.horizontalLayout_scenario_title.setObjectName(u"horizontalLayout_scenario_title")
        self.label_scenario_icon = QLabel(self.frame_scenario)
        self.label_scenario_icon.setObjectName(u"label_scenario_icon")
        self.label_scenario_icon.setMaximumSize(QSize(20, 20))
        self.label_scenario_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-pencil.png"))
        self.label_scenario_icon.setScaledContents(True)

        self.horizontalLayout_scenario_title.addWidget(self.label_scenario_icon)

        self.label_scenario_title = QLabel(self.frame_scenario)
        self.label_scenario_title.setObjectName(u"label_scenario_title")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_scenario_title.setFont(font2)
        self.label_scenario_title.setStyleSheet(u"color: rgb(40, 84, 113);")

        self.horizontalLayout_scenario_title.addWidget(self.label_scenario_title)

        self.horizontalSpacer_scenario_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_scenario_title.addItem(self.horizontalSpacer_scenario_title)

        self.scenario_name_help_button = QToolButton(self.frame_scenario)
        self.scenario_name_help_button.setObjectName(u"scenario_name_help_button")
        self.scenario_name_help_button.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(230, 235, 240);\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210, 218, 225);\n"
"}")
        self.scenario_name_help_button.setIcon(icon)
        self.scenario_name_help_button.setIconSize(QSize(20, 20))
        self.scenario_name_help_button.setAutoRaise(True)

        self.horizontalLayout_scenario_title.addWidget(self.scenario_name_help_button)


        self.verticalLayout_scenario.addLayout(self.horizontalLayout_scenario_title)

        self.label_scenario_desc = QLabel(self.frame_scenario)
        self.label_scenario_desc.setObjectName(u"label_scenario_desc")
        self.label_scenario_desc.setFont(font1)
        self.label_scenario_desc.setStyleSheet(u"color: rgb(70, 70, 70);")
        self.label_scenario_desc.setWordWrap(True)

        self.verticalLayout_scenario.addWidget(self.label_scenario_desc)

        self.scenario_name_box = QLineEdit(self.frame_scenario)
        self.scenario_name_box.setObjectName(u"scenario_name_box")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scenario_name_box.sizePolicy().hasHeightForWidth())
        self.scenario_name_box.setSizePolicy(sizePolicy4)
        self.scenario_name_box.setMaximumSize(QSize(420, 16777215))
        self.scenario_name_box.setFont(font1)

        self.verticalLayout_scenario.addWidget(self.scenario_name_box)


        self.verticalLayout_column_left.addWidget(self.frame_scenario)

        self.frame_capital_cost = QFrame(self.frame_column_left)
        self.frame_capital_cost.setObjectName(u"frame_capital_cost")
        sizePolicy3.setHeightForWidth(self.frame_capital_cost.sizePolicy().hasHeightForWidth())
        self.frame_capital_cost.setSizePolicy(sizePolicy3)
        self.frame_capital_cost.setMaximumSize(QSize(16777215, 150))
        self.frame_capital_cost.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(216, 216, 216);\n"
"    border-radius: 12px;\n"
"}\n"
"QFrame QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"QFrame QLineEdit, QFrame QComboBox, QFrame QDoubleSpinBox, QFrame QTextBrowser {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 6px;\n"
"    padding: 6px 8px;\n"
"    selection-background-color: rgb(40, 84, 113);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.frame_capital_cost.setFrameShape(QFrame.NoFrame)
        self.frame_capital_cost.setFrameShadow(QFrame.Raised)
        self.verticalLayout_capital_cost = QVBoxLayout(self.frame_capital_cost)
        self.verticalLayout_capital_cost.setSpacing(10)
        self.verticalLayout_capital_cost.setObjectName(u"verticalLayout_capital_cost")
        self.verticalLayout_capital_cost.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_capital_cost_title = QHBoxLayout()
        self.horizontalLayout_capital_cost_title.setSpacing(8)
        self.horizontalLayout_capital_cost_title.setObjectName(u"horizontalLayout_capital_cost_title")
        self.label_capital_cost_icon = QLabel(self.frame_capital_cost)
        self.label_capital_cost_icon.setObjectName(u"label_capital_cost_icon")
        self.label_capital_cost_icon.setMaximumSize(QSize(20, 20))
        self.label_capital_cost_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-wallet.png"))
        self.label_capital_cost_icon.setScaledContents(True)

        self.horizontalLayout_capital_cost_title.addWidget(self.label_capital_cost_icon)

        self.label_capital_cost_title = QLabel(self.frame_capital_cost)
        self.label_capital_cost_title.setObjectName(u"label_capital_cost_title")
        self.label_capital_cost_title.setFont(font2)
        self.label_capital_cost_title.setStyleSheet(u"color: rgb(40, 84, 113);")

        self.horizontalLayout_capital_cost_title.addWidget(self.label_capital_cost_title)

        self.horizontalSpacer_capital_cost_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_capital_cost_title.addItem(self.horizontalSpacer_capital_cost_title)

        self.capital_cost_trajectory_help_button = QToolButton(self.frame_capital_cost)
        self.capital_cost_trajectory_help_button.setObjectName(u"capital_cost_trajectory_help_button")
        self.capital_cost_trajectory_help_button.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(230, 235, 240);\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210, 218, 225);\n"
"}")
        self.capital_cost_trajectory_help_button.setIcon(icon)
        self.capital_cost_trajectory_help_button.setIconSize(QSize(20, 20))
        self.capital_cost_trajectory_help_button.setAutoRaise(True)

        self.horizontalLayout_capital_cost_title.addWidget(self.capital_cost_trajectory_help_button)


        self.verticalLayout_capital_cost.addLayout(self.horizontalLayout_capital_cost_title)

        self.label_capital_cost_desc = QLabel(self.frame_capital_cost)
        self.label_capital_cost_desc.setObjectName(u"label_capital_cost_desc")
        self.label_capital_cost_desc.setFont(font1)
        self.label_capital_cost_desc.setStyleSheet(u"color: rgb(70, 70, 70);")
        self.label_capital_cost_desc.setWordWrap(True)

        self.verticalLayout_capital_cost.addWidget(self.label_capital_cost_desc)

        self.capital_cost_box = QComboBox(self.frame_capital_cost)
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.addItem("")
        self.capital_cost_box.setObjectName(u"capital_cost_box")
        sizePolicy4.setHeightForWidth(self.capital_cost_box.sizePolicy().hasHeightForWidth())
        self.capital_cost_box.setSizePolicy(sizePolicy4)
        self.capital_cost_box.setMaximumSize(QSize(300, 16777215))
        self.capital_cost_box.setFont(font1)

        self.verticalLayout_capital_cost.addWidget(self.capital_cost_box)


        self.verticalLayout_column_left.addWidget(self.frame_capital_cost)

        self.frame_load = QFrame(self.frame_column_left)
        self.frame_load.setObjectName(u"frame_load")
        sizePolicy3.setHeightForWidth(self.frame_load.sizePolicy().hasHeightForWidth())
        self.frame_load.setSizePolicy(sizePolicy3)
        self.frame_load.setMaximumSize(QSize(16777215, 200))
        self.frame_load.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(216, 216, 216);\n"
"    border-radius: 12px;\n"
"}\n"
"QFrame QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"QFrame QLineEdit, QFrame QComboBox, QFrame QDoubleSpinBox, QFrame QTextBrowser {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 6px;\n"
"    padding: 6px 8px;\n"
"    selection-background-color: rgb(40, 84, 113);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.frame_load.setFrameShape(QFrame.NoFrame)
        self.frame_load.setFrameShadow(QFrame.Raised)
        self.verticalLayout_load = QVBoxLayout(self.frame_load)
        self.verticalLayout_load.setSpacing(8)
        self.verticalLayout_load.setObjectName(u"verticalLayout_load")
        self.verticalLayout_load.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_load_title = QHBoxLayout()
        self.horizontalLayout_load_title.setSpacing(8)
        self.horizontalLayout_load_title.setObjectName(u"horizontalLayout_load_title")
        self.label_load_icon = QLabel(self.frame_load)
        self.label_load_icon.setObjectName(u"label_load_icon")
        self.label_load_icon.setMaximumSize(QSize(20, 20))
        self.label_load_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-chart-line.png"))
        self.label_load_icon.setScaledContents(True)

        self.horizontalLayout_load_title.addWidget(self.label_load_icon)

        self.label_load_title = QLabel(self.frame_load)
        self.label_load_title.setObjectName(u"label_load_title")
        self.label_load_title.setFont(font2)
        self.label_load_title.setStyleSheet(u"color: rgb(40, 84, 113);")

        self.horizontalLayout_load_title.addWidget(self.label_load_title)

        self.horizontalSpacer_load_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_load_title.addItem(self.horizontalSpacer_load_title)

        self.load_profile_help_button = QToolButton(self.frame_load)
        self.load_profile_help_button.setObjectName(u"load_profile_help_button")
        self.load_profile_help_button.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(230, 235, 240);\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210, 218, 225);\n"
"}")
        self.load_profile_help_button.setIcon(icon)
        self.load_profile_help_button.setIconSize(QSize(20, 20))
        self.load_profile_help_button.setAutoRaise(True)

        self.horizontalLayout_load_title.addWidget(self.load_profile_help_button)


        self.verticalLayout_load.addLayout(self.horizontalLayout_load_title)

        self.label_load_desc = QLabel(self.frame_load)
        self.label_load_desc.setObjectName(u"label_load_desc")
        self.label_load_desc.setFont(font1)
        self.label_load_desc.setStyleSheet(u"color: rgb(70, 70, 70);")
        self.label_load_desc.setWordWrap(True)

        self.verticalLayout_load.addWidget(self.label_load_desc)

        self.horizontalLayout_load_profile = QHBoxLayout()
        self.horizontalLayout_load_profile.setSpacing(10)
        self.horizontalLayout_load_profile.setObjectName(u"horizontalLayout_load_profile")
        self.label_load_profile_text = QLabel(self.frame_load)
        self.label_load_profile_text.setObjectName(u"label_load_profile_text")
        self.label_load_profile_text.setFont(font2)
        self.label_load_profile_text.setStyleSheet(u"color: rgb(40, 84, 113);")

        self.horizontalLayout_load_profile.addWidget(self.label_load_profile_text)

        self.load_profile_box = QComboBox(self.frame_load)
        self.load_profile_box.setObjectName(u"load_profile_box")
        sizePolicy4.setHeightForWidth(self.load_profile_box.sizePolicy().hasHeightForWidth())
        self.load_profile_box.setSizePolicy(sizePolicy4)
        self.load_profile_box.setMaximumSize(QSize(300, 16777215))
        self.load_profile_box.setFont(font1)

        self.horizontalLayout_load_profile.addWidget(self.load_profile_box)

        self.horizontalSpacer_load_profile = QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_load_profile.addItem(self.horizontalSpacer_load_profile)


        self.verticalLayout_load.addLayout(self.horizontalLayout_load_profile)

        self.horizontalLayout_load_growth = QHBoxLayout()
        self.horizontalLayout_load_growth.setSpacing(10)
        self.horizontalLayout_load_growth.setObjectName(u"horizontalLayout_load_growth")
        self.label_load_growth_text = QLabel(self.frame_load)
        self.label_load_growth_text.setObjectName(u"label_load_growth_text")
        self.label_load_growth_text.setFont(font2)
        self.label_load_growth_text.setStyleSheet(u"color: rgb(40, 84, 113);")

        self.horizontalLayout_load_growth.addWidget(self.label_load_growth_text)

        self.annual_load_growth_box = QLineEdit(self.frame_load)
        self.annual_load_growth_box.setObjectName(u"annual_load_growth_box")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.annual_load_growth_box.sizePolicy().hasHeightForWidth())
        self.annual_load_growth_box.setSizePolicy(sizePolicy5)
        self.annual_load_growth_box.setMaximumSize(QSize(140, 16777215))
        self.annual_load_growth_box.setFont(font1)

        self.horizontalLayout_load_growth.addWidget(self.annual_load_growth_box)

        self.horizontalSpacer_load_growth = QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_load_growth.addItem(self.horizontalSpacer_load_growth)

        self.load_growth_help_button = QToolButton(self.frame_load)
        self.load_growth_help_button.setObjectName(u"load_growth_help_button")
        self.load_growth_help_button.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(230, 235, 240);\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210, 218, 225);\n"
"}")
        self.load_growth_help_button.setIcon(icon)
        self.load_growth_help_button.setIconSize(QSize(20, 20))
        self.load_growth_help_button.setAutoRaise(True)

        self.horizontalLayout_load_growth.addWidget(self.load_growth_help_button)


        self.verticalLayout_load.addLayout(self.horizontalLayout_load_growth)


        self.verticalLayout_column_left.addWidget(self.frame_load)

        self.frame_transmission = QFrame(self.frame_column_left)
        self.frame_transmission.setObjectName(u"frame_transmission")
        sizePolicy3.setHeightForWidth(self.frame_transmission.sizePolicy().hasHeightForWidth())
        self.frame_transmission.setSizePolicy(sizePolicy3)
        self.frame_transmission.setMaximumSize(QSize(16777215, 150))
        self.frame_transmission.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(216, 216, 216);\n"
"    border-radius: 12px;\n"
"}\n"
"QFrame QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"QFrame QLineEdit, QFrame QComboBox, QFrame QDoubleSpinBox, QFrame QTextBrowser {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 6px;\n"
"    padding: 6px 8px;\n"
"    selection-background-color: rgb(40, 84, 113);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.frame_transmission.setFrameShape(QFrame.NoFrame)
        self.frame_transmission.setFrameShadow(QFrame.Raised)
        self.verticalLayout_transmission = QVBoxLayout(self.frame_transmission)
        self.verticalLayout_transmission.setSpacing(10)
        self.verticalLayout_transmission.setObjectName(u"verticalLayout_transmission")
        self.verticalLayout_transmission.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_transmission_title = QHBoxLayout()
        self.horizontalLayout_transmission_title.setSpacing(8)
        self.horizontalLayout_transmission_title.setObjectName(u"horizontalLayout_transmission_title")
        self.label_transmission_icon = QLabel(self.frame_transmission)
        self.label_transmission_icon.setObjectName(u"label_transmission_icon")
        self.label_transmission_icon.setMaximumSize(QSize(20, 20))
        self.label_transmission_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-link.png"))
        self.label_transmission_icon.setScaledContents(True)

        self.horizontalLayout_transmission_title.addWidget(self.label_transmission_icon)

        self.label_transmission_title = QLabel(self.frame_transmission)
        self.label_transmission_title.setObjectName(u"label_transmission_title")
        self.label_transmission_title.setFont(font2)
        self.label_transmission_title.setStyleSheet(u"color: rgb(40, 84, 113);")

        self.horizontalLayout_transmission_title.addWidget(self.label_transmission_title)

        self.horizontalSpacer_transmission_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_transmission_title.addItem(self.horizontalSpacer_transmission_title)

        self.trans_expansion_help_button = QToolButton(self.frame_transmission)
        self.trans_expansion_help_button.setObjectName(u"trans_expansion_help_button")
        self.trans_expansion_help_button.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(230, 235, 240);\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210, 218, 225);\n"
"}")
        self.trans_expansion_help_button.setIcon(icon)
        self.trans_expansion_help_button.setIconSize(QSize(20, 20))
        self.trans_expansion_help_button.setAutoRaise(True)

        self.horizontalLayout_transmission_title.addWidget(self.trans_expansion_help_button)


        self.verticalLayout_transmission.addLayout(self.horizontalLayout_transmission_title)

        self.label_transmission_desc = QLabel(self.frame_transmission)
        self.label_transmission_desc.setObjectName(u"label_transmission_desc")
        self.label_transmission_desc.setFont(font1)
        self.label_transmission_desc.setStyleSheet(u"color: rgb(70, 70, 70);")
        self.label_transmission_desc.setWordWrap(True)

        self.verticalLayout_transmission.addWidget(self.label_transmission_desc)

        self.transmission_box = QComboBox(self.frame_transmission)
        self.transmission_box.addItem("")
        self.transmission_box.addItem("")
        self.transmission_box.setObjectName(u"transmission_box")
        sizePolicy4.setHeightForWidth(self.transmission_box.sizePolicy().hasHeightForWidth())
        self.transmission_box.setSizePolicy(sizePolicy4)
        self.transmission_box.setMaximumSize(QSize(300, 16777215))
        self.transmission_box.setFont(font1)

        self.verticalLayout_transmission.addWidget(self.transmission_box)


        self.verticalLayout_column_left.addWidget(self.frame_transmission)

        self.verticalSpacer_left = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_column_left.addItem(self.verticalSpacer_left)


        self.horizontalLayout_columns.addWidget(self.frame_column_left)

        self.frame_column_right = QFrame(self.frame_columns)
        self.frame_column_right.setObjectName(u"frame_column_right")
        sizePolicy2.setHeightForWidth(self.frame_column_right.sizePolicy().hasHeightForWidth())
        self.frame_column_right.setSizePolicy(sizePolicy2)
        self.frame_column_right.setFrameShape(QFrame.NoFrame)
        self.frame_column_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_column_right = QVBoxLayout(self.frame_column_right)
        self.verticalLayout_column_right.setSpacing(18)
        self.verticalLayout_column_right.setObjectName(u"verticalLayout_column_right")
        self.verticalLayout_column_right.setContentsMargins(0, 0, 0, 0)
        self.frame_policy = QFrame(self.frame_column_right)
        self.frame_policy.setObjectName(u"frame_policy")
        sizePolicy3.setHeightForWidth(self.frame_policy.sizePolicy().hasHeightForWidth())
        self.frame_policy.setSizePolicy(sizePolicy3)
        self.frame_policy.setMaximumSize(QSize(16777215, 150))
        self.frame_policy.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(216, 216, 216);\n"
"    border-radius: 12px;\n"
"}\n"
"QFrame QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"QFrame QLineEdit, QFrame QComboBox, QFrame QDoubleSpinBox, QFrame QTextBrowser {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 6px;\n"
"    padding: 6px 8px;\n"
"    selection-background-color: rgb(40, 84, 113);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.frame_policy.setFrameShape(QFrame.NoFrame)
        self.frame_policy.setFrameShadow(QFrame.Raised)
        self.verticalLayout_policy = QVBoxLayout(self.frame_policy)
        self.verticalLayout_policy.setSpacing(10)
        self.verticalLayout_policy.setObjectName(u"verticalLayout_policy")
        self.verticalLayout_policy.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_policy_title = QHBoxLayout()
        self.horizontalLayout_policy_title.setSpacing(8)
        self.horizontalLayout_policy_title.setObjectName(u"horizontalLayout_policy_title")
        self.label_policy_icon = QLabel(self.frame_policy)
        self.label_policy_icon.setObjectName(u"label_policy_icon")
        self.label_policy_icon.setMaximumSize(QSize(20, 20))
        self.label_policy_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-fire.png"))
        self.label_policy_icon.setScaledContents(True)

        self.horizontalLayout_policy_title.addWidget(self.label_policy_icon)

        self.label_policy_title = QLabel(self.frame_policy)
        self.label_policy_title.setObjectName(u"label_policy_title")
        self.label_policy_title.setFont(font2)
        self.label_policy_title.setStyleSheet(u"color: rgb(40, 84, 113);")

        self.horizontalLayout_policy_title.addWidget(self.label_policy_title)

        self.horizontalSpacer_policy_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_policy_title.addItem(self.horizontalSpacer_policy_title)

        self.rps_help_button = QToolButton(self.frame_policy)
        self.rps_help_button.setObjectName(u"rps_help_button")
        self.rps_help_button.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(230, 235, 240);\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210, 218, 225);\n"
"}")
        self.rps_help_button.setIcon(icon)
        self.rps_help_button.setIconSize(QSize(20, 20))
        self.rps_help_button.setAutoRaise(True)

        self.horizontalLayout_policy_title.addWidget(self.rps_help_button)


        self.verticalLayout_policy.addLayout(self.horizontalLayout_policy_title)

        self.label_policy_desc = QLabel(self.frame_policy)
        self.label_policy_desc.setObjectName(u"label_policy_desc")
        self.label_policy_desc.setFont(font1)
        self.label_policy_desc.setStyleSheet(u"color: rgb(70, 70, 70);")
        self.label_policy_desc.setWordWrap(True)

        self.verticalLayout_policy.addWidget(self.label_policy_desc)

        self.rps_box = QComboBox(self.frame_policy)
        self.rps_box.addItem("")
        self.rps_box.addItem("")
        self.rps_box.setObjectName(u"rps_box")
        sizePolicy4.setHeightForWidth(self.rps_box.sizePolicy().hasHeightForWidth())
        self.rps_box.setSizePolicy(sizePolicy4)
        self.rps_box.setMaximumSize(QSize(300, 16777215))
        self.rps_box.setFont(font1)

        self.verticalLayout_policy.addWidget(self.rps_box)


        self.verticalLayout_column_right.addWidget(self.frame_policy)

        self.frame_candidates = QFrame(self.frame_column_right)
        self.frame_candidates.setObjectName(u"frame_candidates")
        sizePolicy3.setHeightForWidth(self.frame_candidates.sizePolicy().hasHeightForWidth())
        self.frame_candidates.setSizePolicy(sizePolicy3)
        self.frame_candidates.setMaximumSize(QSize(16777215, 230))
        self.frame_candidates.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(216, 216, 216);\n"
"    border-radius: 12px;\n"
"}\n"
"QFrame QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"QFrame QLineEdit, QFrame QComboBox, QFrame QDoubleSpinBox, QFrame QTextBrowser {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 6px;\n"
"    padding: 6px 8px;\n"
"    selection-background-color: rgb(40, 84, 113);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QFrame#cand_tech_frame {\n"
"    background-color: rgb(247, 247, 247);\n"
"    border: 1px solid rgb(232, 232, 232);\n"
"    border-radius: 8px;\n"
"}")
        self.frame_candidates.setFrameShape(QFrame.NoFrame)
        self.frame_candidates.setFrameShadow(QFrame.Raised)
        self.verticalLayout_candidates = QVBoxLayout(self.frame_candidates)
        self.verticalLayout_candidates.setSpacing(10)
        self.verticalLayout_candidates.setObjectName(u"verticalLayout_candidates")
        self.verticalLayout_candidates.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_candidates_title = QHBoxLayout()
        self.horizontalLayout_candidates_title.setSpacing(8)
        self.horizontalLayout_candidates_title.setObjectName(u"horizontalLayout_candidates_title")
        self.label_candidates_icon = QLabel(self.frame_candidates)
        self.label_candidates_icon.setObjectName(u"label_candidates_icon")
        self.label_candidates_icon.setMaximumSize(QSize(20, 20))
        self.label_candidates_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-layers.png"))
        self.label_candidates_icon.setScaledContents(True)

        self.horizontalLayout_candidates_title.addWidget(self.label_candidates_icon)

        self.label_candidates_title = QLabel(self.frame_candidates)
        self.label_candidates_title.setObjectName(u"label_candidates_title")
        self.label_candidates_title.setFont(font2)
        self.label_candidates_title.setStyleSheet(u"color: rgb(40, 84, 113);")

        self.horizontalLayout_candidates_title.addWidget(self.label_candidates_title)

        self.horizontalSpacer_candidates_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_candidates_title.addItem(self.horizontalSpacer_candidates_title)

        self.cand_technologies_help_button = QToolButton(self.frame_candidates)
        self.cand_technologies_help_button.setObjectName(u"cand_technologies_help_button")
        self.cand_technologies_help_button.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(230, 235, 240);\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210, 218, 225);\n"
"}")
        self.cand_technologies_help_button.setIcon(icon)
        self.cand_technologies_help_button.setIconSize(QSize(20, 20))
        self.cand_technologies_help_button.setAutoRaise(True)

        self.horizontalLayout_candidates_title.addWidget(self.cand_technologies_help_button)


        self.verticalLayout_candidates.addLayout(self.horizontalLayout_candidates_title)

        self.label_candidates_desc = QLabel(self.frame_candidates)
        self.label_candidates_desc.setObjectName(u"label_candidates_desc")
        self.label_candidates_desc.setFont(font1)
        self.label_candidates_desc.setStyleSheet(u"color: rgb(70, 70, 70);")
        self.label_candidates_desc.setWordWrap(True)

        self.verticalLayout_candidates.addWidget(self.label_candidates_desc)

        self.horizontalLayout_cand_button = QHBoxLayout()
        self.horizontalLayout_cand_button.setSpacing(10)
        self.horizontalLayout_cand_button.setObjectName(u"horizontalLayout_cand_button")
        self.cand_tech_button = QPushButton(self.frame_candidates)
        self.cand_tech_button.setObjectName(u"cand_tech_button")
        sizePolicy5.setHeightForWidth(self.cand_tech_button.sizePolicy().hasHeightForWidth())
        self.cand_tech_button.setSizePolicy(sizePolicy5)
        self.cand_tech_button.setMinimumSize(QSize(220, 0))
        self.cand_tech_button.setFont(font2)
        self.cand_tech_button.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid rgb(40, 84, 113);\n"
"    border-radius: 7px;\n"
"    background-color: rgb(40, 84, 113);\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 7px 16px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 120, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 60, 80);\n"
"}")

        self.horizontalLayout_cand_button.addWidget(self.cand_tech_button)

        self.horizontalSpacer_cand_button = QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_cand_button.addItem(self.horizontalSpacer_cand_button)


        self.verticalLayout_candidates.addLayout(self.horizontalLayout_cand_button)

        self.cand_tech_frame = QFrame(self.frame_candidates)
        self.cand_tech_frame.setObjectName(u"cand_tech_frame")
        sizePolicy3.setHeightForWidth(self.cand_tech_frame.sizePolicy().hasHeightForWidth())
        self.cand_tech_frame.setSizePolicy(sizePolicy3)
        self.cand_tech_frame.setMaximumSize(QSize(16777215, 150))
        self.cand_tech_frame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(247, 247, 247);\n"
"    border: 1px solid rgb(232, 232, 232);\n"
"    border-radius: 8px;\n"
"}\n"
"QFrame QLabel {\n"
"    background-color: transparent;\n"
"}")
        self.cand_tech_frame.setFrameShape(QFrame.NoFrame)
        self.cand_tech_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_cand_tech = QVBoxLayout(self.cand_tech_frame)
        self.verticalLayout_cand_tech.setSpacing(6)
        self.verticalLayout_cand_tech.setObjectName(u"verticalLayout_cand_tech")
        self.verticalLayout_cand_tech.setContentsMargins(12, 10, 12, 10)
        self.label_cand_tech_list_title = QLabel(self.cand_tech_frame)
        self.label_cand_tech_list_title.setObjectName(u"label_cand_tech_list_title")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setBold(True)
        self.label_cand_tech_list_title.setFont(font3)
        self.label_cand_tech_list_title.setStyleSheet(u"color: rgb(40, 84, 113);")

        self.verticalLayout_cand_tech.addWidget(self.label_cand_tech_list_title)

        self.candidate_tech_box = QTextBrowser(self.cand_tech_frame)
        self.candidate_tech_box.setObjectName(u"candidate_tech_box")
        self.candidate_tech_box.setMinimumSize(QSize(0, 70))
        self.candidate_tech_box.setFont(font1)
        self.candidate_tech_box.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_cand_tech.addWidget(self.candidate_tech_box)


        self.verticalLayout_candidates.addWidget(self.cand_tech_frame)


        self.verticalLayout_column_right.addWidget(self.frame_candidates)

        self.frame_retirements = QFrame(self.frame_column_right)
        self.frame_retirements.setObjectName(u"frame_retirements")
        sizePolicy3.setHeightForWidth(self.frame_retirements.sizePolicy().hasHeightForWidth())
        self.frame_retirements.setSizePolicy(sizePolicy3)
        self.frame_retirements.setMaximumSize(QSize(16777215, 230))
        self.frame_retirements.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(216, 216, 216);\n"
"    border-radius: 12px;\n"
"}\n"
"QFrame QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"QFrame QLineEdit, QFrame QComboBox, QFrame QDoubleSpinBox, QFrame QTextBrowser {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(204, 204, 204);\n"
"    border-radius: 6px;\n"
"    padding: 6px 8px;\n"
"    selection-background-color: rgb(40, 84, 113);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QFrame#retirement_frame {\n"
"    background-color: rgb(247, 247, 247);\n"
"    border: 1px solid rgb(232, 232, 232);\n"
"    border-radius: 8px;\n"
"}")
        self.frame_retirements.setFrameShape(QFrame.NoFrame)
        self.frame_retirements.setFrameShadow(QFrame.Raised)
        self.verticalLayout_retirements = QVBoxLayout(self.frame_retirements)
        self.verticalLayout_retirements.setSpacing(10)
        self.verticalLayout_retirements.setObjectName(u"verticalLayout_retirements")
        self.verticalLayout_retirements.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_retirements_title = QHBoxLayout()
        self.horizontalLayout_retirements_title.setSpacing(8)
        self.horizontalLayout_retirements_title.setObjectName(u"horizontalLayout_retirements_title")
        self.label_retirements_icon = QLabel(self.frame_retirements)
        self.label_retirements_icon.setObjectName(u"label_retirements_icon")
        self.label_retirements_icon.setMaximumSize(QSize(20, 20))
        self.label_retirements_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-history.png"))
        self.label_retirements_icon.setScaledContents(True)

        self.horizontalLayout_retirements_title.addWidget(self.label_retirements_icon)

        self.label_retirements_title = QLabel(self.frame_retirements)
        self.label_retirements_title.setObjectName(u"label_retirements_title")
        self.label_retirements_title.setFont(font2)
        self.label_retirements_title.setStyleSheet(u"color: rgb(40, 84, 113);")

        self.horizontalLayout_retirements_title.addWidget(self.label_retirements_title)

        self.horizontalSpacer_retirements_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_retirements_title.addItem(self.horizontalSpacer_retirements_title)

        self.gen_retirement_help_button = QToolButton(self.frame_retirements)
        self.gen_retirement_help_button.setObjectName(u"gen_retirement_help_button")
        self.gen_retirement_help_button.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: transparent;\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: rgb(230, 235, 240);\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210, 218, 225);\n"
"}")
        self.gen_retirement_help_button.setIcon(icon)
        self.gen_retirement_help_button.setIconSize(QSize(20, 20))
        self.gen_retirement_help_button.setAutoRaise(True)

        self.horizontalLayout_retirements_title.addWidget(self.gen_retirement_help_button)


        self.verticalLayout_retirements.addLayout(self.horizontalLayout_retirements_title)

        self.label_retirements_desc = QLabel(self.frame_retirements)
        self.label_retirements_desc.setObjectName(u"label_retirements_desc")
        self.label_retirements_desc.setFont(font1)
        self.label_retirements_desc.setStyleSheet(u"color: rgb(70, 70, 70);")
        self.label_retirements_desc.setWordWrap(True)

        self.verticalLayout_retirements.addWidget(self.label_retirements_desc)

        self.horizontalLayout_retirement_button = QHBoxLayout()
        self.horizontalLayout_retirement_button.setSpacing(10)
        self.horizontalLayout_retirement_button.setObjectName(u"horizontalLayout_retirement_button")
        self.gen_retirement_button = QPushButton(self.frame_retirements)
        self.gen_retirement_button.setObjectName(u"gen_retirement_button")
        sizePolicy5.setHeightForWidth(self.gen_retirement_button.sizePolicy().hasHeightForWidth())
        self.gen_retirement_button.setSizePolicy(sizePolicy5)
        self.gen_retirement_button.setMinimumSize(QSize(200, 0))
        self.gen_retirement_button.setFont(font2)
        self.gen_retirement_button.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid rgb(40, 84, 113);\n"
"    border-radius: 7px;\n"
"    background-color: rgb(40, 84, 113);\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 7px 16px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 120, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 60, 80);\n"
"}")

        self.horizontalLayout_retirement_button.addWidget(self.gen_retirement_button)

        self.horizontalSpacer_retirement_button = QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_retirement_button.addItem(self.horizontalSpacer_retirement_button)


        self.verticalLayout_retirements.addLayout(self.horizontalLayout_retirement_button)

        self.retirement_frame = QFrame(self.frame_retirements)
        self.retirement_frame.setObjectName(u"retirement_frame")
        sizePolicy3.setHeightForWidth(self.retirement_frame.sizePolicy().hasHeightForWidth())
        self.retirement_frame.setSizePolicy(sizePolicy3)
        self.retirement_frame.setMaximumSize(QSize(16777215, 150))
        self.retirement_frame.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(247, 247, 247);\n"
"    border: 1px solid rgb(232, 232, 232);\n"
"    border-radius: 8px;\n"
"}\n"
"QFrame QLabel {\n"
"    background-color: transparent;\n"
"}")
        self.retirement_frame.setFrameShape(QFrame.NoFrame)
        self.retirement_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_retirement = QVBoxLayout(self.retirement_frame)
        self.verticalLayout_retirement.setSpacing(6)
        self.verticalLayout_retirement.setObjectName(u"verticalLayout_retirement")
        self.verticalLayout_retirement.setContentsMargins(12, 10, 12, 10)
        self.label_retirement_list_title = QLabel(self.retirement_frame)
        self.label_retirement_list_title.setObjectName(u"label_retirement_list_title")
        self.label_retirement_list_title.setFont(font3)
        self.label_retirement_list_title.setStyleSheet(u"color: rgb(40, 84, 113);")

        self.verticalLayout_retirement.addWidget(self.label_retirement_list_title)

        self.retirement_box = QTextBrowser(self.retirement_frame)
        self.retirement_box.setObjectName(u"retirement_box")
        self.retirement_box.setMinimumSize(QSize(0, 70))
        self.retirement_box.setFont(font1)
        self.retirement_box.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_retirement.addWidget(self.retirement_box)


        self.verticalLayout_retirements.addWidget(self.retirement_frame)


        self.verticalLayout_column_right.addWidget(self.frame_retirements)

        self.verticalSpacer_right = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_column_right.addItem(self.verticalSpacer_right)


        self.horizontalLayout_columns.addWidget(self.frame_column_right)


        self.verticalLayout_main.addWidget(self.frame_columns)

        self.frame_actions = QFrame(ScenarioBuilderPage)
        self.frame_actions.setObjectName(u"frame_actions")
        sizePolicy1.setHeightForWidth(self.frame_actions.sizePolicy().hasHeightForWidth())
        self.frame_actions.setSizePolicy(sizePolicy1)
        self.frame_actions.setMaximumSize(QSize(16777215, 56))
        self.frame_actions.setFrameShape(QFrame.NoFrame)
        self.frame_actions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_actions = QHBoxLayout(self.frame_actions)
        self.horizontalLayout_actions.setObjectName(u"horizontalLayout_actions")
        self.horizontalLayout_actions.setContentsMargins(0, 0, 0, 0)
        self.label_actions_hint = QLabel(self.frame_actions)
        self.label_actions_hint.setObjectName(u"label_actions_hint")
        self.label_actions_hint.setFont(font1)
        self.label_actions_hint.setStyleSheet(u"color: rgb(100, 100, 100);\n"
"background-color: transparent;")

        self.horizontalLayout_actions.addWidget(self.label_actions_hint)

        self.horizontalSpacer_actions = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_actions.addItem(self.horizontalSpacer_actions)

        self.view_scenario_button = QPushButton(self.frame_actions)
        self.view_scenario_button.setObjectName(u"view_scenario_button")
        sizePolicy5.setHeightForWidth(self.view_scenario_button.sizePolicy().hasHeightForWidth())
        self.view_scenario_button.setSizePolicy(sizePolicy5)
        self.view_scenario_button.setMinimumSize(QSize(180, 0))
        self.view_scenario_button.setFont(font2)
        self.view_scenario_button.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid rgb(40, 84, 113);\n"
"    border-radius: 7px;\n"
"    background-color: rgb(40, 84, 113);\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 7px 16px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 120, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 60, 80);\n"
"}")

        self.horizontalLayout_actions.addWidget(self.view_scenario_button)


        self.verticalLayout_main.addWidget(self.frame_actions)

        self.verticalLayout_main.setStretch(1, 1)

        self.retranslateUi(ScenarioBuilderPage)

        QMetaObject.connectSlotsByName(ScenarioBuilderPage)
    # setupUi

    def retranslateUi(self, ScenarioBuilderPage):
        ScenarioBuilderPage.setWindowTitle(QCoreApplication.translate("ScenarioBuilderPage", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Scenario Builder", None))
        self.label_subtitle.setText(QCoreApplication.translate("ScenarioBuilderPage", u"The QuESt Planning scenario builder turns your model configuration into a runnable scenario.", None))
        self.scenario_builder_help_button.setText("")
        self.label_scenario_icon.setText("")
        self.label_scenario_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"SCENARIO NAME", None))
        self.scenario_name_help_button.setText("")
        self.label_scenario_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"The <b><i>Scenario Name</i></b> you provide should be unique to this <i>QuESt Planning</i> scenario, as it will be used to save the print results.", None))
        self.scenario_name_box.setPlaceholderText(QCoreApplication.translate("ScenarioBuilderPage", u"Base Scenario", None))
        self.label_capital_cost_icon.setText("")
        self.label_capital_cost_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"RESOURCE CAPITAL COSTS", None))
        self.capital_cost_trajectory_help_button.setText("")
        self.label_capital_cost_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Select the <b><i>capital cost trajectory</i></b> that <i>QuESt Planning</i> will use for the energy storage technologies. The cost trajectories are defined in the input csv data.", None))
        self.capital_cost_box.setItemText(0, QCoreApplication.translate("ScenarioBuilderPage", u"Baseline", None))
        self.capital_cost_box.setItemText(1, QCoreApplication.translate("ScenarioBuilderPage", u"Low", None))
        self.capital_cost_box.setItemText(2, QCoreApplication.translate("ScenarioBuilderPage", u"Moderate", None))
        self.capital_cost_box.setItemText(3, QCoreApplication.translate("ScenarioBuilderPage", u"High", None))

        self.label_load_icon.setText("")
        self.label_load_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"LOAD FORECASTS", None))
        self.load_profile_help_button.setText("")
        self.label_load_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Select the <b><i>load forecast</i></b> used by <i>QuESt Planning</i>. The forecasts are defined in the csv data.", None))
        self.label_load_profile_text.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Load Forecast", None))
        self.label_load_growth_text.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Annual Load Growth", None))
        self.annual_load_growth_box.setText(QCoreApplication.translate("ScenarioBuilderPage", u"1.5", None))
        self.annual_load_growth_box.setPlaceholderText(QCoreApplication.translate("ScenarioBuilderPage", u"%", None))
        self.load_growth_help_button.setText("")
        self.label_transmission_icon.setText("")
        self.label_transmission_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"TRANSMISSION EXPANSION", None))
        self.trans_expansion_help_button.setText("")
        self.label_transmission_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Choose whether <i>QuESt Planning</i> may expand the transmission network. Transmission expansion is a feature that will be added in a later release.", None))
        self.transmission_box.setItemText(0, QCoreApplication.translate("ScenarioBuilderPage", u"Yes", None))
        self.transmission_box.setItemText(1, QCoreApplication.translate("ScenarioBuilderPage", u"No", None))

        self.label_policy_icon.setText("")
        self.label_policy_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"FUTURE GENERATION MIX", None))
        self.rps_help_button.setText("")
        self.label_policy_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Select the <b><i>Future Generation Mix</i></b> to be used in the scenario. The schedule can be defined in the csv data, or select <i>Create New...</i> to define custom targets.", None))
        self.rps_box.setItemText(0, QCoreApplication.translate("ScenarioBuilderPage", u"Default", None))
        self.rps_box.setItemText(1, QCoreApplication.translate("ScenarioBuilderPage", u"Create New...", None))

        self.label_candidates_icon.setText("")
        self.label_candidates_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"CANDIDATE TECHNOLOGIES", None))
        self.cand_technologies_help_button.setText("")
        self.label_candidates_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Click the <b><i>Candidate Technologies</i></b> button to select the candidate technologies to be considered in the <i>QuESt Planning</i> optimization.", None))
        self.cand_tech_button.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Candidate Technologies", None))
        self.label_cand_tech_list_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"SELECTED CANDIDATE TECHNOLOGIES", None))
        self.label_retirements_icon.setText("")
        self.label_retirements_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"GENERATION RETIREMENTS", None))
        self.gen_retirement_help_button.setText("")
        self.label_retirements_desc.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Click the <b><i>Retirement Schedule</i></b> button to select the retirement schedule enforced in the <i>QuESt Planning</i> optimization. The <i>Default</i> option uses the schedule detailed in the csv data.", None))
        self.gen_retirement_button.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Retirement Schedule", None))
        self.label_retirement_list_title.setText(QCoreApplication.translate("ScenarioBuilderPage", u"SELECTED RETIREMENT SCHEDULE", None))
        self.label_actions_hint.setText(QCoreApplication.translate("ScenarioBuilderPage", u"Press <i>View Scenario</i> to review the complete scenario and model configuration.", None))
        self.view_scenario_button.setText(QCoreApplication.translate("ScenarioBuilderPage", u"View Scenario", None))
    # retranslateUi

