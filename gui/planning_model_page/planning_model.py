# -*- coding: utf-8 -*-
"""
Control of the Planning Model page.
"""

import os
from PySide6.QtCore import (
    QThreadPool,
)
from PySide6.QtWidgets import (
    QMenu,
    QWidget,
    QErrorMessage,
    QRadioButton,
    QButtonGroup,
    QMessageBox
)
from quest_planning.gui.planning_model_page.ui.ui_planning_model import Ui_planning_model
from quest_planning.gui.tools.tools import YearRadioButton, YearOptionsDialog,AdvancedPlanningSettingsDialog

class PlanningModelPage(QWidget, Ui_planning_model):
    """
    The Planning Model Page.

    User input of various scalar values for the planning model. 
    Also takes in the starting and ending years.
    """

    def __init__(self,tabWidget, data_handler):
        """Initialize the planning model page."""
        super().__init__()

        self.data_handler = data_handler
        self.tabWidget = tabWidget
        self.setupUi(self)
        self.error_message = QErrorMessage()
        self.popup_message = QMessageBox()
        
        #self.year_gap_box.valueChanged.connect(self.on_year_gap_box_activated)
        
        self.next_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3))
        self.previous_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))

        self.next_button.setToolTip('Proceed to Scenario Builder')
        self.previous_button.setToolTip('Return to Power System Data')
        
        self.select_years_button.clicked.connect(self.on_year_box_activated)#the user has to select years
        self.advanced_settings_button.clicked.connect(self.on_advanced_settings_button_clicked)

        self.select_simulation_years_help_button.clicked.connect(self.select_simulation_years_help)
        self.transmission_model_help_button.clicked.connect(self.transmission_model_help)
        self.temporal_selection_help_button.clicked.connect(self.temporal_selection_help)
        self.discount_rate_help_button.clicked.connect(self.discount_rate_help)
        self.base_currency_help_button.clicked.connect(self.base_currency_help)
        self.base_currency_help_button.clicked.connect(self.base_currency_help)
        
    
        self.years = None
        
        self.transmission_box.currentTextChanged.connect(lambda: self.data_handler.set_tx_model(self.transmission_box.currentText()))
        self.trans_model_label.setText(self.transmission_box.currentText())

        temporal_selection = self.temporal_box.currentText()
        
        # Determine the block selection based on the temporal selection
        block_selection_map = {
            'Peak Day': 'Peak_day',
            'Full Year': 'Full_Year',
            'Full Year MY': 'Full_Year_MY',
            'Representative Weeks': 'Repr_Weeks',
            'Seasonal Blocks': 'Seasonal_blocks'
        }
        
        self.block_selection = block_selection_map.get(temporal_selection, None)
            
        #self.temporal_box.currentTextChanged.connect(lambda: self.data_handler.set_block_selection(block_selection))
        self.data_handler.set_block_selection(self.block_selection)
        self.temporal_selection_label.setText(temporal_selection)
        
        # Initialize a variable to keep track of the last temporal selection
        self.last_temporal_selection = None
        
        # Connect the temporal_box's currentTextChanged signal to the on_temporal_selection_changed functions
        self.temporal_box.currentTextChanged.connect(self.on_temporal_selection_changed)
        
        # Should work when text is changed
        self.annual_discount_factor.valueChanged.connect(lambda: self.data_handler.set_discount_rate(float(self.annual_discount_factor.text())))
        self.base_currency_year.textChanged.connect(lambda: self.data_handler.set_base_currency_year(float(self.base_currency_year.text())))
        
        #not working
        #self.transmission_box.currentTextChanged.connect(self.trans_model_label.setText(self.transmission_box.currentText()))
        #self.temporal_box.currentTextChanged.connect(self.temporal_selection_label.setText(self.temporal_box.currentText()))
        
        self.planning_model_info_frame.hide()

        #TODO: for now set in backend
        self.data_handler.set_reserves_option(True)
        self.data_handler.set_tax_credits_option(False)
        self.data_handler.set_es_lifetime_cost_option(False)

        self.changed_values = None
        
    def on_year_gap_box_activated(self):
        '''NOT USED'''
        #self.data_handler.set_year_gap(self.year_gap_box.value())
        self.data_handler.set_years_hours()

    def on_temporal_selection_changed(self):
        """
        Function to handle changes in the temporal selection.
        """
        temporal_selection = self.temporal_box.currentText()
        
        # Determine the block selection based on the temporal selection
        block_selection_map = {
            'Peak Day': 'Peak_day',
            'Full Year': 'Full_Year',
            'Full Year MY': 'Full_Year_MY',
            'Representative Weeks': 'Repr_Weeks',
            'Seasonal Blocks': 'Seasonal_blocks'
        }
        self.block_selection = block_selection_map.get(temporal_selection, None)
        
        # Update the block selection in the data handler
        if self.block_selection:
            self.data_handler.set_block_selection(self.block_selection)
            self.temporal_selection_label.setText(temporal_selection)
        
        # Check if the temporal selection has changed from the last recorded one
        if temporal_selection != self.last_temporal_selection:
            print(f"Temporal selection changed to: {temporal_selection}")
          
            # Update the last temporal selection
            self.last_temporal_selection = temporal_selection
        #else:
            #print("Temporal selection remains unchanged.") 
        
        self.planning_model_info_frame.show()
            
    def on_year_box_activated(self):
        
        years = range(self.begin_date.date().year(),self.end_date.date().year()+1)
        try:
         
            dialog = YearOptionsDialog(years = years)
            
            if dialog.exec():
                self.years = dialog.get_selected_years()
                str_years = [str(item) for item in self.years]
                str_years = ', '.join(str_years)
                self.sim_years_label.setText(str_years)
                #add years to data_handler
                self.data_handler.years = self.years
                #set year gap
                self.data_handler.set_years_hours(self.years)
            
            
        except Exception as e:
            print(e)
            self.error_message.showMessage("Please select the time horizon of the scenario.")
        
        self.planning_model_info_frame.show()
    
    def on_advanced_settings_button_clicked(self):
        #TODO: fix if re-opened
        settings = {"Planning Reserve Margin:":20,#self.data_handler.prm, 
                  "Regulating Reserve Requirement:": 1.0,#self.data_handler.reg_res_req,
                  "Spinning Reserve Requirement:": 3,#self.data_handler.spin_res_req,
                  "Flexibility Reserve Requirement (solar):": 10,#self.data_handler.flex_res_s_req,
                  "Flexibility Reserve Requirement (wind):": 4,#self.data_handler.flex_res_w_req,
                  "System-wide Wind Maximum Investment:": "Default",
                  "System-wide Solar Maximum Investment:": "Default",
                  "System-wide Gas Maximum Investment:": "Default",
                  "System-wide Transmission Maximum Investment:": "Default",
                  "Tax Credits Option:":False,#self.data_handler.tax_credits_option,
                  "Tax Credits End Year:":2032,#self.data_handler.tax_credit_end_year,
                  "End Effects:":10}#self.data_handler.end_effects}

        dialog = AdvancedPlanningSettingsDialog(settings)
        
        if dialog.exec():
            # dictionary of changed values
            self.changed_values = dialog.get_values()
                        
        else:
            self.changed_values = None


    def on_tab_opened(self, i):
        message = 'Warning'
        if i == 2:
            try:
                load_options = self.data_handler.load_data[self.data_handler.data_ls.index('load')].columns
                message +=  "\nNo power system data has been loaded."
            
            except:
                self.error_message.showMessage("No power system data has been loaded.")
    
    def collect_inputs(self):
        """Send all inputs to data handler"""
        if not self.years == None:
            self.data_handler.years = self.years
        else:
            #just assume all years will be simulated
            self.data_handler.years = [year for year in range(self.begin_date.date().year(),self.end_date.date().year()+1)]
        
        #Update data handler
        if not self.changed_values == None:
            self.data_handler.set_reserve_params(self.changed_values["Planning Reserve Margin:"],
                                                 self.changed_values["Regulating Reserve Requirement:"],
                                                 self.changed_values["Spinning Reserve Requirement:"],
                                                 self.changed_values["Flexibility Reserve Requirement (solar):"],
                                                 self.changed_values["Flexibility Reserve Requirement (wind):"])
            self.data_handler.set_system_wide_wind_max(self.changed_values["System-wide Wind Maximum Investment:"])
            self.data_handler.set_system_wide_solar_max(self.changed_values["System-wide Solar Maximum Investment:"])
            self.data_handler.set_system_wide_gas_max(self.changed_values["System-wide Gas Maximum Investment:"])
            self.data_handler.set_system_wide_tx_expansion_max(self.changed_values["System-wide Transmission Maximum Investment:"])
            self.data_handler.set_tax_credits_option(self.changed_values["Tax Credits Option:"])
            self.data_handler.set_tax_credit_end_year(self.changed_values["Tax Credits End Year:"])
            self.data_handler.set_end_effects(self.changed_values["End Effects:"])
        else:
            pass
        
        #self.data_handler.years = [year for year in self.years]#range(self.begin_date.date().year(),self.end_date.date().year()+1)]

        self.data_handler.set_discount_rate(float(self.annual_discount_factor.text()))
        self.data_handler.set_base_currency_year(float(self.base_currency_year.text()))
        self.data_handler.set_tx_model(self.transmission_box.currentText())
        self.data_handler.set_block_selection(self.block_selection)
        #self.on_temporal_selection_changed()

    #Help button functionalities
    def select_simulation_years_help(self):
        """
        Displays a help message in a pop-out window 
        """
        
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Simulation Years")
        self.popup_message.setText("Select the simulation years to be modeled within the QuESt Planning optimization model. Use caution when selecting simulation years, "
                                   "as choosing too many years can lead to increased computational complexity. Select the start and end year of the planning horizon. Once chosen, press the "
                                   "<b><i>Select Simulation Years</i></b> button to navigate to select the intermediate simulation years.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()

    def transmission_model_help(self):
        """
        Displays a help message in a pop-out window 
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Transmission Model")
        self.popup_message.setText("Use the drop down menu to select the transmission model to be modeled within the QuESt Planning optimization model. Currently, QuESt Planning supports the copperplate and transportation model. D.C. power flow constraints are under development.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()
    
    def temporal_selection_help(self):
        """
        Displays a help message in a pop-out window 
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Temporal Resolution")
        self.popup_message.setText("Use the drop down menu to select the temporal resolution to be modeled within the QuESt Planning optimization model. Currently, QuESt Planning supports load blocks and representative weeks. A full year 8760 hourly analysis is under development.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()
    
    def discount_rate_help(self):
        """
        Displays a help message in a pop-out window 
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Discount Rate")
        help_text = (
        "Select an annual discount rate to be used to make the net-present value calculation in the optimization model.<br><br>"
        "The discount factor can be calculated using the formula:<br>"
        "<b>Discount Factor = 1 / (1 + r)^n</b><br>"
        "where:<br>"
        "<b>r</b> = annual discount rate (as a decimal)<br>"
        "<b>n</b> = number of years<br><br>"
        "For example, if the discount rate is 5% (0.05) and the number of years is 10, the discount factor would be:<br>"
        "<b>Discount Factor = 1 / (1 + 0.05)^10 ≈ 0.6139</b>"
        )
    
        self.popup_message.setText(help_text)
        #self.popup_message.setText("Select an annual discount rate to be used to make the net-present value calculation in the optimization model.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()

    def base_currency_help(self):
        """
        Displays a help message in a pop-out window
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Base Currency Year")
        self.popup_message.setText("Select the base currency year where the discount factor calculation is based.")
        self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()
    
    def advanced_settings_help(self):
        """
        Displays a help message in a pop-out window
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Base Currency Year")
        self.popup_message.setText("Select the base currency year where the discount factor calculation is based.")
        self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()


# Connect the dateChanged signal of the QDateEdit to a slot

#self.begin_date.dateChanged.connect(self.update_radio_buttons)
#self.end_date.dateChanged.connect(self.update_radio_buttons)

# Call the slot to initially populate the radio buttons

#self.update_radio_buttons()

# Connect the input boxes/edits to the data_handler
# self.begin_date.dateChanged.connect(lambda: 
#                                     self.data_handler.set_start_year(self.begin_date.date().year()))
# self.end_date.dateChanged.connect(lambda:
#                                   self.data_handler.set_end_year(self.end_date.date().year()))
# self.annual_discount_factor.valueChanged.connect(lambda:
#                                                  self.data_handler.set_scalar('Discount Rate', self.annual_discount_factor.value()))
# self.end_effects.valueChanged.connect(lambda:
#                                       self.data_handler.set_scalar('end_effects', self.end_effects.value()))
# self.prm.valueChanged.connect(lambda: 
#                               self.data_handler.set_scalar('PRM', self.prm.value()))
# self.reg_reserve.valueChanged.connect(lambda:
#                                       self.data_handler.set_scalar('Reg_Res_Req', self.reg_reserve.value()))
# self.spin_reserve.valueChanged.connect(lambda:
#                                        self.data_handler.set_scalar('Spin_Res_Req', self.spin_reserve.value()))
# self.flexible_reserve.valueChanged.connect(lambda:
#                                            self.data_handler.set_scalar('Flex_Res_Req', self.flexible_reserve.value()))

# self.transmission_box.activated.connect(lambda:
#                                         self.data_handler.set_tx_model(self.transmission_box.currentText()))

# self.temporal_box.activated.connect(lambda:
#                                     self.data_handler.set_block_selection(self.temporal_box.currentText()))
'''
def update_radio_buttons(self):
    # Clear existing radio buttons

    for i in reversed(range(self.year_button_layout.count())):
        widget = self.year_button_layout.itemAt(i).widget()
        self.year_button_layout.removeWidget(widget)
        widget.setParent(None)

    # Get the selected year from the QDateEdit

    start_year = self.begin_date.date().year()
    end_year = self.end_date.date().year()

    # Create radio buttons for each year
    # Create a button group

    button_group = QButtonGroup()
    
    for year in range(start_year, end_year):
        radio_button = YearRadioButton(year)
        #radio_button.setChecked(year == selected_year)
        self.year_button_layout.addWidget(radio_button)
        button_group.addButton(radio_button)
        button_group.setId(radio_button, year)

  if i==2:
            #self.data_handler.set_start_year(self.begin_date.date().year())
            #self.data_handler.set_end_year(self.end_date.date().year())
            self.data_handler.set_discount_rate(float(self.annual_discount_factor.text()))
            self.data_handler.set_base_currency_year(float(self.base_currency_year.text()))
            #self.data_handler.set_scalar('Discount Rate', self.annual_discount_factor.value())
            #self.data_handler.set_scalar('Base Currency Year', self.base_currency_year.value())
            #self.data_handler.set_scalar('end_effects', self.end_effects.value())
            #self.data_handler.set_scalar('PRM', self.prm.value())
            #self.data_handler.set_scalar('Reg_Res_Req', self.reg_reserve.value())
            #self.data_handler.set_scalar('Spin_Res_Req', self.spin_reserve.value())
            #self.data_handler.set_scalar('Flex_Res_Req', self.flexible_reserve.value())
            self.data_handler.set_tx_model(self.transmission_box.currentText())
    
            temporal_selection = self.temporal_box.currentText()
    
            if temporal_selection == 'Peak Day':
                block_selection = 'Peak_day'
            elif temporal_selection == 'Full Year':
                block_selection = 'Full_Year'
            elif temporal_selection == 'Full Year MY':
                block_selection = 'Full_Year_MY'
            elif temporal_selection == 'Representative Weeks':
                block_selection = 'Repr_Weeks'
            elif temporal_selection == 'Seasonal Blocks':
                block_selection = 'Seasonal_blocks'
    
            self.data_handler.set_block_selection(block_selection)
'''