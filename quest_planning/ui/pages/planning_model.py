from PySide6.QtWidgets import QCheckBox, QDialog, QMessageBox, QWidget
from PySide6.QtCore import QDate

from quest_planning.ui.forms.planning_model_setup.ui_planning_model import (
    Ui_PlanningModelPage,
)
from quest_planning.ui.forms.planning_model_setup.ui_advanced_settings import (
    Ui_AdvancedSettingsPage,
)
from quest_planning.ui.forms.planning_model_setup.ui_simulation_years import (
    Ui_SimulationYearsPage
)
from quest_planning.ui.utils.help_topics import show_error, show_help

ADVANCED_SETTINGS_DEFAULTS = {
    "Planning Reserve Margin": 20,
    "Regulating Reserve Requirement": 1.0,
    "Spinning Reserve Requirement": 3,
    "Flexibility Reserve Requirement (Solar)": 4,
    "Flexibility Reserve Requirement (Wind)": 10,
    "System-wide Wind Maximum Investment": "Default",
    "System-wide Solar Maximum Investment": "Default",
    "System-wide Gas Maximum Investment": "Default",
    "System-wide Transmission Maximum Investment": "Default",
    "Tax Credits Option": False,
    "Tax Credits End Year": 2032,
    "End Effects": 10,
}

# (setting name, lineEdit objectName) in the order the labels are laid out.
ADVANCED_SETTINGS_FIELDS = (
    ("Planning Reserve Margin", "lineEdit_planning"),
    ("Regulating Reserve Requirement", "lineEdit_reserve"),
    ("Spinning Reserve Requirement", "lineEdit_spinning"),
    ("Flexibility Reserve Requirement (Solar)", "lineEdit_flex_solar"),
    ("Flexibility Reserve Requirement (Wind)", "lineEdit_flex_wind"),
    ("System-wide Wind Maximum Investment", "lineEdit_sys_wind_max"),
    ("System-wide Solar Maximum Investment", "lineEdit_sys_solar_max"),
    ("System-wide Gas Maximum Investment", "lineEdit_sys_gas_max"),
    ("System-wide Transmission Maximum Investment", "lineEdit_sys_trans_max"),
    ("Tax Credits Option", "lineEdit_tax_cred"),
    ("Tax Credits End Year", "lineEdit_tax_cred_end_year"),
    ("End Effects", "lineEdit_end_effects"),
)

# Checkboxes in the simulation years dialog are laid out in fixed-width columns.
YEAR_GRID_COLUMNS = 5

# Temporal combo label -> the value the optimizer compares against. Labels
# missing from this map are not supported yet and are disabled at startup.
TEMPORAL_SELECTION_MAP = {
    "Representative Weeks": "Repr_Weeks",
    "Seasonal Blocks": "Seasonal_blocks",
}


class PlanningModelPage(QWidget):
    def __init__(self, data_handler, parent=None):
        super().__init__(parent)
        self.ui = Ui_PlanningModelPage()
        self.ui.setupUi(self)

        self.data_handler = data_handler
        self.advanced_settings_pane = None
        self.simulation_years_pane = None
        self.year_checkboxes = []
        self.advanced_settings = dict(ADVANCED_SETTINGS_DEFAULTS)
        self.ui.dateEdit_start.setDate(QDate(2022, 1, 1))
        self.ui.dateEdit_end.setDate(QDate(2042, 1, 1))
        self.years = None
        self.ui.annual_discount_factor.setRange(0.5, 50)
        self.ui.annual_discount_factor.setDecimals(2)
        self.ui.annual_discount_factor.setValue(5)
        self.ui.base_currency_year.setText("2021")

        # Options the optimizer understands but this page has no control for.
        # Explicit so they are not at the mercy of the data handler defaults
        self.data_handler.set_reserves_option(True)
        self.data_handler.set_es_lifetime_cost_option(False)

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
        self.ui.advanced_settings_button.clicked.connect(self.on_advanced_settings_button_clicked)
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
        self.ui.button_sim_help.clicked.connect(
            lambda: show_help(self, "Select Simulation Years")
        )
        self.ui.button_trans_help.clicked.connect(
            lambda: show_help(self, "Transmission Model")
        )
        self.ui.button_temporal_help.clicked.connect(
            lambda: show_help(self, "Temporal Selection")
        )
        self.ui.button_discount_help.clicked.connect(
            lambda: show_help(self, "Annual Discount Rate")
        )
        self.ui.button_base_help.clicked.connect(
            lambda: show_help(self, "Base Currency Year")
        )

        # The default dates and widget values are set above the signal
        # connections, so seed the handler from them once here.
        self.disable_unsupported_temporal_options()
        self.on_year_box_activated()
        self.on_transmission_box_activated()
        self.on_temporal_box_activated()
        self.on_discount_factor_changed(self.ui.annual_discount_factor.value())
        self.on_base_currency_year_edited()
        self.apply_advanced_settings_to_handler()

    def disable_unsupported_temporal_options(self):
        """Grey out temporal options the optimizer does not implement yet."""
        model = self.ui.temporal_box.model()
        for index in range(self.ui.temporal_box.count()):
            if self.ui.temporal_box.itemText(index) not in TEMPORAL_SELECTION_MAP:
                model.item(index).setEnabled(False)

    def planning_year_range(self):
        """Return every year between the start and end date edits."""
        begin_year = self.ui.dateEdit_start.date().year()
        end_year = self.ui.dateEdit_end.date().year()
        if end_year < begin_year:
            return []
        return list(range(begin_year, end_year + 1))

    def update_years_label(self):
        """Show the selected years, collapsing a full range to 'start - end'."""
        if not self.years:
            self.ui.label_years_input.setText("----")
        elif len(self.years) == 1:
            self.ui.label_years_input.setText(str(self.years[0]))
        elif self.years == self.planning_year_range():
            self.ui.label_years_input.setText(
                "{} - {}".format(self.years[0], self.years[-1])
            )
        else:
            self.ui.label_years_input.setText(
                ", ".join(str(year) for year in self.years)
            )

    def on_year_box_activated(self):
        # A changed horizon invalidates any previous selection, so fall back to
        # simulating every year in the new range.
        self.years = self.planning_year_range()
        self.update_years_label()
        # start_year/end_year only label the results output, but leaving them
        # None makes the results workbook name itself "..._None-None_...".
        self.data_handler.set_start_year(self.ui.dateEdit_start.date().year())
        self.data_handler.set_end_year(self.ui.dateEdit_end.date().year())
        self.data_handler.set_years_hours(self.years)

    def build_year_checkboxes(self):
        """(Re)create the year checkboxes, keeping any years still in range."""
        pane = self.simulation_years_pane
        layout = pane.ui.yeargridLayout

        for checkbox in self.year_checkboxes:
            layout.removeWidget(checkbox)
            checkbox.setParent(None)
            checkbox.deleteLater()
        self.year_checkboxes = []

        previously_selected = set(self.years or ())
        for index, year in enumerate(self.planning_year_range()):
            checkbox = QCheckBox(str(year), pane.ui.frame_years)
            checkbox.setChecked(year in previously_selected)
            row, column = divmod(index, YEAR_GRID_COLUMNS)
            layout.addWidget(checkbox, row, column)
            self.year_checkboxes.append(checkbox)

    def toggle_all_years(self):
        checkboxes = self.year_checkboxes
        checked = not all(checkbox.isChecked() for checkbox in checkboxes)
        for checkbox in checkboxes:
            checkbox.setChecked(checked)

    def accept_simulation_years(self):
        if not any(checkbox.isChecked() for checkbox in self.year_checkboxes):
            QMessageBox.warning(
                self.simulation_years_pane,
                "Simulation Years",
                "Select at least one simulation year.",
            )
            return
        self.simulation_years_pane.accept()

    def on_select_years_button_clicked(self):
        if self.simulation_years_pane is None:
            dialog = QDialog(self)
            dialog.ui = Ui_SimulationYearsPage()
            dialog.ui.setupUi(dialog)
            dialog.setWindowTitle("Simulation Years Selection")
            dialog.ui.btn_ok.clicked.connect(self.accept_simulation_years)
            dialog.ui.btn_years.clicked.connect(self.toggle_all_years)
            self.simulation_years_pane = dialog

        # The dialog is cached across opens, so rebuild the checkboxes every
        # time to pick up any change to the start and end dates.
        self.build_year_checkboxes()

        if self.simulation_years_pane.exec():
            selected = [
                int(checkbox.text())
                for checkbox in self.year_checkboxes
                if checkbox.isChecked()
            ]
            # Guard against the dialog being accepted some other way with
            # nothing checked, so downstream consumers always get a horizon.
            if selected:
                self.years = selected
                self.update_years_label()
                self.data_handler.set_years_hours(self.years)

    def on_transmission_box_activated(self):
        self.ui.label_trans_input.setText(self.ui.transmission_box.currentText())
        # set_tx_model maps the combo label onto the optimizer's own spelling.
        self.data_handler.set_tx_model(self.ui.transmission_box.currentText())

    def on_temporal_box_activated(self):
        label = self.ui.temporal_box.currentText()
        self.ui.label_temp_input.setText(label)
        selection = TEMPORAL_SELECTION_MAP.get(label)
        if selection is None:
            show_error(
                self,
                "Temporal Selection",
                "{} is not supported yet.".format(label),
            )
            return
        self.data_handler.set_block_selection(selection)

    def on_discount_factor_changed(self, value):
        self.ui.label_discount_input.setText("{:.2f}".format(value))
        self.data_handler.set_discount_rate(value)

    def on_base_currency_year_edited(self):
        text = self.ui.base_currency_year.text()
        self.ui.label_currency_input.setText(text)
        try:
            self.data_handler.set_base_currency_year(int(text))
        except ValueError:
            show_error(
                self,
                "Base Currency Year",
                "Enter a four digit year, not {!r}.".format(text),
            )

    def on_advanced_settings_button_clicked(self):
        if self.advanced_settings_pane is None:
            dialog = QDialog(self)
            dialog.ui = Ui_AdvancedSettingsPage()
            dialog.ui.setupUi(dialog)
            dialog.ui.btn_ok.clicked.connect(dialog.accept)
            dialog.ui.btn_cancel.clicked.connect(dialog.reject)
            self.advanced_settings_pane = dialog

        # The dialog is cached across opens, so seed the fields the first time
        # and show the current values on every later open.
        for name, field in ADVANCED_SETTINGS_FIELDS:
            line_edit = getattr(self.advanced_settings_pane.ui, field)
            line_edit.setText(str(self.advanced_settings[name]))

        if self.advanced_settings_pane.exec():
            for name, field in ADVANCED_SETTINGS_FIELDS:
                line_edit = getattr(self.advanced_settings_pane.ui, field)
                self.advanced_settings[name] = self.convert_setting_value(
                    line_edit.text()
                )
            self.apply_advanced_settings_to_handler()

    def apply_advanced_settings_to_handler(self):
        """Push the accepted advanced settings onto the data handler."""
        s = self.advanced_settings
        # Keywords, not positional: the last two are same-typed and a swapped
        # call would silently set the wrong resource's requirement.
        self.data_handler.set_reserve_params(
            prm=s["Planning Reserve Margin"],
            reg_res_req=s["Regulating Reserve Requirement"],
            spin_res_req=s["Spinning Reserve Requirement"],
            flex_res_s_req=s["Flexibility Reserve Requirement (Solar)"],
            flex_res_w_req=s["Flexibility Reserve Requirement (Wind)"],
        )
        self.data_handler.set_system_wide_wind_max(
            s["System-wide Wind Maximum Investment"]
        )
        self.data_handler.set_system_wide_solar_max(
            s["System-wide Solar Maximum Investment"]
        )
        self.data_handler.set_system_wide_gas_max(
            s["System-wide Gas Maximum Investment"]
        )
        self.data_handler.set_system_wide_tx_expansion_max(
            s["System-wide Transmission Maximum Investment"]
        )
        self.data_handler.set_tax_credits_option(s["Tax Credits Option"])
        self.data_handler.set_tax_credit_end_year(s["Tax Credits End Year"])
        self.data_handler.set_end_effects(s["End Effects"])

    @staticmethod
    def convert_setting_value(value):
        """Convert a dialog field to bool, float, or str."""
        if value.strip().lower() == "true":
            return True
        if value.strip().lower() == "false":
            return False
        try:
            return float(value)
        except ValueError:
            return value
