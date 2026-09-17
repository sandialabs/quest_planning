# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'results_viewer.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QToolButton, QTreeView,
    QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_ResultsViewerPage(object):
    def setupUi(self, ResultsViewerPage):
        if not ResultsViewerPage.objectName():
            ResultsViewerPage.setObjectName(u"ResultsViewerPage")
        ResultsViewerPage.resize(1118, 928)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ResultsViewerPage.sizePolicy().hasHeightForWidth())
        ResultsViewerPage.setSizePolicy(sizePolicy)
        self.verticalLayout_main = QVBoxLayout(ResultsViewerPage)
        self.verticalLayout_main.setSpacing(18)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(24, 24, 24, 24)
        self.frame_header = QFrame(ResultsViewerPage)
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

        self.results_help_button = QToolButton(self.frame_header)
        self.results_help_button.setObjectName(u"results_help_button")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/help_FILL0_wght200_GRAD0_opsz48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.results_help_button.setIcon(icon)
        self.results_help_button.setIconSize(QSize(24, 24))
        self.results_help_button.setAutoRaise(True)

        self.horizontalLayout_header.addWidget(self.results_help_button)


        self.verticalLayout_main.addWidget(self.frame_header)

        self.frame_actions = QFrame(ResultsViewerPage)
        self.frame_actions.setObjectName(u"frame_actions")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_actions.sizePolicy().hasHeightForWidth())
        self.frame_actions.setSizePolicy(sizePolicy2)
        self.frame_actions.setMaximumSize(QSize(16777215, 300))
        self.frame_actions.setFrameShape(QFrame.NoFrame)
        self.frame_actions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_actions = QVBoxLayout(self.frame_actions)
        self.verticalLayout_actions.setSpacing(10)
        self.verticalLayout_actions.setObjectName(u"verticalLayout_actions")
        self.verticalLayout_actions.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_actions_title = QHBoxLayout()
        self.horizontalLayout_actions_title.setSpacing(8)
        self.horizontalLayout_actions_title.setObjectName(u"horizontalLayout_actions_title")
        self.label_actions_icon = QLabel(self.frame_actions)
        self.label_actions_icon.setObjectName(u"label_actions_icon")
        self.label_actions_icon.setMaximumSize(QSize(22, 22))
        self.label_actions_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-chart-pie.png"))
        self.label_actions_icon.setScaledContents(True)

        self.horizontalLayout_actions_title.addWidget(self.label_actions_icon)

        self.label_actions_title = QLabel(self.frame_actions)
        self.label_actions_title.setObjectName(u"label_actions_title")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_actions_title.setFont(font2)

        self.horizontalLayout_actions_title.addWidget(self.label_actions_title)

        self.horizontalSpacer_actions_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_actions_title.addItem(self.horizontalSpacer_actions_title)


        self.verticalLayout_actions.addLayout(self.horizontalLayout_actions_title)

        self.label_actions_desc = QLabel(self.frame_actions)
        self.label_actions_desc.setObjectName(u"label_actions_desc")
        self.label_actions_desc.setFont(font1)
        self.label_actions_desc.setWordWrap(True)

        self.verticalLayout_actions.addWidget(self.label_actions_desc)

        self.horizontalLayout_actions_buttons = QHBoxLayout()
        self.horizontalLayout_actions_buttons.setSpacing(12)
        self.horizontalLayout_actions_buttons.setObjectName(u"horizontalLayout_actions_buttons")
        self.collect_results_button = QPushButton(self.frame_actions)
        self.collect_results_button.setObjectName(u"collect_results_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.collect_results_button.sizePolicy().hasHeightForWidth())
        self.collect_results_button.setSizePolicy(sizePolicy3)
        self.collect_results_button.setMinimumSize(QSize(160, 0))
        self.collect_results_button.setFont(font2)

        self.horizontalLayout_actions_buttons.addWidget(self.collect_results_button)

        self.gen_plots_button = QPushButton(self.frame_actions)
        self.gen_plots_button.setObjectName(u"gen_plots_button")
        sizePolicy3.setHeightForWidth(self.gen_plots_button.sizePolicy().hasHeightForWidth())
        self.gen_plots_button.setSizePolicy(sizePolicy3)
        self.gen_plots_button.setMinimumSize(QSize(160, 0))
        self.gen_plots_button.setFont(font2)

        self.horizontalLayout_actions_buttons.addWidget(self.gen_plots_button)

        self.save_results_button = QPushButton(self.frame_actions)
        self.save_results_button.setObjectName(u"save_results_button")
        sizePolicy3.setHeightForWidth(self.save_results_button.sizePolicy().hasHeightForWidth())
        self.save_results_button.setSizePolicy(sizePolicy3)
        self.save_results_button.setMinimumSize(QSize(160, 0))
        self.save_results_button.setFont(font2)

        self.horizontalLayout_actions_buttons.addWidget(self.save_results_button)

        self.label_actions_hint = QLabel(self.frame_actions)
        self.label_actions_hint.setObjectName(u"label_actions_hint")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        self.label_actions_hint.setFont(font3)

        self.horizontalLayout_actions_buttons.addWidget(self.label_actions_hint)

        self.horizontalSpacer_actions = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_actions_buttons.addItem(self.horizontalSpacer_actions)


        self.verticalLayout_actions.addLayout(self.horizontalLayout_actions_buttons)


        self.verticalLayout_main.addWidget(self.frame_actions)

        self.frame_viewer = QFrame(ResultsViewerPage)
        self.frame_viewer.setObjectName(u"frame_viewer")
        sizePolicy.setHeightForWidth(self.frame_viewer.sizePolicy().hasHeightForWidth())
        self.frame_viewer.setSizePolicy(sizePolicy)
        self.frame_viewer.setFrameShape(QFrame.NoFrame)
        self.frame_viewer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_viewer = QVBoxLayout(self.frame_viewer)
        self.verticalLayout_viewer.setSpacing(10)
        self.verticalLayout_viewer.setObjectName(u"verticalLayout_viewer")
        self.verticalLayout_viewer.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_viewer_title = QHBoxLayout()
        self.horizontalLayout_viewer_title.setSpacing(8)
        self.horizontalLayout_viewer_title.setObjectName(u"horizontalLayout_viewer_title")
        self.label_viewer_icon = QLabel(self.frame_viewer)
        self.label_viewer_icon.setObjectName(u"label_viewer_icon")
        self.label_viewer_icon.setMaximumSize(QSize(22, 22))
        self.label_viewer_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-folder-open.png"))
        self.label_viewer_icon.setScaledContents(True)

        self.horizontalLayout_viewer_title.addWidget(self.label_viewer_icon)

        self.label_viewer_title = QLabel(self.frame_viewer)
        self.label_viewer_title.setObjectName(u"label_viewer_title")
        self.label_viewer_title.setFont(font2)

        self.horizontalLayout_viewer_title.addWidget(self.label_viewer_title)

        self.horizontalSpacer_viewer_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_viewer_title.addItem(self.horizontalSpacer_viewer_title)

        self.png_toggler = QToolButton(self.frame_viewer)
        self.png_toggler.setObjectName(u"png_toggler")
        self.png_toggler.setCheckable(True)
        self.png_toggler.setChecked(True)

        self.horizontalLayout_viewer_title.addWidget(self.png_toggler)

        self.html_toggler = QToolButton(self.frame_viewer)
        self.html_toggler.setObjectName(u"html_toggler")
        self.html_toggler.setCheckable(True)

        self.horizontalLayout_viewer_title.addWidget(self.html_toggler)


        self.verticalLayout_viewer.addLayout(self.horizontalLayout_viewer_title)

        self.label_viewer_desc = QLabel(self.frame_viewer)
        self.label_viewer_desc.setObjectName(u"label_viewer_desc")
        self.label_viewer_desc.setFont(font3)
        self.label_viewer_desc.setWordWrap(True)

        self.verticalLayout_viewer.addWidget(self.label_viewer_desc)

        self.line_divider = QFrame(self.frame_viewer)
        self.line_divider.setObjectName(u"line_divider")
        self.line_divider.setMaximumSize(QSize(16777215, 1))
        self.line_divider.setFrameShape(QFrame.Shape.HLine)
        self.line_divider.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_viewer.addWidget(self.line_divider)

        self.horizontalLayout_viewer_body = QHBoxLayout()
        self.horizontalLayout_viewer_body.setSpacing(12)
        self.horizontalLayout_viewer_body.setObjectName(u"horizontalLayout_viewer_body")
        self.frame_file_browser = QFrame(self.frame_viewer)
        self.frame_file_browser.setObjectName(u"frame_file_browser")
        self.frame_file_browser.setMinimumSize(QSize(240, 0))
        self.frame_file_browser.setMaximumSize(QSize(320, 16777215))
        self.frame_file_browser.setFrameShape(QFrame.NoFrame)
        self.frame_file_browser.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_file_browser)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(12, 12, 12, 12)
        self.label_browser_title = QLabel(self.frame_file_browser)
        self.label_browser_title.setObjectName(u"label_browser_title")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(9)
        font4.setBold(True)
        self.label_browser_title.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_browser_title)

        self.horizontalLayout_browser_folder = QHBoxLayout()
        self.horizontalLayout_browser_folder.setSpacing(8)
        self.horizontalLayout_browser_folder.setObjectName(u"horizontalLayout_browser_folder")
        self.label_browser_folder = QLabel(self.frame_file_browser)
        self.label_browser_folder.setObjectName(u"label_browser_folder")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_browser_folder.sizePolicy().hasHeightForWidth())
        self.label_browser_folder.setSizePolicy(sizePolicy4)
        self.label_browser_folder.setFont(font3)

        self.horizontalLayout_browser_folder.addWidget(self.label_browser_folder)

        self.png_browser = QPushButton(self.frame_file_browser)
        self.png_browser.setObjectName(u"png_browser")
        sizePolicy3.setHeightForWidth(self.png_browser.sizePolicy().hasHeightForWidth())
        self.png_browser.setSizePolicy(sizePolicy3)
        self.png_browser.setMinimumSize(QSize(96, 0))
        self.png_browser.setFont(font4)

        self.horizontalLayout_browser_folder.addWidget(self.png_browser)


        self.verticalLayout_7.addLayout(self.horizontalLayout_browser_folder)

        self.file_browser = QTreeView(self.frame_file_browser)
        self.file_browser.setObjectName(u"file_browser")
        sizePolicy.setHeightForWidth(self.file_browser.sizePolicy().hasHeightForWidth())
        self.file_browser.setSizePolicy(sizePolicy)
        self.file_browser.setMinimumSize(QSize(0, 180))
        self.file_browser.setIconSize(QSize(16, 16))
        self.file_browser.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.file_browser.setHeaderHidden(True)

        self.verticalLayout_7.addWidget(self.file_browser)

        self.line_divider_2 = QFrame(self.frame_file_browser)
        self.line_divider_2.setObjectName(u"line_divider_2")
        self.line_divider_2.setMaximumSize(QSize(16777215, 1))
        self.line_divider_2.setFrameShape(QFrame.Shape.HLine)
        self.line_divider_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_divider_2)

        self.horizontalLayout_browser_map_folder = QHBoxLayout()
        self.horizontalLayout_browser_map_folder.setSpacing(8)
        self.horizontalLayout_browser_map_folder.setObjectName(u"horizontalLayout_browser_map_folder")
        self.label_browser_map_folder = QLabel(self.frame_file_browser)
        self.label_browser_map_folder.setObjectName(u"label_browser_map_folder")
        sizePolicy4.setHeightForWidth(self.label_browser_map_folder.sizePolicy().hasHeightForWidth())
        self.label_browser_map_folder.setSizePolicy(sizePolicy4)
        self.label_browser_map_folder.setFont(font3)

        self.horizontalLayout_browser_map_folder.addWidget(self.label_browser_map_folder)

        self.html_browser = QPushButton(self.frame_file_browser)
        self.html_browser.setObjectName(u"html_browser")
        sizePolicy3.setHeightForWidth(self.html_browser.sizePolicy().hasHeightForWidth())
        self.html_browser.setSizePolicy(sizePolicy3)
        self.html_browser.setMinimumSize(QSize(96, 0))
        self.html_browser.setFont(font4)

        self.horizontalLayout_browser_map_folder.addWidget(self.html_browser)


        self.verticalLayout_7.addLayout(self.horizontalLayout_browser_map_folder)

        self.html_file_browser = QTreeView(self.frame_file_browser)
        self.html_file_browser.setObjectName(u"html_file_browser")
        sizePolicy.setHeightForWidth(self.html_file_browser.sizePolicy().hasHeightForWidth())
        self.html_file_browser.setSizePolicy(sizePolicy)
        self.html_file_browser.setMinimumSize(QSize(0, 120))
        self.html_file_browser.setIconSize(QSize(16, 16))
        self.html_file_browser.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.html_file_browser.setHeaderHidden(True)

        self.verticalLayout_7.addWidget(self.html_file_browser)


        self.horizontalLayout_viewer_body.addWidget(self.frame_file_browser)

        self.stackedWidget = QStackedWidget(self.frame_viewer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.results1_page = QWidget()
        self.results1_page.setObjectName(u"results1_page")
        self.verticalLayout_results = QVBoxLayout(self.results1_page)
        self.verticalLayout_results.setObjectName(u"verticalLayout_results")
        self.verticalLayout_results.setContentsMargins(0, 0, 0, 0)
        self.results_frame = QFrame(self.results1_page)
        self.results_frame.setObjectName(u"results_frame")
        self.results_frame.setFrameShape(QFrame.NoFrame)
        self.results_frame.setFrameShadow(QFrame.Raised)
        self.results_table_layout = QVBoxLayout(self.results_frame)
        self.results_table_layout.setObjectName(u"results_table_layout")
        self.results_table_layout.setContentsMargins(12, 12, 12, 12)

        self.verticalLayout_results.addWidget(self.results_frame)

        self.frame_plots = QFrame(self.results1_page)
        self.frame_plots.setObjectName(u"frame_plots")
        self.frame_plots.setFrameShape(QFrame.NoFrame)
        self.frame_plots.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_plots = QHBoxLayout(self.frame_plots)
        self.horizontalLayout_plots.setSpacing(12)
        self.horizontalLayout_plots.setObjectName(u"horizontalLayout_plots")
        self.horizontalLayout_plots.setContentsMargins(12, 12, 12, 12)
        self.installed_capacity = QFrame(self.frame_plots)
        self.installed_capacity.setObjectName(u"installed_capacity")
        self.installed_capacity.setMinimumSize(QSize(0, 180))
        self.installed_capacity.setFrameShape(QFrame.NoFrame)
        self.installed_capacity.setFrameShadow(QFrame.Raised)
        self.verticalLayout_installed_holder = QVBoxLayout(self.installed_capacity)
        self.verticalLayout_installed_holder.setObjectName(u"verticalLayout_installed_holder")
        self.verticalLayout_installed_holder.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_plots.addWidget(self.installed_capacity)


        self.verticalLayout_results.addWidget(self.frame_plots)

        self.stackedWidget.addWidget(self.results1_page)
        self.png_viewer_page = QWidget()
        self.png_viewer_page.setObjectName(u"png_viewer_page")
        self.verticalLayout_17 = QVBoxLayout(self.png_viewer_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.png_viewer_page)
        self.html_viewer_page = QWidget()
        self.html_viewer_page.setObjectName(u"html_viewer_page")
        self.verticalLayout_3 = QVBoxLayout(self.html_viewer_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.html_viewer_page)
        self.scenario_viewer_page = QWidget()
        self.scenario_viewer_page.setObjectName(u"scenario_viewer_page")
        self.verticalLayout_5 = QVBoxLayout(self.scenario_viewer_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.scenario_viewer_page)

        self.horizontalLayout_viewer_body.addWidget(self.stackedWidget)


        self.verticalLayout_viewer.addLayout(self.horizontalLayout_viewer_body)


        self.verticalLayout_main.addWidget(self.frame_viewer)

        self.verticalLayout_main.setStretch(2, 1)

        self.retranslateUi(ResultsViewerPage)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ResultsViewerPage)
    # setupUi

    def retranslateUi(self, ResultsViewerPage):
        ResultsViewerPage.setWindowTitle(QCoreApplication.translate("ResultsViewerPage", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("ResultsViewerPage", u"View Results", None))
        self.label_title.setProperty("textRole", u"heading")
        self.label_subtitle.setText(QCoreApplication.translate("ResultsViewerPage", u"Gather the optimization results, explore the cost breakdown, and browse the plots and maps produced by the model.", None))
        self.label_subtitle.setProperty("textRole", u"subtitle")
        self.results_help_button.setText("")
        self.results_help_button.setProperty("btnRole", u"icon")
        self.frame_actions.setProperty("cardType", u"card")
        self.label_actions_icon.setText("")
        self.label_actions_title.setText(QCoreApplication.translate("ResultsViewerPage", u"RESULTS", None))
        self.label_actions_title.setProperty("textRole", u"section")
        self.label_actions_desc.setText(QCoreApplication.translate("ResultsViewerPage", u"Click <i>Collect Results</i> to gather the files generated by the optimization model, <i>Generate Plots</i> to build the capacity charts, or <i>Save Results</i> to export the raw optimizer data.", None))
        self.label_actions_desc.setProperty("textRole", u"body")
        self.collect_results_button.setText(QCoreApplication.translate("ResultsViewerPage", u"Collect Results", None))
        self.collect_results_button.setProperty("btnRole", u"primary")
        self.gen_plots_button.setText(QCoreApplication.translate("ResultsViewerPage", u"Generate Plots", None))
        self.gen_plots_button.setProperty("btnRole", u"primary")
        self.save_results_button.setText(QCoreApplication.translate("ResultsViewerPage", u"Save Results", None))
        self.save_results_button.setProperty("btnRole", u"primary")
        self.label_actions_hint.setText(QCoreApplication.translate("ResultsViewerPage", u"Results are written to the folder chosen on the Execute Model step.", None))
        self.label_actions_hint.setProperty("textRole", u"caption")
        self.frame_viewer.setProperty("cardType", u"card")
        self.label_viewer_icon.setText("")
        self.label_viewer_title.setText(QCoreApplication.translate("ResultsViewerPage", u"RESULT FILES", None))
        self.label_viewer_title.setProperty("textRole", u"section")
        self.png_toggler.setText(QCoreApplication.translate("ResultsViewerPage", u"Plots", None))
        self.png_toggler.setProperty("btnRole", u"toggler")
        self.html_toggler.setText(QCoreApplication.translate("ResultsViewerPage", u"Maps", None))
        self.html_toggler.setProperty("btnRole", u"toggler")
        self.label_viewer_desc.setText(QCoreApplication.translate("ResultsViewerPage", u"Browse the results folder below, then drag any plot or map file into the viewer. The <i>Plots</i> and <i>Maps</i> toggle buttons unfold the file browser panel for each file type.", None))
        self.label_viewer_desc.setProperty("textRole", u"caption")
        self.frame_file_browser.setProperty("cardType", u"soft")
        self.label_browser_title.setText(QCoreApplication.translate("ResultsViewerPage", u"POWER SYSTEM PLOTS", None))
        self.label_browser_title.setProperty("textRole", u"section")
        self.label_browser_folder.setText(QCoreApplication.translate("ResultsViewerPage", u"Plots Folder", None))
        self.label_browser_folder.setProperty("textRole", u"caption")
        self.png_browser.setText(QCoreApplication.translate("ResultsViewerPage", u"Open Folder..", None))
        self.png_browser.setProperty("btnRole", u"small")
        self.label_browser_map_folder.setText(QCoreApplication.translate("ResultsViewerPage", u"Maps Folder", None))
        self.label_browser_map_folder.setProperty("textRole", u"caption")
        self.html_browser.setText(QCoreApplication.translate("ResultsViewerPage", u"Open Folder..", None))
        self.html_browser.setProperty("btnRole", u"small")
        self.results_frame.setProperty("cardType", u"card")
        self.frame_plots.setProperty("cardType", u"card")
    # retranslateUi

