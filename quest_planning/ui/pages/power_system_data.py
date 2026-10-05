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

from PySide6.QtWidgets import QFileDialog, QStackedWidget
from pathlib import Path

from quest_planning.ui.forms.power_system_data.ui_power_system import Ui_PowerSystemPage
from quest_planning.ui.utils.help_topics import show_error, show_help
from quest_planning.paths import BASE_DIR, DATA_DIR

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
        self.ui.file_button.clicked.connect(
            lambda: self.select_file(self.ui.file_combo_box)
        )
        self.ui.open_file_button.clicked.connect(
            lambda: self.open_file_button_clicked(
                self.ui.file_combo_box, self.ui.system_name_input
            )
        )
        self.ui.power_system_help_button.clicked.connect(
            lambda: show_help(self, "Upload Power System Data")
        )

        # wire placeholder slot stubs (with-load view)
        self.ui.load_file_button.clicked.connect(
            lambda: self.select_file(self.ui.load_file_combo_box)
        )
        self.ui.load_open_file_button.clicked.connect(
            lambda: self.open_file_button_clicked(
                self.ui.load_file_combo_box, self.ui.load_system_name_input
            )
        )
        self.ui.load_help_button.clicked.connect(
            lambda: show_help(self, "Upload Power System Data")
        )

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

    def select_file(self, combo):
        """Open a native folder picker and record the selection in the given combo box."""
        start_dir = str(DATA_DIR if DATA_DIR.is_dir() else BASE_DIR)
        selected = QFileDialog.getExistingDirectory(
            self, "Select Input Data Folder", start_dir
        )
        if not selected:
            return
        if combo.findText(selected) == -1:
            combo.addItem(selected)
        combo.setCurrentText(selected)

    def open_file_button_clicked(self, combo, name_input):
        """Load the input data from the selected folder and reveal the results."""
        data_dir = combo.currentText()
        if not data_dir:
            show_error(
                self,
                "No Data Folder",
                "Select an input data folder before opening.",
            )
            return
        try:
            # Load the CSVs available in this folder. Some datasets omit
            # optional inputs such as cap_cred.csv and prm.csv.
            data_ls = [path.stem for path in Path(data_dir).glob("*.csv")]
            self.data_handler.set_data_ls_index(data_ls)
            self.data_handler.data_dir = data_dir
            self.data_handler.get_data()

            scenario_page = self.window().pages["page_scenario"]
            scenario_page._load_forecasts()
        except Exception as exc:
            show_error(self, "Data Load Failed", str(exc))
            return
        self._populate_tiles(name_input.text())
        self._populate_plots()
        self._reveal_results()

    def _value_labels(self):
        """The four stat-tile value labels for the currently visible view."""
        u = self.ui
        if self.currentWidget() is u.power_system_data_w_load:
            return (u.load_bus_label, u.load_line_label, u.load_gen_label, u.load_sys_label)
        return (u.bus_label, u.line_label, u.gen_label, u.sys_label)

    def _populate_tiles(self, system_name):
        """Fill the stat tiles from the loaded data and the given system name."""
        d = self.data_handler
        values = (
            "{} Buses (Zones)".format(len(d.load_data[d.index("bus")])),
            "{} Branches".format(len(d.load_data[d.index("branch")])),
            "{} Generators".format(len(d.tech_nums["exist"])),
            system_name,
        )
        for label, value in zip(self._value_labels(), values):
            label.setText(value)

    def _reveal_results(self):
        """Show the overview and plot frames for the currently visible view."""
        u = self.ui
        if self.currentWidget() is u.power_system_data_w_load:
            u.frame_overview_load.show()
            u.frame_plots_load.show()
        else:
            u.frame_overview.show()
            u.frame_plots.show()

    def _plot_widgets(self):
        """The (map, gen-mix, load-profile) plot widgets for the visible view.

        The load-profile widget is None in the standard view, which has no load
        plot card.
        """
        u = self.ui
        if self.currentWidget() is u.power_system_data_w_load:
            return (
                u.load_network_map_widget,
                u.load_generation_mix,
                u.load_profile_widget,
            )
        return u.network_map_widget, u.generation_mix, None

    def _draw(self, widget, draw_fn):
        """Clear a plot widget, run draw_fn(fig, ax) against it, and refresh.

        MatplotlibWidget.error_label is never added to the widget's layout, so it
        cannot surface a message; report failures with a dialog instead and leave
        the card blank.
        """
        fig = widget.figure
        fig.clear()
        ax = fig.add_subplot(111)
        try:
            draw_fn(fig, ax)
        except Exception as exc:
            # Drop the empty axes so a failed card is genuinely blank rather than
            # showing a bare frame with tick marks.
            fig.clear()
            error = str(exc)
        else:
            error = None
        widget.canvas.draw()
        if error is not None:
            show_error(self, "Plot Error", error)

    def _populate_plots(self):
        """Draw the network map, generation mix, and load profile plots."""
        d = self.data_handler
        map_widget, genmix_widget, load_widget = self._plot_widgets()
        self._draw(
            map_widget,
            lambda fig, ax: d.create_network_diagram(fig, ax, use_map=False),
        )
        self._draw(
            genmix_widget, lambda fig, ax: d.current_generation_mix_piechart(fig, ax)
        )
        if load_widget is not None:
            self._draw(
                load_widget,
                lambda fig, ax: d.plot_load_profile(fig, ax, load_forecast="system_wide"),
            )
