from PySide6.QtWidgets import QDialog

from quest_planning.ui.forms.planning_model_setup.ui_advanced_settings import (
    Ui_AdvancedSettingsPage,
)

# (setting name, lineEdit objectName) in the order the labels are laid out.
SETTINGS_FIELDS = (
    ("Planning Reserve Margin", "lineEdit_planning"),
    ("Regulating Reserve Requirement", "lineEdit_reserve"),
    ("Spinning Reserve Requirement", "lineEdit_spinning"),
    ("Flexibility Reserve Requirement", "lineEdit_flex_reserve"),
    ("System-wide Wind Maximum Investment", "lineEdit_sys_wind_max"),
    ("System-wide Solar Maximum Investment", "lineEdit_sys_solar_max"),
    ("System-wide Gas Maximum Investment", "lineEdit_sys_gas_max"),
    ("System-wide Transmission Maximum Investment", "lineEdit_sys_trans_max"),
    ("Tax Credits Option", "lineEdit_tax_cred"),
    ("Tax Credits End Year", "lineEdit_tax_cred_end_year"),
    ("End Effects", "lineEdit_end_effects"),
)


class AdvancedSettingsDialog(QDialog):
    """Edit the advanced planning parameters."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AdvancedSettingsPage()
        self.ui.setupUi(self)

        self.setObjectName("advanced_settings_dialog")

        self._fields = [
            (name, getattr(self.ui, field)) for name, field in SETTINGS_FIELDS
        ]

        self.ui.btn_ok.clicked.connect(self.accept)
        self.ui.btn_cancel.clicked.connect(self.reject)

    def load_settings(self, settings):
        """Seed the fields from the currently stored settings."""
        for name, field in self._fields:
            field.setText(str(settings[name]))

    def settings(self):
        """Read the fields back as a settings dictionary."""
        return {
            name: self.convert_setting_value(field.text())
            for name, field in self._fields
        }

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