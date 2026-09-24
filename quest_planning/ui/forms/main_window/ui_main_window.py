# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
    QStackedWidget, QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1118, 928)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_ribbon = QFrame(self.centralwidget)
        self.frame_ribbon.setObjectName(u"frame_ribbon")
        self.frame_ribbon.setFrameShape(QFrame.NoFrame)
        self.frame_ribbon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_ribbon)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_logo = QFrame(self.frame_ribbon)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setFrameShape(QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_logo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_logo = QLabel(self.frame_logo)
        self.label_logo.setObjectName(u"label_logo")

        self.verticalLayout_3.addWidget(self.label_logo)


        self.verticalLayout_2.addWidget(self.frame_logo)

        self.btn_home = QPushButton(self.frame_ribbon)
        self.btn_home.setObjectName(u"btn_home")

        self.verticalLayout_2.addWidget(self.btn_home)

        self.btn_power_system = QPushButton(self.frame_ribbon)
        self.btn_power_system.setObjectName(u"btn_power_system")

        self.verticalLayout_2.addWidget(self.btn_power_system)

        self.btn_planning = QPushButton(self.frame_ribbon)
        self.btn_planning.setObjectName(u"btn_planning")

        self.verticalLayout_2.addWidget(self.btn_planning)

        self.btn_scenario = QPushButton(self.frame_ribbon)
        self.btn_scenario.setObjectName(u"btn_scenario")

        self.verticalLayout_2.addWidget(self.btn_scenario)

        self.btn_model = QPushButton(self.frame_ribbon)
        self.btn_model.setObjectName(u"btn_model")

        self.verticalLayout_2.addWidget(self.btn_model)

        self.btn_results = QPushButton(self.frame_ribbon)
        self.btn_results.setObjectName(u"btn_results")

        self.verticalLayout_2.addWidget(self.btn_results)

        self.spacer_ribbon = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.spacer_ribbon)

        self.btn_settings = QPushButton(self.frame_ribbon)
        self.btn_settings.setObjectName(u"btn_settings")

        self.verticalLayout_2.addWidget(self.btn_settings)

        self.btn_about = QPushButton(self.frame_ribbon)
        self.btn_about.setObjectName(u"btn_about")

        self.verticalLayout_2.addWidget(self.btn_about)


        self.horizontalLayout.addWidget(self.frame_ribbon)

        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_content)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_landing = QWidget()
        self.page_landing.setObjectName(u"page_landing")
        self.stackedWidget.addWidget(self.page_landing)
        self.page_power_system = QWidget()
        self.page_power_system.setObjectName(u"page_power_system")
        self.stackedWidget.addWidget(self.page_power_system)
        self.page_planning = QWidget()
        self.page_planning.setObjectName(u"page_planning")
        self.stackedWidget.addWidget(self.page_planning)
        self.page_scenario = QWidget()
        self.page_scenario.setObjectName(u"page_scenario")
        self.stackedWidget.addWidget(self.page_scenario)
        self.page_execute = QWidget()
        self.page_execute.setObjectName(u"page_execute")
        self.stackedWidget.addWidget(self.page_execute)
        self.page_results = QWidget()
        self.page_results.setObjectName(u"page_results")
        self.stackedWidget.addWidget(self.page_results)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.stackedWidget.addWidget(self.page_settings)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.stackedWidget.addWidget(self.page_about)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame_nav_btns = QFrame(self.frame_content)
        self.frame_nav_btns.setObjectName(u"frame_nav_btns")
        self.frame_nav_btns.setFrameShape(QFrame.NoFrame)
        self.frame_nav_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_nav_btns)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spacer_nav_btns = QSpacerItem(248, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.spacer_nav_btns)

        self.btn_prev = QPushButton(self.frame_nav_btns)
        self.btn_prev.setObjectName(u"btn_prev")

        self.horizontalLayout_2.addWidget(self.btn_prev)

        self.next_prev = QPushButton(self.frame_nav_btns)
        self.next_prev.setObjectName(u"next_prev")

        self.horizontalLayout_2.addWidget(self.next_prev)


        self.verticalLayout.addWidget(self.frame_nav_btns)


        self.horizontalLayout.addWidget(self.frame_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QuESt Planning", None))
        self.label_logo.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_power_system.setText(QCoreApplication.translate("MainWindow", u"Power System Data", None))
        self.btn_planning.setText(QCoreApplication.translate("MainWindow", u"Planning Model Setup", None))
        self.btn_scenario.setText(QCoreApplication.translate("MainWindow", u"Scenario Builder", None))
        self.btn_model.setText(QCoreApplication.translate("MainWindow", u"Execute Model", None))
        self.btn_results.setText(QCoreApplication.translate("MainWindow", u"Results Viewer", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btn_prev.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.next_prev.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

