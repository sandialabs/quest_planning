from dataclasses import dataclass
import math
from pathlib import Path

from PySide6.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QFileDialog,
    QTableWidgetItem,
)

from quest_planning.ui.forms.scenario_builder.ui_large_load_dialog import (
    Ui_LargeLoadDialog,
)

from quest_planning.ui.forms.scenario_builder.ui_large_load_model import (
    Ui_LargeLoadModelPage,
)
from quest_planning.ui.utils.help_topics import show_error

# This class is for the large load pane itself
class LargeLoadModelDialog(QDialog):

    def __init__(self, parent=None, large_loads=None):
        super().__init__(parent)
        self.ui = Ui_LargeLoadModelPage()
        self.ui.setupUi(self)

        self.large_loads = large_loads if large_loads is not None else []
        self.ui.table_large_loads.setColumnCount(4)
        self.ui.table_large_loads.setHorizontalHeaderLabels(
            ["ID", "BUS", "Capacity (MW)", "Deploy Year"]
        )
        self.ui.table_large_loads.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.ui.btn_add.clicked.connect(self.add_large_load)
        self.ui.btn_remove.clicked.connect(self.remove_large_load)
        self.ui.btn_ok.clicked.connect(self.accept)
        self.ui.btn_cancel.clicked.connect(self.reject)
        self.ui.checkBox.toggled.connect(self.update_load_controls)
        self.ui.checkBox_2.toggled.connect(self.update_onsite_option)
        self.update_load_controls(self.ui.checkBox.isChecked())
        self.update_onsite_option(self.ui.checkBox_2.isChecked())

    def update_load_controls(self, enabled):
        self.ui.frame.setEnabled(enabled)

    def update_onsite_option(self, enabled):
        self._onsite_resources_enabled = enabled

    def exec(self):
        self.refresh_large_load_table()
        return super().exec()

    def options(self):
        return {
            "large_load_option": self.ui.checkBox.isChecked(),
            "ll_resource_option": self.ui.checkBox_2.isChecked(),
            "large_load_flex": self.ui.checkBox_4.isChecked(),
            "large_load_growth": self.ui.doubleSpinBox.value(),
            "ll_self_sufficiency": self.ui.doubleSpinBox_2.value(),
        }

    def add_large_load(self):
        dialog = LargeLoadDialog(
            self,
            onsite_resources_enabled=self.ui.checkBox_2.isChecked(),
        )
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        try:
            load = dialog.large_load()
        except ValueError as exc:
            show_error(self, "Large Load", str(exc))
            return
        self.large_loads.append(load)
        self.refresh_large_load_table()

    def remove_large_load(self):
        row = self.ui.table_large_loads.currentRow()
        if row < 0 or row >= len(self.large_loads):
            return

        del self.large_loads[row]
        self.refresh_large_load_table()

    def refresh_large_load_table(self):
        table = self.ui.table_large_loads
        table.setRowCount(len(self.large_loads))
        for row, load in enumerate(self.large_loads):
            for column, value in enumerate(
                (load.id, load.bus, load.capacity_mw, load.deploy_year)
            ):
                table.setItem(row, column, QTableWidgetItem(str(value)))


class LargeLoadDialog(QDialog):
    """Collect the identifying and deployment fields for one large load."""

    def __init__(self, parent=None, onsite_resources_enabled=False):
        super().__init__(parent)
        self.ui = Ui_LargeLoadDialog()
        self.ui.setupUi(self)
        self._onsite_resources_enabled = onsite_resources_enabled
        self.ui.frame_onsite.setEnabled(onsite_resources_enabled)
        for field in (
            self.ui.lineEdit_max_cap,
            self.ui.lineEdit_max_energy,
            self.ui.lineEdit_power,
        ):
            field.setText("0")
        self.ui.comboBox_type.addItems(["normalized", "absolute"])
        self.ui.btn_file.clicked.connect(self.select_profile_file)
        self.ui.btn_add.clicked.connect(self.accept_large_load)
        self.ui.btn_cancel.clicked.connect(self.reject)

    def select_profile_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Large Load Profile", "", "CSV Files (*.csv);;All Files (*)"
        )
        if file_name:
            self.ui.lineEdit_file.setText(file_name)

    def accept_large_load(self):
        try:
            self.large_load()
        except ValueError as exc:
            show_error(self, "Invalid Large Load", str(exc))
            return
        self.accept()

    @staticmethod
    def _required_text(field, label):
        value = field.text().strip()
        if not value:
            raise ValueError("{} cannot be empty.".format(label))
        return value

    @staticmethod
    def _required_number(field, label, integer=False, positive=False):
        text = field.text().strip()
        if not text:
            raise ValueError("{} cannot be empty.".format(label))
        try:
            value = int(text) if integer else float(text)
        except ValueError as exc:
            raise ValueError("{} must be a number.".format(label)) from exc
        if not integer and not math.isfinite(value):
            raise ValueError("{} must be a finite number.".format(label))
        if positive and value <= 0:
            raise ValueError("{} must be greater than zero.".format(label))
        if not positive and value < 0:
            raise ValueError("{} cannot be negative.".format(label))
        return value

    @classmethod
    def _optional_number(cls, field, label):
        if not field.text().strip():
            return 0
        return cls._required_number(field, label)

    def large_load(self):
        load_id = self._required_text(self.ui.lineEdit_id, "ID")
        bus = self._required_number(
            self.ui.lineEdit_bus, "Bus", integer=True, positive=True
        )
        capacity_mw = self._required_number(
            self.ui.lineEdit_cap, "Capacity (MW)", positive=True
        )
        deploy_year = self._required_number(
            self.ui.lineEdit_deploy, "Deploy Year", integer=True, positive=True
        )
        profile_file = self._required_text(self.ui.lineEdit_file, "Profile file")
        if not Path(profile_file).suffix:
            raise ValueError("Profile file must include its file extension.")

        ng_candidate = (
            self._onsite_resources_enabled
            and self.ui.checkBox_ngas_cand.isChecked()
        )
        bess_candidate = (
            self._onsite_resources_enabled
            and self.ui.checkBox_bess.isChecked()
        )
        ng_capacity = (
            self._required_number(
                self.ui.lineEdit_max_cap,
                "Natural Gas Max Capacity (MW)",
                positive=True,
            )
            if ng_candidate
            else self._optional_number(
                self.ui.lineEdit_max_cap,
                "Natural Gas Max Capacity (MW)",
            )
        )
        bess_energy = (
            self._required_number(
                self.ui.lineEdit_max_energy,
                "BESS Max Energy (MWh)",
                positive=True,
            )
            if bess_candidate
            else self._optional_number(
                self.ui.lineEdit_max_energy,
                "BESS Max Energy (MWh)",
            )
        )
        bess_power = (
            self._required_number(
                self.ui.lineEdit_power,
                "BESS Max Power (MW)",
                positive=True,
            )
            if bess_candidate
            else self._optional_number(
                self.ui.lineEdit_power,
                "BESS Max Power (MW)",
            )
        )
        onsite_resources = {
            "ng": {
                "candidate": ng_candidate,
                "max_capacity_mw": ng_capacity,
            },
            "bess": {
                "candidate": bess_candidate,
                "max_energy_mwh": bess_energy,
                "max_power_mw": bess_power,
            },
        }
        return LargeLoadData(
            id=load_id,
            bus=bus,
            capacity_mw=capacity_mw,
            deploy_year=deploy_year,
            profile_file=Path(profile_file).name,
            profile_type=self.ui.comboBox_type.currentText() or "normalized",
            onsite_resources=onsite_resources,
        )


# This class is for the Large Load Object that holds each specfic large load
@dataclass
class LargeLoadData:
    id: str
    bus: int
    capacity_mw: float
    deploy_year: int
    profile_file: str
    profile_type: str
    onsite_resources: dict

    def to_config(self):
        return {
            "id": self.id,
            "bus": self.bus,
            "capacity_mw": self.capacity_mw,
            "deploy_year": self.deploy_year,
            "profile_file": self.profile_file,
            "profile_type": self.profile_type,
            "onsite_resources": self.onsite_resources,
        }

