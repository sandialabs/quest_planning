# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'large_load_model.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_LargeLoadModelPage(object):
    def setupUi(self, LargeLoadModelPage):
        if not LargeLoadModelPage.objectName():
            LargeLoadModelPage.setObjectName(u"LargeLoadModelPage")
        LargeLoadModelPage.resize(480, 520)
        self.verticalLayout = QVBoxLayout(LargeLoadModelPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(LargeLoadModelPage)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_title.setFont(font)

        self.verticalLayout.addWidget(self.label_title)

        self.frame_default = QFrame(LargeLoadModelPage)
        self.frame_default.setObjectName(u"frame_default")
        self.frame_default.setFrameShape(QFrame.Box)
        self.frame_default.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame_default)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_default)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.checkBox = QCheckBox(self.frame_default)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_default)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.frame_default)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.frame_3 = QFrame(self.frame_default)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(False)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_3)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.gridLayout.addWidget(self.doubleSpinBox_2, 1, 1, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.frame_3)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_default)

        self.frame = QFrame(LargeLoadModelPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_large_title = QLabel(self.frame)
        self.label_large_title.setObjectName(u"label_large_title")
        self.label_large_title.setFont(font)

        self.verticalLayout_3.addWidget(self.label_large_title)

        self.table_large_loads = QTableWidget(self.frame)
        if (self.table_large_loads.columnCount() < 4):
            self.table_large_loads.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_large_loads.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_large_loads.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_large_loads.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_large_loads.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_large_loads.setObjectName(u"table_large_loads")
        self.table_large_loads.setColumnCount(4)

        self.verticalLayout_3.addWidget(self.table_large_loads)

        self.frame_table_ctrl = QFrame(self.frame)
        self.frame_table_ctrl.setObjectName(u"frame_table_ctrl")
        self.frame_table_ctrl.setFrameShape(QFrame.NoFrame)
        self.frame_table_ctrl.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_table_ctrl)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_add = QPushButton(self.frame_table_ctrl)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout_2.addWidget(self.btn_add)

        self.btn_remove = QPushButton(self.frame_table_ctrl)
        self.btn_remove.setObjectName(u"btn_remove")

        self.horizontalLayout_2.addWidget(self.btn_remove)


        self.verticalLayout_3.addWidget(self.frame_table_ctrl)


        self.verticalLayout.addWidget(self.frame)

        self.frame_buttons = QFrame(LargeLoadModelPage)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(279, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.frame_buttons)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_ok = QPushButton(self.frame_buttons)
        self.btn_ok.setObjectName(u"btn_ok")

        self.horizontalLayout.addWidget(self.btn_ok)


        self.verticalLayout.addWidget(self.frame_buttons)


        self.retranslateUi(LargeLoadModelPage)

        QMetaObject.connectSlotsByName(LargeLoadModelPage)
    # setupUi

    def retranslateUi(self, LargeLoadModelPage):
        LargeLoadModelPage.setWindowTitle(QCoreApplication.translate("LargeLoadModelPage", u"Large Load Model Page", None))
        self.label_title.setText(QCoreApplication.translate("LargeLoadModelPage", u"Large Load Configuration", None))
        self.label.setText(QCoreApplication.translate("LargeLoadModelPage", u"Scenario", None))
        self.checkBox.setText(QCoreApplication.translate("LargeLoadModelPage", u"Enable Large Loads", None))
        self.checkBox_2.setText(QCoreApplication.translate("LargeLoadModelPage", u"Enable Onsite Resources", None))
        self.checkBox_4.setText(QCoreApplication.translate("LargeLoadModelPage", u"Enable Large Load Flexibility", None))
        self.label_2.setText(QCoreApplication.translate("LargeLoadModelPage", u"Large Load Growth", None))
        self.label_3.setText(QCoreApplication.translate("LargeLoadModelPage", u"Self Sufficiency", None))
        self.label_large_title.setText(QCoreApplication.translate("LargeLoadModelPage", u"Large Loads", None))
        ___qtablewidgetitem = self.table_large_loads.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LargeLoadModelPage", u"ID", None));
        ___qtablewidgetitem1 = self.table_large_loads.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LargeLoadModelPage", u"BUS", None));
        ___qtablewidgetitem2 = self.table_large_loads.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LargeLoadModelPage", u"Capacity (MW)", None));
        ___qtablewidgetitem3 = self.table_large_loads.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("LargeLoadModelPage", u"Deploy Year", None));
        self.btn_add.setText(QCoreApplication.translate("LargeLoadModelPage", u"Add Large Load", None))
        self.btn_remove.setText(QCoreApplication.translate("LargeLoadModelPage", u"Remove", None))
        self.btn_cancel.setText(QCoreApplication.translate("LargeLoadModelPage", u"Cancel", None))
        self.btn_ok.setText(QCoreApplication.translate("LargeLoadModelPage", u"OK", None))
    # retranslateUi

