import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "quest_planning"))

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from .ui.forms.landing.ui_landing import Ui_LandingPage


class LandingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LandingPage()
        self.ui.setupUi(self)

        self._logo_pixmap = self.ui.label_logo.pixmap()
        self._footer_logos = [
            self.ui.label_quest,
            self.ui.label_doe,
            self.ui.label_snl,
        ]
        self._footer_pixmaps = [lbl.pixmap() for lbl in self._footer_logos]

        self._update_logo()

    def _update_logo(self):
        label = self.ui.label_logo
        if self._logo_pixmap is None or self._logo_pixmap.isNull():
            return
        scaled = self._logo_pixmap.scaled(
            label.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        label.setPixmap(scaled)

        for lbl, orig in zip(self._footer_logos, self._footer_pixmaps):
            if orig is None or orig.isNull():
                continue
            footer_scaled = orig.scaled(
                lbl.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            lbl.setPixmap(footer_scaled)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_logo()

    def showEvent(self, event):
        super().showEvent(event)
        self._update_logo()


def main():
    app = QApplication(sys.argv)

    window = LandingPage()
    window.resize(739, 761)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
