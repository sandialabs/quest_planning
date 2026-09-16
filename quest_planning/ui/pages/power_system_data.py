# -*- coding: utf-8 -*-
"""
Skeleton for the Power System Data page.

This widget is a QStackedWidget designed to be embedded in the
QStackedWidget of the main window (main_window.ui -> stackedWidget ->
page_power_system). Navigation between the wizard pages is handled by
the main window shell; this widget only manages its own content.

Two views are provided (switchable via setShowWithLoad()):
  * page_standard            -- network map + generation mix (canonical names)
  * power_system_data_w_load -- adds the load profile plot (load_* names)
"""

import sys

from PySide6.QtWidgets import QApplication, QStackedWidget

from quest_planning.ui.forms.power_system_data.ui_power_system import Ui_PowerSystemPage


class PowerSystemPage(QStackedWidget):
    """
    Page for uploading and selecting power system data.

    Placeholder skeleton: UI is laid out, the data-reading logic from
    gui/power_system_data_page will be ported in here.
    """

    def __init__(self, stacked_widget=None, data_handler=None):
        """
        Initialize the power system data page.
        """
        super().__init__()

        self.stacked_widget = stacked_widget
        self.data_handler = data_handler

        self.ui = Ui_PowerSystemPage()
        self.ui.setupUi(self)

        self.ui.file_button.setToolTip("Browse on computer for input data folder")
        self.ui.open_file_button.setToolTip("Open the input data and load into QuESt Planning")
        self.ui.power_system_help_button.setToolTip("Help: upload power system data")
        self.ui.load_file_button.setToolTip("Browse on computer for input data folder")
        self.ui.load_open_file_button.setToolTip("Open the input data and load into QuESt Planning")
        self.ui.load_help_button.setToolTip("Help: upload power system data")

        # wire placeholder slot stubs (standard view)
        self.ui.file_button.clicked.connect(self.select_file)
        self.ui.open_file_button.clicked.connect(self.open_file_button_clicked)
        self.ui.power_system_help_button.clicked.connect(self.display_help_message)

        # wire placeholder slot stubs (with-load view)
        self.ui.load_file_button.clicked.connect(self.select_file)
        self.ui.load_open_file_button.clicked.connect(self.open_file_button_clicked)
        self.ui.load_help_button.clicked.connect(self.display_help_message)

        # initially hide the system overview and plot content on both views
        self.ui.frame_overview.hide()
        self.ui.frame_plots.hide()
        self.ui.frame_overview_load.hide()
        self.ui.frame_plots_load.hide()

        # start on the standard view
        self.setShowWithLoad(False)

    @property
    def page_standard(self):
        """The standard (no load profile) view."""
        return self.ui.page_standard

    @property
    def page_with_load(self):
        """The view that includes the load profile plot."""
        return self.ui.power_system_data_w_load

    def setShowWithLoad(self, enabled):
        """Switch between the standard view and the with-load view."""
        if enabled:
            self.setCurrentWidget(self.ui.power_system_data_w_load)
        else:
            self.setCurrentWidget(self.ui.page_standard)

    def display_help_message(self):
        """Placeholder: display the upload help pop-up."""
        pass

    def select_file(self):
        """Placeholder: select a data directory via QFileDialog."""
        pass

    def open_file_button_clicked(self):
        """Placeholder: load data from the selected folder."""
        pass


def main():
    app = QApplication(sys.argv)

    page = PowerSystemPage()
    page.resize(1118, 928)
    page.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()