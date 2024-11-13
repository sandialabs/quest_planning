# -*- coding: utf-8 -*-
"""
Tools for various items in the Quest Planning tool. 
"""

from PySide6.QtWidgets import (QApplication, 
                               QLineEdit, 
                               QDialogButtonBox, 
                               QFormLayout, 
                               QDialog, 
                               QComboBox, 
                               QPushButton,
                               QGraphicsView,
                               QRadioButton,
                               QVBoxLayout,
                               QCheckBox,
                               QGridLayout,
                               QHBoxLayout,
                               QWidget,
                               QLabel,
                               QListWidget,
                               QDialogButtonBox,
                               QListWidgetItem,
                               QFrame,
                               QFileDialog,
                               QSpacerItem,
                               QSizePolicy,
                               QErrorMessage,
                               QProgressBar,
                               QTextEdit,
                               QInputDialog,
                               QScrollArea
                               )
from PySide6.QtCore import (
    QThread,QPropertyAnimation, QEasingCurve,Qt, Signal, Slot
)
from PySide6.QtGui import QFont

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from typing import List
import pandas as pd
import math
import traceback
import sys
from typing import Dict, Union

class AdvancedPlanningSettingsDialog(QDialog):
    """
    Dialog to specify advanced settings for the planning model
    """
    def __init__(self, settings: Dict[str, str], parent=None):
        super().__init__(parent)
        
        self.resize(400,300)

        self.setWindowTitle("Advanced Planning Model Settings")
        
         # Dictionary to hold the QTextEdit widgets
        self.text_edits = {}
        
        # Create the main layout
        main_layout = QVBoxLayout()
        
        # Create a title label and set it to bold and centered
        title_label = QLabel("Configure advanced settings in QuESt Planning")
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(14)  # Adjust the font size as needed
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        
        # Add the title label to the main layout
        main_layout.addWidget(title_label)

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        # Create a widget to hold the settings
        settings_widget = QWidget()
        settings_layout = QFormLayout(settings_widget)
        
        # Create a layout for each label and text edit pair
        for label_text, default_value in settings.items():
            #row_layout = QHBoxLayout()
            
            # Create the label and set it to bold
            label = QLabel(label_text)
            font = QFont()
            font.setBold(True)
            label.setFont(font)
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            
            # Create the line edit and set the default value
            line_edit = QLineEdit()
            line_edit.setText(str(default_value))
            
            # Store the label and line edit as a tuple in the list
            self.text_edits[label_text] = line_edit
            
            # Add the label and line edit to the form layout
            settings_layout.addRow(label, line_edit)
        
        # Set the settings widget as the scroll area's widget
        scroll_area.setWidget(settings_widget)
        
        # Add the scroll area to the main layout
        main_layout.addWidget(scroll_area)
        
        # Add standard dialog buttons (OK and Cancel)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        
        main_layout.addWidget(button_box)
        
        # Set the main layout for the dialog
        self.setLayout(main_layout)
    
    def get_values(self) -> Dict[str, str]:
        """
        Retrieve the current values from the text edit boxes.
        """
        return {label: self.convert_value(text_edit.text()) for label, text_edit in self.text_edits.items()}

    @staticmethod
    def convert_value(value: str) -> Union[str, bool,float]:
        """
        Convert string values to appropriate types.
        """
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        try:
            return float(value)
        except ValueError:
            return value

class TechDialog(QDialog):
    """
    Dialog to create a new technology. 

    Takes a list of labels for the inputs as an argument.
    The dialog has a form layout with labels and line edits to take 
    inputs for the various technology characteristics.
    """
    def __init__(self, labels:List[str], parent=None):
        super().__init__(parent)
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QFormLayout(self)
        
        self.inputs = []
        for lab in labels:
            self.inputs.append(QLineEdit(self))
            layout.addRow(lab, self.inputs[-1])
        
        layout.addWidget(buttonBox)
        
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
    
    def getInputs(self):
        return tuple(input.text() for input in self.inputs)

class RetirementDialog(QDialog):
    """
    Dialog to set retirement dates for generators.

    Takes a pandas dataframe with a column that contains the generator
    names and a list of the years in the optimization as arguments.
    """
    def __init__(self, generators:pd.DataFrame, years:List[int], parent=None):
        super().__init__(parent)

        self.resize(300,400)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        formWidget = QWidget()
        formlayout = QFormLayout(formWidget)

        self.retirements = {}

        self.layout = QVBoxLayout(self)  # Use QVBoxLayout as the main layout

        # Create radio buttons for retirement options
        self.defaultRetirementRadio = QRadioButton("Use default retirements")
        self.customTechRetirementRadio = QRadioButton("Set custom retirement by technology")
        self.customRetirementRadio = QRadioButton("Set custom retirements by generator")
        self.defaultRetirementRadio.setChecked(True)  # Set default retirement as the default option
        self.message = 'Default generation retirement schedule'

        # Add radio buttons to the layout
        self.layout.addWidget(self.defaultRetirementRadio)
        # Add the custom technology retirement radio button
        self.layout.addWidget(self.customTechRetirementRadio)

        # Create a layout for custom technology retirements
        customTechRetirementLayout = QHBoxLayout()
        self.tech_retirement_qboxes = {}
        technologies = ["Natural Gas", "Coal", "Nuclear", "Oil"]
        for tech in technologies:
            label = QLabel(f"{tech}:")
            combo_box = QComboBox(self, objectName=f"{tech.lower().replace(' ', '_')}_qbox")
            combo_box.addItem("Default")
            combo_box.addItems([str(year) for year in years])
            combo_box.adjustSize()
            combo_box.setEnabled(False)
            self.tech_retirement_qboxes[tech] = combo_box
            customTechRetirementLayout.addWidget(label)
            customTechRetirementLayout.addWidget(combo_box)

        self.layout.addLayout(customTechRetirementLayout)

        self.layout.addWidget(self.customRetirementRadio)

         # Create a layout for custom retirements
        customRetirementLayout = QHBoxLayout()
        self.retirements_qbox = QComboBox(self, objectName="retirements_box")
        self.retirements_qbox.addItems(generators['Gen_name'])

        self.years_qbox = QComboBox(self, objectName="years_qbox")
        self.years_qbox.addItems([str(year) for year in years])
        self.years_qbox.adjustSize()

        self.set_button = QPushButton("Set", self, objectName="set_button")
        self.set_button.clicked.connect(self._set_button_clicked)

        # Initially disable the widgets until customRetirementRadio is selected
        self.retirements_qbox.setEnabled(False)
        self.years_qbox.setEnabled(False)
        self.set_button.setEnabled(False)

        customRetirementLayout.addWidget(QLabel("Generator: "))
        customRetirementLayout.addWidget(self.retirements_qbox)
        customRetirementLayout.addWidget(QLabel("Year: "))
        customRetirementLayout.addWidget(self.years_qbox)
        customRetirementLayout.addWidget(self.set_button)
        #self.layout.addRow(buttonBox)

        self.layout.addLayout(customRetirementLayout)

        self.layout.addWidget(formWidget)  # Add the form layout to the main layout

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(buttonBox)

        # Connect the toggled signal of customRetirementRadio to a slot method
        self.customRetirementRadio.toggled.connect(self.onCustomRetirementToggled)

        # Connect the toggled signal of defaultRetirementRadio to a slot method
        self.defaultRetirementRadio.toggled.connect(self.onDefaultRetirementToggled)

        # Connect the toggled signal of customTechRetirementRadio to a slot method
        self.customTechRetirementRadio.toggled.connect(self.onCustomTechRetirementToggled)
    
    def _set_button_clicked(self):
        """Saves retirement years to a dictionary."""
        generator = self.retirements_qbox.currentText()
        year = self.years_qbox.currentText()

        self.retirements_qbox.setCurrentIndex(0)
        self.years_qbox.setCurrentIndex(0)

        if self.customRetirementRadio.isChecked():
            self.retirements[generator] = year
        elif self.customTechRetirementRadio.isChecked():
            for tech, combo_box in self.tech_retirement_edits.items():
                years = combo_box.toPlainText().split()
                self.retirements[tech] = years
    
    def onCustomRetirementToggled(self, checked):
        """Enable or disable widgets based on the customRetirementRadio state."""
        self.retirements_qbox.setEnabled(checked)
        self.years_qbox.setEnabled(checked)
        self.set_button.setEnabled(checked)
        self.message = 'Custom Retirement Schedule:'

    def onDefaultRetirementToggled(self, checked):
        """Print default statement"""
        #print('made it')
        self.message = 'Default generation retirement schedule'
    
    def onCustomTechRetirementToggled(self, checked):
        """Enable or disable widgets based on the customTechRetirementRadio state."""
        self.retirements_qbox.setEnabled(False)
        self.years_qbox.setEnabled(False)
        self.set_button.setEnabled(checked)
        for combo_box in self.tech_retirement_edits.values():
            combo_box.setEnabled(checked)
        self.message = 'Custom Retirement by Technology Schedule:'

class CandidateSelectionDialog(QDialog):
        '''Dialog to select candidate technologies'''
        def __init__(self, parent=None,cand_tech=None,data_handler = None):
            super().__init__(parent)
            
            self.data_handler = data_handler

            self.setStyleSheet("background-color: white;")

            self.main_layout = QVBoxLayout(self)

            self.setWindowTitle('Select Candidate Generation Technologies')
            self.layout = QHBoxLayout()

            # Create and set the title
            title = QLabel("Select the Candidate Technologies")
            font = QFont()
            font.setBold(True)
            font.setPointSize(13)
            title.setFont(font)
            title.setStyleSheet("color: blue;")
            
            #Add title
            self.main_layout.addWidget(title)

            self.main_layout.addLayout(self.layout)

            # List widget for candidate technologies
            self.listWidget = QListWidget()
            self.listWidget.setSelectionMode(QListWidget.NoSelection)  # Disable selection as we're using checkboxes
            # Add  candidate technologies checkbox items
            #techs = ['Tech 1', 'Tech 2', 'Tech 3', 'Custom']
            
            self.techs = cand_tech['Tech_Name']

            self.addCheckBoxItem('Default')
            for tech in self.techs:
                self.addCheckBoxItem(tech)
            self.addCheckBoxItem('Custom')
            self.layout.addWidget(self.listWidget)

            # Create a frame for customization but do not add it yet
            self.customization_frame = self.create_customization_frame()
            self.customization_frame.setVisible(False)  # Initially hidden
            self.layout.addWidget(self.customization_frame)
            
            # OK and Cancel buttons
            self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)
            self.main_layout.addWidget(self.buttonBox)

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

            #self.customization_frame = None
            #Add selection Frame
            #self.add_selection_frame()

            
        
        def addCheckBoxItem(self, text):
            '''Adds a checkbox item to the listWidget'''
            item = QListWidgetItem(self.listWidget)
            # This ensures the item takes the size of the checkbox
            item.setSizeHint(QCheckBox().sizeHint())
            
            # Create the checkbox widget and set its label
            checkBox = QCheckBox(text)
            
            # Special handling for "Custom" option
            if text == "Custom":# or text not in self.techs or text != "Default":
                checkBox.stateChanged.connect(self.handleCustomOption)
                self.customCheckBox = checkBox
            
            # Special handling for default option
            elif text == "Default":
                checkBox.stateChanged.connect(self.handleDefaultOption)
                self.defaultCheckBox = checkBox
            
            else:
                checkBox.stateChanged.connect(self.handleNonDefaultOption)

            # Add the checkbox to the list
            self.listWidget.setItemWidget(item, checkBox)
            
        def handleCustomOption(self, state):
            '''Handle state change for "Custom" checkbox'''            
            if state == Qt.CheckState.Checked or state == 2:
                print("Custom option selected")
                self.customization_frame = self.add_selection_frame()
                self.layout.addWidget(self.customization_frame)
                self.customization_frame.setVisible(True)
            elif state == Qt.CheckState.Unchecked or state == 0:
                print("Custom option deselected")
                # And here for when it's deselected
                self.customization_frame.setVisible(False)

        def handleDefaultOption(self, state):
            '''Handle "Default" checkbox'''
            for index in range(self.listWidget.count()):
                item = self.listWidget.item(index)
                checkBox = self.listWidget.itemWidget(item)
                if checkBox.text() != "Default":
                    checkBox.setEnabled(state != Qt.CheckState.Checked)#disable other options
        
        def handleNonDefaultOption(self, state):
            '''Handle non-default checkboxes'''
            if state == Qt.CheckState.Checked:
                # Uncheck and disable the "Default" checkbox
                self.defaultCheckBox.setChecked(False)
                self.defaultCheckBox.setEnabled(False)
            else:
                # Enable the "Default" checkbox only if all non-default checkboxes are unchecked
                allUnchecked = True
                for index in range(self.listWidget.count()):
                    item = self.listWidget.item(index)
                    checkBox = self.listWidget.itemWidget(item)
                    if checkBox.text() != "Default" and checkBox.isChecked():
                        allUnchecked = False
                        break
                if allUnchecked:
                    self.defaultCheckBox.setEnabled(True)

        def create_customization_frame(self):
            '''Creates and returns a frame for customizing technologies'''
            frame = QFrame()
            layout = QVBoxLayout(frame)

            # Add a title
            title = QLabel("Customize Technologies")
            layout.addWidget(title)

            return frame

        def selectedTechnologies(self):
            '''Returns the selected technologies as a list'''
            selectedTechs = []
            for index in range(self.listWidget.count()):
                item = self.listWidget.item(index)
                checkBox = self.listWidget.itemWidget(item)
                if checkBox.isChecked():
                    selectedTechs.append(checkBox.text())
            return selectedTechs
        
        def on_add_new_tech(self, device_box, type_box,tech_name):

            device = device_box.currentText()
            storage = False
            if type_box.currentText() == 'Generation':
                device_data = self.generation_devices[device]
            elif type_box.currentText() == 'Energy Storage':
                device_data = self.energy_storage_devices[device]
                storage = True
            
             # Remove the "Custom" checkbox item
            for index in range(self.listWidget.count()):
                item = self.listWidget.item(index)
                checkBox = self.listWidget.itemWidget(item)
                if checkBox.text() == "Custom":
                    self.listWidget.takeItem(index)
                    break

            #add to list of available technologies       
            self.addCheckBoxItem(tech_name.toPlainText())
            #acivate button when added
            self.customCheckBox.setChecked(True)

            #add Custom back to the bottom
            self.addCheckBoxItem('Custom')
            
            #TODO: add to data_handler
            self.data_handler.add_candidate_tech(device_data, storage)

        def on_type_selection(self, val, device_box):
            device_box.clear()
            if val == 0:
                device_box.addItems(self.generation_devices)
            elif val == 1:
                device_box.addItems(self.energy_storage_devices)
            else:
                print('No selection made')

        def get_bus_selection(self, val, bus_box):

            # selections, done = QInputDialog.getText(
            #     self, 'Bus Input', 'Enter Bus Names (Numbers)?:'
            # )

            # bus_box.addItem(selections)

            if bus_box.currentText() == 'New Selection':
                selections, done = QInputDialog.getText(
                    self, 'Bus Input', 'Enter Bus Names (Numbers)?:'
                )

                all_items = [bus_box.itemText(i) for i in range(bus_box.count())]
                all_items.insert(-1, selections)
                bus_box.clear()
                bus_box.addItems(all_items)
                bus_box.setCurrentText(selections)
            else:
                print('Something went wrong')
                print(bus_box.currentText())

        def get_new_technology(self, val, device_box, type_box):

            # dialog = InputDialog(labels=['Name', 'MWh', 'MW', 'RTE'])

            # if dialog.exec():
            #     print(dialog.getInputs())
            #     device_box.addItem(dialog.getInputs()[0])

            if val == 'Custom':
                gen_type = type_box.currentText()
                if gen_type == 'Generation':
                    dialog_labels = ['Name', 'Capital Cost $/MW', 'Deployable Year', 'Lead Time',
                                                'Candidate Capacity', 'System Capacity', 'Ramp Rate', 
                                                'PTC Credit', 'ITC Credit', 'Capacity Credit']
                elif gen_type == 'Energy Storage':
                    dialog_labels = ['Name', 'Capital Cost $/MWh', 'Capital Cost $/MW', 
                                                'Min Duration', 'Max Duration', 'RTE', 'Deployable Year', 
                                                'Lead Time', 'Candidate Capacity']
                    
                dialog = TechDialog(labels=dialog_labels)

                if dialog.exec():
                    input = dialog.getInputs()[0]
                    all_items = [device_box.itemText(i) for i in range(device_box.count())]
                    all_items.insert(-1, input[0])
                    device_box.clear()
                    device_box.addItems(all_items)
                    device_box.setCurrentText(input[0])

                    if gen_type == 'Generation':
                        self.generation_devices[input[0]] = dict([(dialog_labels[i], label) for i, label in enumerate(dialog_labels)])
                    elif gen_type == 'Energy Storage':
                        self.energy_storage_devices[input[0]] = dict([(dialog_labels[i], label) for i, label in enumerate(dialog_labels)])
                    
        def add_selection_frame(self):
            self.selections += 1

            frame = QFrame(objectName='tech_frame{}'.format(self.selections))
            tech_name = QTextEdit(objectName='tech_name{}'.format(self.selections))
            type_box = QComboBox(objectName='type_box{}'.format(self.selections))
            device_box = QComboBox(objectName='device_box{}'.format(self.selections))
            bus_box = QComboBox(objectName='bus_box{}'.format(self.selections))
            add_new_tech_button = QPushButton(objectName='add_tech_button')

            type_box.activated.connect(lambda x, z=device_box: self.on_type_selection(x, z))
            type_box.addItem('Generation')
            type_box.addItem('Energy Storage')

            device_box.addItems(self.generation_devices)
            device_box.setInsertPolicy(QComboBox.InsertAfterCurrent)
            device_box.currentTextChanged.connect(lambda x, y=device_box, z=type_box: self.get_new_technology(x, y, z))

            bus_box.addItems(['All Buses', 'New Selection'])   
            bus_box.currentTextChanged.connect(lambda x, y=bus_box: self.get_bus_selection(x,y))

            add_new_tech_button.clicked.connect(lambda x=device_box, y=type_box, z=tech_name: self.on_add_new_tech(x, y,z))
            add_new_tech_button.setText('Add Technology')
            add_new_tech_button.setStyleSheet("QPushButton { background-color: blue; color: white;font-weight:bold}")

            # Create and set the title
            title = QLabel("Add a Customized Technology")
            font = QFont()
            font.setBold(True)
            font.setPointSize(12)
            title.setFont(font)

            # Create labels for each component
            tech_name_label = QLabel("Technology Name:")
            type_box_label = QLabel("Category:")
            device_box_label = QLabel("Device:")
            bus_box_label = QLabel("Candidate Location:")
            
            layout = QVBoxLayout(frame)
            layout.addWidget(title)
            layout.addWidget(tech_name_label)
            layout.addWidget(tech_name)
            layout.addWidget(type_box_label)
            layout.addWidget(type_box)
            layout.addWidget(device_box_label)
            layout.addWidget(device_box)
            layout.addWidget(bus_box_label)
            layout.addWidget(bus_box)
            layout.addWidget(add_new_tech_button)

            self.customization_frame.layout().addWidget(frame)

            return frame

class CustomSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Custom Technology Selection')
        layout = QVBoxLayout(self)
        
        # Assuming add_selection_frame is modified to return the frame and its components
        self.selection_frame = self.add_selection_frame()#parent.add_selection_frame()
        layout.addWidget(self.selection_frame)
        
        # OK and Cancel buttons (optional, depending on your needs)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        layout.addWidget(self.buttonBox)

class MatplotlibWidget(QGraphicsView):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

class ScenarioInfoDialog(QDialog):
    def __init__(self, parent=None, scenario_info=None,planning_model_info = None,system_name = None):
        super().__init__(parent)
        self.setWindowTitle("Scenario Summary")
        self.setStyleSheet("background-color: white;")
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setMinimumSize(400, 300)
        self.scenario_info = scenario_info
        self.planning_model_info = planning_model_info
        self.system_name = system_name

        #Set title
        scenario_name_label = QLabel(f"{scenario_info.get('Scenario Name', 'Scenario')} Scenario")
        scenario_name_label.setFont(QFont("Arial", 16, QFont.Bold))
        scenario_name_label.setStyleSheet("color: blue;")
        scenario_name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(scenario_name_label)

        # Add system name as subheading
        if self.system_name:
            system_name_label = QLabel(system_name)
            system_name_label.setFont(QFont("Arial", 12, QFont.Bold))
            system_name_label.setStyleSheet("color: gray;")
            system_name_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(system_name_label)

        # add a horizontal line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)

        # Display Planning Model Info
        self.display_info(planning_model_info, section_title="Planning Model Information")
        
        # add a horizontal line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)

        # Display Scenario Info (without Scenario Name)
        scenario_info.pop("Scenario Name", None)  

        if scenario_info is not None:
            self.display_info(scenario_info,section_title="Scenario Information")

        # Save Button
        self.add_save_button_with_spacers(layout)

    def add_save_button_with_spacers(self, layout):
        # Create a horizontal layout for the button and spacers
        button_layout = QHBoxLayout()
        
        # Left spacer
        left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(left_spacer)
        
        # Save Button
        self.save_button = QPushButton("Save Scenario Info")
        self.save_button.setStyleSheet("QPushButton {background-color: rgb(129, 194, 65); color: white; font-weight: bold; font-size: 12pt;}")

        self.save_button.clicked.connect(self.save_info_to_file)
        button_layout.addWidget(self.save_button)
        
        # Right spacer
        right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(right_spacer)
        
        # Create a QWidget to hold the QHBoxLayout
        button_container = QWidget()
        button_container.setLayout(button_layout)
        layout.addWidget(button_container)

    def display_info(self, info, section_title=None):
        if section_title:
            section_label = QLabel(section_title)
            section_label.setFont(QFont("Arial", 12, QFont.Bold))
            self.layout().addWidget(section_label)

        for key, value in info.items():
            if isinstance(value, list):
                # Display lists as bulleted lists
                label = QLabel(f"{key}:")
                font = QFont("Arial", 12)
                font.setItalic(True)
                #label.setFont(QFont("Arial", 12, QFont.StyleItalic))
                label.setFont(font)
                self.layout().addWidget(label)
                text_edit = QTextEdit()
                text_edit.setReadOnly(True)
                text_edit.setStyleSheet("background-color: white; border: none;")
                text_edit.setText("\n".join([f"• {item}" for item in value]))
                self.layout().addWidget(text_edit)
            else:
                label = QLabel(f"{key}: {value}")
                font = QFont("Arial", 12)
                font.setItalic(True)
                #label.setFont(QFont("Arial", 12, QFont.StyleItalic))
                label.setFont(font)
                self.layout().addWidget(label)

        #for key, value in info.items():
         ##   label = QLabel(f"<b>{key}:</b> {value}")
           # label.setTextFormat(Qt.RichText)
          #  self.layout().addWidget(label)

    #def display_info(self, info):
      #  for key, value in info.items():
       #     label = QLabel(f"<b>{key}:</b> {value}")
       #     label.setTextFormat(Qt.RichText)
       #     self.layout().addWidget(label)
    
    def save_info_to_file(self):
        # Open file dialog to choose save location
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", 
                                                  f"{self.scenario_info.get('Scenario Name', 'scenario')}.txt", 
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                for key, value in self.scenario_info.items():
                    file.write(f"{key}: {value}\n")
            print(f"Scenario information saved to {fileName}")

class RPSDialog(QDialog):
    """
    Dialog to set rps targets.

    Takes a pandas dataframe with a column that contains the generator
    names and a list of the years in the optimization as arguments.
    """
    def __init__(self, years:List[int], parent=None):
        super().__init__(parent)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QFormLayout(self)

        self.rps_layout = {}
        self.rps_schedule = {}

        for year in years:
            self.rps_layout[year] = QLineEdit(self)
            layout.addRow("{}".format(year), self.rps_layout[year])

        self.set_button = QPushButton("Set", self, objectName="set_button")
        self.set_button.clicked.connect(self._set_button_clicked)

        layout.addRow(self.set_button)
        layout.addRow(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        self.error_message = QErrorMessage()

    def _set_button_clicked(self):
        """Saves retirement years to a dictionary."""
        for year in self.rps_layout:
            #self.rps_schedule[year] = self.rps_layout[year].text()
            text = self.rps_layout[year].text().strip()  # Use strip() to remove leading/trailing whitespace
            if text:
                self.rps_schedule[year] = text #if text else None
            else:
                self.error_message.showMessage("Please fill out all years with an RPS target")

class LoadingSplashScreen(QDialog):
    def __init__(self, parent=None,title="Loading"):
        super().__init__(parent, Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.setModal(True)  # Make the dialog modal to block interaction with the main window
        
        self.setWindowTitle(title)
        layout = QVBoxLayout()
        
        self.label = QLabel("Loading data, please wait...")
        layout.addWidget(self.label)
        
        self.progressBar = QProgressBar(self)
        self.progressBar.setRange(0,0)  # Indeterminate mode
        layout.addWidget(self.progressBar)
        
        self.setLayout(layout)

    def show_message(self, message):
        self.label.setText(message)
        self.show()


class YearOptionsDialog(QDialog):
    def __init__(self,years:List[int],parent=None):
        super().__init__(parent)
        self.setWindowTitle("Simulation Year Options")

        layout = QVBoxLayout(self)
        #layout.setAlignment(Qt.AlignCenter)  

        #years = [2022, 2023, 2024, 2025]  # Example list of years

        '''
        
        checkbox = QCheckBox('All years')
        layout.addWidget(checkbox)
        self.checkboxes.append(checkbox)
        '''
        num_columns=math.ceil(len(years)/5)
        
        self.checkboxes = []
        checkboxes_layout = QGridLayout()
        for i, year in enumerate(years):
            checkbox = QCheckBox(str(year))
            row = i // num_columns
            col = i % num_columns
            checkboxes_layout.addWidget(checkbox, row, col)
            self.checkboxes.append(checkbox)
        layout.addLayout(checkboxes_layout)
        
        buttons_layout = QHBoxLayout()
        
        
        all_years_button = QPushButton("All Years")
        all_years_button.clicked.connect(self.toggle_all_years)
        buttons_layout.addWidget(all_years_button)
        
        button = QPushButton("OK")
        button.clicked.connect(self.accept)
        buttons_layout.addWidget(button)
        layout.addLayout(buttons_layout)
    
    def toggle_all_years(self):
        all_checked = all(checkbox.isChecked() for checkbox in self.checkboxes)
        for checkbox in self.checkboxes:
            checkbox.setChecked(not all_checked)
            
    def get_selected_years(self):
        selected_years = []
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                selected_years.append(int(checkbox.text()))
        return selected_years

class YearRadioButton(QRadioButton):
    def __init__(self, year, parent=None):
        super(YearRadioButton, self).__init__(str(year), parent)
        self.year = year

class TabAnimator():
    def __init__(self, tab_widget):
        self.tab_widget = tab_widget
        
    def fade_in_tab_widget(self,index):
        if index == self.tab_widget.currentIndex():
            current_widget = self.tab_widget.widget(index)
            current_widget.setWindowOpacity(0.0)  # Set initial opacity to 0 (fully transparent)


            animation = QPropertyAnimation(current_widget, b"windowOpacity")
            #animation = QPropertyAnimation(self.tab_widget, b"windowOpacity")
            animation.setDuration(1000)  # Set the duration of the animation in milliseconds
    
            animation.setStartValue(0.0)  # Set the initial opacity to 0 (fully transparent)
    
            animation.setEndValue(1.0)  # Set the final opacity to 1 (fully opaque)
    
            animation.setEasingCurve(QEasingCurve.InOutQuad)  # Set the easing curve for a smooth animation
    
            current_widget.show()#self.tab_widget.show()  # Make sure the tab widget is visible before starting the animation
    
            animation.start(QPropertyAnimation.DeleteWhenStopped)  # Start the animation and delete it when finished
        
    def fade_out_tab_widget(self):
        animation = QPropertyAnimation(self.tab_widget, b"windowOpacity")
        animation.setDuration(1000)  # Set the duration of the animation in milliseconds

        animation.setStartValue(1.0)  # Set the initial opacity to 0 (fully transparent)

        animation.setEndValue(0.0)  # Set the final opacity to 1 (fully opaque)

        animation.setEasingCurve(QEasingCurve.InOutQuad)  # Set the easing curve for a smooth animation

        self.tab_widget.show()  # Make sure the tab widget is visible before starting the animation

        animation.start(QPropertyAnimation.DeleteWhenStopped)  # Start the animation and delete it when finished

class StdoutBuffer:
    def __init__(self, worker_thread):
        self.worker_thread = worker_thread
        self.buffer = ""

    def write(self, text):
        self.buffer += text
        lines = self.buffer.split("\n")
        for line in lines[:-1]:
            self.worker_thread.output_updated.emit(line)
        self.buffer = lines[-1]

    def flush(self):
        pass


class ExecuteFunction(QThread):
    """
    Thread to execute functions outside of the main thread.

    Takes the funtion and arguments (optional) as inputs.
    """
    task_failed = Signal()
    finished = Signal()
    output_updated = Signal(str)
    
    def __init__(self, function, args = None):
        super().__init__()
        self._function = function
        self._args = args#None

    def run(self):
        try:
            if self._args == None:

                self._function()
            else:

                self._function(*self._args)
            
            self.finished.emit()
        except Exception as e:
            traceback.print_exc()
            self.task_failed.emit()

        #else:
            #self.finished.emit()
            #print("Function executed")

class ExecuteFunctionBuffer(QThread):
    """
    Thread to execute functions outside of the main thread. this function uses buffer to print out info into the GUI.

    Takes the funtion and arguments (optional) as inputs.
    """
    task_failed = Signal()
    finished = Signal()
    output_updated = Signal(str)
    
    def __init__(self, function, args = None):
        super().__init__()
        self._function = function
        self._args = args#None

    def run(self):
        try:
            if self._args == None:
                # Redirect stdout to a buffer
                stdout_buffer = StdoutBuffer(self)
                sys.stdout = stdout_buffer
                self._function()
                # Restore stdout
                sys.stdout = sys.__stdout__
 
            else:
                # Redirect stdout to a buffer
                stdout_buffer = StdoutBuffer(self)
                sys.stdout = stdout_buffer
                
                self._function(*self._args)

                # Restore stdout
                sys.stdout = sys.__stdout__
 

            self.finished.emit()
        except Exception as e:
            traceback.print_exc()
            self.task_failed.emit()

        #else:
            #self.finished.emit()
            #print("Function executed")

class TabAnimator():
    def __init__(self, tab_widget):
        self.tab_widget = tab_widget
        
    def fade_in_tab_widget(self,index):
        if index == self.tab_widget.currentIndex():
            current_widget = self.tab_widget.widget(index)
            current_widget.setWindowOpacity(0.0)  # Set initial opacity to 0 (fully transparent)


            animation = QPropertyAnimation(current_widget, b"windowOpacity")
            #animation = QPropertyAnimation(self.tab_widget, b"windowOpacity")
            animation.setDuration(1000)  # Set the duration of the animation in milliseconds
    
'''
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = InputDialog(labels=["First", "Second", "Third", "Fourth"])
    if dialog.exec():
        print(dialog.getInputs())
    exit(0)
'''
'''ARCHIVE

# class CandidateTechDialog(QDialog):
#     def __init__(self, candidate_tech:List[str], years:List[int], parent=None):
#         super().__init__(parent)

#         buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
#         layout = QFormLayout(self)

#         self.commercialized = {}

#         self.candidate_qbox = QComboBox(self, objectName="candidate_box")
#         self.candidate_qbox.addItems(candidate_tech)

#         self.years_qbox = QComboBox(self, objectName="years_qbox")
#         self.years_qbox.addItems([str(year) for year in years])

#         self.set_button = QPushButton("Set", self, objectName="set_button")
#         self.set_button.clicked.connect(self._set_button_clicked)

#         layout.addRow("Candidate Technology: ", self.candidate_qbox)
#         layout.addRow("Year: ", self.years_qbox)
#         layout.addRow(self.set_button)
#         layout.addRow(buttonBox)

#         buttonBox.accepted.connect(self.accept)
#         buttonBox.rejected.connect(self.reject)

    # def _set_button_clicked(self):
    #     tech = self.candidate_qbox.currentText()
    #     year = self.years_qbox.currentText()

    #     self.candidate_qbox.setCurrentIndex(0)
    #     self.years_qbox.setCurrentIndex(0)

    #     self.commercialized[tech] = year

    '''