# -*- coding: utf-8 -*-
"""
Control of the Results page
"""

import os
import traceback

from PySide6.QtCore import (
    QThreadPool,
    QUrl,
    Qt,
    QPoint,
    QTimer
)
from PySide6.QtWidgets import (
    QMenu,
    QWidget,
    QSizePolicy,
    QErrorMessage,
    QFileDialog,
    QInputDialog,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QPushButton,
    QMessageBox,
    QTableWidget, 
    QTableWidgetItem
)
from PySide6.QtGui import QDesktopServices,QFont,QColor, QPixmap, QPainter, QRegion
from quest_planning.gui.results_page.ui.ui_results import Ui_results
from quest_planning.gui.tools.tools import LoadingSplashScreen
from quest_planning.gui.results_page.drag_widget import FileBrowser, ImageGrid, WebEngineView
from quest_planning.gui.results_page.scenario_view import CSVScenarioSelector


class ResultsPage(QWidget, Ui_results):
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
        self.setupUi(self)
        self.error_message = QErrorMessage()
        self.popup_message = QMessageBox()
        self.tabWidget = tabWidget

        #Connect buttons to the corresponding actions
        self.collect_results_button.clicked.connect(self.collect_results_button_clicked)
        self.gen_plots_button.clicked.connect(self.gen_plots_button_clicked)
        self.open_results_folder_button.clicked.connect(self.on_open_results_folder_button_clicked)
        #self.open_maps_button.clicked.connect(self.open_map_button_clicked)
        self.save_results_button.clicked.connect(self.save_results_button_clicked)

        self.results_help_button.clicked.connect(self.results_help)
        self.previous_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(4))
        
        self.previous_button.setToolTip('Return to Execute Model')
        
        #Hide results windows initially
        #self.results_frame.hide()
        #self.cost_breakdown_label.hide()
        #self.results_table_1.hide()
        self.installed_capacity.hide()
        self.es_capacity.hide()
        #self.quest_planning_label.hide()
        #self.system_name_label.hide()

        #Set the systema name for informational purposes
        #self.system_name_label.setText(self.data_handler.system)

        #Connecting the png viewer
        #self.colllect_page_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.results1_page))
        self.image_grid1 = ImageGrid()
        # self.image_grid2 = ImageGrid()
        # self.image_grid3 = ImageGrid()
        self.file_browser = FileBrowser()
        self.verticalLayout_4.addWidget(self.file_browser)
        self.verticalLayout_17.addWidget(self.image_grid1)
        # self.verticalLayout_8.addWidget(self.image_grid2)
        # self.verticalLayout_9.addWidget(self.image_grid3)
        self.html_file_browser = FileBrowser()
        self.html_view1 = WebEngineView()
        # self.html_view2 = WebEngineView()
        # self.html_view3 = WebEngineView()
        self.verticalLayout_6.addWidget(self.html_file_browser)
        self.verticalLayout_3.addWidget(self.html_view1)
        # self.verticalLayout_12.addWidget(self.html_view2)
        # self.verticalLayout_13.addWidget(self.html_view3)
        self.png_toggler.clicked.connect(self.png_toggle)
        self.html_toggler.clicked.connect(self.html_toggle)
        self.png_counter = 0
        self.html_counter = 0
        self.open_results_folder_button.setChecked(True)
        self.png_browser.clicked.connect(self.png_open_file_browser)
        self.html_browser.clicked.connect(self.html_open_file_browser)
       # self.collect_splash_screen = LoadingSplashScreen(self,title = "Collecting Results")

       ## scenario viewer
        self.scenario_view_button.setEnabled(False)
        self.open_maps_button.setEnabled(False)
       # self.scenario_view_button.clicked.connect(self.scen_view)
        self.scenario_widget = CSVScenarioSelector()
        self.verticalLayout_5.addWidget(self.scenario_widget)

    def scen_view(self):
        self.stackedWidget.setCurrentWidget(self.scenario_viewer_page)

    def png_open_file_browser(self):

        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "")

        if folder_path:

            self.file_browser.setRootPath(folder_path)
   
    def html_open_file_browser(self):

        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "")

        if folder_path:

            self.html_file_browser.setRootPath(folder_path)

    def html_toggle(self):
        if self.html_counter==0:

            self.frame_7.setMinimumWidth(0)
            self.frame_7.setMaximumWidth(0)
            self.html_counter = 1
        else:
            
            self.frame_7.setMinimumWidth(230)
            self.frame_7.setMaximumWidth(230)
            self.html_counter = 0


    def png_toggle(self):
        if self.png_counter==0:

            self.frame_5.setMinimumWidth(0)
            self.frame_5.setMaximumWidth(0)
            self.png_counter = 1
        else:
            
            self.frame_5.setMinimumWidth(230)
            self.frame_5.setMaximumWidth(230)
            self.png_counter = 0

    def display_error_message(self,rd):
        if rd is None:
            self.error_message.showMessage("No solution exists")
        else:
            pass

    def plot_installed_capacity(self):
        '''Function to show installed capacity'''
        fig = self.installed_capacity.figure
        fig.clear()  # Clear existing content
        fig.tight_layout()  # Adjust layout
        fig.set_constrained_layout(True)

        ax = fig.add_subplot(111)
         
        self.results_viewer.stacked_resource_bar(fig,ax,figsize = None)
        
        # Refresh the canvas
        #self.installed_capacity.canvas.draw()

    def plot_es_installed_capacity(self):
        '''Function to show installed energy storage capacity'''
        
        fig = self.es_capacity.figure
        fig.clear()  # Clear existing content
        fig.tight_layout()  # Adjust layout
        fig.set_constrained_layout(True)

        ax = fig.add_subplot(111)
         
        self.results_viewer.plot_es_system(fig,ax,figsize = None)
        # Refresh the canvas
        #self.installed_capacity.canvas.draw()
        
    def gen_plots_button_clicked(self):
        """
            Construct the plots once the generate-plots button is clicked
        """
        if self.results_viewer.rd is None:
            self.error_message.showMessage("No solution exists")
        else:
            self.results_frame.show()

            self.installed_capacity.show()
            self.es_capacity.show()

            self.plot_installed_capacity()
            self.plot_es_installed_capacity()


    def collect_results_button_clicked(self):
        """
            Collect results and print cost results
        """
        # self.collect_splash_screen = LoadingSplashScreen(self,title = "Collecting Results")
        # self.collect_splash_screen.show_message("Processing")
        if self.results_viewer.rd is None:
            #Close splash screen
            #self.collect_splash_screen.accept()
            #self.error_message.showMessage("No solution exists")
            self.results_frame.show()
            #self.cost_breakdown_label.show()
            #self.results_table.show()
            #self.quest_planning_label.show()
            self.populate_results_table()


            
        else:
            self.results_frame.show()
            #self.cost_breakdown_label.show()
            #self.results_table.show()
            #self.quest_planning_label.show()
            #self.system_name_label.show()
            self.populate_results_table()

            #Create map and print all results to the results folder
            self.results_viewer.plot_results()
            self.results_viewer.create_map()


            #Close splash screen
            #self.collect_splash_screen.accept()

            
    def sum_costs(self,c):
        c_sum = c.sum()[0]/1e6#convert to millions
        #print(c_sum)
        return c_sum

    def populate_results_table(self):
        '''fill in results table with cost breakdown'''
        if hasattr(self, 'results_table'):
            self.results_table_layout.removeWidget(self.results_table)

        self.results_table = QTableWidget()
        # Set the number of columns to 2 (one for labels, one for values)
        self.results_table.setColumnCount(2)

        # Set the column headers
        self.results_table.setHorizontalHeaderLabels(["Cost Category", "NPV (M$)"])
        self.results_table.horizontalHeader().setStyleSheet("""
                    QHeaderView::section {
                    background-color: rgb(0, 85, 255);
                    color: white;
                    font-weight: bold;
                    font-size: 10pt;
                    border: 1px solid black;}                                                            
                                            """)

        # Set the number of rows 
        self.results_table.setRowCount(6)
        
        # Define the cost labels
        cost_labels = ["Generation Investment Costs", "Transmission Investment Costs", "Fixed O&M Costs", "Variable O&M Costs", "Fuel Costs", "Total Costs"]
        if self.results_viewer.rd is None:
            cost_values = [2000, 1500, 1200, 800, 500, 6000]  # Example values
        else:
            cost_values = [self.sum_costs(self.results_viewer.rd['annual_gen_inv_cost']),
                self.sum_costs(self.results_viewer.rd['annual_trans_inv_cost']),
                self.sum_costs(self.results_viewer.rd['annual_fom_cost']),
                self.sum_costs(self.results_viewer.rd['annual_vom_cost']),
                self.sum_costs(self.results_viewer.rd['annual_fuel_cost']),
                self.sum_costs(self.results_viewer.rd['annual_total_cost'])
                ]
        
        max_value = max(cost_values)

        # Set table properties
        self.results_table.setEditTriggers(QTableWidget.NoEditTriggers)  # Disable editing
        self.results_table.setSelectionMode(QTableWidget.NoSelection)  # Disable selection
        #self.results_table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)  # Center align column headers
        #self.results_table.verticalHeader().setDefaultAlignment(Qt.AlignCenter)  # Center align row headers
        
        self.results_table.verticalHeader().setVisible(False)  # Hide row labels

        # Bold and larger font for headers
        '''
        header_font = QFont()
        header_font.setBold(True)
        header_font.setPointSize(12)  # Adjust size as needed
        self.results_table.horizontalHeader().setFont(header_font)
        '''

        #self.results_table.horizontalHeader().setStyleSheet("border: 1px solid black;")  # Black borders for headers

        # General styling for the table
        #self.results_table.setStyleSheet("""
        #QTableWidget::item {border: 1px solid black;}  # Black borders for items
        #""")
        #QTableWidget {font-size: 12px; border: 1px solid black;}
        
        # Populate the table with cost labels and placeholder data
        for row, (label, value) in enumerate(zip(cost_labels, cost_values)):
            item_label = QTableWidgetItem(label)
            item_value = QTableWidgetItem(f"{value:,.2f}")

            # Apply heatmap color based on value
            intensity = value / max_value
            color = QColor(255 * (1 - intensity), 255, 255 * (1 - intensity))
            item_value.setBackground(color)

                        
            # Bold font for "Total Costs"
            if label == "Total Costs":
                font = QFont()
                font.setBold(True)
                font.setItalic(True)
                item_label.setFont(font)
                item_value.setFont(font)
                item_label.setBackground(QColor(169, 169, 169))  # Light gray background for total row
                item_value.setBackground(QColor(color))  # Light gray background for total row
            else:
                font = QFont()
                font.setItalic(True)
                item_label.setFont(font)
                item_label.setBackground(QColor(225, 225, 225))

            self.results_table.setItem(row, 0, item_label)
            self.results_table.setItem(row, 1, item_value)

        # Resize columns to fit content
        self.results_table.resizeColumnsToContents()


            
        self.results_table_layout.addWidget(self.results_table)
        self.save_table_as_png()
        self.on_open_results_folder_button_clicked()
        
    


    def save_table_as_png(self):
        if hasattr(self, 'results_table'):
            # Ensure the table is fully laid out and its size is correctly calculated
            self.results_table.resizeColumnsToContents()
            self.results_table.resizeRowsToContents()
            self.results_table.setFixedSize(self.results_table.horizontalHeader().length() + self.results_table.verticalHeader().width(),
                                            self.results_table.verticalHeader().length() + self.results_table.horizontalHeader().height())

            # Get the size of the table
            size = self.results_table.size()

            # Create a QPixmap with the size of the table
            pixmap = QPixmap(size)
            pixmap.fill(Qt.transparent)  # Fill the pixmap with a transparent background

            # Render the table onto the QPixmap
            painter = QPainter(pixmap)
            self.results_table.render(painter, QPoint(), QRegion(self.results_table.rect()), QWidget.RenderFlag.DrawWindowBackground | QWidget.RenderFlag.DrawChildren)
            painter.end()

            # Save the QPixmap as a PNG file
            table_dir = os.path.join(self.results_viewer.folder_path, "table.png")
            pixmap.save(table_dir)

    def on_open_results_folder_button_clicked(self):
        '''open results folder'''
        self.stackedWidget.setCurrentWidget(self.png_viewer_page)
        if self.results_viewer.rd is None:
            self.error_message.showMessage("No solution exists")
            #self.file_browser.setRootPath(r"C:\Users\ylpomer\Desktop\planning\results")    
        else:
            directory = self.results_viewer.folder_path
            if os.path.exists(directory):
                #QDesktopServices.openUrl(QUrl.fromLocalFile(directory))
                self.file_browser.setRootPath(directory)
            else:
                QMessageBox.warning(self, "Error", "The folder does not exist.", QMessageBox.StandardButton.Ok)


    def open_map_button_clicked(self):
        '''Open the map htmls'''
        self.stackedWidget.setCurrentWidget(self.html_viewer_page)
        if self.results_viewer.rd is None:
            self.error_message.showMessage("No solution exists")
            #self.html_file_browser.setRootPath(r"C:\Users\ylpomer\Desktop\planning\results")
        else:
            directory = self.results_viewer.map_folder_path
            
            if os.path.exists(directory):
                #QDesktopServices.openUrl(QUrl.fromLocalFile(directory))
                self.html_file_browser.setRootPath(directory)
            else:
                QMessageBox.warning(self, "Error", "The folder does not exist.", QMessageBox.StandardButton.Ok)


    def save_results_button_clicked(self):
        '''Save results to an excel file'''
        if self.results_viewer.rd is None:
            self.error_message.showMessage("No solution exists")
        else:
            self.results_viewer.export_results()
        
    '''Help information'''
    def results_help(self):
        """
        Displays a help message in a pop-out window
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Collect & Analyze Results")
        help_text = ("The <b>Results:</b> page provides a summary of the optimization results.<br><br> "
        "You can view the cost breakdown, generate plots, and open the results folder. <br><br>" \
        "To begin, click the <b>Open Folder</b> button to gather the results generated by the optimization model. "
        )
        '''
        help_text = (
        "Click the buttons on the <b>Results:</b> page in the following order: <br><br>"
        "<b>Collect Results:</b> Click this button to gather the results generated by the optimization model. "
        "This will compile all relevant data into a structured format for further analysis. A breakdown of the costs will be displayed in the main page.<br><br>"
        
        "<b>Generate Plots:</b> Click this button to create plots of the optimal generation mix and energy storage investments.<br><br>"
        
        "<b>Open Results Folder:</b> This button allows you to navigate to the folder where the results are saved. "
        "You can view, edit, or share the results files from this location.<br><br>"
        
        "<b>Open Maps:</b> Click this button to view any generated maps related to the optimization results. "
        "<br><br>"
        
        "<b>Save Results:</b> Use this button to save the current results to a specified location on your computer."
        )
        '''
    
        self.popup_message.setText(help_text)
        self.popup_message.exec_()
        