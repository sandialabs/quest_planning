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

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog, QStackedWidget, QWidget, QPushButton,
)
from pathlib import Path

from quest_planning.ui.forms.power_system_data.ui_power_system import Ui_PowerSystemPage
from quest_planning.ui.forms.power_system_data.ui_power_system_visual_popup import Ui_PowerSystemDataVisualizationPage as UiVisualizationPopup
from quest_planning.ui.utils.help_topics import show_error, show_help
from quest_planning.paths import BASE_DIR, DATA_DIR


class VisualizationWindow(QWidget, UiVisualizationPopup):
    """Separate window containing charts for the loaded power-system data."""

    def __init__(self, data_handler, parent=None):
        # Qt.Window makes this an independent top-level window even though it
        # keeps the power-system page as its owner.
        super().__init__(parent, Qt.Window)
        self.data_handler = data_handler
        self.setWindowTitle("Power System Visualization")
        self.setupUi(self)
        self.resize(1400, 800)

    def refresh(self):
        """Redraw all charts using the currently loaded data."""
        d = self.data_handler
        bus_count = len(d.load_data[d.index("bus")])
        branch_count = len(d.load_data[d.index("branch")])
        generator_count = len(d.tech_nums["exist"])
        system_name = getattr(d, "system_name", None) or "Loaded power system"
        self.bus_label.setText(str(bus_count))
        self.line_label.setText(str(branch_count))
        self.gen_label.setText(str(generator_count))
        self.sys_label.setText(str(system_name))

        for widget in (self.network_map_widget, self.generation_mix):
            widget.figure.clear()
        map_ax = self.network_map_widget.figure.add_subplot(111)
        pie_ax = self.generation_mix.figure.add_subplot(111)
        d.create_network_diagram(
            self.network_map_widget.figure, map_ax, use_map=False
        )
        d.current_generation_mix_piechart(
            self.generation_mix.figure, pie_ax
        )
        self.network_map_widget.canvas.draw()
        self.generation_mix.canvas.draw()

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

        # Visualization is unavailable until a complete data set has loaded.
        self.visualization_window = VisualizationWindow(self.data_handler, self)
        # QWidget instances can become visible when their parent is shown;
        # keep the chart window closed until the button is clicked.
        self.visualization_window.hide()
        # Older generated UI files do not yet contain the button from the .ui
        # form, so create it here as a backwards-compatible fallback.
        if not hasattr(self.ui, "btn_visualization"):
            self.ui.btn_visualization = QPushButton("Open Visualization", self)
            self.ui.verticalLayout_main.addWidget(self.ui.btn_visualization)
        self.ui.btn_visualization.setEnabled(False)
        self.ui.btn_visualization.clicked.connect(self.show_visualization)

        self.ui.file_button.setToolTip("Browse on computer for input data folder")
        self.ui.open_file_button.setToolTip("Open the input data and load into QuESt Planning")
        self.ui.power_system_help_button.setToolTip("Help: upload power system data")
        # The form may contain either the standard view, the load view, or
        # both, depending on which generated UI file is installed.
        for name, tip in (
            ("load_file_button", "Browse on computer for input data folder"),
            ("load_open_file_button", "Open the input data and load into QuESt Planning"),
            ("load_help_button", "Help: upload power system data"),
        ):
            widget = getattr(self.ui, name, None)
            if widget is not None:
                widget.setToolTip(tip)

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
        if hasattr(self.ui, "load_file_button"):
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
        for name in ("frame_overview", "frame_plots", "frame_overview_load", "frame_plots_load"):
            widget = getattr(self.ui, name, None)
            if widget is not None:
                widget.hide()

        # The application now uses the standard page only.  Keep this helper
        # for compatibility with older callers that may still invoke it.
        self.setShowWithLoad(False)

    def show_visualization(self):
        """Open (or raise) the chart window for the loaded data."""
        try:
            self.visualization_window.refresh()
        except Exception as exc:
            self.ui.btn_visualization.setEnabled(False)
            show_error(self, "Visualization Error", str(exc))
            return
        self.visualization_window.show()
        self.visualization_window.raise_()
        self.visualization_window.activateWindow()

    @property
    def page_standard(self):
        """The standard (no load profile) view."""
        return self.ui.page_standard

    @property
    def page_with_load(self):
        """Return the legacy load page when it is present."""
        return getattr(self.ui, "power_system_data_w_load", None)

    def setShowWithLoad(self, enabled):
        """Select a view, falling back to standard when load view was removed."""
        if enabled and hasattr(self.ui, "power_system_data_w_load"):
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
            system_name = name_input.text().strip() or Path(data_dir).name
            self.data_handler.set_system_name(system_name)

            scenario_page = self.window().pages["page_scenario"]
            scenario_page._load_forecasts()
        except Exception as exc:
            show_error(self, "Data Load Failed", str(exc))
            return
        self._populate_tiles(name_input.text())
        plots_loaded = self._populate_plots()
        self._reveal_results()
        # Only allow the popup after the data and its visualizations loaded
        # successfully.
        self.ui.btn_visualization.setEnabled(plots_loaded)

    def _value_labels(self):
        """The four stat-tile value labels for the currently visible view."""
        u = self.ui
        if getattr(u, "power_system_data_w_load", None) is self.currentWidget():
            return tuple(
                getattr(u, name, None)
                for name in ("load_bus_label", "load_line_label", "load_gen_label", "load_sys_label")
            )
        return tuple(
            getattr(u, name, None)
            for name in ("bus_label", "line_label", "gen_label", "sys_label")
        )

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
            if label is not None:
                label.setText(value)

    def _reveal_results(self):
        """Show the overview and plot frames for the currently visible view."""
        u = self.ui
        if getattr(u, "power_system_data_w_load", None) is self.currentWidget():
            for name in ("frame_overview_load", "frame_plots_load"):
                widget = getattr(u, name, None)
                if widget is not None:
                    widget.show()
        else:
            for name in ("frame_overview", "frame_plots"):
                widget = getattr(u, name, None)
                if widget is not None:
                    widget.show()

    def _plot_widgets(self):
        """The (map, gen-mix, load-profile) plot widgets for the visible view.

        The load-profile widget is None in the standard view, which has no load
        plot card.
        """
        u = self.ui
        if getattr(u, "power_system_data_w_load", None) is self.currentWidget():
            return tuple(
                getattr(u, name, None)
                for name in ("load_network_map_widget", "load_generation_mix", "load_profile_widget")
            )
        return (
            getattr(u, "network_map_widget", None),
            getattr(u, "generation_mix", None),
            None,
        )

    def _draw(self, widget, draw_fn):
        """Clear a plot widget, run draw_fn(fig, ax) against it, and refresh.

        MatplotlibWidget.error_label is never added to the widget's layout, so it
        cannot surface a message; report failures with a dialog instead and leave
        the card blank.
        """
        if widget is None:
            return True
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
            return False
        return True

    def _populate_plots(self):
        """Draw the network map, generation mix, and load profile plots."""
        d = self.data_handler
        map_widget, genmix_widget, load_widget = self._plot_widgets()
        plots_loaded = self._draw(
            map_widget,
            lambda fig, ax: d.create_network_diagram(fig, ax, use_map=False),
        )
        plots_loaded = self._draw(
            genmix_widget, lambda fig, ax: d.current_generation_mix_piechart(fig, ax)
        ) and plots_loaded
        if load_widget is not None:
            plots_loaded = self._draw(
                load_widget,
                lambda fig, ax: d.plot_load_profile(fig, ax, load_forecast="system_wide"),
            ) and plots_loaded
        return plots_loaded
