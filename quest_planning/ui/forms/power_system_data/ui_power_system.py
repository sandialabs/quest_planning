# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'power_system.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

from quest_planning.matplotlibwidget import MatplotlibWidget
import quest_planning.resources_rc

class Ui_PowerSystemPage(object):
    def setupUi(self, PowerSystemPage):
        if not PowerSystemPage.objectName():
            PowerSystemPage.setObjectName(u"PowerSystemPage")
        PowerSystemPage.resize(739, 761)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PowerSystemPage.sizePolicy().hasHeightForWidth())
        PowerSystemPage.setSizePolicy(sizePolicy)
        self.page_standard = QWidget()
        self.page_standard.setObjectName(u"page_standard")
        self.verticalLayout_main = QVBoxLayout(self.page_standard)
        self.verticalLayout_main.setSpacing(18)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(24, 24, 24, 24)
        self.frame_header = QFrame(self.page_standard)
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

        self.power_system_help_button = QToolButton(self.frame_header)
        self.power_system_help_button.setObjectName(u"power_system_help_button")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/help_FILL0_wght200_GRAD0_opsz48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.power_system_help_button.setIcon(icon)
        self.power_system_help_button.setIconSize(QSize(24, 24))
        self.power_system_help_button.setAutoRaise(True)

        self.horizontalLayout_header.addWidget(self.power_system_help_button)


        self.verticalLayout_main.addWidget(self.frame_header)

        self.frame_source = QFrame(self.page_standard)
        self.frame_source.setObjectName(u"frame_source")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_source.sizePolicy().hasHeightForWidth())
        self.frame_source.setSizePolicy(sizePolicy2)
        self.frame_source.setMaximumSize(QSize(16777215, 180))
        self.frame_source.setFrameShape(QFrame.NoFrame)
        self.frame_source.setFrameShadow(QFrame.Raised)
        self.verticalLayout_source = QVBoxLayout(self.frame_source)
        self.verticalLayout_source.setSpacing(10)
        self.verticalLayout_source.setObjectName(u"verticalLayout_source")
        self.verticalLayout_source.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_source_title = QHBoxLayout()
        self.horizontalLayout_source_title.setSpacing(8)
        self.horizontalLayout_source_title.setObjectName(u"horizontalLayout_source_title")
        self.label_source_icon = QLabel(self.frame_source)
        self.label_source_icon.setObjectName(u"label_source_icon")
        self.label_source_icon.setMaximumSize(QSize(22, 22))
        self.label_source_icon.setPixmap(QPixmap(u":/icon/images/icons/dataset_FILL0_wght200_GRAD0_opsz48.png"))
        self.label_source_icon.setScaledContents(True)

        self.horizontalLayout_source_title.addWidget(self.label_source_icon)

        self.label_source_title = QLabel(self.frame_source)
        self.label_source_title.setObjectName(u"label_source_title")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_source_title.setFont(font2)

        self.horizontalLayout_source_title.addWidget(self.label_source_title)

        self.horizontalSpacer_source_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_source_title.addItem(self.horizontalSpacer_source_title)


        self.verticalLayout_source.addLayout(self.horizontalLayout_source_title)

        self.gridLayout_source = QGridLayout()
        self.gridLayout_source.setObjectName(u"gridLayout_source")
        self.gridLayout_source.setHorizontalSpacing(14)
        self.gridLayout_source.setVerticalSpacing(10)
        self.label_system_name = QLabel(self.frame_source)
        self.label_system_name.setObjectName(u"label_system_name")
        self.label_system_name.setMinimumSize(QSize(100, 0))
        self.label_system_name.setFont(font2)
        self.label_system_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_source.addWidget(self.label_system_name, 0, 0, 1, 1)

        self.system_name_input = QLineEdit(self.frame_source)
        self.system_name_input.setObjectName(u"system_name_input")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.system_name_input.sizePolicy().hasHeightForWidth())
        self.system_name_input.setSizePolicy(sizePolicy3)
        self.system_name_input.setMaximumSize(QSize(500, 16777215))
        self.system_name_input.setFont(font1)

        self.gridLayout_source.addWidget(self.system_name_input, 0, 1, 1, 1)

        self.label_data_folder = QLabel(self.frame_source)
        self.label_data_folder.setObjectName(u"label_data_folder")
        self.label_data_folder.setFont(font2)
        self.label_data_folder.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_source.addWidget(self.label_data_folder, 1, 0, 1, 1)

        self.horizontalLayout_folder = QHBoxLayout()
        self.horizontalLayout_folder.setSpacing(10)
        self.horizontalLayout_folder.setObjectName(u"horizontalLayout_folder")
        self.file_combo_box = QComboBox(self.frame_source)
        self.file_combo_box.setObjectName(u"file_combo_box")
        sizePolicy3.setHeightForWidth(self.file_combo_box.sizePolicy().hasHeightForWidth())
        self.file_combo_box.setSizePolicy(sizePolicy3)
        self.file_combo_box.setFont(font1)

        self.horizontalLayout_folder.addWidget(self.file_combo_box)

        self.file_button = QPushButton(self.frame_source)
        self.file_button.setObjectName(u"file_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.file_button.sizePolicy().hasHeightForWidth())
        self.file_button.setSizePolicy(sizePolicy4)
        self.file_button.setMinimumSize(QSize(110, 0))
        self.file_button.setFont(font2)

        self.horizontalLayout_folder.addWidget(self.file_button)

        self.open_file_button = QPushButton(self.frame_source)
        self.open_file_button.setObjectName(u"open_file_button")
        sizePolicy4.setHeightForWidth(self.open_file_button.sizePolicy().hasHeightForWidth())
        self.open_file_button.setSizePolicy(sizePolicy4)
        self.open_file_button.setMinimumSize(QSize(110, 0))
        self.open_file_button.setFont(font2)

        self.horizontalLayout_folder.addWidget(self.open_file_button)

        self.horizontalLayout_folder.setStretch(0, 1)

        self.gridLayout_source.addLayout(self.horizontalLayout_folder, 1, 1, 1, 1)


        self.verticalLayout_source.addLayout(self.gridLayout_source)


        self.verticalLayout_main.addWidget(self.frame_source)

        self.frame_overview = QFrame(self.page_standard)
        self.frame_overview.setObjectName(u"frame_overview")
        sizePolicy2.setHeightForWidth(self.frame_overview.sizePolicy().hasHeightForWidth())
        self.frame_overview.setSizePolicy(sizePolicy2)
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
        self.label_overview_title.setFont(font2)

        self.horizontalLayout_overview_title.addWidget(self.label_overview_title)

        self.horizontalSpacer_overview_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        self.label_bus_title.setFont(font3)

        self.verticalLayout_tile_bus.addWidget(self.label_bus_title)

        self.bus_label = QLabel(self.frame_tile_bus)
        self.bus_label.setObjectName(u"bus_label")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.bus_label.setFont(font4)

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
        self.label_line_title.setFont(font3)

        self.verticalLayout_tile_line.addWidget(self.label_line_title)

        self.line_label = QLabel(self.frame_tile_line)
        self.line_label.setObjectName(u"line_label")
        self.line_label.setFont(font4)

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
        self.label_gen_title.setFont(font3)

        self.verticalLayout_tile_gen.addWidget(self.label_gen_title)

        self.gen_label = QLabel(self.frame_tile_gen)
        self.gen_label.setObjectName(u"gen_label")
        self.gen_label.setFont(font4)

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
        self.label_sys_title.setFont(font3)

        self.verticalLayout_tile_sys.addWidget(self.label_sys_title)

        self.sys_label = QLabel(self.frame_tile_sys)
        self.sys_label.setObjectName(u"sys_label")
        self.sys_label.setFont(font4)

        self.verticalLayout_tile_sys.addWidget(self.sys_label)


        self.horizontalLayout_tile_sys.addLayout(self.verticalLayout_tile_sys)


        self.horizontalLayout_stats.addWidget(self.frame_tile_sys)


        self.verticalLayout_overview.addLayout(self.horizontalLayout_stats)


        self.verticalLayout_main.addWidget(self.frame_overview)

        self.frame_plots = QFrame(self.page_standard)
        self.frame_plots.setObjectName(u"frame_plots")
        sizePolicy.setHeightForWidth(self.frame_plots.sizePolicy().hasHeightForWidth())
        self.frame_plots.setSizePolicy(sizePolicy)
        self.frame_plots.setMinimumSize(QSize(0, 300))
        self.frame_plots.setFrameShape(QFrame.NoFrame)
        self.frame_plots.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_plots = QHBoxLayout(self.frame_plots)
        self.horizontalLayout_plots.setSpacing(18)
        self.horizontalLayout_plots.setObjectName(u"horizontalLayout_plots")
        self.frame_map_card = QFrame(self.frame_plots)
        self.frame_map_card.setObjectName(u"frame_map_card")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_map_card.sizePolicy().hasHeightForWidth())
        self.frame_map_card.setSizePolicy(sizePolicy5)
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
        self.label_map_title.setFont(font2)

        self.horizontalLayout_map_title.addWidget(self.label_map_title)

        self.horizontalSpacer_map_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_map_title.addItem(self.horizontalSpacer_map_title)


        self.verticalLayout_map_card.addLayout(self.horizontalLayout_map_title)

        self.network_map_widget = MatplotlibWidget(self.frame_map_card)
        self.network_map_widget.setObjectName(u"network_map_widget")
        sizePolicy.setHeightForWidth(self.network_map_widget.sizePolicy().hasHeightForWidth())
        self.network_map_widget.setSizePolicy(sizePolicy)
        self.network_map_widget.setMinimumSize(QSize(0, 0))

        self.verticalLayout_map_card.addWidget(self.network_map_widget)


        self.horizontalLayout_plots.addWidget(self.frame_map_card)

        self.frame_genmix_card = QFrame(self.frame_plots)
        self.frame_genmix_card.setObjectName(u"frame_genmix_card")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(3)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_genmix_card.sizePolicy().hasHeightForWidth())
        self.frame_genmix_card.setSizePolicy(sizePolicy6)
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
        self.label_genmix_title.setFont(font2)

        self.horizontalLayout_genmix_title.addWidget(self.label_genmix_title)

        self.horizontalSpacer_genmix_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_genmix_title.addItem(self.horizontalSpacer_genmix_title)


        self.verticalLayout_genmix_card.addLayout(self.horizontalLayout_genmix_title)

        self.generation_mix = MatplotlibWidget(self.frame_genmix_card)
        self.generation_mix.setObjectName(u"generation_mix")
        sizePolicy.setHeightForWidth(self.generation_mix.sizePolicy().hasHeightForWidth())
        self.generation_mix.setSizePolicy(sizePolicy)
        self.generation_mix.setMinimumSize(QSize(0, 0))

        self.verticalLayout_genmix_card.addWidget(self.generation_mix)


        self.horizontalLayout_plots.addWidget(self.frame_genmix_card)


        self.verticalLayout_main.addWidget(self.frame_plots)

        PowerSystemPage.addWidget(self.page_standard)
        self.power_system_data_w_load = QWidget()
        self.power_system_data_w_load.setObjectName(u"power_system_data_w_load")
        self.verticalLayout_load = QVBoxLayout(self.power_system_data_w_load)
        self.verticalLayout_load.setSpacing(18)
        self.verticalLayout_load.setObjectName(u"verticalLayout_load")
        self.verticalLayout_load.setContentsMargins(24, 24, 24, 24)
        self.frame_header_load = QFrame(self.power_system_data_w_load)
        self.frame_header_load.setObjectName(u"frame_header_load")
        sizePolicy1.setHeightForWidth(self.frame_header_load.sizePolicy().hasHeightForWidth())
        self.frame_header_load.setSizePolicy(sizePolicy1)
        self.frame_header_load.setMaximumSize(QSize(16777215, 80))
        self.frame_header_load.setFrameShape(QFrame.NoFrame)
        self.frame_header_load.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_header_load = QHBoxLayout(self.frame_header_load)
        self.horizontalLayout_header_load.setObjectName(u"horizontalLayout_header_load")
        self.horizontalLayout_header_load.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_header_text_load = QVBoxLayout()
        self.verticalLayout_header_text_load.setSpacing(2)
        self.verticalLayout_header_text_load.setObjectName(u"verticalLayout_header_text_load")
        self.label_title_load = QLabel(self.frame_header_load)
        self.label_title_load.setObjectName(u"label_title_load")
        self.label_title_load.setFont(font)

        self.verticalLayout_header_text_load.addWidget(self.label_title_load)

        self.label_subtitle_load = QLabel(self.frame_header_load)
        self.label_subtitle_load.setObjectName(u"label_subtitle_load")
        self.label_subtitle_load.setFont(font1)

        self.verticalLayout_header_text_load.addWidget(self.label_subtitle_load)


        self.horizontalLayout_header_load.addLayout(self.verticalLayout_header_text_load)

        self.horizontalSpacer_header_load = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_header_load.addItem(self.horizontalSpacer_header_load)

        self.load_help_button = QToolButton(self.frame_header_load)
        self.load_help_button.setObjectName(u"load_help_button")
        self.load_help_button.setIcon(icon)
        self.load_help_button.setIconSize(QSize(24, 24))
        self.load_help_button.setAutoRaise(True)

        self.horizontalLayout_header_load.addWidget(self.load_help_button)


        self.verticalLayout_load.addWidget(self.frame_header_load)

        self.frame_source_load = QFrame(self.power_system_data_w_load)
        self.frame_source_load.setObjectName(u"frame_source_load")
        sizePolicy2.setHeightForWidth(self.frame_source_load.sizePolicy().hasHeightForWidth())
        self.frame_source_load.setSizePolicy(sizePolicy2)
        self.frame_source_load.setMaximumSize(QSize(16777215, 180))
        self.frame_source_load.setFrameShape(QFrame.NoFrame)
        self.frame_source_load.setFrameShadow(QFrame.Raised)
        self.verticalLayout_source_load = QVBoxLayout(self.frame_source_load)
        self.verticalLayout_source_load.setSpacing(10)
        self.verticalLayout_source_load.setObjectName(u"verticalLayout_source_load")
        self.verticalLayout_source_load.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_source_title_load = QHBoxLayout()
        self.horizontalLayout_source_title_load.setSpacing(8)
        self.horizontalLayout_source_title_load.setObjectName(u"horizontalLayout_source_title_load")
        self.label_source_icon_load = QLabel(self.frame_source_load)
        self.label_source_icon_load.setObjectName(u"label_source_icon_load")
        self.label_source_icon_load.setMaximumSize(QSize(22, 22))
        self.label_source_icon_load.setPixmap(QPixmap(u":/icon/images/icons/dataset_FILL0_wght200_GRAD0_opsz48.png"))
        self.label_source_icon_load.setScaledContents(True)

        self.horizontalLayout_source_title_load.addWidget(self.label_source_icon_load)

        self.label_source_title_load = QLabel(self.frame_source_load)
        self.label_source_title_load.setObjectName(u"label_source_title_load")
        self.label_source_title_load.setFont(font2)

        self.horizontalLayout_source_title_load.addWidget(self.label_source_title_load)

        self.horizontalSpacer_source_title_load = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_source_title_load.addItem(self.horizontalSpacer_source_title_load)


        self.verticalLayout_source_load.addLayout(self.horizontalLayout_source_title_load)

        self.gridLayout_source_load = QGridLayout()
        self.gridLayout_source_load.setObjectName(u"gridLayout_source_load")
        self.gridLayout_source_load.setHorizontalSpacing(14)
        self.gridLayout_source_load.setVerticalSpacing(10)
        self.label_system_name_load = QLabel(self.frame_source_load)
        self.label_system_name_load.setObjectName(u"label_system_name_load")
        self.label_system_name_load.setMinimumSize(QSize(100, 0))
        self.label_system_name_load.setFont(font2)
        self.label_system_name_load.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_source_load.addWidget(self.label_system_name_load, 0, 0, 1, 1)

        self.load_system_name_input = QLineEdit(self.frame_source_load)
        self.load_system_name_input.setObjectName(u"load_system_name_input")
        sizePolicy3.setHeightForWidth(self.load_system_name_input.sizePolicy().hasHeightForWidth())
        self.load_system_name_input.setSizePolicy(sizePolicy3)
        self.load_system_name_input.setMaximumSize(QSize(500, 16777215))
        self.load_system_name_input.setFont(font1)

        self.gridLayout_source_load.addWidget(self.load_system_name_input, 0, 1, 1, 1)

        self.label_data_folder_load = QLabel(self.frame_source_load)
        self.label_data_folder_load.setObjectName(u"label_data_folder_load")
        self.label_data_folder_load.setFont(font2)
        self.label_data_folder_load.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_source_load.addWidget(self.label_data_folder_load, 1, 0, 1, 1)

        self.horizontalLayout_folder_load = QHBoxLayout()
        self.horizontalLayout_folder_load.setSpacing(10)
        self.horizontalLayout_folder_load.setObjectName(u"horizontalLayout_folder_load")
        self.load_file_combo_box = QComboBox(self.frame_source_load)
        self.load_file_combo_box.setObjectName(u"load_file_combo_box")
        sizePolicy3.setHeightForWidth(self.load_file_combo_box.sizePolicy().hasHeightForWidth())
        self.load_file_combo_box.setSizePolicy(sizePolicy3)
        self.load_file_combo_box.setFont(font1)

        self.horizontalLayout_folder_load.addWidget(self.load_file_combo_box)

        self.load_file_button = QPushButton(self.frame_source_load)
        self.load_file_button.setObjectName(u"load_file_button")
        sizePolicy4.setHeightForWidth(self.load_file_button.sizePolicy().hasHeightForWidth())
        self.load_file_button.setSizePolicy(sizePolicy4)
        self.load_file_button.setMinimumSize(QSize(110, 0))
        self.load_file_button.setFont(font2)

        self.horizontalLayout_folder_load.addWidget(self.load_file_button)

        self.load_open_file_button = QPushButton(self.frame_source_load)
        self.load_open_file_button.setObjectName(u"load_open_file_button")
        sizePolicy4.setHeightForWidth(self.load_open_file_button.sizePolicy().hasHeightForWidth())
        self.load_open_file_button.setSizePolicy(sizePolicy4)
        self.load_open_file_button.setMinimumSize(QSize(110, 0))
        self.load_open_file_button.setFont(font2)

        self.horizontalLayout_folder_load.addWidget(self.load_open_file_button)

        self.horizontalLayout_folder_load.setStretch(0, 1)

        self.gridLayout_source_load.addLayout(self.horizontalLayout_folder_load, 1, 1, 1, 1)


        self.verticalLayout_source_load.addLayout(self.gridLayout_source_load)


        self.verticalLayout_load.addWidget(self.frame_source_load)

        self.frame_overview_load = QFrame(self.power_system_data_w_load)
        self.frame_overview_load.setObjectName(u"frame_overview_load")
        sizePolicy2.setHeightForWidth(self.frame_overview_load.sizePolicy().hasHeightForWidth())
        self.frame_overview_load.setSizePolicy(sizePolicy2)
        self.frame_overview_load.setMaximumSize(QSize(16777215, 180))
        self.frame_overview_load.setFrameShape(QFrame.NoFrame)
        self.frame_overview_load.setFrameShadow(QFrame.Raised)
        self.verticalLayout_overview_load = QVBoxLayout(self.frame_overview_load)
        self.verticalLayout_overview_load.setSpacing(10)
        self.verticalLayout_overview_load.setObjectName(u"verticalLayout_overview_load")
        self.verticalLayout_overview_load.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_overview_title_load = QHBoxLayout()
        self.horizontalLayout_overview_title_load.setSpacing(8)
        self.horizontalLayout_overview_title_load.setObjectName(u"horizontalLayout_overview_title_load")
        self.label_overview_icon_load = QLabel(self.frame_overview_load)
        self.label_overview_icon_load.setObjectName(u"label_overview_icon_load")
        self.label_overview_icon_load.setMaximumSize(QSize(22, 22))
        self.label_overview_icon_load.setPixmap(QPixmap(u":/icon/images/icons/cil-view-module.png"))
        self.label_overview_icon_load.setScaledContents(True)

        self.horizontalLayout_overview_title_load.addWidget(self.label_overview_icon_load)

        self.label_overview_title_load = QLabel(self.frame_overview_load)
        self.label_overview_title_load.setObjectName(u"label_overview_title_load")
        self.label_overview_title_load.setFont(font2)

        self.horizontalLayout_overview_title_load.addWidget(self.label_overview_title_load)

        self.horizontalSpacer_overview_title_load = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_overview_title_load.addItem(self.horizontalSpacer_overview_title_load)


        self.verticalLayout_overview_load.addLayout(self.horizontalLayout_overview_title_load)

        self.horizontalLayout_stats_load = QHBoxLayout()
        self.horizontalLayout_stats_load.setSpacing(14)
        self.horizontalLayout_stats_load.setObjectName(u"horizontalLayout_stats_load")
        self.frame_tile_bus_load = QFrame(self.frame_overview_load)
        self.frame_tile_bus_load.setObjectName(u"frame_tile_bus_load")
        self.frame_tile_bus_load.setFrameShape(QFrame.NoFrame)
        self.frame_tile_bus_load.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_tile_bus_load = QHBoxLayout(self.frame_tile_bus_load)
        self.horizontalLayout_tile_bus_load.setSpacing(10)
        self.horizontalLayout_tile_bus_load.setObjectName(u"horizontalLayout_tile_bus_load")
        self.label_bus_icon_load = QLabel(self.frame_tile_bus_load)
        self.label_bus_icon_load.setObjectName(u"label_bus_icon_load")
        self.label_bus_icon_load.setMaximumSize(QSize(26, 26))
        self.label_bus_icon_load.setPixmap(QPixmap(u":/icon/images/icons/cil-location-pin.png"))
        self.label_bus_icon_load.setScaledContents(True)

        self.horizontalLayout_tile_bus_load.addWidget(self.label_bus_icon_load)

        self.verticalLayout_tile_bus_load = QVBoxLayout()
        self.verticalLayout_tile_bus_load.setSpacing(0)
        self.verticalLayout_tile_bus_load.setObjectName(u"verticalLayout_tile_bus_load")
        self.label_bus_title_load = QLabel(self.frame_tile_bus_load)
        self.label_bus_title_load.setObjectName(u"label_bus_title_load")
        self.label_bus_title_load.setFont(font3)

        self.verticalLayout_tile_bus_load.addWidget(self.label_bus_title_load)

        self.load_bus_label = QLabel(self.frame_tile_bus_load)
        self.load_bus_label.setObjectName(u"load_bus_label")
        self.load_bus_label.setFont(font4)

        self.verticalLayout_tile_bus_load.addWidget(self.load_bus_label)


        self.horizontalLayout_tile_bus_load.addLayout(self.verticalLayout_tile_bus_load)


        self.horizontalLayout_stats_load.addWidget(self.frame_tile_bus_load)

        self.frame_tile_line_load = QFrame(self.frame_overview_load)
        self.frame_tile_line_load.setObjectName(u"frame_tile_line_load")
        self.frame_tile_line_load.setFrameShape(QFrame.NoFrame)
        self.frame_tile_line_load.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_tile_line_load = QHBoxLayout(self.frame_tile_line_load)
        self.horizontalLayout_tile_line_load.setSpacing(10)
        self.horizontalLayout_tile_line_load.setObjectName(u"horizontalLayout_tile_line_load")
        self.label_line_icon_load = QLabel(self.frame_tile_line_load)
        self.label_line_icon_load.setObjectName(u"label_line_icon_load")
        self.label_line_icon_load.setMaximumSize(QSize(26, 26))
        self.label_line_icon_load.setPixmap(QPixmap(u":/icon/images/icons/cil-layers.png"))
        self.label_line_icon_load.setScaledContents(True)

        self.horizontalLayout_tile_line_load.addWidget(self.label_line_icon_load)

        self.verticalLayout_tile_line_load = QVBoxLayout()
        self.verticalLayout_tile_line_load.setSpacing(0)
        self.verticalLayout_tile_line_load.setObjectName(u"verticalLayout_tile_line_load")
        self.label_line_title_load = QLabel(self.frame_tile_line_load)
        self.label_line_title_load.setObjectName(u"label_line_title_load")
        self.label_line_title_load.setFont(font3)

        self.verticalLayout_tile_line_load.addWidget(self.label_line_title_load)

        self.load_line_label = QLabel(self.frame_tile_line_load)
        self.load_line_label.setObjectName(u"load_line_label")
        self.load_line_label.setFont(font4)

        self.verticalLayout_tile_line_load.addWidget(self.load_line_label)


        self.horizontalLayout_tile_line_load.addLayout(self.verticalLayout_tile_line_load)


        self.horizontalLayout_stats_load.addWidget(self.frame_tile_line_load)

        self.frame_tile_gen_load = QFrame(self.frame_overview_load)
        self.frame_tile_gen_load.setObjectName(u"frame_tile_gen_load")
        self.frame_tile_gen_load.setFrameShape(QFrame.NoFrame)
        self.frame_tile_gen_load.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_tile_gen_load = QHBoxLayout(self.frame_tile_gen_load)
        self.horizontalLayout_tile_gen_load.setSpacing(10)
        self.horizontalLayout_tile_gen_load.setObjectName(u"horizontalLayout_tile_gen_load")
        self.label_gen_icon_load = QLabel(self.frame_tile_gen_load)
        self.label_gen_icon_load.setObjectName(u"label_gen_icon_load")
        self.label_gen_icon_load.setMaximumSize(QSize(26, 26))
        self.label_gen_icon_load.setPixmap(QPixmap(u":/icon/images/icons/cil-lightbulb.png"))
        self.label_gen_icon_load.setScaledContents(True)

        self.horizontalLayout_tile_gen_load.addWidget(self.label_gen_icon_load)

        self.verticalLayout_tile_gen_load = QVBoxLayout()
        self.verticalLayout_tile_gen_load.setSpacing(0)
        self.verticalLayout_tile_gen_load.setObjectName(u"verticalLayout_tile_gen_load")
        self.label_gen_title_load = QLabel(self.frame_tile_gen_load)
        self.label_gen_title_load.setObjectName(u"label_gen_title_load")
        self.label_gen_title_load.setFont(font3)

        self.verticalLayout_tile_gen_load.addWidget(self.label_gen_title_load)

        self.load_gen_label = QLabel(self.frame_tile_gen_load)
        self.load_gen_label.setObjectName(u"load_gen_label")
        self.load_gen_label.setFont(font4)

        self.verticalLayout_tile_gen_load.addWidget(self.load_gen_label)


        self.horizontalLayout_tile_gen_load.addLayout(self.verticalLayout_tile_gen_load)


        self.horizontalLayout_stats_load.addWidget(self.frame_tile_gen_load)

        self.frame_tile_sys_load = QFrame(self.frame_overview_load)
        self.frame_tile_sys_load.setObjectName(u"frame_tile_sys_load")
        self.frame_tile_sys_load.setFrameShape(QFrame.NoFrame)
        self.frame_tile_sys_load.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_tile_sys_load = QHBoxLayout(self.frame_tile_sys_load)
        self.horizontalLayout_tile_sys_load.setSpacing(10)
        self.horizontalLayout_tile_sys_load.setObjectName(u"horizontalLayout_tile_sys_load")
        self.label_sys_icon_load = QLabel(self.frame_tile_sys_load)
        self.label_sys_icon_load.setObjectName(u"label_sys_icon_load")
        self.label_sys_icon_load.setMaximumSize(QSize(26, 26))
        self.label_sys_icon_load.setPixmap(QPixmap(u":/icon/images/icons/cil-house.png"))
        self.label_sys_icon_load.setScaledContents(True)

        self.horizontalLayout_tile_sys_load.addWidget(self.label_sys_icon_load)

        self.verticalLayout_tile_sys_load = QVBoxLayout()
        self.verticalLayout_tile_sys_load.setSpacing(0)
        self.verticalLayout_tile_sys_load.setObjectName(u"verticalLayout_tile_sys_load")
        self.label_sys_title_load = QLabel(self.frame_tile_sys_load)
        self.label_sys_title_load.setObjectName(u"label_sys_title_load")
        self.label_sys_title_load.setFont(font3)

        self.verticalLayout_tile_sys_load.addWidget(self.label_sys_title_load)

        self.load_sys_label = QLabel(self.frame_tile_sys_load)
        self.load_sys_label.setObjectName(u"load_sys_label")
        self.load_sys_label.setFont(font4)

        self.verticalLayout_tile_sys_load.addWidget(self.load_sys_label)


        self.horizontalLayout_tile_sys_load.addLayout(self.verticalLayout_tile_sys_load)


        self.horizontalLayout_stats_load.addWidget(self.frame_tile_sys_load)


        self.verticalLayout_overview_load.addLayout(self.horizontalLayout_stats_load)


        self.verticalLayout_load.addWidget(self.frame_overview_load)

        self.frame_plots_load = QFrame(self.power_system_data_w_load)
        self.frame_plots_load.setObjectName(u"frame_plots_load")
        sizePolicy.setHeightForWidth(self.frame_plots_load.sizePolicy().hasHeightForWidth())
        self.frame_plots_load.setSizePolicy(sizePolicy)
        self.frame_plots_load.setMinimumSize(QSize(0, 300))
        self.frame_plots_load.setFrameShape(QFrame.NoFrame)
        self.frame_plots_load.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_plots_load = QHBoxLayout(self.frame_plots_load)
        self.horizontalLayout_plots_load.setSpacing(18)
        self.horizontalLayout_plots_load.setObjectName(u"horizontalLayout_plots_load")
        self.frame_map_card_load = QFrame(self.frame_plots_load)
        self.frame_map_card_load.setObjectName(u"frame_map_card_load")
        sizePolicy5.setHeightForWidth(self.frame_map_card_load.sizePolicy().hasHeightForWidth())
        self.frame_map_card_load.setSizePolicy(sizePolicy5)
        self.frame_map_card_load.setFrameShape(QFrame.NoFrame)
        self.frame_map_card_load.setFrameShadow(QFrame.Raised)
        self.verticalLayout_map_card_load = QVBoxLayout(self.frame_map_card_load)
        self.verticalLayout_map_card_load.setSpacing(8)
        self.verticalLayout_map_card_load.setObjectName(u"verticalLayout_map_card_load")
        self.verticalLayout_map_card_load.setContentsMargins(16, 12, 16, 16)
        self.horizontalLayout_map_title_load = QHBoxLayout()
        self.horizontalLayout_map_title_load.setSpacing(8)
        self.horizontalLayout_map_title_load.setObjectName(u"horizontalLayout_map_title_load")
        self.label_map_icon_load = QLabel(self.frame_map_card_load)
        self.label_map_icon_load.setObjectName(u"label_map_icon_load")
        self.label_map_icon_load.setMaximumSize(QSize(20, 20))
        self.label_map_icon_load.setPixmap(QPixmap(u":/icon/images/icons/cil-map.png"))
        self.label_map_icon_load.setScaledContents(True)

        self.horizontalLayout_map_title_load.addWidget(self.label_map_icon_load)

        self.label_map_title_load = QLabel(self.frame_map_card_load)
        self.label_map_title_load.setObjectName(u"label_map_title_load")
        self.label_map_title_load.setFont(font2)

        self.horizontalLayout_map_title_load.addWidget(self.label_map_title_load)

        self.horizontalSpacer_map_title_load = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_map_title_load.addItem(self.horizontalSpacer_map_title_load)


        self.verticalLayout_map_card_load.addLayout(self.horizontalLayout_map_title_load)

        self.load_network_map_widget = MatplotlibWidget(self.frame_map_card_load)
        self.load_network_map_widget.setObjectName(u"load_network_map_widget")
        sizePolicy.setHeightForWidth(self.load_network_map_widget.sizePolicy().hasHeightForWidth())
        self.load_network_map_widget.setSizePolicy(sizePolicy)
        self.load_network_map_widget.setMinimumSize(QSize(0, 0))

        self.verticalLayout_map_card_load.addWidget(self.load_network_map_widget)


        self.horizontalLayout_plots_load.addWidget(self.frame_map_card_load)

        self.frame_load_card = QFrame(self.frame_plots_load)
        self.frame_load_card.setObjectName(u"frame_load_card")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(3)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.frame_load_card.sizePolicy().hasHeightForWidth())
        self.frame_load_card.setSizePolicy(sizePolicy7)
        self.frame_load_card.setFrameShape(QFrame.NoFrame)
        self.frame_load_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_load_card = QVBoxLayout(self.frame_load_card)
        self.verticalLayout_load_card.setSpacing(8)
        self.verticalLayout_load_card.setObjectName(u"verticalLayout_load_card")
        self.verticalLayout_load_card.setContentsMargins(16, 12, 16, 16)
        self.horizontalLayout_load_title = QHBoxLayout()
        self.horizontalLayout_load_title.setSpacing(8)
        self.horizontalLayout_load_title.setObjectName(u"horizontalLayout_load_title")
        self.label_load_icon = QLabel(self.frame_load_card)
        self.label_load_icon.setObjectName(u"label_load_icon")
        self.label_load_icon.setMaximumSize(QSize(20, 20))
        self.label_load_icon.setPixmap(QPixmap(u":/icon/images/icons/cil-chart-line.png"))
        self.label_load_icon.setScaledContents(True)

        self.horizontalLayout_load_title.addWidget(self.label_load_icon)

        self.label_load_title = QLabel(self.frame_load_card)
        self.label_load_title.setObjectName(u"label_load_title")
        self.label_load_title.setFont(font2)

        self.horizontalLayout_load_title.addWidget(self.label_load_title)

        self.horizontalSpacer_load_title = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_load_title.addItem(self.horizontalSpacer_load_title)


        self.verticalLayout_load_card.addLayout(self.horizontalLayout_load_title)

        self.load_profile_widget = MatplotlibWidget(self.frame_load_card)
        self.load_profile_widget.setObjectName(u"load_profile_widget")
        sizePolicy.setHeightForWidth(self.load_profile_widget.sizePolicy().hasHeightForWidth())
        self.load_profile_widget.setSizePolicy(sizePolicy)
        self.load_profile_widget.setMinimumSize(QSize(0, 150))

        self.verticalLayout_load_card.addWidget(self.load_profile_widget)


        self.horizontalLayout_plots_load.addWidget(self.frame_load_card)

        self.frame_genmix_card_load = QFrame(self.frame_plots_load)
        self.frame_genmix_card_load.setObjectName(u"frame_genmix_card_load")
        sizePolicy7.setHeightForWidth(self.frame_genmix_card_load.sizePolicy().hasHeightForWidth())
        self.frame_genmix_card_load.setSizePolicy(sizePolicy7)
        self.frame_genmix_card_load.setFrameShape(QFrame.NoFrame)
        self.frame_genmix_card_load.setFrameShadow(QFrame.Raised)
        self.verticalLayout_genmix_card_load = QVBoxLayout(self.frame_genmix_card_load)
        self.verticalLayout_genmix_card_load.setSpacing(8)
        self.verticalLayout_genmix_card_load.setObjectName(u"verticalLayout_genmix_card_load")
        self.verticalLayout_genmix_card_load.setContentsMargins(16, 12, 16, 16)
        self.horizontalLayout_genmix_title_load = QHBoxLayout()
        self.horizontalLayout_genmix_title_load.setSpacing(8)
        self.horizontalLayout_genmix_title_load.setObjectName(u"horizontalLayout_genmix_title_load")
        self.label_genmix_icon_load = QLabel(self.frame_genmix_card_load)
        self.label_genmix_icon_load.setObjectName(u"label_genmix_icon_load")
        self.label_genmix_icon_load.setMaximumSize(QSize(20, 20))
        self.label_genmix_icon_load.setPixmap(QPixmap(u":/icon/images/icons/cil-chart-pie.png"))
        self.label_genmix_icon_load.setScaledContents(True)

        self.horizontalLayout_genmix_title_load.addWidget(self.label_genmix_icon_load)

        self.label_genmix_title_load = QLabel(self.frame_genmix_card_load)
        self.label_genmix_title_load.setObjectName(u"label_genmix_title_load")
        self.label_genmix_title_load.setFont(font2)

        self.horizontalLayout_genmix_title_load.addWidget(self.label_genmix_title_load)

        self.horizontalSpacer_genmix_title_load = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_genmix_title_load.addItem(self.horizontalSpacer_genmix_title_load)


        self.verticalLayout_genmix_card_load.addLayout(self.horizontalLayout_genmix_title_load)

        self.load_generation_mix = MatplotlibWidget(self.frame_genmix_card_load)
        self.load_generation_mix.setObjectName(u"load_generation_mix")
        sizePolicy.setHeightForWidth(self.load_generation_mix.sizePolicy().hasHeightForWidth())
        self.load_generation_mix.setSizePolicy(sizePolicy)
        self.load_generation_mix.setMinimumSize(QSize(0, 150))

        self.verticalLayout_genmix_card_load.addWidget(self.load_generation_mix)


        self.horizontalLayout_plots_load.addWidget(self.frame_genmix_card_load)


        self.verticalLayout_load.addWidget(self.frame_plots_load)

        PowerSystemPage.addWidget(self.power_system_data_w_load)

        self.retranslateUi(PowerSystemPage)

        PowerSystemPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PowerSystemPage)
    # setupUi

    def retranslateUi(self, PowerSystemPage):
        PowerSystemPage.setWindowTitle(QCoreApplication.translate("PowerSystemPage", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("PowerSystemPage", u"Power System Data", None))
        self.label_title.setProperty("textRole", u"heading")
        self.label_subtitle.setText(QCoreApplication.translate("PowerSystemPage", u"Select the folder containing your power system input data.", None))
        self.label_subtitle.setProperty("textRole", u"subtitle")
        self.power_system_help_button.setText("")
        self.power_system_help_button.setProperty("btnRole", u"icon")
        self.frame_source.setProperty("cardType", u"card")
        self.label_source_icon.setText("")
        self.label_source_title.setText(QCoreApplication.translate("PowerSystemPage", u"DATA SOURCE", None))
        self.label_source_title.setProperty("textRole", u"section")
        self.label_system_name.setText(QCoreApplication.translate("PowerSystemPage", u"System Name", None))
        self.system_name_input.setText(QCoreApplication.translate("PowerSystemPage", u"Default System Name", None))
        self.label_data_folder.setText(QCoreApplication.translate("PowerSystemPage", u"Data Folder", None))
        self.file_button.setText(QCoreApplication.translate("PowerSystemPage", u"Browse", None))
        self.open_file_button.setText(QCoreApplication.translate("PowerSystemPage", u"Open", None))
        self.open_file_button.setProperty("btnRole", u"primary")
        self.frame_overview.setProperty("cardType", u"tile")
        self.label_overview_icon.setText("")
        self.label_overview_title.setText(QCoreApplication.translate("PowerSystemPage", u"SYSTEM OVERVIEW", None))
        self.label_overview_title.setProperty("textRole", u"section")
        self.frame_tile_bus.setProperty("cardType", u"tile")
        self.label_bus_icon.setText("")
        self.label_bus_title.setText(QCoreApplication.translate("PowerSystemPage", u"Buses (Zones)", None))
        self.label_bus_title.setProperty("textRole", u"caption")
        self.bus_label.setText(QCoreApplication.translate("PowerSystemPage", u"--", None))
        self.bus_label.setProperty("textRole", u"section")
        self.frame_tile_line.setProperty("cardType", u"tile")
        self.label_line_icon.setText("")
        self.label_line_title.setText(QCoreApplication.translate("PowerSystemPage", u"Branches", None))
        self.label_line_title.setProperty("textRole", u"caption")
        self.line_label.setText(QCoreApplication.translate("PowerSystemPage", u"--", None))
        self.line_label.setProperty("textRole", u"section")
        self.frame_tile_gen.setProperty("cardType", u"tile")
        self.label_gen_icon.setText("")
        self.label_gen_title.setText(QCoreApplication.translate("PowerSystemPage", u"Generators", None))
        self.label_gen_title.setProperty("textRole", u"caption")
        self.gen_label.setText(QCoreApplication.translate("PowerSystemPage", u"--", None))
        self.gen_label.setProperty("textRole", u"section")
        self.frame_tile_sys.setProperty("cardType", u"tile")
        self.label_sys_icon.setText("")
        self.label_sys_title.setText(QCoreApplication.translate("PowerSystemPage", u"System Name", None))
        self.label_sys_title.setProperty("textRole", u"caption")
        self.sys_label.setText(QCoreApplication.translate("PowerSystemPage", u"--", None))
        self.sys_label.setProperty("textRole", u"section")
        self.frame_map_card.setProperty("cardType", u"card")
        self.label_map_icon.setText("")
        self.label_map_title.setText(QCoreApplication.translate("PowerSystemPage", u"NETWORK MAP", None))
        self.label_map_title.setProperty("textRole", u"section")
        self.frame_genmix_card.setProperty("cardType", u"card")
        self.label_genmix_icon.setText("")
        self.label_genmix_title.setText(QCoreApplication.translate("PowerSystemPage", u"GENERATION MIX", None))
        self.label_genmix_title.setProperty("textRole", u"section")
        self.label_title_load.setText(QCoreApplication.translate("PowerSystemPage", u"Power System Data", None))
        self.label_title_load.setProperty("textRole", u"heading")
        self.label_subtitle_load.setText(QCoreApplication.translate("PowerSystemPage", u"Select the folder containing your power system input data (includes load profile).", None))
        self.label_subtitle_load.setProperty("textRole", u"subtitle")
        self.load_help_button.setText("")
        self.load_help_button.setProperty("btnRole", u"icon")
        self.frame_source_load.setProperty("cardType", u"card")
        self.label_source_icon_load.setText("")
        self.label_source_title_load.setText(QCoreApplication.translate("PowerSystemPage", u"DATA SOURCE", None))
        self.label_source_title_load.setProperty("textRole", u"section")
        self.label_system_name_load.setText(QCoreApplication.translate("PowerSystemPage", u"System Name", None))
        self.load_system_name_input.setText(QCoreApplication.translate("PowerSystemPage", u"Default System Name", None))
        self.label_data_folder_load.setText(QCoreApplication.translate("PowerSystemPage", u"Data Folder", None))
        self.load_file_button.setText(QCoreApplication.translate("PowerSystemPage", u"Browse", None))
        self.load_open_file_button.setText(QCoreApplication.translate("PowerSystemPage", u"Open", None))
        self.load_open_file_button.setProperty("btnRole", u"primary")
        self.frame_overview_load.setProperty("cardType", u"tile")
        self.label_overview_icon_load.setText("")
        self.label_overview_title_load.setText(QCoreApplication.translate("PowerSystemPage", u"SYSTEM OVERVIEW", None))
        self.label_overview_title_load.setProperty("textRole", u"section")
        self.frame_tile_bus_load.setProperty("cardType", u"tile")
        self.label_bus_icon_load.setText("")
        self.label_bus_title_load.setText(QCoreApplication.translate("PowerSystemPage", u"Buses (Zones)", None))
        self.label_bus_title_load.setProperty("textRole", u"caption")
        self.load_bus_label.setText(QCoreApplication.translate("PowerSystemPage", u"--", None))
        self.load_bus_label.setProperty("textRole", u"section")
        self.frame_tile_line_load.setProperty("cardType", u"tile")
        self.label_line_icon_load.setText("")
        self.label_line_title_load.setText(QCoreApplication.translate("PowerSystemPage", u"Branches", None))
        self.label_line_title_load.setProperty("textRole", u"caption")
        self.load_line_label.setText(QCoreApplication.translate("PowerSystemPage", u"--", None))
        self.load_line_label.setProperty("textRole", u"section")
        self.frame_tile_gen_load.setProperty("cardType", u"tile")
        self.label_gen_icon_load.setText("")
        self.label_gen_title_load.setText(QCoreApplication.translate("PowerSystemPage", u"Generators", None))
        self.label_gen_title_load.setProperty("textRole", u"caption")
        self.load_gen_label.setText(QCoreApplication.translate("PowerSystemPage", u"--", None))
        self.load_gen_label.setProperty("textRole", u"section")
        self.frame_tile_sys_load.setProperty("cardType", u"tile")
        self.label_sys_icon_load.setText("")
        self.label_sys_title_load.setText(QCoreApplication.translate("PowerSystemPage", u"System Name", None))
        self.label_sys_title_load.setProperty("textRole", u"caption")
        self.load_sys_label.setText(QCoreApplication.translate("PowerSystemPage", u"--", None))
        self.load_sys_label.setProperty("textRole", u"section")
        self.frame_map_card_load.setProperty("cardType", u"card")
        self.label_map_icon_load.setText("")
        self.label_map_title_load.setText(QCoreApplication.translate("PowerSystemPage", u"NETWORK MAP", None))
        self.label_map_title_load.setProperty("textRole", u"section")
        self.frame_load_card.setProperty("cardType", u"card")
        self.label_load_icon.setText("")
        self.label_load_title.setText(QCoreApplication.translate("PowerSystemPage", u"LOAD PROFILE", None))
        self.label_load_title.setProperty("textRole", u"section")
        self.frame_genmix_card_load.setProperty("cardType", u"card")
        self.label_genmix_icon_load.setText("")
        self.label_genmix_title_load.setText(QCoreApplication.translate("PowerSystemPage", u"GENERATION MIX", None))
        self.label_genmix_title_load.setProperty("textRole", u"section")
    # retranslateUi

