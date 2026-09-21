# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'execute_model.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import quest_planning.resources_rc

class Ui_ExecuteModelPage(object):
    def setupUi(self, ExecuteModelPage):
        if not ExecuteModelPage.objectName():
            ExecuteModelPage.setObjectName(u"ExecuteModelPage")
        ExecuteModelPage.resize(1118, 928)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ExecuteModelPage.sizePolicy().hasHeightForWidth())
        ExecuteModelPage.setSizePolicy(sizePolicy)
        self.verticalLayout_main = QVBoxLayout(ExecuteModelPage)
        self.verticalLayout_main.setSpacing(18)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.verticalLayout_main.setContentsMargins(24, 24, 24, 24)
        self.frame_header = QFrame(ExecuteModelPage)
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

        self.pushButton = QPushButton(self.frame_header)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icon/images/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setFlat(True)

        self.horizontalLayout_header.addWidget(self.pushButton)


        self.verticalLayout_main.addWidget(self.frame_header)

        self.frame_execution = QFrame(ExecuteModelPage)
        self.frame_execution.setObjectName(u"frame_execution")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_execution.sizePolicy().hasHeightForWidth())
        self.frame_execution.setSizePolicy(sizePolicy2)
        self.frame_execution.setMaximumSize(QSize(16777215, 360))
        self.frame_execution.setFrameShape(QFrame.NoFrame)
        self.frame_execution.setFrameShadow(QFrame.Raised)
        self.verticalLayout_execution = QVBoxLayout(self.frame_execution)
        self.verticalLayout_execution.setSpacing(10)
        self.verticalLayout_execution.setObjectName(u"verticalLayout_execution")
        self.verticalLayout_execution.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_execution_title = QHBoxLayout()
        self.horizontalLayout_execution_title.setSpacing(8)
        self.horizontalLayout_execution_title.setObjectName(u"horizontalLayout_execution_title")
        self.label_execution_title = QLabel(self.frame_execution)
        self.label_execution_title.setObjectName(u"label_execution_title")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_execution_title.setFont(font2)

        self.horizontalLayout_execution_title.addWidget(self.label_execution_title)

        self.horizontalSpacer_execution_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_execution_title.addItem(self.horizontalSpacer_execution_title)


        self.verticalLayout_execution.addLayout(self.horizontalLayout_execution_title)

        self.label_execution_desc = QLabel(self.frame_execution)
        self.label_execution_desc.setObjectName(u"label_execution_desc")
        self.label_execution_desc.setFont(font1)
        self.label_execution_desc.setWordWrap(True)

        self.verticalLayout_execution.addWidget(self.label_execution_desc)

        self.horizontalLayout_results_folder = QHBoxLayout()
        self.horizontalLayout_results_folder.setSpacing(10)
        self.horizontalLayout_results_folder.setObjectName(u"horizontalLayout_results_folder")
        self.label_results_folder = QLabel(self.frame_execution)
        self.label_results_folder.setObjectName(u"label_results_folder")
        self.label_results_folder.setMinimumSize(QSize(150, 0))
        self.label_results_folder.setFont(font2)
        self.label_results_folder.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_results_folder.addWidget(self.label_results_folder)

        self.results_file_box = QComboBox(self.frame_execution)
        self.results_file_box.setObjectName(u"results_file_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.results_file_box.sizePolicy().hasHeightForWidth())
        self.results_file_box.setSizePolicy(sizePolicy3)
        self.results_file_box.setMaximumSize(QSize(520, 16777215))
        self.results_file_box.setFont(font1)
        self.results_file_box.setEditable(True)

        self.horizontalLayout_results_folder.addWidget(self.results_file_box)

        self.browse_folder_button = QPushButton(self.frame_execution)
        self.browse_folder_button.setObjectName(u"browse_folder_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.browse_folder_button.sizePolicy().hasHeightForWidth())
        self.browse_folder_button.setSizePolicy(sizePolicy4)
        self.browse_folder_button.setMinimumSize(QSize(110, 0))
        self.browse_folder_button.setFont(font2)

        self.horizontalLayout_results_folder.addWidget(self.browse_folder_button)

        self.horizontalSpacer_results_folder = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_results_folder.addItem(self.horizontalSpacer_results_folder)


        self.verticalLayout_execution.addLayout(self.horizontalLayout_results_folder)

        self.horizontalLayout_solver = QHBoxLayout()
        self.horizontalLayout_solver.setSpacing(10)
        self.horizontalLayout_solver.setObjectName(u"horizontalLayout_solver")
        self.label_solver = QLabel(self.frame_execution)
        self.label_solver.setObjectName(u"label_solver")
        self.label_solver.setMinimumSize(QSize(150, 0))
        self.label_solver.setFont(font2)
        self.label_solver.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_solver.addWidget(self.label_solver)

        self.solver_select_box = QComboBox(self.frame_execution)
        self.solver_select_box.addItem("")
        self.solver_select_box.addItem("")
        self.solver_select_box.addItem("")
        self.solver_select_box.addItem("")
        self.solver_select_box.addItem("")
        self.solver_select_box.setObjectName(u"solver_select_box")
        sizePolicy3.setHeightForWidth(self.solver_select_box.sizePolicy().hasHeightForWidth())
        self.solver_select_box.setSizePolicy(sizePolicy3)
        self.solver_select_box.setMaximumSize(QSize(300, 16777215))
        self.solver_select_box.setFont(font1)

        self.horizontalLayout_solver.addWidget(self.solver_select_box)

        self.label_solver_hint = QLabel(self.frame_execution)
        self.label_solver_hint.setObjectName(u"label_solver_hint")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        self.label_solver_hint.setFont(font3)
        self.label_solver_hint.setWordWrap(True)

        self.horizontalLayout_solver.addWidget(self.label_solver_hint)

        self.horizontalSpacer_solver = QSpacerItem(20, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_solver.addItem(self.horizontalSpacer_solver)


        self.verticalLayout_execution.addLayout(self.horizontalLayout_solver)

        self.line_divider = QFrame(self.frame_execution)
        self.line_divider.setObjectName(u"line_divider")
        self.line_divider.setMaximumSize(QSize(16777215, 1))
        self.line_divider.setFrameShape(QFrame.HLine)
        self.line_divider.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_execution.addWidget(self.line_divider)

        self.horizontalLayout_actions = QHBoxLayout()
        self.horizontalLayout_actions.setSpacing(12)
        self.horizontalLayout_actions.setObjectName(u"horizontalLayout_actions")
        self.build_button = QPushButton(self.frame_execution)
        self.build_button.setObjectName(u"build_button")
        sizePolicy4.setHeightForWidth(self.build_button.sizePolicy().hasHeightForWidth())
        self.build_button.setSizePolicy(sizePolicy4)
        self.build_button.setMinimumSize(QSize(160, 0))
        self.build_button.setFont(font2)

        self.horizontalLayout_actions.addWidget(self.build_button)

        self.run_button = QPushButton(self.frame_execution)
        self.run_button.setObjectName(u"run_button")
        sizePolicy4.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy4)
        self.run_button.setMinimumSize(QSize(160, 0))
        self.run_button.setFont(font2)

        self.horizontalLayout_actions.addWidget(self.run_button)

        self.label_actions_hint = QLabel(self.frame_execution)
        self.label_actions_hint.setObjectName(u"label_actions_hint")
        self.label_actions_hint.setFont(font3)

        self.horizontalLayout_actions.addWidget(self.label_actions_hint)

        self.horizontalSpacer_actions = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_actions.addItem(self.horizontalSpacer_actions)


        self.verticalLayout_execution.addLayout(self.horizontalLayout_actions)


        self.verticalLayout_main.addWidget(self.frame_execution)

        self.model_status_frame = QFrame(ExecuteModelPage)
        self.model_status_frame.setObjectName(u"model_status_frame")
        sizePolicy.setHeightForWidth(self.model_status_frame.sizePolicy().hasHeightForWidth())
        self.model_status_frame.setSizePolicy(sizePolicy)
        self.model_status_frame.setFrameShape(QFrame.NoFrame)
        self.model_status_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_status = QVBoxLayout(self.model_status_frame)
        self.verticalLayout_status.setSpacing(10)
        self.verticalLayout_status.setObjectName(u"verticalLayout_status")
        self.verticalLayout_status.setContentsMargins(20, 14, 20, 14)
        self.horizontalLayout_status_title = QHBoxLayout()
        self.horizontalLayout_status_title.setSpacing(8)
        self.horizontalLayout_status_title.setObjectName(u"horizontalLayout_status_title")
        self.label_status_title = QLabel(self.model_status_frame)
        self.label_status_title.setObjectName(u"label_status_title")
        self.label_status_title.setFont(font2)

        self.horizontalLayout_status_title.addWidget(self.label_status_title)

        self.horizontalSpacer_status_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_status_title.addItem(self.horizontalSpacer_status_title)


        self.verticalLayout_status.addLayout(self.horizontalLayout_status_title)

        self.label_status_desc = QLabel(self.model_status_frame)
        self.label_status_desc.setObjectName(u"label_status_desc")
        self.label_status_desc.setFont(font3)

        self.verticalLayout_status.addWidget(self.label_status_desc)

        self.report_progress_box = QPlainTextEdit(self.model_status_frame)
        self.report_progress_box.setObjectName(u"report_progress_box")
        sizePolicy.setHeightForWidth(self.report_progress_box.sizePolicy().hasHeightForWidth())
        self.report_progress_box.setSizePolicy(sizePolicy)
        self.report_progress_box.setMinimumSize(QSize(0, 200))
        self.report_progress_box.setReadOnly(True)
        self.report_progress_box.setProperty("codeRole", True)

        self.verticalLayout_status.addWidget(self.report_progress_box)


        self.verticalLayout_main.addWidget(self.model_status_frame)


        self.retranslateUi(ExecuteModelPage)

        QMetaObject.connectSlotsByName(ExecuteModelPage)
    # setupUi

    def retranslateUi(self, ExecuteModelPage):
        ExecuteModelPage.setWindowTitle(QCoreApplication.translate("ExecuteModelPage", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("ExecuteModelPage", u"Execute Model", None))
        self.label_title.setProperty("textRole", QCoreApplication.translate("ExecuteModelPage", u"heading", None))
        self.label_subtitle.setText(QCoreApplication.translate("ExecuteModelPage", u"The Execute Model step builds the QuESt Planning optimization model and solves it with your selected solver.", None))
        self.label_subtitle.setProperty("textRole", QCoreApplication.translate("ExecuteModelPage", u"subtitle", None))
        self.pushButton.setText("")
        self.frame_execution.setProperty("cardType", QCoreApplication.translate("ExecuteModelPage", u"card", None))
        self.label_execution_title.setText(QCoreApplication.translate("ExecuteModelPage", u"MODEL EXECUTION", None))
        self.label_execution_title.setProperty("textRole", QCoreApplication.translate("ExecuteModelPage", u"section", None))
        self.label_execution_desc.setText(QCoreApplication.translate("ExecuteModelPage", u"The <b><i>QuESt Planning</i></b> optimization model is built and solved in this step. Choose where the results will be saved, select the solver, then press <i>Build Model</i> followed by <i>Solve Model</i>.", None))
        self.label_execution_desc.setProperty("textRole", QCoreApplication.translate("ExecuteModelPage", u"body", None))
        self.label_results_folder.setText(QCoreApplication.translate("ExecuteModelPage", u"Results Folder", None))
        self.label_results_folder.setProperty("textRole", QCoreApplication.translate("ExecuteModelPage", u"section", None))
        self.browse_folder_button.setText(QCoreApplication.translate("ExecuteModelPage", u"Browse", None))
        self.label_solver.setText(QCoreApplication.translate("ExecuteModelPage", u"Solver", None))
        self.label_solver.setProperty("textRole", QCoreApplication.translate("ExecuteModelPage", u"section", None))
        self.solver_select_box.setItemText(0, QCoreApplication.translate("ExecuteModelPage", u"Clp", None))
        self.solver_select_box.setItemText(1, QCoreApplication.translate("ExecuteModelPage", u"GLPK", None))
        self.solver_select_box.setItemText(2, QCoreApplication.translate("ExecuteModelPage", u"Gurobi", None))
        self.solver_select_box.setItemText(3, QCoreApplication.translate("ExecuteModelPage", u"HiGHs", None))
        self.solver_select_box.setItemText(4, QCoreApplication.translate("ExecuteModelPage", u"Other (Upcoming)", None))

        self.label_solver_hint.setText(QCoreApplication.translate("ExecuteModelPage", u"The solver and any required licenses must be installed and accessible.", None))
        self.label_solver_hint.setProperty("textRole", QCoreApplication.translate("ExecuteModelPage", u"caption", None))
        self.build_button.setText(QCoreApplication.translate("ExecuteModelPage", u"Build Model", None))
        self.build_button.setProperty("btnRole", QCoreApplication.translate("ExecuteModelPage", u"primary", None))
        self.run_button.setText(QCoreApplication.translate("ExecuteModelPage", u"Solve Model", None))
        self.run_button.setProperty("btnRole", QCoreApplication.translate("ExecuteModelPage", u"primary", None))
        self.label_actions_hint.setText(QCoreApplication.translate("ExecuteModelPage", u"Build the model first, then solve it. Progress appears in the Model Status panel.", None))
        self.label_actions_hint.setProperty("textRole", QCoreApplication.translate("ExecuteModelPage", u"caption", None))
        self.model_status_frame.setProperty("cardType", QCoreApplication.translate("ExecuteModelPage", u"card", None))
        self.label_status_title.setText(QCoreApplication.translate("ExecuteModelPage", u"MODEL STATUS", None))
        self.label_status_title.setProperty("textRole", QCoreApplication.translate("ExecuteModelPage", u"section", None))
        self.label_status_desc.setText(QCoreApplication.translate("ExecuteModelPage", u"Optimization Model Solve Status:", None))
        self.label_status_desc.setProperty("textRole", QCoreApplication.translate("ExecuteModelPage", u"caption", None))
        self.report_progress_box.setPlainText(QCoreApplication.translate("ExecuteModelPage", u"Ready to build the model.", None))
    # retranslateUi

