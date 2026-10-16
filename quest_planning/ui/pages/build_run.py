from PySide6.QtWidgets import QWidget

from quest_planning.ui.forms.execute_model.ui_execute_model import (
    Ui_ExecuteModelPage,
)
from quest_planning.ui.utils.help_topics import show_error, show_help


class ExecuteModelPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ExecuteModelPage()
        self.ui.setupUi(self)

        self.setObjectName("execute_model_page")

        self.ui.model_status_frame.setHidden(True)

        self.ui.browse_folder_button.setToolTip(
            "Browse for the folder where the results will be saved."
        )
        self.ui.build_button.setToolTip("Build the optimization model.")
        self.ui.run_button.setToolTip("Solve the optimization model.")
        self.ui.btn_model_help.setToolTip("Help: build and solve the model.")
        self.ui.solver_select_box.setToolTip(
            "Select the solver installed on this machine."
        )

        self.ui.browse_folder_button.clicked.connect(self.select_file)
        self.ui.build_button.clicked.connect(self.on_build_button_clicked)
        self.ui.run_button.clicked.connect(self.on_run_button_clicked)
        self.ui.btn_model_help.clicked.connect(
            lambda: show_help(self, "Build & Solve Optimization Model")
        )
        self.data_handler = None
        self.optimizer = None
        self.scenario_page = None

    def set_model_flow(self, data_handler, optimizer, scenario_page):
        """Connect this page to the application's shared model objects."""
        self.data_handler = data_handler
        self.optimizer = optimizer
        self.scenario_page = scenario_page

    def select_file(self):
        self.ui.results_file_box.addItem(
            "TBD - QFileDialog.getExistingDirectory()"
        )

    def update_output_box(self, text):
        self.ui.report_progress_box.appendPlainText(str(text))

    def on_build_button_clicked(self):
        if self.scenario_page is None:
            show_error(self, "Build Model", "Scenario Builder is not connected.")
            return False
        try:
            self.scenario_page.apply_scenario_to_data_handler()
            self.scenario_page.apply_large_loads_to_data_handler()
            self.data_handler.construct_load_blocks()
        except Exception as exc:
            show_error(self, "Build Model", str(exc))
            return False
        return True

    def on_run_button_clicked(self):
        if self.optimizer is None:
            return
        if not self.on_build_button_clicked():
            return
        self.optimizer.run()
