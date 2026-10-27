# -*- coding: utf-8 -*-s
"""
Control of the Power System Data page.
"""

import os
from PySide6.QtCore import (
    QThread,
    Signal,
)
from PySide6.QtWidgets import (
    QMenu,
    QWidget,
    QFileDialog,
    QApplication,
    QVBoxLayout,
    QMessageBox
)
from quest_planning.gui.power_system_data_page.ui.ui_power_system_data import Ui_power_system_data
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from quest_planning.gui.tools.tools import ExecuteFunction
#from gui.matplotlibwidget import MatplotlibWidget
from quest_planning.gui.tools.tools import TabAnimator, ExecuteFunction, MatplotlibWidget, LoadingSplashScreen


class PowerSystemDataPage(QWidget, Ui_power_system_data):
    """
    The page for user to upload and select power system data.

    Loads data from excel/csv to the data handler.
    Displays system info on power system data page.

    Threading design
    ----------------
    Two sequential background threads are used so the main window stays
    responsive during long data loads:

      Thread 1 (read_data):   data_handler.get_data()  — pure I/O, no Qt
      Thread 2 (read_plot_data): _data_read_and_plot_worker() — matplotlib
                                  figure construction (no Qt widget calls)

    After Thread 2 finishes, the _data_ready Signal is queued onto the main
    thread's event loop where _apply_data_labels() safely updates all widgets.
    """

    # Signal emitted from the background thread with computed label strings.
    # Qt queues this onto the main thread's event loop automatically because
    # the connection is cross-thread (worker thread -> main-thread slot).
    _data_ready = Signal(str, str, str)          # bus_text, line_text, gen_text
    # Signal used to propagate error text to the map widget safely.
    _map_error = Signal(str)

    def __init__(self, tabWidget, data_handler):
        """
        Initialize the power system data page.
        Connects data reading functionality to the open file button.
        """
        super().__init__()

        self.data_handler = data_handler

        self.setupUi(self)
        self.tabWidget = tabWidget
        self.popup_message = QMessageBox()
        self.file_button.clicked.connect(self.select_file)
        self.open_file_button.clicked.connect(self.open_file_button_clicked)
        self.power_system_help_button.clicked.connect(self.display_help_message)

        self.file_button.setToolTip('Browse on computer for input data folder')
        self.open_file_button.setToolTip('Open the input data and load into QuESt Planning')

        # next and previous navigation buttons
        self.next_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.previous_button.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))

        self.next_button.setToolTip('Proceed to Planning Model Setup')
        self.previous_button.setToolTip('Return to Start Page')

        # Initially hide the power_system_data frames
        self.power_system_data_frame.hide()
        #self.divider_line.hide()
        self.bus_label.hide()
        self.line_label.hide()
        self.gen_label.hide()
        self.sys_label.hide()
        self.network_map_widget.hide()
        #self.load_profile_widget.hide()
        self.generation_mix.hide()
        self.line_bottom.hide()
        #self.line_top.hide()

        # Wire cross-thread signals to main-thread slots.
        self._data_ready.connect(self._apply_data_labels)
        self._map_error.connect(self.network_map_widget.error_label.setText)

        # Pre-fetch the matplotlib figure references while we are still on the
        # main thread so background workers can read them without touching the
        # QWidget itself.
        self._map_figure = self.network_map_widget.figure
        self._pie_figure = self.generation_mix.figure

    # ------------------------------------------------------------------
    # Help / file selection
    # ------------------------------------------------------------------

    def display_help_message(self):
        """Displays a help message in a pop-out window with an OK button."""
        self.popup_message.setIcon(QMessageBox.Information)
        self.popup_message.setWindowTitle("Upload Power System Data")
        self.popup_message.setText(
            "Use the <b><i>Browse</i></b> button to navigate to the folder of the input data. "
            "Next, use the <b><i>Open</i></b> button to open the folder and pre-process the input data."
        )
        self.popup_message.setStandardButtons(QMessageBox.Ok)
        self.popup_message.exec_()

    def select_file(self):
        """Selects file directory using a QFileDialog and adds to the file_combo_box."""
        dir_select = QFileDialog.getExistingDirectory()
        self.file_combo_box.addItem(dir_select)

    # ------------------------------------------------------------------
    # Main import pipeline
    # ------------------------------------------------------------------

    def open_file_button_clicked(self):
        """
        Reads data from the selected folder.
        Two sequential background threads are used so the main window stays
        responsive during long data loads.
        """
        self.splash_screen = LoadingSplashScreen(self, title="Loading Data")
        self.splash_screen.show_message("Loading data, please wait...")

        dir_select = self.file_combo_box.currentText()
        self.data_handler.data_dir = dir_select

        # Snapshot system name here (main thread) so the background worker
        # doesn't need to read system_name_input.text() itself.
        self._system_name = self.system_name_input.text()

        self.read_data = ExecuteFunction(self.data_handler.get_data)
        self.read_data.finished.connect(self.end_read_data)
        self.read_data.task_failed.connect(self._on_load_failed)

        self.read_plot_data = ExecuteFunction(self._data_read_and_plot_worker)
        self.read_plot_data.finished.connect(self.end_read_plot_data)
        self.read_plot_data.task_failed.connect(self._on_load_failed)

        self.read_data.start()

    # ------------------------------------------------------------------
    # Background-thread worker  (NO Qt widget calls allowed here)
    # ------------------------------------------------------------------

    def _data_read_and_plot_worker(self):
        """
        Runs entirely in a background QThread.

        Only pure data processing and matplotlib figure construction are
        performed here. All Qt widget interactions are forbidden -- they must
        be scheduled onto the main thread via signals.
        """
        # Build the matplotlib figures using the pre-fetched figure objects.
        self._plot_pie_worker()
        self._show_map_worker()

        # Compute label strings (pure data -- no widget access).
        self.data_handler.get_tech_nums()
        bus_text  = 'Buses (Zones): {}'.format(
            len(self.data_handler.load_data[self.data_handler.data_ls.index('bus')]))
        line_text = 'Branches: {}'.format(
            len(self.data_handler.load_data[self.data_handler.data_ls.index('branch')]))
        gen_text  = 'Generators: {}'.format(
            len(self.data_handler.tech_nums['exist']))

        # Emit -- Qt queues this onto the main-thread event loop.
        self._data_ready.emit(bus_text, line_text, gen_text)

    # ------------------------------------------------------------------
    # Main-thread slots  (safe to touch Qt widgets)
    # ------------------------------------------------------------------

    def _apply_data_labels(self, bus_text, line_text, gen_text):
        """
        Slot connected to _data_ready.  Called on the main thread.

        Updates all labels, shows the data panels, and gathers the final
        user inputs (system name) which require main-thread widget access.
        """
        sys_text = 'System Name: {}'.format(self.system_name_input.text())

        self.bus_label.setText(bus_text)
        self.line_label.setText(line_text)
        self.gen_label.setText(gen_text)
        self.sys_label.setText(sys_text)

        #self.divider_line.show()
        self.bus_label.show()
        self.line_label.show()
        self.gen_label.show()
        self.sys_label.show()

        # Show the data panels now that we know the data is ready.
        self.power_system_data_frame.show()
        self.line_bottom.show()
        #self.line_top.show()
        self.network_map_widget.show()
        #self.load_profile_widget.show()
        self.generation_mix.show()

        # Refresh the matplotlib canvases now the widgets are visible.
        self.generation_mix.canvas.draw()
        self.network_map_widget.canvas.draw()

        # Persist the user-supplied system name into the data handler.
        self.data_handler.set_system_name(self.system_name_input.text())
        self.data_handler.set_data_ls_index(None)

    def end_read_data(self):
        self._release_thread('read_data')
        self.read_plot_data.start()

    def end_read_plot_data(self):
        self._release_thread('read_plot_data')
        self.splash_screen.accept()

    def _on_load_failed(self):
        """
        Called on the main thread when either background thread raises an
        unhandled exception. Closes the splash screen and shows an error so
        the UI never freezes waiting for a thread that already died.
        """
        self._release_thread('read_data')
        self._release_thread('read_plot_data')
        self.splash_screen.accept()
        error_box = QMessageBox(self)
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Data Load Error")
        error_box.setText(
            "Failed to load the power system data.\n\n"
            "Please check that the selected folder contains all required CSV files "
            "and review the console output for details."
        )
        error_box.exec_()

    def _release_thread(self, attr_name):
        """
        Wait for a QThread to fully stop, then release the instance reference.

        Using *attr_name* (a string) lets us set the instance attribute to
        None, not merely delete a local variable -- which is what the old
        ``del thread`` pattern did (it only unbound the local name and left
        the ``self.read_data`` / ``self.read_plot_data`` references alive).
        """
        thread = getattr(self, attr_name, None)
        if thread is not None:
            thread.wait()
            setattr(self, attr_name, None)

    # ------------------------------------------------------------------
    # Pure matplotlib workers  (no Qt widget attribute access)
    # ------------------------------------------------------------------

    def _show_map_worker(self):
        """
        Render the network diagram into the pre-fetched figure object.
        Runs on the background thread -- no Qt widget calls.
        """
        fig = self._map_figure
        fig.clear()
        fig.tight_layout()
        fig.set_constrained_layout(True)
        ax = fig.add_subplot(111)

        try:
            self.data_handler.create_network_diagram(fig, ax, use_map=False)
        except Exception as e:
            print(f"Network diagram error: {e}")
            # Safely update the error label via the queued signal.
            self._map_error.emit("Mapping function is unavailable")

    def _plot_pie_worker(self):
        """
        Render the generation-mix pie chart into the pre-fetched figure object.
        Runs on the background thread -- no Qt widget calls.
        """
        fig = self._pie_figure
        fig.clear()
        fig.tight_layout()
        fig.set_constrained_layout(True)
        ax = fig.add_subplot(111)
        self.data_handler.current_generation_mix_piechart(fig, ax)
        # canvas.draw() is a Qt call -- deferred to _apply_data_labels on the
        # main thread.

    # ------------------------------------------------------------------
    # Legacy / convenience entry points (main-thread only)
    # ------------------------------------------------------------------

    def show_map(self):
        """Re-render the network map (call from main thread only)."""
        self._show_map_worker()
        self.network_map_widget.canvas.draw()

    def plot_pie(self):
        """Re-render the generation-mix pie chart (call from main thread only)."""
        self._plot_pie_worker()
        self.generation_mix.canvas.draw()

    def plot_load(self):
        """Function to display load profile (call from main thread only)."""
        fig = self.load_profile_widget.figure
        fig.clear()
        ax = fig.add_subplot(111)
        self.data_handler.plot_load_profile(fig, ax, load_forecast='system_wide')
        self.load_profile_widget.canvas.draw()

    def collect_inputs(self):
        """Persist user inputs from the page into the data handler (main thread only)."""
        self.data_handler.set_system_name(self.system_name_input.text())
        self.data_handler.set_data_ls_index(None)


'''
    def next_tab(self,tabWidget):
        #next and previous navigation buttons
        i = tabWidget.currentIndex()
        next_i = (i + 1) % tabWidget.count()
        tabWidget.setCurrentIndex(next_i)

    def prev_tab(self,tabWidget):
        i = tabWidget.currentIndex()
        prev_i = (i - 1) % tabWidget.count()
        tabWidget.setCurrentIndex(prev_i)
'''
