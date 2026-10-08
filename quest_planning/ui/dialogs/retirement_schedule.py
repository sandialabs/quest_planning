from typing import Any, Dict, List

from PySide6.QtWidgets import QButtonGroup, QDialog

from quest_planning.ui.forms.scenario_builder.ui_retirement_schedule import (
    Ui_RetirementSchedulePage,
)


class RetirementScheduleDialog(QDialog):
    def __init__(self, generators: Any, years: Any, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_RetirementSchedulePage()
        self.ui.setupUi(self)

        self.generators = generators
        self.years = self._normalize_years(years)
        self.generator_retirements: Dict[str, int] = {}
        self.populate_combo_boxes()

        self.retirement_mode_group = QButtonGroup(self)
        self.retirement_mode_group.setExclusive(True)
        self.retirement_mode_group.addButton(self.ui.radioButton_default)
        self.retirement_mode_group.addButton(self.ui.radioButton_tech)
        self.retirement_mode_group.addButton(self.ui.radioButton_gen)

        self.ui.btn_add_retirement.clicked.connect(self.add_retirement)
        self.ui.btn_ok.clicked.connect(self.accept)
        self.ui.btn_cancel.clicked.connect(self.reject)

        self.ui.radioButton_default.toggled.connect(
            self.update_retirement_controls
        )
        self.ui.radioButton_tech.toggled.connect(
            self.update_retirement_controls
        )
        self.ui.radioButton_gen.toggled.connect(
            self.update_retirement_controls
        )
        self.update_retirement_controls()

    @staticmethod
    def _normalize_years(years: Any) -> List[int]:
        """Return distinct integer years, skipping missing or invalid values."""
        if years is None:
            return []

        normalized = []
        for year in years:
            try:
                integer_year = int(year)
            except (TypeError, ValueError, OverflowError):
                continue
            if integer_year not in normalized:
                normalized.append(integer_year)
        return normalized

    def update_retirement_controls(self, _checked: bool = False) -> None:
        self.ui.frame_custom_tech.setEnabled(
            self.ui.radioButton_tech.isChecked()
        )
        self.ui.frame_custom_gen.setEnabled(
            self.ui.radioButton_gen.isChecked()
        )

    def add_retirement(self) -> None:
        """Add or replace a generator retirement using the current choices."""
        generator_combo = self.ui.comboBox_generator
        year_combo = self.ui.comboBox_retirement_year
        generator = generator_combo.currentText().strip()
        year = year_combo.currentData()

        if generator_combo.currentIndex() < 0 or not generator or year is None:
            return

        try:
            self.generator_retirements[generator] = int(year)
        except (TypeError, ValueError, OverflowError):
            return

    def populate_combo_boxes(self) -> None:
        """Populate generator and year choices from the supplied planning data."""
        generator_combo = self.ui.comboBox_generator
        generator_combo.clear()

        if self.generators is not None and "Gen_name" in self.generators.columns:
            names = (
                self.generators["Gen_name"]
                .dropna()
                .astype(str)
                .str.strip()
            )
            generator_names = list(dict.fromkeys(name for name in names if name))
            generator_combo.addItems(generator_names)

        year_combo = self.ui.comboBox_retirement_year
        technology_combos = (
            self.ui.comboBox_ngas,
            self.ui.comboBox_nuclear,
            self.ui.comboBox_coal,
            self.ui.comboBox_oil,
        )
        for combo_box in (year_combo, *technology_combos):
            combo_box.clear()

        for year in self.years:
            year_combo.addItem(str(year), year)

        for combo_box in technology_combos:
            combo_box.addItem("Default", None)
            for year in self.years:
                combo_box.addItem(str(year), year)

    def selected_retirement(self) -> Dict[str, Any]:
        """Return the selected mode and its values in a stable structure."""
        if self.ui.radioButton_tech.isChecked():
            technology_combos = {
                "Natural Gas": self.ui.comboBox_ngas,
                "Nuclear": self.ui.comboBox_nuclear,
                "Coal": self.ui.comboBox_coal,
                "Oil": self.ui.comboBox_oil,
            }
            values = {}
            for technology, combo_box in technology_combos.items():
                year = combo_box.currentData()
                if year is not None:
                    values[technology] = int(year)
            return {"mode": "technology", "values": values}

        if self.ui.radioButton_gen.isChecked():
            return {
                "mode": "generator",
                "values": self.generator_retirements.copy(),
            }

        return {"mode": "default", "values": {}}
