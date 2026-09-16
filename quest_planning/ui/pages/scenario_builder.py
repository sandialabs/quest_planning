import sys

from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QWidget

from quest_planning.ui.forms.scenario_builder.ui_scenario_builder import (
    Ui_ScenarioBuilderPage,
)
from quest_planning.ui.forms.scenario_builder.ui_view_scenario import (
    Ui_ViewScenarioDialog,
)


class ScenarioBuilderPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ScenarioBuilderPage()
        self.ui.setupUi(self)

        self.setObjectName("scenario_builder_page")

        self._planning_model_page = None
        self._power_system_page = None
        self._view_dialog = None

        self.ui.cand_tech_frame.setHidden(True)
        self.ui.retirement_frame.setHidden(True)

        self.ui.scenario_name_box.setToolTip(
            "Unique name used to save the scenario results."
        )
        self.ui.capital_cost_box.setToolTip(
            "Select the capital cost trajectory for energy storage technologies."
        )
        self.ui.load_profile_box.setToolTip(
            "Select the load forecast for the scenario."
        )
        self.ui.annual_load_growth_box.setToolTip(
            "Annual load growth (%). Only used when a single year of load data is provided."
        )
        self.ui.rps_box.setToolTip("Select the Future Generation Mix for the scenario.")
        self.ui.transmission_box.setToolTip(
            "Choose whether transmission expansion is allowed."
        )
        self.ui.cand_tech_button.setToolTip(
            "Select the candidate technologies for the optimization."
        )
        self.ui.gen_retirement_button.setToolTip(
            "Select the generation retirement schedule."
        )
        self.ui.view_scenario_button.setToolTip(
            "Review the complete scenario before running the optimizer."
        )
        self.ui.scenario_builder_help_button.setToolTip(
            "Help: build a scenario in QuESt Planning."
        )

        self.ui.cand_tech_button.clicked.connect(self.on_cand_tech_button_clicked)
        self.ui.gen_retirement_button.clicked.connect(
            self.on_gen_retirement_button_clicked
        )
        self.ui.view_scenario_button.clicked.connect(self.open_view_scenario)

        self.ui.scenario_builder_help_button.clicked.connect(
            lambda: self.display_help_message("Scenario Builder")
        )
        self.ui.scenario_name_help_button.clicked.connect(
            lambda: self.display_help_message("Select Scenario Name")
        )
        self.ui.capital_cost_trajectory_help_button.clicked.connect(
            lambda: self.display_help_message("Select Capital Costs")
        )
        self.ui.load_profile_help_button.clicked.connect(
            lambda: self.display_help_message("Select Load Forecasts")
        )
        self.ui.load_growth_help_button.clicked.connect(
            lambda: self.display_help_message("Select Annual Load Growth")
        )
        self.ui.rps_help_button.clicked.connect(
            lambda: self.display_help_message(
                "Select Renewable Portfolio Standard Goals"
            )
        )
        self.ui.trans_expansion_help_button.clicked.connect(
            lambda: self.display_help_message("Select Transmission Expansion Option")
        )
        self.ui.cand_technologies_help_button.clicked.connect(
            lambda: self.display_help_message("Candidate Technologies Selection")
        )
        self.ui.gen_retirement_help_button.clicked.connect(
            lambda: self.display_help_message("Generation Retirements Selection")
        )

    def set_planning_model_page(self, page):
        """Supply the Planning Model page so selections can be summarized."""
        self._planning_model_page = page

    def set_power_system_page(self, page):
        """Supply the Power System Data page for the system name."""
        self._power_system_page = page

    def on_cand_tech_button_clicked(self):
        pass

    def on_gen_retirement_button_clicked(self):
        pass

    def planning_model_info(self):
        """Collect the Planning Model configuration as a dictionary."""
        page = self._planning_model_page
        if page is None:
            return {
                "Simulation Years": "--",
                "Transmission Model": "--",
                "Temporal Selection": "--",
                "Discount Factor": "--",
                "Base Currency Year": "--",
            }
        return {
            "Simulation Years": page.ui.sim_years_label.text(),
            "Transmission Model": page.ui.transmission_box.currentText(),
            "Temporal Selection": page.ui.temporal_box.currentText(),
            "Discount Factor": "{:.2f}".format(
                page.ui.annual_discount_factor.value()
            ),
            "Base Currency Year": page.ui.base_currency_year.text(),
        }

    def scenario_info(self):
        """Collect the scenario selections as a dictionary."""
        load_forecast = self.ui.load_profile_box.currentText() or "--"
        candidate_tech = (
            self.ui.candidate_tech_box.toPlainText()
            if not self.ui.cand_tech_frame.isHidden()
            else "No technologies selected"
        )
        retirement = (
            self.ui.retirement_box.toPlainText()
            if not self.ui.retirement_frame.isHidden()
            else "No retirement schedule selected"
        )
        return {
            "Scenario Name": self.ui.scenario_name_box.text()
            or "Unnamed Scenario",
            "Resource Capital Costs": self.ui.capital_cost_box.currentText(),
            "Load Forecasts": load_forecast,
            "Annual Load Growth": self.ui.annual_load_growth_box.text(),
            "Renewable Portfolio Standards": self.ui.rps_box.currentText(),
            "Transmission Expansion": self.ui.transmission_box.currentText(),
            "Candidate Technologies": candidate_tech,
            "Retirement Schedule": retirement,
        }

    def open_view_scenario(self, blocking=True):
        """Populate and show the View Scenario dialog."""
        if self._view_dialog is None:
            self._view_dialog = QDialog()
            self._view_dialog.ui = Ui_ViewScenarioDialog()
            self._view_dialog.ui.setupUi(self._view_dialog)
            self._view_dialog.ui.save_scenario_button.clicked.connect(
                self.save_info_to_file
            )
            self._view_dialog.ui.close_button.clicked.connect(
                self._view_dialog.reject
            )

        system_name = "--"
        if self._power_system_page is not None:
            system_name = self._power_system_page.ui.system_name_input.text() or "--"
        self._view_dialog.ui.system_name_label.setText(
            "Power System: {}".format(system_name)
        )

        pm = self.planning_model_info()
        self._view_dialog.ui.sim_years_value.setText(pm["Simulation Years"])
        self._view_dialog.ui.trans_model_value.setText(pm["Transmission Model"])
        self._view_dialog.ui.temporal_value.setText(pm["Temporal Selection"])
        self._view_dialog.ui.discount_value.setText(pm["Discount Factor"])
        self._view_dialog.ui.base_currency_value.setText(pm["Base Currency Year"])

        sc = self.scenario_info()
        self._view_dialog.ui.capital_cost_value.setText(sc["Resource Capital Costs"])
        self._view_dialog.ui.load_forecast_value.setText(sc["Load Forecasts"])
        self._view_dialog.ui.annual_load_growth_value.setText(sc["Annual Load Growth"])
        self._view_dialog.ui.rps_value.setPlainText(sc["Renewable Portfolio Standards"])
        self._view_dialog.ui.transmission_expansion_value.setText(
            sc["Transmission Expansion"]
        )
        self._view_dialog.ui.candidate_tech_value.setPlainText(
            sc["Candidate Technologies"]
        )
        self._view_dialog.ui.retirement_value.setPlainText(sc["Retirement Schedule"])

        if blocking:
            self._view_dialog.exec()

    def save_info_to_file(self):
        """Write a text summary of the scenario to a user-chosen file."""
        info = self.planning_model_info()
        info.update(self.scenario_info())

        default_name = "{}.txt".format(info["Scenario Name"])
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            default_name,
            "All Files (*);;Text Files (*.txt)",
        )
        if not file_name:
            return
        with open(file_name, "w") as file:
            for key, value in info.items():
                file.write("{}: {}\n".format(key, value))

    def display_help_message(self, topic):
        pass


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet("* { background-color: #f0f0f0; color: #000000; }")
    page = ScenarioBuilderPage()
    page.setGeometry(0, 0, 1118, 928)
    page.show()
    for name in (
        "scenario_name_box",
        "scenario_name_help_button",
        "capital_cost_box",
        "capital_cost_trajectory_help_button",
        "load_profile_box",
        "load_profile_help_button",
        "annual_load_growth_box",
        "load_growth_help_button",
        "rps_box",
        "rps_help_button",
        "transmission_box",
        "trans_expansion_help_button",
        "cand_tech_button",
        "cand_technologies_help_button",
        "candidate_tech_box",
        "cand_tech_frame",
        "gen_retirement_button",
        "gen_retirement_help_button",
        "retirement_box",
        "retirement_frame",
        "view_scenario_button",
    ):
        print("has {}: {}".format(name, hasattr(page.ui, name)))
    print("cand frame hidden:", page.ui.cand_tech_frame.isHidden())
    print("retirement frame hidden:", page.ui.retirement_frame.isHidden())
    print("scenario name placeholder:", page.ui.scenario_name_box.placeholderText())
    print("annual load growth:", repr(page.ui.annual_load_growth_box.text()))
    print(
        "capital costs items:",
        [page.ui.capital_cost_box.itemText(i) for i in range(page.ui.capital_cost_box.count())],
    )
    print(
        "rps items:",
        [page.ui.rps_box.itemText(i) for i in range(page.ui.rps_box.count())],
    )
    print(
        "transmission items:",
        [page.ui.transmission_box.itemText(i) for i in range(page.ui.transmission_box.count())],
    )
    sys.exit(app.exec())


if __name__ == "__main__":
    main()