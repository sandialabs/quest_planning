# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 08:06:11 2024

@author: cjnewlu

CJN edits - 4/12/24
"""

import os
import traceback

from PySide6.QtCore import (
    QThreadPool,
)
from PySide6.QtWidgets import (
    QMenu,
    QWidget,
    QSizePolicy,
    QErrorMessage,
    QInputDialog,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QPushButton,
    QMessageBox
)
from quest_planning.build_run_page.ui.build_run import Ui_build_run
from tools.tools import RetirementDialog, TechDialog, RPSDialog, ExecuteFunction

class BuildRunPage(QWidget, Ui_build_run):
    """
        Make scenario selections, build and run the scenario.
    """

    def __init__(self,tabWidget, data_handler, optimizer, results_viewer):
        """Initialize the scenario builder page."""
        super().__init__()
#           Set up the ui
        self.data_handler = data_handler
        self.optimizer = optimizer
        self.results_viewer = results_viewer
        self.tabWidget = tabWidget
        self.setupUi(self)
        self.error_message = QErrorMessage()
        self.popup_message = QMessageBox()
        
        self.build_button.clicked.connect(self.on_build_button_clicked)
        self.run_button.clicked.connect(self.on_run_button_clicked)
        self.solver_text.returnPressed.connect(lambda:
                                             self.data_handler.set_solver(self.solver_text.text()))
            
        self.next_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(5))
        self.previous_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3))
    
    def on_build_button_clicked(self):
        """
            Build the optimization model. Ensure everything is properly enforced.
        """

        self.construct_load_blocks = ExecuteFunction(self.data_handler.construct_load_blocks)
        self.construct_load_blocks.finished.connect(lambda x=self.construct_load_blocks: self.thread_finished(x))

        self.instantiate_model = ExecuteFunction(self.optimizer.instantiate_model)
        self.instantiate_model.finished.connect(lambda x=self.instantiate_model: self.thread_finished(x))

        self.populate_model = ExecuteFunction(self.optimizer.populate_model)
        self.populate_model.finished.connect(lambda x=self.populate_model: self.thread_finished(x))


        try:
            self.construct_load_blocks.start()
            self.popup_message.setText("Constructing Load Blocks")
            self.popup_message.setStandardButtons(QMessageBox.NoButton)
            self.popup_message.exec()
        except Exception:
            traceback.print_exc()
            self.error_message.showMessage("Load Block Construction Failed.")
        else:
            try:
                self.instantiate_model.start()
                self.popup_message.setText("Instantiating Model")
                self.popup_message.setStandardButtons(QMessageBox.NoButton)
                self.popup_message.exec()
            except Exception:
                traceback.print_exc()
                self.error_message.showMessage("Model Instantiation Failed.")
            else:
                try:
                    self.populate_model.start()
                    self.popup_message.setText("Populating Model")
                    self.popup_message.setStandardButtons(QMessageBox.NoButton)
                    self.popup_message.exec()
                except Exception:
                    traceback.print_exc()
                    self.error_message.showMessage("Model Population Failed.")
                else:
                    self.popup_message.setText("Model Successfully Built")
                    self.popup_message.setStandardButtons(QMessageBox.Ok)
                    self.popup_message.buttonClicked.connect(self.popup_message.done(1))
                    self.popup_message.exec()

    def on_run_button_clicked(self):
        """
            Run the optimization model and generate results. Point to the results directory.
        """
        self.solve_model = ExecuteFunction(self.optimizer.solve_model)
        self.solve_model.finished.connect(lambda x=self.solve_model: self.thread_finished(x))

        self.process_results = ExecuteFunction(self.results_viewer.process_results, args=[self.optimizer.get_results, self.optimizer.report])
        self.process_results.finished.connect(lambda x=self.process_results: self.thread_finished(x))

        try:
            self.solve_model.start()
            self.popup_message.setText("Solving Model")
            self.popup_message.setStandardButtons(QMessageBox.NoButton)
            self.popup_message.exec()
        except Exception:
            traceback.print_exc()
            self.error_message.showMessage("Failed to run optimization.")
        else:
            try:
                self.process_results._args = [*self.optimizer.get_results(), self.optimizer.report]
                self.process_results.start()
                self.popup_message.setText("Processing Results")
                self.popup_message.setStandardButtons(QMessageBox.NoButton)
                self.popup_message.exec()
            except Exception:
                traceback.print_exc()
                self.error_message.showMessage("Failed to run optimization")
            else:
                self.popup_message.setText("Success: Find the results in a directory I haven't taken the time to find yet")
                self.popup_message.setStandardButtons(QMessageBox.Ok)
                self.popup_message.buttonClicked.connect(self.popup_message.done(1))
                self.popup_message.exec()


    def thread_finished(self, thread):
        """Kills thread"""
        self.popup_message.done(1)
        del thread
        
    def on_tab_opened(self, i):
        '''Tab opened'''
        if i == 4:
            try:
                load_options = self.data_handler.load_data[self.data_handler.data_ls.index('load')].columns
                load_options = [x for x in load_options if x not in ['datetime', 'year', 'month', 'day1', 'day', 'hour']]
                self.load_profile_box.addItems(load_options)
            except Exception as e:
                print(e)
                self.error_message.showMessage("No power system data has been loaded.")
        