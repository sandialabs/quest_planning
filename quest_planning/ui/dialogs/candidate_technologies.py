from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from quest_planning.ui.forms.scenario_builder.ui_candidate_technologies import (
    Ui_CandidateTechnologiesPage,
)

_CHECKED = Qt.CheckState.Checked.value

class CandidateTechnologiesDialog(QDialog):
    """Select the candidate technologies eligible for the optimization."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CandidateTechnologiesPage()
        self.ui.setupUi(self)

        self.setObjectName("candidate_technologies_dialog")

        self._default = self.ui.checkBox_default
        self._checkboxes = [
            self.ui.checkBox_default,
            self.ui.checkBox_wind,
            self.ui.checkBox_solar,
            self.ui.checkBox_lion,
            self.ui.checkBox_flow,
            self.ui.checkBox_therm,
            self.ui.checkBox_custom,
        ]

        self.ui.frame_new_tech.setHidden(True)

        self.ui.btn_ok.clicked.connect(self.accept)
        self.ui.btn_cancel.clicked.connect(self.reject)

        self.ui.checkBox_default.stateChanged.connect(self.on_default_toggled)
        self.ui.checkBox_custom.stateChanged.connect(self.on_custom_toggled)
        for checkbox in self._specifics():
            checkbox.stateChanged.connect(self.on_technology_toggled)

    def _specifics(self):
        """Return every checkbox except the Default shortcut."""
        return [cb for cb in self._checkboxes if cb is not self._default]

    def on_default_toggled(self, state):
        """Checking Default clears and locks every specific technology."""
        if state == _CHECKED:
            for checkbox in self._specifics():
                checkbox.setChecked(False)
                checkbox.setEnabled(False)
            self.ui.frame_new_tech.setHidden(True)
        else:
            for checkbox in self._checkboxes:
                checkbox.setEnabled(True)

    def on_custom_toggled(self, state):
        """Reveal the custom technology inputs only while Custom is checked."""
        self.ui.frame_new_tech.setHidden(state != _CHECKED)

    def on_technology_toggled(self, state):
        """Default becomes available again once the last specific tech is off."""
        if state == _CHECKED:
            self._default.setChecked(False)
            self._default.setEnabled(False)
        elif not self.selected_technologies():
            self._default.setEnabled(True)

    def selected_technologies(self):
        """Return the checked technology labels in display order."""
        return [
            checkbox.text()
            for checkbox in self._checkboxes
            if checkbox.isChecked()
        ]
