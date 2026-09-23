from PySide6.QtWidgets import QWidget

from quest_planning.ui.forms.execute_model.ui_execute_model import (
    Ui_ExecuteModelPage,
)


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
            lambda: self.display_help_message("Build & Solve Optimization Model")
        )

    def select_file(self):
        self.ui.results_file_box.addItem(
            "TBD - QFileDialog.getExistingDirectory()"
        )

    def update_output_box(self, text):
        self.ui.report_progress_box.appendPlainText(str(text))

    def on_build_button_clicked(self):
        pass

    def on_run_button_clicked(self):
        pass

    def display_help_message(self, topic):
        pass