# -*- coding: utf-8 -*-
"""
Control of the Scenario Builder page.
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
from quest_planning.gui.scenario_builder_page.ui.ui_scenario_builder import Ui_scenario_builder
from quest_planning.gui.tools.tools import RetirementDialog, TechDialog, RPSDialog, ExecuteFunction,ScenarioInfoDialog,CandidateSelectionDialog

class ScenarioBuilderPage(QWidget, Ui_scenario_builder):
    """
        Make scenario selections, build and run the scenario.
    """

    def __init__(self,tabWidget, data_handler,power_system_data_page,planning_model_page, optimizer, results_viewer):
        """Initialize the scenario builder page."""
        super().__init__()
        #Set up the ui
        self.data_handler = data_handler
        self.optimizer = optimizer
        self.results_viewer = results_viewer
        self.planning_model_page = planning_model_page
        self.power_system_data_page = power_system_data_page
        self.power_system_data_page.collect_inputs()

        self.tabWidget = tabWidget
        self.setupUi(self)

        self.cand_tech_button.clicked.connect(self.on_cand_tech_button_clicked)
        #self.cand_energy_storage_button.clicked.connect(self.on_cand_energy_storage_button_clicked)
        self.gen_retirement_button.clicked.connect(self.on_gen_retirement_button_clicked)
        self.view_scenario_button.clicked.connect(self.on_view_scenario_button_clicked)

        self.next_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(4))
        self.previous_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.next_button.setToolTip('Proceed to Execute Model')
        self.previous_button.setToolTip('Return to Planning Model Setup')

        self.scenario_name_help_button.clicked.connect(self.scenario_name_help)
        self.capital_cost_trajectory_help_button.clicked.connect(self.capital_cost_trajectory_help)
        self.load_profile_help_button.clicked.connect(self.load_profile_help)
        self.load_growth_help_button.clicked.connect(self.load_growth_help)
        self.rps_help_button.clicked.connect(self.rps_help)
        self.trans_expansion_help_button.clicked.connect(self.trans_expansion_help)
        self.cand_technologies_help_button.clicked.connect(self.cand_technologies_help)
        self.gen_retirement_help_button.clicked.connect(self.gen_retirement_help)


        self.error_message = QErrorMessage()
        self.popup_message = QMessageBox()

        
        #self.retirements_button.clicked.connect(self.on_retirements_button_clicked)
       
        self.rps_box.activated.connect(self.on_rps_box_activated)
                
        self.load_profile_box.activated.connect(lambda:
                                                self.data_handler.set_load_profile(self.load_profile_box.currentText()))
        self.capital_cost_box.activated.connect(lambda:
                                        self.data_handler.set_capital_cost_trend(self.capital_cost_box.currentText()))
        self.transmission_box.activated.connect(lambda:
                                        self.data_handler.set_transmission_expansion(self.transmission_box.currentText()))

        #candidate technologies selections
        self.selections = 0
        self.generation_devices = {'Solar': {'Name': 'Solar', 'Capital Cost $/MW': 1166, 
                                             'Deployable Year': 2020, 'Lead Time': 1,
                                             'Candidate Capacity': 50, 'System Capacity': 0,
                                             'Ramp Rate': 0, 'PTC Credit': 26, 'ITC Credit': 0,
                                             'Capacity Credit': 0.28, 'Lifetime': 20},
                                'Wind': [], 
                                'Natural Gas': [], 
                                'Custom': []
        }
        self.energy_storage_devices = {'Lithium Ion Battery': [], 
                                       'Flow Battery': [],
                                       #'Vanadium Redox Flow Battery': [],
                                       #'Zinc Battery': [], 
                                       #'Thermal': [], 
                                       #'Gravitational': [], 
                                       #'Pumped Storage Hydro': [],
                                       #'Hydrogen': [], 
                                       #'Compressed Air': [], 
                                       'Custom': []
        }
        self.rps = None
        self.rps_schedules = {}#self.data_handler.load_data[self.data_handler.data_ls.index('policy')]['RPS'].loc[self.data_handler.load_data[self.data_handler.data_ls.index('policy')]['Years'] in self.data_handler.years]
        
        self.devices = {}
        self.scenario_name = self.scenario_name_box.text()
        self.data_handler.set_scenario(self.scenario_name)

        #Set annual load growth if selected
        self.data_handler.set_load_growth(self.annual_load_growth_box.text())

        self.retirement_frame.hide()
        self.cand_tech_frame.hide()

        #TODO 
        #self.tech_frame_layout.addWidget(self.add_selection_frame())
        #self.tech_frame_layout.addStretch()

        self.update()

        self.retirements_print = None

    def on_cand_tech_button_clicked(self):
        '''function for when candidate generation button is clicked'''
        tech = self.data_handler.load_data[self.data_handler.data_ls.index('tech')]
        #only consider candidates that the user wants eligible by filtering by CandCap
        cand_tech = tech.loc[tech['CandCap'] > 0]#passes a dataframe
        dialog = CandidateSelectionDialog(self,cand_tech = cand_tech,data_handler = self.data_handler)#cand_tech = self.data_handler.tech_categories['candidates'])
        if dialog.exec():
            selectedTechs = dialog.selectedTechnologies()
            
            # Display candidate techs in bulleted list
            heading = "<b><u>Selected Candidate Technologies:</u></b><br>"

            formattedTechs = heading+'<br>'.join([f"• {tech}" for tech in selectedTechs])
            self.candidate_tech_box.setHtml(formattedTechs)
            self.cand_tech_frame.show()
        else:
            self.candidate_tech_box.setText('No technology selected')

    
    def on_gen_retirement_button_clicked(self):
        '''function for when genration retirement button is clicked'''
        try:
            dialog = RetirementDialog(generators=self.data_handler.load_data[self.data_handler.data_ls.index('gen')], years=self.data_handler.years)

            if dialog.exec():
                #Clear the box in case of repeat click
                self.retirement_box.clear()

                self.data_handler.set_retirements(dialog.retirements)
                #print('Retirements Set')
                heading = "<b><u>Selected Retirement Schedule:</u></b><br>"
                self.retirement_box.setHtml(heading + dialog.message)
                #full_message = dialog.message if hasattr(dialog, 'message') else ""
                if dialog.retirements:
                    # Show retirements in QTextEdit box
                    retirement_text = "\n".join([f"{gen}: {year}" for gen, year in dialog.retirements.items()])
                    #full_message += "\n" + retirement_text if full_message else retirement_text

                    self.retirement_box.append(retirement_text)#str(dialog.retirements))

                #show retirements text edit box
                self.retirement_frame.show()

                self.retirements_print = dialog.retirements
        except Exception as e:
            print(e)
            self.error_message.showMessage("No power system data has been loaded.")
    
    def on_rps_box_activated(self):
        self.rps = self.rps_box.currentText()
        
        try:
            if self.rps == 'Create New...':
                dialog = RPSDialog(years = self.data_handler.years)
                
                if dialog.exec():
                    #self.rps_schedules[str(self.rps_box.count())] = dialog.rps_schedule
                    self.rps_schedules = dialog.rps_schedule
                    self.rps_box.addItem(str(self.rps_box.count()))
                    self.data_handler.set_rps_schedule(self.rps_schedules,option = self.rps)
            elif self.rps == 'Default':
                '''use default csv data-no action needed'''
                #print('Default RPS Policy')
                policy_data = self.data_handler.load_data[self.data_handler.data_ls.index('policy')]
                
                self.rps_schedules = policy_data['RPS'][policy_data['Years'].isin(self.data_handler.years)]
                #print(self.rps_schedules)
                self.data_handler.set_rps_schedule(self.rps_schedules,option = self.rps)
            else:#The user does nothing
                '''use default csv data-no action needed'''
                #print('yes')
                #print(self.rps_schedules)
                #self.rps_schedules = self.data_handler.load_data[self.data_handler.data_ls.index('policy')]['RPS'].loc[self.data_handler.load_data[self.data_handler.data_ls.index('policy')]['Years'] in self.data_handler.years]
                #rps_schedule = self.rps_schedules[self.rps_box.currentText()]
                policy_data = self.data_handler.load_data[self.data_handler.data_ls.index('policy')]
                self.rps_schedules = policy_data['RPS'][policy_data['Years'].isin(self.data_handler.years)]

                self.data_handler.set_rps_schedule(self.rps_schedules,option = None)

        except Exception as e:
            print(e)
            self.error_message.showMessage("Failed to set Future Generation Mix Schedule")

        #print(self.rps_schedules)
    def on_tab_opened(self, i):
        self.data_handler.set_load_profile(self.load_profile_box.currentText())
        self.data_handler.set_capital_cost_trend(self.capital_cost_box.currentText())

        

        if self.transmission_box.currentText() =="No":
            tx_flag = False
        else:
            tx_flag = True
        self.data_handler.set_transmission_expansion(tx_flag)#self.transmission_box.currentText())
        
        message = 'Warning:'
        show_warning = False

        if i == 3:
            try:
                #load_options = self.data_handler.load_data
                load_options = self.data_handler.load_data[self.data_handler.data_ls.index('load')].columns
                load_options = [x for x in load_options if x not in ['Company', 'datetime', 'year', 'month', 'day1', 'day', 'hour']]
                self.load_profile_box.addItems(load_options)
                if not load_options or load_options is None:
                    message += "\nNo power system data has been loaded."
                    show_warning = True
            except (AttributeError, IndexError):
                message += "\nNo power system data has been loaded."
                show_warning = True

            try:
                years = self.data_handler.years
                if not years or years is None:
                    message += "\nSimulation years have not been defined. Return to Planning Model Setup."
                    show_warning = True
            except AttributeError:
                message += "\nSimulation years have not been defined. Return to Planning Model Setup."
                show_warning = True

            try:
                #set default RPS schedule at beginning
                policy_data = self.data_handler.load_data[self.data_handler.data_ls.index('policy')]
                        
                self.rps_schedules = policy_data['RPS'][policy_data['Years'].isin(self.data_handler.years)]
                if self.rps_schedules is None or self.rps_schedules.empty:
                    message += "\nYears have not been defined. Check the default input data."
                    show_warning = True
                #print(self.rps_schedules)
            except AttributeError:
                message += "\nYears have not been defined. Check the default input data."
                show_warning = True

            if show_warning:
                self.error_message.showMessage(message)
        
            #try:
                #load_options = self.data_handler.load_data[self.data_handler.data_ls.index('load')].columns
                #load_options = [x for x in load_options if x not in ['Company', 'datetime', 'year', 'month', 'day1', 'day', 'hour']]
               # self.load_profile_box.addItems(load_options)
            #except Exception as e:
                #print(e)
               # self.error_message.showMessage("No power system data has been loaded.")
        
    
    def collect_inputs(self):
        '''Called before build and solve'''
        #Set Future generation mix
        self.on_rps_box_activated()
        #Set load forecast
        self.data_handler.set_load_profile(self.load_profile_box.currentText())
        #Set annual load growth if selected
        self.data_handler.set_load_growth(self.annual_load_growth_box.text())
        #Set capital cost trend
        self.data_handler.set_capital_cost_trend(self.capital_cost_box.currentText())
        #Set transmission expansion option - pass boolean
        if self.transmission_box.currentText() =="No":
            tx_flag = False
        else:
            tx_flag = True
        self.data_handler.set_transmission_expansion(tx_flag)
        #Set scenario name
        self.scenario_name = self.scenario_name_box.text()
        self.data_handler.set_scenario(self.scenario_name)

    def on_view_scenario_button_clicked(self):
        '''open scenario build information in separate window'''

        #Collect inputs from planning_model_page
        self.planning_model_page.collect_inputs()

        planning_model_info = {
            "Simulation Years": self.planning_model_page.years,
            "Transmission Model": self.planning_model_page.transmission_box.currentText(),
            "Temporal Selection": self.planning_model_page.temporal_box.currentText(),
            "Discount Factor": self.planning_model_page.annual_discount_factor.text(),
            "Base Currency Year": self.planning_model_page.base_currency_year.text()
        }

        scenario_info = {
            "Scenario Name": self.scenario_name_box.text(),
            "Resource Capital Costs": self.capital_cost_box.currentText(),
            "Load Forecasts": self.load_profile_box.currentText(),
            "Annual Load Growth": self.annual_load_growth_box.text(),
            "Renewable Portfolio Standards": self.rps_schedules,
            "Transmission Expansion": self.transmission_box.currentText(),
            "Candidate Technologies": self.candidate_tech_box.toPlainText(),
            "Retirement Schedule": self.retirements_print#self.retirement_box.toPlainText()
        }
            
        dialog = ScenarioInfoDialog(self, scenario_info,planning_model_info,system_name = self.data_handler.system)
        dialog.exec_()

    '''Help button information'''

    def scenario_name_help(self):
        """
        Displays a help message in a pop-out window 
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Scenario Name")
        self.popup_message.setText("Select a <b><i>Scenario Name</i></b>. This scenario should be unique as it will be used to save print results.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()
    
    def capital_cost_trajectory_help(self):
        """
        Displays a help message in a pop-out window 
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Capital Costs")
        self.popup_message.setText("Select the capital cost trajectory for energy storage technologies. The cost trajectories are low, mid, and high. These trajectories are defined in the input csv data.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()

    def load_profile_help(self):
        """
        Displays a help message in a pop-out window 
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Load Forecasts")
        self.popup_message.setText("Select the load forecasts for the scenario. The load forecasts are defined in the csv data.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()
    
    def load_growth_help(self):
        """
        Displays a help message in a pop-out window 
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Annual Load Growth")
        self.popup_message.setText("Select the annual load growth for the scenario. The annual load growth is defines a percentage (%). NOTE: the annual load growth parameter is only defined when only one year of load data is provided.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()

    def rps_help(self):
        """
        Displays a help message in a pop-out window
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Renewable Portfolio Standard Goals")
        self.popup_message.setText("Select the Future Generation Mix to be used in the scenario. The Future Generation Mix schedule can be defined in the csv data. Alternatively, you can select <b><i>Custom</i></b> option to define custom RPS targets.<br>"
                                   "You can also select to enforce CO2 emisison reduction and CO2 intensity reduction targets. These targets must be defined in the csv data.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()
    
    def trans_expansion_help(self):
        """
        Displays a help message in a pop-out window 
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Select Transmission Expansion Option")
        self.popup_message.setText("Transmission expansion is a feature that will be added in a later release of QuESt Planning.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()

    def cand_technologies_help(self):
        """
        Displays a help message in a pop-out window 
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Candidate Technologies Selection")
        self.popup_message.setText("Click the <b><i>Candidate Technologies</i></b> button to select the candidate technologies to be considered in the QuESt Planning optimization.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()
    
    def gen_retirement_help(self):
        """
        Displays a help message in a pop-out window 
        """
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Generation Retirements Selection")
        self.popup_message.setText("Click the <b><i>Retirement Schedule</i></b> to select the retirement schedule to be enforced in the QuESt Planning optimization.The <b><i>Default</i></b> option is the retirement schedule detailed in the csv data.")
        #self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()


'''
        try:
            self.rps = self.rps_box.currentText()
            
            if self.rps == None or self.rps == 'Default RPS Policy':
                print(self.rps)
                self.rps_schedules = self.data_handler.load_data[self.data_handler.data_ls.index('policy')]['RPS'].loc[self.data_handler.load_data[self.data_handler.data_ls.index('policy')]['Years'] in self.data_handler.years]
                print(self.rps_schedules)
            else:
                pass
        except:
            self.rps_schedules = {'RPS':'No power system data loaded'}
'''

