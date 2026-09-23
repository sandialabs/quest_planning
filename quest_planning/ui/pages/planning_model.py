from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate, Qt

from quest_planning.ui.forms.planning_model_setup.ui_planning_model import (
    Ui_PlanningModelPage,
)


class PlanningModelPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PlanningModelPage()
        self.ui.setupUi(self)

        self.ui.dateEdit_start.setDate(QDate(2022, 1, 1))
        self.ui.dateEdit_end.setDate(QDate(2042, 1, 1))
        self.ui.annual_discount_factor.setRange(0.5, 50)
        self.ui.annual_discount_factor.setDecimals(2)
        self.ui.annual_discount_factor.setValue(5)
        self.ui.base_currency_year.setText("2021")

        self.setObjectName("planning_model_page")

        self.ui.button_sim_help.setToolTip(
            "Choose the years of study for the planning model."
        )
        self.ui.button_trans_help.setToolTip(
            "Select the level of fidelity used to model transmission."
        )
        self.ui.button_temporal_help.setToolTip(
            "Select the temporal resolution of the planning model."
        )
        self.ui.button_discount_help.setToolTip(
            "Annual discount rate used for the economic analysis."
        )
        self.ui.button_base_help.setToolTip(
            "Standard year used to adjust costs for inflation."
        )
        self.ui.button_years_select.setToolTip(
            "Browse to a file of simulation years or enter them manually."
        )
        self.ui.advanced_settings_button.setToolTip(
            "Open the advanced planning settings dialog."
        )

        self.ui.dateEdit_start.dateChanged.connect(self.on_year_box_activated)
        self.ui.dateEdit_end.dateChanged.connect(self.on_year_box_activated)
        self.ui.button_years_select.clicked.connect(self.on_select_years_button_clicked)
        self.ui.transmission_box.currentIndexChanged.connect(
            self.on_transmission_box_activated
        )
        self.ui.temporal_box.currentIndexChanged.connect(self.on_temporal_box_activated)
        self.ui.annual_discount_factor.valueChanged.connect(
            self.on_discount_factor_changed
        )
        self.ui.base_currency_year.editingFinished.connect(
            self.on_base_currency_year_edited
        )
        self.ui.advanced_settings_button.clicked.connect(
            self.on_advanced_settings_button_clicked
        )
        self.ui.button_sim_help.clicked.connect(
            lambda: self.display_help_message("Select Simulation Years")
        )
        self.ui.button_trans_help.clicked.connect(
            lambda: self.display_help_message("Transmission Model")
        )
        self.ui.button_temporal_help.clicked.connect(
            lambda: self.display_help_message("Temporal Selection")
        )
        self.ui.button_discount_help.clicked.connect(
            lambda: self.display_help_message("Annual Discount Rate")
        )
        self.ui.button_base_help.clicked.connect(
            lambda: self.display_help_message("Base Currency Year")
        )

    def on_year_box_activated(self):
        begin_year = self.ui.dateEdit_start.date().year()
        end_year = self.ui.dateEdit_end.date().year()
        if end_year >= begin_year:
            self.ui.label_years_input.setText(
                "{} - {}".format(begin_year, end_year)
            )

    def on_select_years_button_clicked(self):
        pass

    def on_transmission_box_activated(self):
        self.ui.label_trans_input.setText(self.ui.transmission_box.currentText())

    def on_temporal_box_activated(self):
        self.ui.label_temp_input.setText(self.ui.temporal_box.currentText())

    def on_discount_factor_changed(self, value):
        self.ui.label_discount_input.setText("{:.2f}".format(value))

    def on_base_currency_year_edited(self):
        self.ui.label_currency_input.setText(self.ui.base_currency_year.text())

    def on_advanced_settings_button_clicked(self):
        pass

    def display_help_message(self, topic):
        pass