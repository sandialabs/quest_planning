from PySide6.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QFileDialog,
    QTableWidgetItem,
    QWidget,
)
from pathlib import Path

from quest_planning.ui.forms.scenario_builder.ui_scenario_builder import (
    Ui_ScenarioBuilderPage,
)

from quest_planning.ui.forms.scenario_builder.ui_view_scenario import (
    Ui_ViewScenarioDialog,
)

from quest_planning.ui.dialogs.candidate_technologies import (
    CandidateTechnologiesDialog,
)

from quest_planning.ui.dialogs.large_load_model import (
    LargeLoadModelDialog,
)

from quest_planning.ui.dialogs.retirement_schedule import (
    RetirementScheduleDialog,
)
from quest_planning.ui.dialogs.rps_schedule import RPSScheduleDialog
from quest_planning.ui.utils.help_topics import show_error

from quest_planning.ui.utils.help_topics import show_help


class ScenarioBuilderPage(QWidget):
    def __init__(self, data_handler, parent=None):
        super().__init__(parent)
        self.ui = Ui_ScenarioBuilderPage()
        self.ui.setupUi(self)

        self.setObjectName("scenario_builder_page")

        self.data_handler = data_handler
        self._planning_model_page = None
        self._power_system_page = None
        self._view_dialog = None
        self._candidate_technologies = None
        self._selected_candidate_technologies = None
        self._candidate_capacity_baseline = None
        self._candidate_capacity_gen_frame = None
        self._custom_rps_targets = None
        self._policy_baseline = None
        self._policy_frame = None
        self._large_load_model = None
        self.large_loads = []
        self.large_load_options = {
            "large_load_option": False,
            "ll_resource_option": False,
            "large_load_flex": False,
            "large_load_growth": 0.0,
            "ll_self_sufficiency": 0.0,
        }
        self._retirement_schedule = None
        self.retirements_print = None

        self.ui.cand_tech_frame.setHidden(True)
        self.ui.retirement_frame.setHidden(True)
        self.ui.frame_large_load_selection.setHidden(True)

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
            "Choose whether transmission expansin is allowed."
        )
        self.ui.cand_tech_button.setToolTip(
            "Select the candidate technologies for the optimization."
        )
        self.ui.gen_retirement_button.setToolTip(
            "Select the generation retirement schedule."
        )
        self.ui.btn_view_scenario.setToolTip(
            "Review the complete scenario before running the optimizer."
        )
        self.ui.btn_title_help.setToolTip(
            "Help: build a scenario in QuESt Planning."
        )

        self.ui.cand_tech_button.clicked.connect(self.on_cand_tech_button_clicked)
        self.ui.gen_retirement_button.clicked.connect(
            self.on_gen_retirement_button_clicked
        )
        self.ui.btn_view_scenario.clicked.connect(self.open_view_scenario)
        self.ui.btn_large_load.clicked.connect(self.on_large_load_button_clicked)
        self.ui.rps_box.activated.connect(self.on_rps_activated)

        self.ui.btn_title_help.clicked.connect(
            lambda: show_help(self, "Scenario Builder")
        )
        self.ui.btn_scenario_help.clicked.connect(
            lambda: show_help(self, "Select Scenario Name")
        )
        self.ui.btn_capita_help.clicked.connect(
            lambda: show_help(self, "Select Capital Costs")
        )
        self.ui.btn_load_help.clicked.connect(
            lambda: show_help(self, "Select Load Forecasts")
        )
        self.ui.btn_growth_help.clicked.connect(
            lambda: show_help(self, "Select Annual Load Growth")
        )
        self.ui.btn_generation_help.clicked.connect(
            lambda: show_help(self, "Select Renewable Portfolio Standard Goals")
        )
        self.ui.btn_trans_help.clicked.connect(
            lambda: show_help(self, "Select Transmission Expansion Option")
        )
        self.ui.btn_candidates_help.clicked.connect(
            lambda: show_help(self, "Candidate Technologies Selection")
        )
        self.ui.btn_generatio_help.clicked.connect(
            lambda: show_help(self, "Generation Retirements Selection")
        )
        self.ui.btn_model_help.clicked.connect(
            lambda: show_help(self, "Large Load Model Selection")
        )

    def set_planning_model_page(self, page):
        """Supply the Planning Model page so selections can be summarized."""
        self._planning_model_page = page

    def set_power_system_page(self, page):
        """Supply the Power System Data page for the system name."""
        self._power_system_page = page

    def _load_forecasts(self):
        if self.data_handler.load_data is None:
            return

        load_df = self.data_handler.load_data[self.data_handler.index("load")]
        hour_position = load_df.columns.get_loc("hour")
        columns = load_df.columns[hour_position + 1:].tolist()

        self.ui.load_profile_box.clear()
        self.ui.load_profile_box.addItems(columns)

    def on_cand_tech_button_clicked(self):
        """Collect the candidate technologies eligible for the optimization."""
        if self._candidate_technologies is None:
            self._candidate_technologies = CandidateTechnologiesDialog(
                self, selected=self._selected_candidate_technologies
            )

        if self._candidate_technologies.exec() != QDialog.DialogCode.Accepted:
            return

        selected = self._candidate_technologies.selected_technologies()
        self._selected_candidate_technologies = selected

        if not selected:
            self.ui.candidate_tech_box.setText("No technology selected")
            self.ui.cand_tech_frame.setHidden(True)
            return

        # heading = "<b><u>Selected Candidate Technologies:</u></b><br>"
        bullets = "<br>".join(["• {}".format(tech) for tech in selected])
        self.ui.candidate_tech_box.setHtml(bullets)
        self.ui.cand_tech_frame.setHidden(False)

    def on_rps_activated(self, _index=None):
        """Collect a custom yearly RPS schedule when requested."""
        option = self.ui.rps_box.currentText()
        if option != "Create New...":
            self._custom_rps_targets = None
            return
        years = getattr(self.data_handler, "years", None)
        if not years:
            show_error(self, "RPS Schedule", "Select simulation years first.")
            self.ui.rps_box.setCurrentIndex(0)
            return
        dialog = RPSScheduleDialog(years, self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            self.ui.rps_box.setCurrentIndex(0)
            self._custom_rps_targets = None
            return
        try:
            self._custom_rps_targets = dialog.targets()
        except ValueError as exc:
            show_error(self, "RPS Schedule", str(exc))
            self.ui.rps_box.setCurrentIndex(0)
            self._custom_rps_targets = None

    def on_large_load_button_clicked(self):
        if self._large_load_model is None:
            self._large_load_model = LargeLoadModelDialog(
                self, large_loads=self.large_loads
            )
        if self._large_load_model.exec() == QDialog.DialogCode.Accepted:
            self.large_load_options = self._large_load_model.options()

    def on_gen_retirement_button_clicked(self):
        """Configure generator retirement schedules."""
        generators = None
        load_data = getattr(self.data_handler, "load_data", None)
        data_ls = getattr(self.data_handler, "data_ls", None)
        if load_data is not None and data_ls and "gen" in data_ls:
            generators = load_data[data_ls.index("gen")]

        dialog = RetirementScheduleDialog(
            generators=generators,
            years=getattr(self.data_handler, "years", None),
            parent=self,
        )

        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        retirement = dialog.selected_retirement()

        if retirement["mode"] == "generator":
            self.data_handler.set_retirements(retirement["values"])

        self.ui.retirement_box.setHtml(
            self.format_retirement_schedule(retirement)
        )
        self.ui.retirement_frame.setHidden(False)
        self.retirements_print = retirement

    def format_retirement_schedule(self, retirement):
        mode = retirement["mode"]
        values = retirement["values"]

        if mode == "default":
            return "Default generation retirement schedule"

        if mode == "technology":
            heading = "Technology-specific retirement schedule"
        else:
            heading = "Generator-specific retirement schedule"

        if not values:
            return "{}<br>No custom retirements selected".format(heading)

        lines = "<br>".join(
            f"• {name}: {year}"
            for name, year in values.items()
        )

        return "{}<br>{}".format(heading, lines)

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
            "Simulation Years": page.ui.label_years_input.text(),
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
            "Large Loads": "{} configured".format(len(self.large_loads)),
        }

    def large_load_config(self):
        """Return the large-load settings in the data handler's config shape."""
        data_dir = getattr(self.data_handler, "data_dir", "")
        data_folder = ""
        if data_dir:
            data_folder = Path(data_dir).name
            expected_data_root = Path(__file__).resolve().parents[2] / "data_explan"
            try:
                data_folder = str(
                    Path(data_dir).resolve().relative_to(expected_data_root)
                )
            except ValueError:
                pass
        return {
            **self.large_load_options, # copes KV pairs from dict to new dict plus append rests syntatic sugar
            "data_folder": data_folder,
            "large_loads": self._large_load_records_for_handler(),
        }

    def _large_load_records_for_handler(self):
        records = [load.to_config() for load in self.large_loads]
        if not self.large_load_options.get("ll_resource_option", False):
            for record in records:
                for resource in record.get("onsite_resources", {}).values():
                    resource["candidate"] = False
        return records

    def apply_scenario_to_data_handler(self):
        """Apply the current Scenario Builder controls to the shared handler."""
        name = self.ui.scenario_name_box.text().strip()
        self.data_handler.set_scenario(name or "Base Scenario")

        load_profile = self.ui.load_profile_box.currentText().strip()
        if not load_profile:
            raise ValueError("Select a load forecast before building the model.")
        self.data_handler.set_load_profile(load_profile)

        try:
            growth = float(self.ui.annual_load_growth_box.text().strip())
        except ValueError as exc:
            raise ValueError("Annual load growth must be a number.") from exc
        self.data_handler.set_load_growth(growth)

        capital_cost = self.ui.capital_cost_box.currentText()
        self.data_handler.set_capital_cost_trend(
            "Moderate" if capital_cost == "Baseline" else capital_cost
        )
        self.data_handler.set_transmission_expansion(
            self.ui.transmission_box.currentText() == "Yes"
        )

        self.apply_rps_to_data_handler()
        self.apply_candidate_technologies_to_data_handler()

    def apply_rps_to_data_handler(self):
        """Restore default RPS data or apply the custom schedule and policy flag."""
        policy = self.data_handler.load_data[self.data_handler.index("policy")]
        if self._policy_frame is not policy:
            self._policy_frame = policy
            self._policy_baseline = policy["RPS"].copy(deep=True)
        policy["RPS"] = self._policy_baseline

        option = self.ui.rps_box.currentText()
        if option == "Create New...":
            if not self._custom_rps_targets:
                raise ValueError("Configure all custom RPS targets before building.")
            self.data_handler.set_rps_schedule(
                self._custom_rps_targets, option=option
            )
        self.data_handler.set_rps_policy(True)

    def apply_candidate_technologies_to_data_handler(self):
        """Filter dataset candidate rows according to the user's selection."""
        gen = self.data_handler.load_data[self.data_handler.index("gen")]
        if self._candidate_capacity_gen_frame is not gen:
            self._candidate_capacity_gen_frame = gen
            self._candidate_capacity_baseline = gen["CandCap"].copy(deep=True)
        gen["CandCap"] = self._candidate_capacity_baseline

        selected = self._selected_candidate_technologies
        if selected is None or "Default" in selected:
            return
        if "Custom" in selected:
            raise ValueError(
                "Custom candidate technologies are not available in this selector."
            )

        tech_by_label = {
            "Wind": {"Wind_Cand"},
            "Solar": {"Solar_Cand"},
            "Li-ion Battery 1": {"Li_Ion_Cand", "Li_Ion_Cand_1"},
            "Flow Battery": {"Flow_Cand"},
            "Therm": {"Therm_Cand"},
        }
        selected_techs = set().union(
            *(tech_by_label.get(label, set()) for label in selected)
        )
        candidate_rows = gen["Tech"].astype(str).str.endswith("_Cand")
        keep_rows = gen["Tech"].isin(selected_techs)
        gen.loc[candidate_rows & ~keep_rows, "CandCap"] = 0

    def apply_large_loads_to_data_handler(self):
        """Load configured profiles into the shared GUI data handler."""
        config = self.large_load_config()
        self.data_handler.set_large_load_option(config["large_load_option"])
        self.data_handler.set_large_load_flex(config["large_load_flex"])
        self.data_handler.set_ll_self_sufficiency(
            config["ll_self_sufficiency"]
        )
        self.data_handler.ll_load_growth = config["large_load_growth"]
        if not config["large_load_option"]:
            self.data_handler.processed_ll = []
            self.data_handler.process_large_loads()
            return
        if not config["data_folder"]:
            raise ValueError(
                "Load the power system data before configuring large loads."
            )
        for load in config["large_loads"]:
            profile_path = (
                Path(getattr(self.data_handler, "data_dir"))
                / "large_loads"
                / load["profile_file"]
            )
            if not profile_path.is_file():
                raise ValueError(
                    "Large load profile was not found: {}".format(profile_path)
                )
        self.data_handler.read_large_loads_config(config)
        self.data_handler.process_large_loads()

    def open_view_scenario(self):
        """Populate and show the View Scenario dialog."""
        if self._view_dialog is None:
            self._view_dialog = QDialog(self)
            self._view_dialog.ui = Ui_ViewScenarioDialog()
            self._view_dialog.ui.setupUi(self._view_dialog)
            self._view_dialog.ui.save_scenario_button.clicked.connect(
                self.save_info_to_file
            )
            self._view_dialog.ui.close_button.clicked.connect(
                self._view_dialog.reject
            )
            self._view_dialog.ui.large_loads_table.setEditTriggers(
                QAbstractItemView.EditTrigger.NoEditTriggers
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
        table = self._view_dialog.ui.large_loads_table
        table.setRowCount(0)
        table.setRowCount(len(self.large_loads))
        for row, load in enumerate(self.large_loads):
            for column, value in enumerate(
                (load.id, load.bus, load.capacity_mw, load.deploy_year)
            ):
                table.setItem(row, column, QTableWidgetItem(str(value)))

        self._view_dialog.exec()

    def save_info_to_file(self):
        """Write a text summary of the scenario to a user-chosen file."""
        info = self.planning_model_info()
        info.update(self.scenario_info())
        info["Large Loads"] = ""
        if self.large_loads:
            info["Large Loads"] = "\n" + "\n".join(
                "  - {id}, bus {bus}, {capacity_mw} MW, deploy {deploy_year}".format(
                    **load.to_config()
                )
                for load in self.large_loads
            )

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
