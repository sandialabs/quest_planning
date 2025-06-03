# -*- coding: utf-8 -*-
"""
Control of the Model Execution page.
"""

import os
import traceback
import warnings
warnings.filterwarnings("ignore")

from PySide6.QtCore import (
    QThreadPool,
    Qt,
    Signal,
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
    QMessageBox,
    QFileDialog
)
from quest_planning.gui.build_run_page.ui.ui_build_run import Ui_build_run
from quest_planning.gui.tools.tools import RetirementDialog, TechDialog, RPSDialog, ExecuteFunction, StdoutBuffer,ExecuteFunctionBuffer, LoadingSplashScreen
import sys
#from planning_model import PlanningModelPage


class BuildRunPage(QWidget, Ui_build_run):
    """
        Make scenario selections, build and run the scenario.
    """

    solved_it = Signal()

    def __init__(self, tabWidget, data_handler, optimizer, results_viewer,
                 planning_model_page, scenario_builder_page):
        """Initialize the buildrun page."""
        super().__init__()
#           Set up the ui
        self.data_handler = data_handler
        self.optimizer = optimizer
        self.results_viewer = results_viewer
        self.tabWidget = tabWidget
        self.planning_model_page = planning_model_page
        self.scenario_builder_page = scenario_builder_page

        self.setupUi(self)
        self.error_message = QErrorMessage()
        self.popup_message = QMessageBox()

        self.construct_load_blocks_flag = False
        self.instantiate_model_flag = False
        self.populate_model_flag = False
        self.solve_model_flag = False
        self.process_results_flag = False
        
        self.results_dir_select = None
        self.browse_folder_button.clicked.connect(self.select_file)

        self.build_button.clicked.connect(self.on_build_button_clicked)
        self.run_button.clicked.connect(self.on_run_button_clicked)
        self.build_run_help_button.clicked.connect(self.build_run_help)
        
        self.solver_select_box.currentTextChanged.connect(lambda:
                                             self.data_handler.set_solver(self.solver_select_box.currentText()))
            
        self.next_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(5))
        self.previous_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3))
        self.next_button.setToolTip('Proceed to Results Viewer')
        self.previous_button.setToolTip('Return to Scenario Builder')

        self.model_status_frame.hide()
#self.line_top.hide()
    
    def select_file(self):
        """Selects file directory using a QFileDialog and adds to the file_combo_box."""
        dir_select = QFileDialog.getExistingDirectory()
        self.results_file_box.addItem(dir_select)
        

    def on_build_button_clicked(self):
        """
            Build the optimization model. Ensure everything is properly enforced.
        """
        #Update all user-defined inputs and start build
        #self.start_build = ExecuteFunctionBuffer(self.collect_inputs())
        #self.start_build.output_updated.connect(self.update_output_box)
        #self.start_build.finished.connect(self.end_start_build)
        
        self.collect_inputs()

        self.splash_screen = LoadingSplashScreen(self,title = "Building Model")
        self.splash_screen.show_message("Building Pyomo Model")

        self.construct_load_blocks = ExecuteFunctionBuffer(self.data_handler.construct_load_blocks)
        self.construct_load_blocks.output_updated.connect(self.update_output_box)
        self.construct_load_blocks.finished.connect(self.end_construct_load_blocks)
        self.construct_load_blocks.task_failed.connect(self.construct_load_blocks_failed)

        self.instantiate_model = ExecuteFunctionBuffer(self.optimizer.instantiate_model)
        self.instantiate_model.output_updated.connect(self.update_output_box)
        self.instantiate_model.finished.connect(self.end_instantiate_model)
        self.instantiate_model.task_failed.connect(self.instantiate_model_failed)

        self.populate_model = ExecuteFunctionBuffer(self.optimizer.populate_model)
        self.populate_model.output_updated.connect(self.update_output_box)
        self.populate_model.finished.connect(self.end_populate_model)
        self.populate_model.task_failed.connect(self.populate_model_failed)

        #self.start_build.start()
        self.construct_load_blocks.start()
    
    def on_run_button_clicked(self):
        """
            Run the optimization model and generate results. Point to the results directory.
        """

        self.splash_screen_run = LoadingSplashScreen(self,title = "Solving Model")
        self.splash_screen_run.show_message("Optimizing...")

        self.solve_model = ExecuteFunctionBuffer(self.optimizer.solve_model)
        #self.solve_model.finished.connect(lambda x=self.solve_model: self.thread_finished(x))
        self.solve_model.output_updated.connect(self.update_output_box)
        self.solve_model.finished.connect(self.end_solve_model)
        self.solve_model.task_failed.connect(self.solve_model_failed)

        self.process_results = ExecuteFunctionBuffer(self.results_viewer.process_results_gui, args=[self.optimizer.get_results, self.optimizer.report,self.results_dir_select])
        self.process_results.output_updated.connect(self.update_output_box)
        self.process_results.finished.connect(self.end_process_results)
        self.process_results.task_failed.connect(self.process_results_failed)
        #self.process_results.finished.connect(lambda x=self.process_results: self.thread_finished(x))
       
        #print("Solving Model")
        self.solve_model.start()

    def update_output_box(self,text):
        self.report_progress_box.append(text)

    def construct_load_blocks_failed(self):
        self.construct_load_blocks_flag = True

    def instantiate_model_failed(self):
        self.instantiate_model_flag = True

    def populate_model_failed(self):
        self.populate_model_flag = True
    
    def solve_model_failed(self):
        self.solve_model_flag = True

    def process_results_failed(self):
        self.process_results_flag = True

    def end_start_build(self):
        self.thread_finished(self.start_build)

        self.construct_load_blocks.start()

    def end_construct_load_blocks(self):
        self.thread_finished(self.construct_load_blocks)

        if self.construct_load_blocks_flag:
            self.popup_message.done(1)
            self.error_message.showMessage("Load Block Construction Failed")
        else:
            self.instantiate_model.start()


    def end_instantiate_model(self):
        self.thread_finished(self.instantiate_model)

        if self.instantiate_model_flag:
            self.popup_message.done(1)
            self.error_message.showMessage("Model Instantiation Failed")
        else:
            self.populate_model.start()
            

        
    def end_populate_model(self):
        
        if hasattr(self, 'populate_model'):
            try:
                self.populate_model.finished.disconnect(self.end_populate_model)
                try:
                    self.populate_model.output_updated.disconnect(self.update_output_box)
                except RuntimeError:
                    pass
            
                self.populate_model.deleteLater()

                self.thread_finished(self.populate_model)
            
                if self.populate_model_flag:
                    self.popup_message.done(1)
                    self.error_message.showMessage("Model Population Failed")
                else:
                    
                    self.splash_screen.accept()
            except RuntimeError:
                pass
            
          

    def collect_inputs(self):
        '''collect solver and results folder call functions from each page to load inputs'''
        #print("Pyomo Model Building")
        self.model_status_frame.show()
       # self.line_top.show()

        #Solver collected if changed
     
        #to data handler
        self.data_handler.set_solver(self.solver_select_box.currentText())
        #to optimizer - TODO - won't work if the solver requires a capital letter
        select_solver = str(self.solver_select_box.currentText().lower())
        self.optimizer.solver = select_solver

        #update results file folder location
        self.results_dir_select = self.results_file_box.currentText()
        #print("results folder")
        #print(self.results_file_box.currentText())

        #Collect inputs from other pagess
        self.planning_model_page.collect_inputs()
        self.scenario_builder_page.collect_inputs()

    def end_solve_model(self):
        '''ends the solve thread and starts processing results'''
        
        if hasattr(self, 'solve_model'):
            try:
                self.solve_model.finished.disconnect(self.end_solve_model)
                try:
                    self.solve_model.output_updated.disconnect(self.update_output_box)
                except RuntimeError:
                    pass
           
                self.solve_model.deleteLater()
                #del self.solve_model
                self.thread_finished(self.solve_model)
           
                if self.solve_model_flag:
                    self.popup_message.done(1)
                    self.error_message.showMessage("Failed to run optimization.")
                else:
                    #print('Process Results!')
                    self.process_results._args = [*self.optimizer.get_results(), self.optimizer.report,self.results_dir_select]
                    self.process_results.start()
            except RuntimeError:
                pass

            
    
    def end_process_results(self):
        '''ends the processing results thread'''
        if hasattr(self, 'process_results'):
            try:
                self.process_results.finished.disconnect(self.end_process_results)
                try:
                    self.process_results.output_updated.disconnect(self.update_output_box)
                except RuntimeError:
                    pass
           
                self.process_results.deleteLater()
                
                self.thread_finished(self.process_results)
                self.splash_screen_run.accept()

                if self.process_results_flag:
                    self.popup_message.done(1)
                    self.error_message.showMessage("Process results failed")
                else:
                    print("Collecting Results")
                    self.solved_it.emit()
                    # self.popup_message.setText("Model has solved to optimality and results have been processed. Please proceed to the Results page.")
                    # self.popup_message.setStandardButtons(QMessageBox.Ok)
                    # self.popup_message.exec()

            except RuntimeError:
                pass

   
    def thread_finished(self, thread):
        """Kills thread"""
        thread.wait()
        del thread
        

    def on_tab_opened(self, i):
        '''Tab opened - sanity check; TODO: clean up'''
        if i == 4:
            try:
                load_options = self.data_handler.load_data[self.data_handler.data_ls.index('load')].columns
            except Exception as e:
                self.error_message.showMessage("No power system data has been loaded.")
    
    
    def build_run_help(self):
        """
        Displays a help message in a pop-out window
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Build & Solve Optimization Model")
        self.popup_message.setText("Click the <b><i>Browse</i></b> button to select a Results folder to save the results. By default, a results folder will be created after an optimal solve.<br><br>"
                                   "Select a <b><i>Solver</i></b> to be used in the optimization. Note, the solver and accompanying licenses, if required, must be installed and accessible.<br><br>"
                                   "Next, click the <b><i>Build</i></b> button to build the optimization model. The status of the build will appear within the QuESt Planning window.<br><br>"
                                   "Once, the model has been successfully built. Click the <b><i>Solve</i></b> button to solve the optimization model.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()
    
