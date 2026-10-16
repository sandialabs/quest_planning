from PySide6.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit


class RPSScheduleDialog(QDialog):
    """Collect percentage RPS targets for the selected simulation years."""

    def __init__(self, years, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set Renewable Portfolio Standard")
        self._fields = {}
        layout = QFormLayout(self)
        for year in years:
            field = QLineEdit(self)
            field.setPlaceholderText("Target percent")
            self._fields[int(year)] = field
            layout.addRow(str(year), field)
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel,
            parent=self,
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

    def targets(self):
        targets = {}
        for year, field in self._fields.items():
            text = field.text().strip()
            if not text:
                raise ValueError("Enter an RPS target for every simulation year.")
            try:
                value = float(text)
            except ValueError as exc:
                raise ValueError(
                    "RPS targets must be numeric percentages."
                ) from exc
            if not 0 <= value <= 100:
                raise ValueError("RPS targets must be between 0 and 100 percent.")
            targets[year] = value
        return targets
