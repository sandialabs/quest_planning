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

        self.ui.begin_date.setDate(QDate(2022, 1, 1))
        self.ui.end_date.setDate(QDate(2042, 1, 1))
        self.ui.annual_discount_factor.setRange(0.5, 50)
        self.ui.annual_discount_factor.setDecimals(2)
        self.ui.annual_discount_factor.setValue(5)
        self.ui.base_currency_year.setText("2021")

        self.setObjectName("planning_model_page")

        self.ui.planning_model_info_frame.setHidden(True)

        self.ui.planning_model_help_button.setToolTip(
            "Help for the planning model settings."
        )
        self.ui.select_simulation_years_help_button.setToolTip(
            "Choose the years of study for the planning model."
        )
        self.ui.transmission_model_help_button.setToolTip(
            "Select the level of fidelity used to model transmission."
        )
        self.ui.temporal_selection_help_button.setToolTip(
            "Select the temporal resolution of the planning model."
        )
        self.ui.discount_rate_help_button.setToolTip(
            "Annual discount rate used for the economic analysis."
        )
        self.ui.base_currency_help_button.setToolTip(
            "Standard year used to adjust costs for inflation."
        )
        self.ui.select_years_button.setToolTip(
            "Browse to a file of simulation years or enter them manually."
        )
        self.ui.advanced_settings_button.setToolTip(
            "Open the advanced planning settings dialog."
        )

        self.ui.begin_date.dateChanged.connect(self.on_year_box_activated)
        self.ui.end_date.dateChanged.connect(self.on_year_box_activated)
        self.ui.select_years_button.clicked.connect(self.on_select_years_button_clicked)
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
        self.ui.planning_model_help_button.clicked.connect(
            lambda: self.display_help_message("Planning Model")
        )
        self.ui.select_simulation_years_help_button.clicked.connect(
            lambda: self.display_help_message("Select Simulation Years")
        )
        self.ui.transmission_model_help_button.clicked.connect(
            lambda: self.display_help_message("Transmission Model")
        )
        self.ui.temporal_selection_help_button.clicked.connect(
            lambda: self.display_help_message("Temporal Selection")
        )
        self.ui.discount_rate_help_button.clicked.connect(
            lambda: self.display_help_message("Annual Discount Rate")
        )
        self.ui.base_currency_help_button.clicked.connect(
            lambda: self.display_help_message("Base Currency Year")
        )

    def on_year_box_activated(self):
        begin_year = self.ui.begin_date.date().year()
        end_year = self.ui.end_date.date().year()
        if end_year >= begin_year:
            self.ui.sim_years_label.setText(
                "{} - {}".format(begin_year, end_year)
            )
            self.ui.planning_model_info_frame.show()

    def on_select_years_button_clicked(self):
        pass

    def on_transmission_box_activated(self):
        self.ui.trans_model_label.setText(self.ui.transmission_box.currentText())
        self.ui.planning_model_info_frame.show()

    def on_temporal_box_activated(self):
        self.ui.temporal_selection_label.setText(self.ui.temporal_box.currentText())
        self.ui.planning_model_info_frame.show()

    def on_discount_factor_changed(self, value):
        self.ui.discount_rate_label.setText("{:.2f}".format(value))
        self.ui.planning_model_info_frame.show()

    def on_base_currency_year_edited(self):
        self.ui.base_currency_label.setText(self.ui.base_currency_year.text())
        self.ui.planning_model_info_frame.show()

    def on_advanced_settings_button_clicked(self):
        pass

    def display_help_message(self, topic):
        pass