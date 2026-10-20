"""Reusable splash dialogs for long-running UI operations."""

from abc import ABCMeta, abstractmethod
from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QDialog, QLabel, QProgressBar, QVBoxLayout


class _QtABCMeta(type(QDialog), ABCMeta):
    """Combine Qt's widget metaclass with Python's abstract class support."""


class AbstractSplashScreen(QDialog, metaclass=_QtABCMeta):
    """Shared, non-blocking visual shell for operation-specific splash dialogs.

    Subclasses provide their title and initial status. The caller controls
    status/progress updates and closes the dialog when its operation finishes.
    """

    @abstractmethod
    def dialog_title(self) -> str:
        """Return the title shown in the window and status area."""

    @abstractmethod
    def initial_status(self) -> str:
        """Return the initial operation status shown to the user."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(self.dialog_title())
        self.setWindowIcon(QIcon(":/logos/images/logo/Quest_App_Icon.svg"))
        self.setModal(True)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 24, 28, 24)
        layout.setSpacing(14)

        self.icon_label = QLabel(self)
        self.icon_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(":/logos/images/logo/Quest_App_Icon_256.png")
        if not pixmap.isNull():
            self.icon_label.setPixmap(
                pixmap.scaled(72, 72, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
        layout.addWidget(self.icon_label)

        self.status_label = QLabel(self.initial_status(), self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setTextVisible(False)
        layout.addWidget(self.progress_bar)

        self.setMinimumWidth(340)

    def set_status(self, message: str) -> None:
        """Update the displayed status; call from the GUI thread."""
        self.status_label.setText(message)

    def set_progress(self, value: Optional[int]) -> None:
        """Set determinate progress, or use ``None`` for an activity indicator."""
        if value is None:
            self.progress_bar.setRange(0, 0)
            self.progress_bar.setTextVisible(False)
            return

        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(max(0, min(100, int(value))))
        self.progress_bar.setTextVisible(True)


class ExecuteModelSplash(AbstractSplashScreen):
    """Progress dialog shown while building and solving the optimization model."""

    def dialog_title(self) -> str:
        return "Executing Model"

    def initial_status(self) -> str:
        return "Preparing the optimization model..."
