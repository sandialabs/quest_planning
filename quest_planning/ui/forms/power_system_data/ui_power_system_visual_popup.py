# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'power_system_visual_popup.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from quest_planning.matplotlibwidget import MatplotlibWidget
import quest_planning.resources_rc

class Ui_PowerSystemDataVisualizationPage(object):
    def setupUi(self, PowerSystemDataVisualizationPage):
        if not PowerSystemDataVisualizationPage.objectName():
            PowerSystemDataVisualizationPage.setObjectName(u"PowerSystemDataVisualizationPage")
        PowerSystemDataVisualizationPage.resize(892, 781)
        self.verticalLayout = QVBoxLayout(PowerSystemDataVisualizationPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_overview = QFrame(PowerSystemDataVisualizationPage)
        self.frame_overview.setObjectName(u"frame_overview")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_overview.sizePolicy().hasHeightForWidth())
        self.frame_overview.setSizePolicy(sizePolicy)
        self.frame_overview.setMaximumSize(QSize(16777215, 180))
        self.frame_overview.setFrameShape(QFrame.NoFrame)
        self.frame_overview.setFrameShadow(QFrame.Raised)
        self.verticalLayout_overview = QVBoxLayout(self.frame_overview)
        self.verticalLayout_overview.setSpacing(10)
        self.verticalLayout_overview.setObjectName(u"verticalLayout_overview")
        self.verticalLayout_overview.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_overview_title = QHBoxLayout()
        self.horizontalLayout_overview_title.setSpacing(8)
        self.horizontalLayout_overview_title.setObjectName(u"horizontalLayout_overview_title")
        self.label_overview_icon = QLabel(self.frame_overview)
        self.label_overview_icon.setObjectName(u"label_overview_icon")
        self.label_overview_icon.setMaximumSize(QSize(22, 22))
        self.label_overview_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-view-module.png"))
        self.label_overview_icon.setScaledContents(True)

        self.horizontalLayout_overview_title.addWidget(self.label_overview_icon)

        self.label_overview_title = QLabel(self.frame_overview)
        self.label_overview_title.setObjectName(u"label_overview_title")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.label_overview_title.setFont(font)

        self.horizontalLayout_overview_title.addWidget(self.label_overview_title)

        self.horizontalSpacer_overview_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_overview_title.addItem(self.horizontalSpacer_overview_title)


        self.verticalLayout_overview.addLayout(self.horizontalLayout_overview_title)

        self.horizontalLayout_stats = QHBoxLayout()
        self.horizontalLayout_stats.setSpacing(14)
        self.horizontalLayout_stats.setObjectName(u"horizontalLayout_stats")
        self.frame_tile_bus = QFrame(self.frame_overview)
        self.frame_tile_bus.setObjectName(u"frame_tile_bus")
        self.frame_tile_bus.setFrameShape(QFrame.NoFrame)
        self.frame_tile_bus.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_tile_bus = QHBoxLayout(self.frame_tile_bus)
        self.horizontalLayout_tile_bus.setSpacing(10)
        self.horizontalLayout_tile_bus.setObjectName(u"horizontalLayout_tile_bus")
        self.label_bus_icon = QLabel(self.frame_tile_bus)
        self.label_bus_icon.setObjectName(u"label_bus_icon")
        self.label_bus_icon.setMaximumSize(QSize(26, 26))
        self.label_bus_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-location-pin.png"))
        self.label_bus_icon.setScaledContents(True)

        self.horizontalLayout_tile_bus.addWidget(self.label_bus_icon)

        self.verticalLayout_tile_bus = QVBoxLayout()
        self.verticalLayout_tile_bus.setSpacing(0)
        self.verticalLayout_tile_bus.setObjectName(u"verticalLayout_tile_bus")
        self.label_bus_title = QLabel(self.frame_tile_bus)
        self.label_bus_title.setObjectName(u"label_bus_title")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        self.label_bus_title.setFont(font1)

        self.verticalLayout_tile_bus.addWidget(self.label_bus_title)

        self.bus_label = QLabel(self.frame_tile_bus)
        self.bus_label.setObjectName(u"bus_label")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.bus_label.setFont(font2)

        self.verticalLayout_tile_bus.addWidget(self.bus_label)


        self.horizontalLayout_tile_bus.addLayout(self.verticalLayout_tile_bus)


        self.horizontalLayout_stats.addWidget(self.frame_tile_bus)

        self.frame_tile_line = QFrame(self.frame_overview)
        self.frame_tile_line.setObjectName(u"frame_tile_line")
        self.frame_tile_line.setFrameShape(QFrame.NoFrame)
        self.frame_tile_line.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_tile_line = QHBoxLayout(self.frame_tile_line)
        self.horizontalLayout_tile_line.setSpacing(10)
        self.horizontalLayout_tile_line.setObjectName(u"horizontalLayout_tile_line")
        self.label_line_icon = QLabel(self.frame_tile_line)
        self.label_line_icon.setObjectName(u"label_line_icon")
        self.label_line_icon.setMaximumSize(QSize(26, 26))
        self.label_line_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-layers.png"))
        self.label_line_icon.setScaledContents(True)

        self.horizontalLayout_tile_line.addWidget(self.label_line_icon)

        self.verticalLayout_tile_line = QVBoxLayout()
        self.verticalLayout_tile_line.setSpacing(0)
        self.verticalLayout_tile_line.setObjectName(u"verticalLayout_tile_line")
        self.label_line_title = QLabel(self.frame_tile_line)
        self.label_line_title.setObjectName(u"label_line_title")
        self.label_line_title.setFont(font1)

        self.verticalLayout_tile_line.addWidget(self.label_line_title)

        self.line_label = QLabel(self.frame_tile_line)
        self.line_label.setObjectName(u"line_label")
        self.line_label.setFont(font2)

        self.verticalLayout_tile_line.addWidget(self.line_label)


        self.horizontalLayout_tile_line.addLayout(self.verticalLayout_tile_line)


        self.horizontalLayout_stats.addWidget(self.frame_tile_line)

        self.frame_tile_gen = QFrame(self.frame_overview)
        self.frame_tile_gen.setObjectName(u"frame_tile_gen")
        self.frame_tile_gen.setFrameShape(QFrame.NoFrame)
        self.frame_tile_gen.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_tile_gen = QHBoxLayout(self.frame_tile_gen)
        self.horizontalLayout_tile_gen.setSpacing(10)
        self.horizontalLayout_tile_gen.setObjectName(u"horizontalLayout_tile_gen")
        self.label_gen_icon = QLabel(self.frame_tile_gen)
        self.label_gen_icon.setObjectName(u"label_gen_icon")
        self.label_gen_icon.setMaximumSize(QSize(26, 26))
        self.label_gen_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-lightbulb.png"))
        self.label_gen_icon.setScaledContents(True)

        self.horizontalLayout_tile_gen.addWidget(self.label_gen_icon)

        self.verticalLayout_tile_gen = QVBoxLayout()
        self.verticalLayout_tile_gen.setSpacing(0)
        self.verticalLayout_tile_gen.setObjectName(u"verticalLayout_tile_gen")
        self.label_gen_title = QLabel(self.frame_tile_gen)
        self.label_gen_title.setObjectName(u"label_gen_title")
        self.label_gen_title.setFont(font1)

        self.verticalLayout_tile_gen.addWidget(self.label_gen_title)

        self.gen_label = QLabel(self.frame_tile_gen)
        self.gen_label.setObjectName(u"gen_label")
        self.gen_label.setFont(font2)

        self.verticalLayout_tile_gen.addWidget(self.gen_label)


        self.horizontalLayout_tile_gen.addLayout(self.verticalLayout_tile_gen)


        self.horizontalLayout_stats.addWidget(self.frame_tile_gen)

        self.frame_tile_sys = QFrame(self.frame_overview)
        self.frame_tile_sys.setObjectName(u"frame_tile_sys")
        self.frame_tile_sys.setFrameShape(QFrame.NoFrame)
        self.frame_tile_sys.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_tile_sys = QHBoxLayout(self.frame_tile_sys)
        self.horizontalLayout_tile_sys.setSpacing(10)
        self.horizontalLayout_tile_sys.setObjectName(u"horizontalLayout_tile_sys")
        self.label_sys_icon = QLabel(self.frame_tile_sys)
        self.label_sys_icon.setObjectName(u"label_sys_icon")
        self.label_sys_icon.setMaximumSize(QSize(26, 26))
        self.label_sys_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-house.png"))
        self.label_sys_icon.setScaledContents(True)

        self.horizontalLayout_tile_sys.addWidget(self.label_sys_icon)

        self.verticalLayout_tile_sys = QVBoxLayout()
        self.verticalLayout_tile_sys.setSpacing(0)
        self.verticalLayout_tile_sys.setObjectName(u"verticalLayout_tile_sys")
        self.label_sys_title = QLabel(self.frame_tile_sys)
        self.label_sys_title.setObjectName(u"label_sys_title")
        self.label_sys_title.setFont(font1)

        self.verticalLayout_tile_sys.addWidget(self.label_sys_title)

        self.sys_label = QLabel(self.frame_tile_sys)
        self.sys_label.setObjectName(u"sys_label")
        self.sys_label.setFont(font2)

        self.verticalLayout_tile_sys.addWidget(self.sys_label)


        self.horizontalLayout_tile_sys.addLayout(self.verticalLayout_tile_sys)


        self.horizontalLayout_stats.addWidget(self.frame_tile_sys)


        self.verticalLayout_overview.addLayout(self.horizontalLayout_stats)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_overview.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame_overview)

        self.frame = QFrame(PowerSystemDataVisualizationPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_map_card = QFrame(self.frame)
        self.frame_map_card.setObjectName(u"frame_map_card")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_map_card.sizePolicy().hasHeightForWidth())
        self.frame_map_card.setSizePolicy(sizePolicy1)
        self.frame_map_card.setFrameShape(QFrame.NoFrame)
        self.frame_map_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_map_card = QVBoxLayout(self.frame_map_card)
        self.verticalLayout_map_card.setSpacing(8)
        self.verticalLayout_map_card.setObjectName(u"verticalLayout_map_card")
        self.verticalLayout_map_card.setContentsMargins(16, 12, 16, 16)
        self.horizontalLayout_map_title = QHBoxLayout()
        self.horizontalLayout_map_title.setSpacing(8)
        self.horizontalLayout_map_title.setObjectName(u"horizontalLayout_map_title")
        self.label_map_icon = QLabel(self.frame_map_card)
        self.label_map_icon.setObjectName(u"label_map_icon")
        self.label_map_icon.setMaximumSize(QSize(20, 20))
        self.label_map_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-map.png"))
        self.label_map_icon.setScaledContents(True)

        self.horizontalLayout_map_title.addWidget(self.label_map_icon)

        self.label_map_title = QLabel(self.frame_map_card)
        self.label_map_title.setObjectName(u"label_map_title")
        self.label_map_title.setFont(font)

        self.horizontalLayout_map_title.addWidget(self.label_map_title)

        self.horizontalSpacer_map_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_map_title.addItem(self.horizontalSpacer_map_title)


        self.verticalLayout_map_card.addLayout(self.horizontalLayout_map_title)

        self.network_map_widget = MatplotlibWidget(self.frame_map_card)
        self.network_map_widget.setObjectName(u"network_map_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.network_map_widget.sizePolicy().hasHeightForWidth())
        self.network_map_widget.setSizePolicy(sizePolicy2)
        self.network_map_widget.setMinimumSize(QSize(0, 0))

        self.verticalLayout_map_card.addWidget(self.network_map_widget)


        self.horizontalLayout.addWidget(self.frame_map_card)

        self.frame_genmix_card = QFrame(self.frame)
        self.frame_genmix_card.setObjectName(u"frame_genmix_card")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_genmix_card.sizePolicy().hasHeightForWidth())
        self.frame_genmix_card.setSizePolicy(sizePolicy3)
        self.frame_genmix_card.setFrameShape(QFrame.NoFrame)
        self.frame_genmix_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_genmix_card = QVBoxLayout(self.frame_genmix_card)
        self.verticalLayout_genmix_card.setSpacing(8)
        self.verticalLayout_genmix_card.setObjectName(u"verticalLayout_genmix_card")
        self.verticalLayout_genmix_card.setContentsMargins(16, 12, 16, 16)
        self.horizontalLayout_genmix_title = QHBoxLayout()
        self.horizontalLayout_genmix_title.setSpacing(8)
        self.horizontalLayout_genmix_title.setObjectName(u"horizontalLayout_genmix_title")
        self.label_genmix_icon = QLabel(self.frame_genmix_card)
        self.label_genmix_icon.setObjectName(u"label_genmix_icon")
        self.label_genmix_icon.setMaximumSize(QSize(20, 20))
        self.label_genmix_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-chart-pie.png"))
        self.label_genmix_icon.setScaledContents(True)

        self.horizontalLayout_genmix_title.addWidget(self.label_genmix_icon)

        self.label_genmix_title = QLabel(self.frame_genmix_card)
        self.label_genmix_title.setObjectName(u"label_genmix_title")
        self.label_genmix_title.setFont(font)

        self.horizontalLayout_genmix_title.addWidget(self.label_genmix_title)

        self.horizontalSpacer_genmix_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_genmix_title.addItem(self.horizontalSpacer_genmix_title)


        self.verticalLayout_genmix_card.addLayout(self.horizontalLayout_genmix_title)

        self.generation_mix = MatplotlibWidget(self.frame_genmix_card)
        self.generation_mix.setObjectName(u"generation_mix")
        sizePolicy2.setHeightForWidth(self.generation_mix.sizePolicy().hasHeightForWidth())
        self.generation_mix.setSizePolicy(sizePolicy2)
        self.generation_mix.setMinimumSize(QSize(0, 0))

        self.verticalLayout_genmix_card.addWidget(self.generation_mix)


        self.horizontalLayout.addWidget(self.frame_genmix_card)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(PowerSystemDataVisualizationPage)

        QMetaObject.connectSlotsByName(PowerSystemDataVisualizationPage)
    # setupUi

    def retranslateUi(self, PowerSystemDataVisualizationPage):
        PowerSystemDataVisualizationPage.setWindowTitle(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"Data Visualization", None))
        self.frame_overview.setProperty("cardType", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"tile", None))
        self.label_overview_icon.setText("")
        self.label_overview_title.setText(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"SYSTEM OVERVIEW", None))
        self.label_overview_title.setProperty("textRole", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"section", None))
        self.frame_tile_bus.setProperty("cardType", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"tile", None))
        self.label_bus_icon.setText("")
        self.label_bus_title.setText(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"Buses (Zones)", None))
        self.label_bus_title.setProperty("textRole", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"caption", None))
        self.bus_label.setText(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"--", None))
        self.bus_label.setProperty("textRole", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"section", None))
        self.frame_tile_line.setProperty("cardType", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"tile", None))
        self.label_line_icon.setText("")
        self.label_line_title.setText(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"Branches", None))
        self.label_line_title.setProperty("textRole", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"caption", None))
        self.line_label.setText(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"--", None))
        self.line_label.setProperty("textRole", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"section", None))
        self.frame_tile_gen.setProperty("cardType", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"tile", None))
        self.label_gen_icon.setText("")
        self.label_gen_title.setText(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"Generators", None))
        self.label_gen_title.setProperty("textRole", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"caption", None))
        self.gen_label.setText(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"--", None))
        self.gen_label.setProperty("textRole", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"section", None))
        self.frame_tile_sys.setProperty("cardType", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"tile", None))
        self.label_sys_icon.setText("")
        self.label_sys_title.setText(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"System Name", None))
        self.label_sys_title.setProperty("textRole", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"caption", None))
        self.sys_label.setText(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"--", None))
        self.sys_label.setProperty("textRole", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"section", None))
        self.frame_map_card.setProperty("cardType", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"card", None))
        self.label_map_icon.setText("")
        self.label_map_title.setText(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"NETWORK MAP", None))
        self.label_map_title.setProperty("textRole", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"section", None))
        self.frame_genmix_card.setProperty("cardType", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"card", None))
        self.label_genmix_icon.setText("")
        self.label_genmix_title.setText(QCoreApplication.translate("PowerSystemDataVisualizationPage", u"GENERATION MIX", None))
        self.label_genmix_title.setProperty("textRole", QCoreApplication.translate("PowerSystemDataVisualizationPage", u"section", None))
    # retranslateUi

