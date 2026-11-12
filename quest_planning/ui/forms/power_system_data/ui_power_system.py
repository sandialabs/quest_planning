# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'power_system.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_PowerSystemPage(object):
    def setupUi(self, PowerSystemPage):
        if not PowerSystemPage.objectName():
            PowerSystemPage.setObjectName(u"PowerSystemPage")
        PowerSystemPage.resize(892, 781)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
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

        self.horizontalSpacer_header = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer_header)


        self.verticalLayout_main.addWidget(self.frame_header)

        self.frame_source = QFrame(self.page_standard)
        self.frame_source.setObjectName(u"frame_source")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
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

        self.horizontalSpacer_source_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
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

        self.power_system_help_button = QToolButton(self.frame_source)
        self.power_system_help_button.setObjectName(u"power_system_help_button")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/help_FILL0_wght200_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.power_system_help_button.setIcon(icon)
        self.power_system_help_button.setIconSize(QSize(24, 24))
        self.power_system_help_button.setAutoRaise(True)

        self.horizontalLayout_folder.addWidget(self.power_system_help_button)

        self.horizontalLayout_folder.setStretch(0, 1)

        self.gridLayout_source.addLayout(self.horizontalLayout_folder, 1, 1, 1, 1)


        self.verticalLayout_source.addLayout(self.gridLayout_source)


        self.verticalLayout_main.addWidget(self.frame_source)

        self.frame_viz = QFrame(self.page_standard)
        self.frame_viz.setObjectName(u"frame_viz")
        self.frame_viz.setFrameShape(QFrame.NoFrame)
        self.frame_viz.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_viz)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_visualization = QPushButton(self.frame_viz)
        self.btn_visualization.setObjectName(u"btn_visualization")

        self.verticalLayout.addWidget(self.btn_visualization)


        self.verticalLayout_main.addWidget(self.frame_viz)

        self.begin_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_main.addItem(self.begin_spacer)

        PowerSystemPage.addWidget(self.page_standard)

        self.retranslateUi(PowerSystemPage)

        PowerSystemPage.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PowerSystemPage)
    # setupUi

    def retranslateUi(self, PowerSystemPage):
        PowerSystemPage.setWindowTitle(QCoreApplication.translate("PowerSystemPage", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("PowerSystemPage", u"Power System Data", None))
        self.label_title.setProperty("textRole", QCoreApplication.translate("PowerSystemPage", u"heading", None))
        self.label_subtitle.setText(QCoreApplication.translate("PowerSystemPage", u"Select the folder containing your power system input data.", None))
        self.label_subtitle.setProperty("textRole", QCoreApplication.translate("PowerSystemPage", u"subtitle", None))
        self.frame_source.setProperty("cardType", QCoreApplication.translate("PowerSystemPage", u"card", None))
        self.label_source_icon.setText("")
        self.label_source_title.setText(QCoreApplication.translate("PowerSystemPage", u"DATA SOURCE", None))
        self.label_source_title.setProperty("textRole", QCoreApplication.translate("PowerSystemPage", u"section", None))
        self.label_system_name.setText(QCoreApplication.translate("PowerSystemPage", u"System Name", None))
        self.system_name_input.setText(QCoreApplication.translate("PowerSystemPage", u"Default System Name", None))
        self.label_data_folder.setText(QCoreApplication.translate("PowerSystemPage", u"Data Folder", None))
        self.file_button.setText(QCoreApplication.translate("PowerSystemPage", u"Browse", None))
        self.open_file_button.setText(QCoreApplication.translate("PowerSystemPage", u"Open", None))
        self.open_file_button.setProperty("btnRole", QCoreApplication.translate("PowerSystemPage", u"primary", None))
        self.power_system_help_button.setText("")
        self.power_system_help_button.setProperty("btnRole", QCoreApplication.translate("PowerSystemPage", u"icon", None))
        self.btn_visualization.setText(QCoreApplication.translate("PowerSystemPage", u"Open Visualization ", None))
        self.frame_viz.setProperty("cardType", QCoreApplication.translate("PowerSystemPage", u"card", None))
        self.btn_visualization.setProperty("btnRole", QCoreApplication.translate("PowerSystemPage", u"primary", None))
    # retranslateUi
