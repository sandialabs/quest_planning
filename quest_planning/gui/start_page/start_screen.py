# -*- coding: utf-8 -*-
"""
Control of the Start page.
"""
import os
from PySide6.QtCore import (
    QThreadPool,
    Qt,
    QUrl
)
from PySide6.QtWidgets import (
    QMenu,
    QWidget,
    QMessageBox,
    QTextBrowser,
    QDialog,
    QVBoxLayout
)
from PySide6.QtGui import QDesktopServices
from quest_planning.gui.start_page.ui.ui_start_screen import Ui_start_screen
from quest_planning.gui.tools.tools import TabAnimator#NOT USED
import markdown


class StartScreen(QWidget, Ui_start_screen):
    """
    The landing screen.

    Utility for buttons are imported.
    Update state based on files at launch
    """

    def __init__(self,tabWidget):
        """Initialize the home page."""
        super().__init__()
#           Set up the ui
        self.tabWidget = tabWidget
        self.setupUi(self)
        self.start_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.doc_button.clicked.connect(self.on_doc_button_clicked)
        self.start_button.setToolTip('Start QuESt Planning')
        self.doc_button.setToolTip('Open QuESt Planning README file')
        self.popup_message = QMessageBox()
        self.readme_html = None
        
        #self.results_viewer_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(5))
        # Hide the results viewer button
        #self.label_8.hide()
        #self.results_viewer_button.hide()

        #self.results_viewer_button.setToolTip('Proceed to Results Viewer to anayze scenario results')
    def on_doc_button_clicked(self):
        """
            Navigate to the documentation page and display README.md content.
        """
        readme_path = os.path.join(os.getcwd(), 'quest_planning\README.md')
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as file:
                readme_content = file.read()
            
            # Convert Markdown to HTML
            self.readme_html = markdown.markdown(readme_content)

             # Display in a QTextBrowser within a QDialog
            self.display_doc_dialog(self.readme_html)
        else:
            self.popup_message.setText("QuESt Planning Documentation in progress.")
            self.popup_message.setStandardButtons(QMessageBox.Ok)
            self.popup_message.buttonClicked.connect(self.popup_message.done(1))
            self.popup_message.exec()
    
    def display_doc_dialog(self, html_content):
        """
        Display the README content in a dialog.
        """
        dialog = QDialog(self,Qt.WindowFlags(Qt.WindowSystemMenuHint | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint))
        dialog.setWindowTitle("Documentation")
        layout = QVBoxLayout()
        text_browser = QTextBrowser()
        text_browser.setHtml(html_content)
        text_browser.setStyleSheet("background-color: white;")
        text_browser.setOpenExternalLinks(True)
        text_browser.anchorClicked.connect(lambda url: self.handle_link_click(url))
        layout.addWidget(text_browser)
        dialog.setLayout(layout)
        dialog.resize(800, 600)
        dialog.exec_()
    
    def handle_link_click(self, url):
        """
        Custom handling of link clicks. Handles external versus internal
        """
        if url.scheme() in ['http', 'https']:
            # Open external links in the default web browser
            QDesktopServices.openUrl(url)
            #self.display_doc_dialog(self.readme_html)
            return
        else:
            # Handle internal links here. Do nothing
            pass
            
        
        