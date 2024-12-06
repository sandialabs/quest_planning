"""
Control of the Candidate Technologies Page. 

Author: Walker Olis
Last Edit: 2/27/24

"""

import os
from PySide6.QtCore import (
    QThreadPool
)
from PySide6.QtWidgets import (
    QMenu,
    QWidget,
    QInputDialog,
    QComboBox,
    QFrame,
    QHBoxLayout
)
from quest_planning.gui.candidate_technologies_page.ui.candidate_technologies import Ui_candidate_technologies
from quest_planning.gui.tools.tools import TechDialog


class CandidateTechnologiesPage(QWidget, Ui_candidate_technologies):
    """
    The landing screen.

    Utility for buttons are imported.
    Update state based on files at launch
    """

    def __init__(self):
        """Initialize the home page."""
        super().__init__()
#           Set up the ui

        self.setupUi(self)
        self.selections = 0
        self.generation_devices = ['Solar', 'Wind', 'Natural Gas', 'Custom']
        self.energy_storage_devices = ['Lithium Ion Battery', 'Vanadium Redox Flow Battery',
                                       'Zinc Battery', 'Thermal', 'Gravitational', 'Pumped Storage Hydro',
                                       'Hydrogen', 'Compressed Air', 'Custom']
        
        self.add_new_tech_button.clicked.connect(self.on_add_new_tech)

        # for bus_box in self.frame_2.findChildren(QComboBox):
        #     bus_box.textActivated('New Selection...').connect(lambda x=bus_box: self.get_bus_selection(x))

        # for device_box in self.frame_3.findChildren(QComboBox):
        #     device_box.textActivated('Create New Device').connect(lambda x=device_box: self.get_new_technology(x))

    def on_add_new_tech(self):
        push_button = self.tech_frame_layout.takeAt(self.selections)

        self.tech_frame_layout.addWidget(self.add_selection_frame())
        self.tech_frame_layout.addWidget(push_button.widget())
        self.update()

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

    def get_new_technology(self, val, device_box):

        # dialog = InputDialog(labels=['Name', 'MWh', 'MW', 'RTE'])

        # if dialog.exec():
        #     print(dialog.getInputs())
        #     device_box.addItem(dialog.getInputs()[0])

        if device_box.currentText() == 'Custom':
            dialog = TechDialog(labels=['Name', 'MWh', 'MW', 'RTE'])

            if dialog.exec():
                input = dialog.getInputs()[0]
                all_items = [device_box.itemText(i) for i in range(device_box.count())]
                all_items.insert(-1, input)
                device_box.clear()
                device_box.addItems(all_items)
                device_box.setCurrentText(input)
            
    def add_selection_frame(self):
        self.selections += 1

        frame = QFrame(objectName='tech_frame{}'.format(self.selections))
        type_box = QComboBox(objectName='type_box{}'.format(self.selections))
        device_box = QComboBox(objectName='device_box{}'.format(self.selections))
        bus_box = QComboBox(objectName='bus_box{}'.format(self.selections))

        type_box.activated.connect(lambda x, z=device_box: self.on_type_selection(x, z))
        type_box.addItem('Generation')
        type_box.addItem('Energy Storage')

        device_box.addItems(self.generation_devices)
        device_box.setInsertPolicy(QComboBox.InsertAfterCurrent)
        device_box.currentTextChanged.connect(lambda x, y=device_box: self.get_new_technology(x, y))

        bus_box.addItems(['All Buses', 'New Selection'])   
        bus_box.currentTextChanged.connect(lambda x, y=bus_box: self.get_bus_selection(x,y))



        new_layout = QHBoxLayout(frame)
        new_layout.addWidget(type_box)
        new_layout.addWidget(device_box)
        new_layout.addWidget(bus_box)

        return frame