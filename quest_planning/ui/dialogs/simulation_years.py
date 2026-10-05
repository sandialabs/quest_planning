from PySide6.QtWidgets import QCheckBox, QDialog, QMessageBox

from quest_planning.ui.forms.planning_model_setup.ui_simulation_years import (
    Ui_SimulationYearsPage,
)

# Checkboxes are laid out in fixed-width columns.
YEAR_GRID_COLUMNS = 5


class SimulationYearsDialog(QDialog):
    """Choose which years within the planning horizon to simulate."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SimulationYearsPage()
        self.ui.setupUi(self)

        self.setObjectName("simulation_years_dialog")
        self.setWindowTitle("Simulation Years Selection")

        self.year_checkboxes = []

        self.ui.btn_ok.clicked.connect(self.accept_selection)
        self.ui.btn_years.clicked.connect(self.toggle_all_years)

    def build_year_checkboxes(self, years, selected=()):
        """(Re)create the checkboxes for years, checking those in selected."""
        layout = self.ui.yeargridLayout

        for checkbox in self.year_checkboxes:
            layout.removeWidget(checkbox)
            checkbox.setParent(None)
            checkbox.deleteLater()
        self.year_checkboxes = []

        selected = set(selected or ())
        for index, year in enumerate(years):
            checkbox = QCheckBox(str(year), self.ui.frame_years)
            checkbox.setChecked(year in selected)
            row, column = divmod(index, YEAR_GRID_COLUMNS)
            layout.addWidget(checkbox, row, column)
            self.year_checkboxes.append(checkbox)

    def toggle_all_years(self):
        """Check every year if any is unchecked, otherwise clear them all."""
        checked = not all(checkbox.isChecked() for checkbox in self.year_checkboxes)
        for checkbox in self.year_checkboxes:
            checkbox.setChecked(checked)

    def selected_years(self):
        """Return the checked years in ascending order."""
        return [
            int(checkbox.text())
            for checkbox in self.year_checkboxes
            if checkbox.isChecked()
        ]

    def accept_selection(self):
        """Accept only once at least one year is checked."""
        if not self.selected_years():
            QMessageBox.warning(
                self,
                "Simulation Years",
                "Select at least one simulation year.",
            )
            return
        self.accept()