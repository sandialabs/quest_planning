# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resultspSmkks.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)

from quest_planning.matplotlibwidget import MatplotlibWidget
import quest_planning.resources_rc

class Ui_results(object):
    def setupUi(self, results):
        if not results.objectName():
            results.setObjectName(u"results")
        results.resize(1071, 657)
        results.setMaximumSize(QSize(16777215, 16777215))
        results.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(results)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(results)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	border: 2px solid #8f8f8f;\n"
"	border-radius: 5px;\n"
"	background-color: rgba(140, 140, 140, .5);\n"
"\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"    QPushButton:hover {\n"
"        background-color: rgb(240, 240, 240);\n"
"		border-radius:5px;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(180, 180, 180);		\n"
"		 border-radius:5px;\n"
"    }\n"
"    QPushButton:checked {\n"
"        background-color: rgb(230, 230, 230);		\n"
"		 border-radius:5px;\n"
"    }")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.open_results_folder_button = QPushButton(self.frame_3)
        self.open_results_folder_button.setObjectName(u"open_results_folder_button")
        self.open_results_folder_button.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.open_results_folder_button.setFont(font)
        self.open_results_folder_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/results_icons/images/results_icons/stacks_24dp_5F6368_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_results_folder_button.setIcon(icon)
        self.open_results_folder_button.setIconSize(QSize(40, 40))
        self.open_results_folder_button.setCheckable(True)
        self.open_results_folder_button.setChecked(True)
        self.open_results_folder_button.setAutoExclusive(True)
        self.open_results_folder_button.setFlat(True)

        self.verticalLayout.addWidget(self.open_results_folder_button, 0, Qt.AlignLeft)

        self.open_maps_button = QPushButton(self.frame_3)
        self.open_maps_button.setObjectName(u"open_maps_button")
        self.open_maps_button.setMaximumSize(QSize(200, 16777215))
        self.open_maps_button.setFont(font)
        self.open_maps_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/results_icons/images/results_icons/open_run_24dp_5F6368_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_maps_button.setIcon(icon1)
        self.open_maps_button.setIconSize(QSize(32, 32))
        self.open_maps_button.setCheckable(True)
        self.open_maps_button.setAutoExclusive(True)
        self.open_maps_button.setFlat(True)

        self.verticalLayout.addWidget(self.open_maps_button, 0, Qt.AlignLeft)

        self.scenario_view_button = QPushButton(self.frame_3)
        self.scenario_view_button.setObjectName(u"scenario_view_button")
        icon2 = QIcon()
        icon2.addFile(u":/results_icons/images/results_icons/data_check_24dp_5F6368_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scenario_view_button.setIcon(icon2)
        self.scenario_view_button.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.scenario_view_button)

        self.save_results_button = QPushButton(self.frame_3)
        self.save_results_button.setObjectName(u"save_results_button")
        self.save_results_button.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/results_icons/images/results_icons/save_24dp_5F6368_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_results_button.setIcon(icon3)
        self.save_results_button.setIconSize(QSize(32, 32))
        self.save_results_button.setFlat(True)

        self.verticalLayout.addWidget(self.save_results_button, 0, Qt.AlignLeft)

        self.results_help_button = QToolButton(self.frame_3)
        self.results_help_button.setObjectName(u"results_help_button")
        self.results_help_button.setStyleSheet(u"QToolButton {\n"
"	background-color: transparent;\n"
"}\n"
"    QToolButton:hover {\n"
"        background-color: rgb(230, 230, 230);\n"
"		border-radius:5px;\n"
"    }\n"
"    QToolButton:pressed {\n"
"        background-color: rgb(180, 180, 180);		\n"
"		 border-radius:5px;\n"
"    }")
        icon4 = QIcon()
        icon4.addFile(u":/icon/images/icons/ainfo_24dp_5F6368_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.results_help_button.setIcon(icon4)
        self.results_help_button.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.results_help_button, 0, Qt.AlignLeft)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_3)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.results1_page = QWidget()
        self.results1_page.setObjectName(u"results1_page")
        self.horizontalLayout_2 = QHBoxLayout(self.results1_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.results_frame = QFrame(self.results1_page)
        self.results_frame.setObjectName(u"results_frame")
        self.results_frame.setStyleSheet(u"")
        self.results_frame.setFrameShape(QFrame.NoFrame)
        self.results_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.results_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.results_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(208, 208, 208);\n"
"border-radius: 25px;\n"
"\n"
"color: black;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.installed_capacity = MatplotlibWidget(self.frame_2)
        self.installed_capacity.setObjectName(u"installed_capacity")
        self.installed_capacity.setMinimumSize(QSize(350, 200))
        self.installed_capacity.setMaximumSize(QSize(650, 500))
        self.installed_capacity.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.installed_capacity, 0, 1, 1, 1)

        self.es_capacity = MatplotlibWidget(self.frame_2)
        self.es_capacity.setObjectName(u"es_capacity")
        self.es_capacity.setMinimumSize(QSize(350, 200))
        self.es_capacity.setMaximumSize(QSize(650, 600))
        self.es_capacity.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.es_capacity, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 7, 1)

        self.collect_results_button = QPushButton(self.results_frame)
        self.collect_results_button.setObjectName(u"collect_results_button")
        self.collect_results_button.setMinimumSize(QSize(200, 0))
        self.collect_results_button.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.collect_results_button.setFont(font1)
        self.collect_results_button.setStyleSheet(u"QPushButton {\n"
"        border: 1px solid rgb(40, 84, 113);\n"
"        border-radius: 7px;\n"
"        background-color: rgb(40, 84, 113);\n"
"        color: white;\n"
"		 font: 700 10pt \"Segoe UI\";\n"
"        padding: 1px;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(60, 120, 150);\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: rgb(20, 60, 80);\n"
"    }")
        self.collect_results_button.setIconSize(QSize(32, 32))
        self.collect_results_button.setFlat(True)

        self.gridLayout_2.addWidget(self.collect_results_button, 0, 0, 1, 1)

        self.gen_plots_button = QPushButton(self.results_frame)
        self.gen_plots_button.setObjectName(u"gen_plots_button")
        self.gen_plots_button.setMaximumSize(QSize(200, 16777215))
        self.gen_plots_button.setFont(font1)
        self.gen_plots_button.setStyleSheet(u"QPushButton {\n"
"        border: 1px solid rgb(40, 84, 113);\n"
"        border-radius: 7px;\n"
"        background-color: rgb(40, 84, 113);\n"
"        color: white;\n"
"		 font: 700 10pt \"Segoe UI\";\n"
"        padding: 1px;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(60, 120, 150);\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: rgb(20, 60, 80);\n"
"    }")
        self.gen_plots_button.setIconSize(QSize(32, 32))
        self.gen_plots_button.setFlat(True)

        self.gridLayout_2.addWidget(self.gen_plots_button, 1, 0, 1, 1)

        self.table_frame = QFrame(self.results_frame)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setMinimumSize(QSize(0, 0))
        self.table_frame.setMaximumSize(QSize(250, 16777215))
        self.table_frame.setStyleSheet(u"background-color: rgb(208, 208, 208);\n"
"border-radius: 25px;\n"
"\n"
"color: black;")
        self.table_frame.setFrameShape(QFrame.NoFrame)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.results_table_layout = QHBoxLayout(self.table_frame)
        self.results_table_layout.setObjectName(u"results_table_layout")
        self.results_table_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.table_frame, 2, 0, 5, 1)


        self.horizontalLayout_2.addWidget(self.results_frame)

        self.stackedWidget.addWidget(self.results1_page)
        self.png_viewer_page = QWidget()
        self.png_viewer_page.setObjectName(u"png_viewer_page")
        self.horizontalLayout_3 = QHBoxLayout(self.png_viewer_page)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.png_viewer_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(230, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(208, 208, 208);\n"
"border-radius: 25px;\n"
"\n"
"color: black;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.png_browser = QPushButton(self.frame_5)
        self.png_browser.setObjectName(u"png_browser")
        self.png_browser.setStyleSheet(u"QPushButton {\n"
"        border: 1px solid rgb(40, 84, 113);\n"
"        border-radius: 7px;\n"
"        background-color: rgb(40, 84, 113);\n"
"        color: white;\n"
"		 font: 700 10pt \"Segoe UI\";\n"
"        padding: 1px;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(60, 120, 150);\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: rgb(20, 60, 80);\n"
"    }")
        self.png_browser.setFlat(True)

        self.verticalLayout_4.addWidget(self.png_browser, 0, Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.frame_5)

        self.png_toggler = QPushButton(self.png_viewer_page)
        self.png_toggler.setObjectName(u"png_toggler")
        self.png_toggler.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"    QPushButton:hover {\n"
"        background-color: rgb(230, 230, 230);\n"
"		border-radius:5px;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(180, 180, 180);		\n"
"		 border-radius:5px;\n"
"    }\n"
"    QPushButton:checked {\n"
"        background-color: rgb(160, 160, 160);		\n"
"		 border-radius:5px;\n"
"    }")
        icon5 = QIcon()
        icon5.addFile(u":/results_icons/images/results_icons/more_vert_24dp_5F6368_FILL0_wght200_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.png_toggler.setIcon(icon5)
        self.png_toggler.setIconSize(QSize(24, 32))
        self.png_toggler.setFlat(True)

        self.horizontalLayout_3.addWidget(self.png_toggler, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")

        self.horizontalLayout_3.addLayout(self.verticalLayout_17)

        self.horizontalLayout_3.setStretch(2, 1)
        self.stackedWidget.addWidget(self.png_viewer_page)
        self.html_viewer_page = QWidget()
        self.html_viewer_page.setObjectName(u"html_viewer_page")
        self.horizontalLayout_4 = QHBoxLayout(self.html_viewer_page)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.html_viewer_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(230, 0))
        self.frame_7.setStyleSheet(u"background-color: rgb(208, 208, 208);\n"
"border-radius: 25px;\n"
"\n"
"color: black;")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.html_browser = QPushButton(self.frame_7)
        self.html_browser.setObjectName(u"html_browser")
        self.html_browser.setStyleSheet(u"QPushButton {\n"
"        border: 1px solid rgb(40, 84, 113);\n"
"        border-radius: 7px;\n"
"        background-color: rgb(40, 84, 113);\n"
"        color: white;\n"
"		 font: 700 10pt \"Segoe UI\";\n"
"        padding: 1px;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(60, 120, 150);\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: rgb(20, 60, 80);\n"
"    }")

        self.verticalLayout_6.addWidget(self.html_browser, 0, Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.html_toggler = QPushButton(self.html_viewer_page)
        self.html_toggler.setObjectName(u"html_toggler")
        self.html_toggler.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"}\n"
"    QPushButton:hover {\n"
"        background-color: rgb(230, 230, 230);\n"
"		border-radius:5px;\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(180, 180, 180);		\n"
"		 border-radius:5px;\n"
"    }\n"
"    QPushButton:checked {\n"
"        background-color: rgb(160, 160, 160);		\n"
"		 border-radius:5px;\n"
"    }")
        self.html_toggler.setIcon(icon5)
        self.html_toggler.setIconSize(QSize(24, 32))
        self.html_toggler.setFlat(True)

        self.horizontalLayout_4.addWidget(self.html_toggler)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4.setStretch(2, 1)
        self.stackedWidget.addWidget(self.html_viewer_page)
        self.scenario_viewer_page = QWidget()
        self.scenario_viewer_page.setObjectName(u"scenario_viewer_page")
        self.verticalLayout_8 = QVBoxLayout(self.scenario_viewer_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.stackedWidget.addWidget(self.scenario_viewer_page)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_4 = QFrame(results)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(500, 60))
        self.label_2.setStyleSheet(u"image: url(:/logos/images/logo/results_icon.png);")

        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignHCenter)

        self.previous_button = QPushButton(self.frame_4)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setMinimumSize(QSize(100, 0))
        self.previous_button.setStyleSheet(u"QPushButton {\n"
"        border: 1px solid rgb(40, 84, 113);\n"
"        border-radius: 7px;\n"
"        background-color: rgb(40, 84, 113);\n"
"        color: white;\n"
"		 font: 700 10pt \"Segoe UI\";\n"
"        padding: 1px;\n"
"    }\n"
"QPushButton:hover {\n"
"        background-color: rgb(60, 120, 150);\n"
"    }\n"
"QPushButton:pressed {\n"
"        background-color: rgb(20, 60, 80);\n"
"    }")

        self.gridLayout_5.addWidget(self.previous_button, 0, 0, 1, 1, Qt.AlignLeft)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 2, 1, 1, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.retranslateUi(results)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(results)
    # setupUi

    def retranslateUi(self, results):
        results.setWindowTitle(QCoreApplication.translate("results", u"Form", None))
#if QT_CONFIG(tooltip)
        self.open_results_folder_button.setToolTip(QCoreApplication.translate("results", u"<html><head/><body><p><span style=\" font-weight:400;\">Open Results Folder</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_results_folder_button.setText("")
#if QT_CONFIG(tooltip)
        self.open_maps_button.setToolTip(QCoreApplication.translate("results", u"<html><head/><body><p><span style=\" font-weight:400;\">Under Construction</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_maps_button.setText("")
#if QT_CONFIG(tooltip)
        self.scenario_view_button.setToolTip(QCoreApplication.translate("results", u"<html><head/><body><p><span style=\" font-size:12pt;\">Under Construction</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.scenario_view_button.setText("")
#if QT_CONFIG(tooltip)
        self.save_results_button.setToolTip(QCoreApplication.translate("results", u"<html><head/><body><p>Save Results</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.save_results_button.setText("")
#if QT_CONFIG(tooltip)
        self.results_help_button.setToolTip(QCoreApplication.translate("results", u"<html><head/><body><p>Help</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.results_help_button.setText("")
#if QT_CONFIG(tooltip)
        self.collect_results_button.setToolTip(QCoreApplication.translate("results", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.collect_results_button.setText(QCoreApplication.translate("results", u"Collect Results", None))
#if QT_CONFIG(tooltip)
        self.gen_plots_button.setToolTip(QCoreApplication.translate("results", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gen_plots_button.setText(QCoreApplication.translate("results", u"Generate Plots", None))
        self.png_browser.setText(QCoreApplication.translate("results", u"Open Folder..", None))
        self.png_toggler.setText("")
        self.html_browser.setText(QCoreApplication.translate("results", u"Open Folder..", None))
        self.html_toggler.setText("")
        self.label_2.setText("")
        self.previous_button.setText(QCoreApplication.translate("results", u"Previous", None))
        self.label.setText("")
    # retranslateUi

