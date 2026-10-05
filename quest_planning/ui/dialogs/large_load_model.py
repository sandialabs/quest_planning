from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from quest_planning.ui.forms.scenario_builder.ui_large_load_model import (
    Ui_LargeLoadModelPage,
)

class LargeLoadModelDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LargeLoadModelPage()
        self.ui.setupUi(self)

        self.ui.btn_ok.clicked.connect(self.accept)
        self.ui.btn_cancel.clicked.connect(self.reject)

