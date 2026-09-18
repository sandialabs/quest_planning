# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainzxLMsp.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1220, 632)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(9500000, 5000000))
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(40, 84, 113);\n"
"    width: 8px;\n"
"    margin: 0px 0 0px 0;\n"
"	border-radius: 4px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(129,194,65);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     height: 0px;\n"
"}\n"
" QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"}\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"    background: rgb(40, 84, 113);\n"
"    height: 8px;\n"
"    margin: 0px 0 0px 0;\n"
"	border-radius: 4px;\n"
" }\n"
" QScrollBar::handle:horizontal {	\n"
"	background: rgb(129,194,65);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal {\n"
"     width: 0px;\n"
"}\n"
" QScrollBar::sub-line:horizonta"
                        "l {\n"
"	width: 0px;\n"
"}\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"     background: none;\n"
" }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
" }\n"
"\n"
"QProgressBar::handle:horizontal {	\n"
"	background: rgb(129,194,65);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
" }\n"
"\n"
"#frame_2 {\n"
"  	border-top: 0.5px solid rgb(211,211,211);\n"
"	border-bottom:0.5px solid rgb(211,211,211);\n"
" 	background-color: rgb(245, 248, 251);\n"
"}\n"
"#frame_3, #label {	\n"
"	background-color: rgb(244,245,235);\n"
"}\n"
"\n"
"#frame_5 {\n"
"background-color: rgb(40, 84, 113);\n"
"}\n"
"#label_5 {\n"
"	font: 40pt;\n"
"	color: rgb(251, 255, 255);\n"
"}\n"
"\n"
"#data_app, #tech_app, #eval_app, #btm_app, #perf_app, #eq_app, #micr_app, #plan_app {\n"
"	border: 0px solid rgb(40, 84, 113);\n"
"	border-radius: 6px;\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMaximumSize(QSize(16777215, 0))
        self.frame_5.setStyleSheet(u"border-radius: 15px;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_button = QPushButton(self.frame_5)
        self.home_button.setObjectName(u"home_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.home_button.sizePolicy().hasHeightForWidth())
        self.home_button.setSizePolicy(sizePolicy2)
        self.home_button.setMinimumSize(QSize(48, 46))
        self.home_button.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	padding-left: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(129, 194, 65);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(129, 194, 65);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:checked {	\n"
"	background-color: rgb(129, 194, 65);\n"
"	border-radius: 4px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/logos/images/logo/Quest_App_Icon_50_transparent.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/logos/images/logo/Quest_App_Icon_50_transparent.png", QSize(), QIcon.Normal, QIcon.On)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QSize(44, 48))

        self.horizontalLayout.addWidget(self.home_button)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(129, 194, 65);\n"
"background-color: rgb(40, 84, 113);")

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.top_right_frame = QFrame(self.frame_5)
        self.top_right_frame.setObjectName(u"top_right_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.top_right_frame.sizePolicy().hasHeightForWidth())
        self.top_right_frame.setSizePolicy(sizePolicy3)
        self.top_right_frame.setMinimumSize(QSize(0, 48))
        self.top_right_frame.setStyleSheet(u"QFrame{background-color: rgb(40, 84, 113);}\n"
"QPushButton {	\n"
"	background-color: rgb(245, 245, 245);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(129, 194, 65);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: transparent;\n"
"	border-radius: 4px;\n"
"}")
        self.top_right_frame.setFrameShape(QFrame.NoFrame)
        self.top_right_frame.setFrameShadow(QFrame.Raised)
        self.top_right_frame.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.top_right_frame)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.min_resize_button = QPushButton(self.top_right_frame)
        self.min_resize_button.setObjectName(u"min_resize_button")
        sizePolicy2.setHeightForWidth(self.min_resize_button.sizePolicy().hasHeightForWidth())
        self.min_resize_button.setSizePolicy(sizePolicy2)
        self.min_resize_button.setMinimumSize(QSize(36, 36))
        self.min_resize_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/images/icons/remove_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min_resize_button.setIcon(icon1)
        self.min_resize_button.setIconSize(QSize(24, 24))
        self.min_resize_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.min_resize_button)

        self.norm_resize_button = QPushButton(self.top_right_frame)
        self.norm_resize_button.setObjectName(u"norm_resize_button")
        sizePolicy2.setHeightForWidth(self.norm_resize_button.sizePolicy().hasHeightForWidth())
        self.norm_resize_button.setSizePolicy(sizePolicy2)
        self.norm_resize_button.setMinimumSize(QSize(36, 36))
        self.norm_resize_button.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/images/icons/open_in_new_FILL0_wght200_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon/images/icons/apps_FILL0_wght700_GRAD-25_opsz20.png", QSize(), QIcon.Normal, QIcon.On)
        icon2.addFile(u":/icon/images/icons/check_box_outline_blank_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Selected, QIcon.On)
        self.norm_resize_button.setIcon(icon2)
        self.norm_resize_button.setIconSize(QSize(24, 24))
        self.norm_resize_button.setCheckable(False)
        self.norm_resize_button.setChecked(False)
        self.norm_resize_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.norm_resize_button)

        self.max_resize_button = QPushButton(self.top_right_frame)
        self.max_resize_button.setObjectName(u"max_resize_button")
        sizePolicy2.setHeightForWidth(self.max_resize_button.sizePolicy().hasHeightForWidth())
        self.max_resize_button.setSizePolicy(sizePolicy2)
        self.max_resize_button.setMinimumSize(QSize(36, 36))
        self.max_resize_button.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/images/icons/open_in_new_down_FILL0_wght200_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon/images/icons/open_in_new_down_FILL0_wght200_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.On)
        icon3.addFile(u":/icon/images/icons/check_box_outline_blank_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Selected, QIcon.On)
        self.max_resize_button.setIcon(icon3)
        self.max_resize_button.setIconSize(QSize(24, 24))
        self.max_resize_button.setCheckable(False)
        self.max_resize_button.setChecked(False)
        self.max_resize_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.max_resize_button)

        self.exit_app_button = QPushButton(self.top_right_frame)
        self.exit_app_button.setObjectName(u"exit_app_button")
        sizePolicy2.setHeightForWidth(self.exit_app_button.sizePolicy().hasHeightForWidth())
        self.exit_app_button.setSizePolicy(sizePolicy2)
        self.exit_app_button.setMinimumSize(QSize(36, 36))
        self.exit_app_button.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/images/icons/close_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_app_button.setIcon(icon4)
        self.exit_app_button.setIconSize(QSize(24, 24))
        self.exit_app_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.exit_app_button)


        self.horizontalLayout.addWidget(self.top_right_frame)


        self.verticalLayout.addWidget(self.frame_5)

        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    padding: 5px 15px;\n"
"    border: 1px solid transparent;\n"
"    color: rgb(40, 84, 113); /* Updated to the specified blue */\n"
"    border-bottom: 2px solid transparent;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: rgb(40, 84, 113); /* Updated to the specified blue */\n"
"    border-bottom: 2px solid rgb(40, 84, 113); /* Updated to the specified blue */\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: rgba(40, 84, 113, 0.1); /* Lighter version of the specified blue */\n"
"    color: rgb(40, 84, 113); /* Updated to the specified blue */\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QTextBrowser {\n"
"    border: 1px solid rgb(40, 84, 113); /* Updated to the specified blue */\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: rgb(233, 233, 233);\n"
"}\n"
"")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.start = QWidget()
        self.start.setObjectName(u"start")
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        self.start.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.start_page_layout = QVBoxLayout(self.start)
        self.start_page_layout.setObjectName(u"start_page_layout")
        self.tabWidget.addTab(self.start, "")
        self.power_system_data = QWidget()
        self.power_system_data.setObjectName(u"power_system_data")
        sizePolicy.setHeightForWidth(self.power_system_data.sizePolicy().hasHeightForWidth())
        self.power_system_data.setSizePolicy(sizePolicy)
        self.power_system_data.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.power_system_data_page_layout = QVBoxLayout(self.power_system_data)
        self.power_system_data_page_layout.setObjectName(u"power_system_data_page_layout")
        self.tabWidget.addTab(self.power_system_data, "")
        self.planning_model_page = QWidget()
        self.planning_model_page.setObjectName(u"planning_model_page")
        self.planning_model_page.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.planning_model_page_layout = QVBoxLayout(self.planning_model_page)
        self.planning_model_page_layout.setObjectName(u"planning_model_page_layout")
        self.tabWidget.addTab(self.planning_model_page, "")
        self.scenario_builder_page = QWidget()
        self.scenario_builder_page.setObjectName(u"scenario_builder_page")
        sizePolicy.setHeightForWidth(self.scenario_builder_page.sizePolicy().hasHeightForWidth())
        self.scenario_builder_page.setSizePolicy(sizePolicy)
        self.scenario_builder_page.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.scenario_builder_page_layout = QVBoxLayout(self.scenario_builder_page)
        self.scenario_builder_page_layout.setObjectName(u"scenario_builder_page_layout")
        self.tabWidget.addTab(self.scenario_builder_page, "")
        self.build_run = QWidget()
        self.build_run.setObjectName(u"build_run")
        self.build_run.setMinimumSize(QSize(0, 0))
        self.build_run.setMaximumSize(QSize(1000000, 1000000))
        self.build_run.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.build_run_page_layout = QVBoxLayout(self.build_run)
        self.build_run_page_layout.setObjectName(u"build_run_page_layout")
        self.tabWidget.addTab(self.build_run, "")
        self.results = QWidget()
        self.results.setObjectName(u"results")
        self.results.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.results_page_layout = QVBoxLayout(self.results)
        self.results_page_layout.setObjectName(u"results_page_layout")
        self.tabWidget.addTab(self.results, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(0, 24))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_button.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">QuESt Planning</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.min_resize_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.min_resize_button.setText("")
#if QT_CONFIG(tooltip)
        self.norm_resize_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Restore Down</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.norm_resize_button.setText("")
#if QT_CONFIG(tooltip)
        self.max_resize_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.max_resize_button.setText("")
#if QT_CONFIG(tooltip)
        self.exit_app_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.exit_app_button.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.start), QCoreApplication.translate("MainWindow", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.power_system_data), QCoreApplication.translate("MainWindow", u"Power System Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.planning_model_page), QCoreApplication.translate("MainWindow", u"Planning Model Setup", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scenario_builder_page), QCoreApplication.translate("MainWindow", u"Scenario Builder", None))
#if QT_CONFIG(tooltip)
        self.build_run.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Run Model</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.build_run), QCoreApplication.translate("MainWindow", u"Execute Model", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results), QCoreApplication.translate("MainWindow", u"Results Viewer", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Developed by Sandia National Laboratories", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ver 1.0", None))
    # retranslateUi

