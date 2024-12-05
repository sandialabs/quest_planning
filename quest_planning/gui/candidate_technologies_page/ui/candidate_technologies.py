# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'candidate_technologies.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_candidate_technologies(object):
    def setupUi(self, candidate_technologies):
        if not candidate_technologies.objectName():
            candidate_technologies.setObjectName(u"candidate_technologies")
        candidate_technologies.resize(965, 748)
        self.verticalLayout_4 = QVBoxLayout(candidate_technologies)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_4 = QFrame(candidate_technologies)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_13)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.tech_frame = QFrame(candidate_technologies)
        self.tech_frame.setObjectName(u"tech_frame")
        self.tech_frame.setFrameShape(QFrame.StyledPanel)
        self.tech_frame.setFrameShadow(QFrame.Raised)
        self.tech_frame_layout = QVBoxLayout(self.tech_frame)
        self.tech_frame_layout.setObjectName(u"tech_frame_layout")
        self.add_new_tech_button = QPushButton(self.tech_frame)
        self.add_new_tech_button.setObjectName(u"add_new_tech_button")

        self.tech_frame_layout.addWidget(self.add_new_tech_button)


        self.verticalLayout_4.addWidget(self.tech_frame)


        self.retranslateUi(candidate_technologies)

        QMetaObject.connectSlotsByName(candidate_technologies)
    # setupUi

    def retranslateUi(self, candidate_technologies):
        candidate_technologies.setWindowTitle(QCoreApplication.translate("candidate_technologies", u"Form", None))
        self.label_13.setText(QCoreApplication.translate("candidate_technologies", u"Please select the candidate technologies", None))
        self.add_new_tech_button.setText(QCoreApplication.translate("candidate_technologies", u"Add New Technology", None))
    # retranslateUi

