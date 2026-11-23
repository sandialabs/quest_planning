from PySide6.QtCore import QSize, QTimer, Signal, Qt
from PySide6.QtWidgets import QSizePolicy, QWidget

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

        # Keep the source pixmap and scale it in resizeEvent.  The generated
        # form's fixed maximum size is too large for lower-resolution Windows
        # displays and otherwise causes the logo to be clipped.
        self._logo_source = self.ui.label_logo.pixmap()
        self.ui.label_logo.setScaledContents(False)
        self.ui.label_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.label_logo.setMaximumSize(QSize(16777215, 16777215))
        self.ui.frame_logo.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        self.ui.horizontalLayout.setContentsMargins(0, 12, 0, 0)

        self.setObjectName("landing_page")

        self.ui.btn_about.setToolTip("Open QuESt Planning Documentation")
        self.ui.btn_start.setToolTip("Start QuESt Planning")

        self.ui.btn_about.clicked.connect(self.about_requested.emit)
        self.ui.btn_start.clicked.connect(self.start_requested.emit)

        # The first resize can happen before the parent layouts have reached
        # their final size. Update once more after Qt has completed layout.
        QTimer.singleShot(0, self._update_logo_pixmap)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_logo_pixmap()

    def showEvent(self, event):
        super().showEvent(event)
        QTimer.singleShot(0, self._update_logo_pixmap)

    def _update_logo_pixmap(self):
        """Fit the logo to the final label bounds without clipping it."""
        if self._logo_source and not self._logo_source.isNull():
            available = self.ui.label_logo.contentsRect().size()
            if available.width() > 0 and available.height() > 0:
                self.ui.label_logo.setPixmap(
                    self._logo_source.scaled(
                        available,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation,
                    )
                )
