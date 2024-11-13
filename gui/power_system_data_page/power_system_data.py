# -*- coding: utf-8 -*-s
"""
Control of the Power System Data page.
"""

import os
from PySide6.QtCore import (
    QThread,
)
from PySide6.QtWidgets import (
    QMenu,
    QWidget,
    QFileDialog,
    QApplication,
    QVBoxLayout,
    QMessageBox
)
from quest_planning.gui.power_system_data_page.ui.ui_power_system_data import Ui_power_system_data
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from quest_planning.gui.tools.tools import ExecuteFunction
#from gui.matplotlibwidget import MatplotlibWidget
from quest_planning.gui.tools.tools import TabAnimator,ExecuteFunction, MatplotlibWidget, LoadingSplashScreen


class PowerSystemDataPage(QWidget, Ui_power_system_data):
    """
    The page for user to upload and select power system data.

    Loads data from excel/csv to the data handler.
    Displays system info on power system data page.
    """

    def __init__(self,tabWidget, data_handler):
        """
        Initialize the power system data page.
        Connects data reading functionality to the open file button.
        """
        super().__init__()

        self.data_handler = data_handler


        self.setupUi(self)
        self.tabWidget = tabWidget
        self.popup_message = QMessageBox()
        self.file_button.clicked.connect(self.select_file)
        self.open_file_button.clicked.connect(self.open_file_button_clicked)
        self.power_system_help_button.clicked.connect(self.display_help_message)

        self.file_button.setToolTip('Browse on computer for input data folder')
        self.open_file_button.setToolTip('Open the input data and load into QuESt Planning')

        #next and previous navigation buttons
        self.next_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.previous_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))

        self.next_button.setToolTip('Proceed to Planning Model Setup')
        self.previous_button.setToolTip('Return to Start Page')
        
        # Initially hide the power_system_data frames
        self.power_system_data_frame.hide()
        self.divider_line.hide()
        self.bus_label.hide()
        self.line_label.hide()
        self.gen_label.hide()
        self.sys_label.hide()
        self.network_map_widget.hide()
        #self.load_profile_widget.hide() 
        self.generation_mix.hide()
        self.line_bottom.hide()  
        #self.line_top.hide()  

    def display_help_message(self):
        """
        Displays a help message in a pop-out window with an OK button.
        """
        
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Upload Power System Data")
        self.popup_message.setText("Use the <b><i>Browse</i></b> button to navigate to the folder of the input data. "
        "Next, use the <b><i>Open</i></b> button to open the folder and pre-process the input data.")
        self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()

    def select_file(self):
        """Selects file directory using a QFileDialog and adds to the file_combo_box."""
        dir_select = QFileDialog.getExistingDirectory()
        self.file_combo_box.addItem(dir_select)
    

    def open_file_button_clicked(self):
        """
        Reads data from selected file.
        Threading is used from ExecuteFunction class as to not freeze the main window.
        """
        self.splash_screen = LoadingSplashScreen(self,title="Loading Data")
        self.splash_screen.show_message("Loading data, please wait...")

        dir_select = self.file_combo_box.currentText()
        self.data_handler.data_dir = dir_select
        self.read_data = ExecuteFunction(self.data_handler.get_data)
        #self.read_data.finished.connect(self.data_read)
        self.read_data.finished.connect(self.end_read_data)

        self.read_plot_data = ExecuteFunction(self.data_read_and_plot)
        self.read_plot_data.finished.connect(self.end_read_plot_data)
        self.read_data.start()
    
    def data_read_and_plot(self):
        
        #self.plot_load()
        self.plot_pie()
        self.show_map()
        self.data_read()

        # Show the power_system_data_frame when the file is opened
        self.power_system_data_frame.show()
        self.line_bottom.show()  
        #self.line_top.show() 
        self.network_map_widget.show()
        #self.load_profile_widget.show() 
        self.generation_mix.show() 
        
        self.collect_inputs()
    
    def end_read_data(self):
        self.thread_finished(self.read_data)
        self.read_plot_data.start()
        #self.splash_screen.accept()
    
    def end_read_plot_data(self):
        self.thread_finished(self.read_plot_data)
        self.splash_screen.accept()
    
    def thread_finished(self, thread):
        """Kills thread"""
        del thread

    def data_read(self):
        """
        Function to call when read_data thread is finished.
        Sets text in power system data page and deletes thread.
        """
        #Get tech numbers
        self.data_handler.get_tech_nums()
        
        self.bus_label.setText('Buses (Zones): {}'.format(len(self.data_handler.load_data[self.data_handler.data_ls.index('bus')])))
        self.line_label.setText('Branches: {}'.format(len(self.data_handler.load_data[self.data_handler.data_ls.index('branch')])))
        self.gen_label.setText('Generators: {}'.format(len(self.data_handler.tech_nums['exist'])))#self.data_handler.load_data[self.data_handler.data_ls.index('gen')])))
        self.sys_label.setText('System Name: {}'.format(self.system_name_input.text()))#self.data_handler.scalars.loc['System']['Value']))
        
        self.divider_line.show()
        self.bus_label.show()
        self.line_label.show()
        self.gen_label.show()
        self.sys_label.show()
       
        #del self.read_data
        #
        #self.data_read_and_plot()
    
    def show_map(self):
        '''Show map '''
       
        fig = self.network_map_widget.figure
        fig.clear()  # Clear existing content
        fig.tight_layout()  # Adjust layout
        fig.set_constrained_layout(True)
        ax = fig.add_subplot(111)
        
        self.data_handler.create_network_diagram(fig,ax,use_map=False)
        
        # Refresh the canvas
        self.network_map_widget.canvas.draw()
        
            
    def plot_load(self):
        '''Function to display load profile'''
        fig = self.load_profile_widget.figure
        fig.clear()  # Clear existing content
        #fig.set_constrained_layout(True)  # Enable constrained layout

        ax = fig.add_subplot(111)
        
        # Call the method to plot the load profile
        self.data_handler.plot_load_profile(fig, ax, load_forecast='system_wide')
        
        # Refresh the canvas
        self.load_profile_widget.canvas.draw()
    
    def plot_pie(self):
        '''Function to show current gen mix'''
        fig = self.generation_mix.figure
        fig.clear()  # Clear existing content
        fig.tight_layout()  # Adjust layout
        fig.set_constrained_layout(True)

        ax = fig.add_subplot(111)
        self.data_handler.current_generation_mix_piechart(fig,ax)

        # Refresh the canvas
        self.generation_mix.canvas.draw()
    
    def collect_inputs(self):
        '''collect inputs'''
        self.data_handler.set_system_name(self.system_name_input.text())
        self.data_handler.set_data_ls_index(None)

'''    
    def next_tab(self,tabWidget):
        #next and previous navigation buttons
        i = tabWidget.currentIndex()
        next_i = (i + 1) % tabWidget.count()
        tabWidget.setCurrentIndex(next_i)
         
    def prev_tab(self,tabWidget):
        i = tabWidget.currentIndex()
        prev_i = (i - 1) % tabWidget.count()
        tabWidget.setCurrentIndex(prev_i)
'''