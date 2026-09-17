import os

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QDialog, QMessageBox, QTextBrowser, QVBoxLayout, QWidget

from quest_planning.ui.forms.landing.ui_landing import Ui_LandingPage


class LandingPage(QWidget):
    """
    Home/landing page of QuESt Planning.

    Provides the QuESt Planning introduction, a Documentation button and a
    Start button that switches the application to the first setup page.
    """

    start_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LandingPage()
        self.ui.setupUi(self)

        self.setObjectName("landing_page")

        self.popup_message = QMessageBox()

        self.ui.pushButton.setToolTip("Open QuESt Planning README file")
        self.ui.pushButton_2.setToolTip("Start QuESt Planning")

        self.ui.pushButton.clicked.connect(self.on_doc_button_clicked)
        self.ui.pushButton_2.clicked.connect(self.start_requested.emit)

    def on_doc_button_clicked(self):
        """Display the QuESt Planning README.md content in a dialog."""
        readme_path = os.path.join(
            os.getcwd(), "quest_planning", "README.md"
        )
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as file:
                readme_content = file.read()
            try:
                import markdown

                html_content = markdown.markdown(readme_content)
            except ImportError:
                html_content = "<pre>{}</pre>".format(readme_content)
            self.display_doc_dialog(html_content)
        else:
            self.popup_message.setText(
                "QuESt Planning Documentation in progress."
            )
            self.popup_message.setStandardButtons(QMessageBox.Ok)
            self.popup_message.exec()

    def display_doc_dialog(self, html_content):
        """Show the README content in a QDialog with a QTextBrowser."""
        dialog = QDialog(
            self,
            Qt.WindowFlags(
                Qt.WindowSystemMenuHint
                | Qt.WindowMinMaxButtonsHint
                | Qt.WindowCloseButtonHint
            ),
        )
        dialog.setWindowTitle("Documentation")
        layout = QVBoxLayout()
        text_browser = QTextBrowser()
        text_browser.setHtml(html_content)
        text_browser.setStyleSheet("background-color: white;")
        text_browser.setOpenExternalLinks(True)
        text_browser.anchorClicked.connect(self.handle_link_click)
        layout.addWidget(text_browser)
        dialog.setLayout(layout)
        dialog.resize(800, 600)
        dialog.exec()

    def handle_link_click(self, url):
        """Open external links in the default web browser."""
        if url.scheme() in ["http", "https"]:
            QDesktopServices.openUrl(url)