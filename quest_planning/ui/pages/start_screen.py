from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from quest_planning.ui.forms.landing.ui_landing import Ui_LandingPage


class LandingPage(QWidget):
    """
    Home/landing page of QuESt Planning.

    Provides the QuESt Planning introduction, a Documentation button and a
    Start button that switches the application to the first setup page.
    """

    start_requested = Signal()
    about_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LandingPage()
        self.ui.setupUi(self)

        self.setObjectName("landing_page")

        self.ui.btn_about.setToolTip("Open QuESt Planning Documentation")
        self.ui.btn_start.setToolTip("Start QuESt Planning")

        self.ui.btn_about.clicked.connect(self.about_requested.emit)
        self.ui.btn_start.clicked.connect(self.start_requested.emit)