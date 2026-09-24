# -*- coding: utf-8 -*-
"""
Control of the main window for the QuESt Planning Application.
"""
import sys

from PySide6.QtCore import Qt, QSettings, QTimer
from PySide6.QtGui import QIcon, QImageReader, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from quest_planning.ui.forms.main_window.ui_main_window import Ui_MainWindow
from quest_planning.ui.pages.start_screen import LandingPage
from quest_planning.ui.pages.power_system_data import PowerSystemPage
from quest_planning.ui.pages.planning_model import PlanningModelPage
from quest_planning.ui.pages.scenario_builder import ScenarioBuilderPage
from quest_planning.ui.pages.build_run import ExecuteModelPage
from quest_planning.ui.pages.results import ResultsViewerPage
from quest_planning.ui.styles import apply_stylesheet

from quest_planning.explan.explan_data_handler import ExplanDataHandler
from quest_planning.explan.explan_optimizer import ExplanOptimizer
from quest_planning.explan.explan_results_viewer import ExplanResultsViewer
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="PIL.Image")


time_count = 0


class QuestPlanning(QMainWindow):
    """The main window that contains the stacked widget for the separate pages."""

    __pages__ = (
        ("page_landing", "btn_home"),
        ("page_power_system", "btn_power_system"),
        ("page_planning", "btn_planning"),
        ("page_scenario", "btn_scenario"),
        ("page_execute", "btn_model"),
        ("page_results", "btn_results"),
        ("page_settings", "btn_settings"),
        ("page_about", "btn_about"),
    )

    def __init__(self, *args, **kwargs):
        """Initialize the app and load in the widgets."""
        super().__init__()

        self.data_handler = ExplanDataHandler()
        self.optimizer = ExplanOptimizer(
            self.data_handler, solver=self.data_handler.solver
        )
        self.results_viewer = ExplanResultsViewer(self.data_handler)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("QuESt Planning")
        self.setWindowIcon(QIcon(":/logos/images/logo/Quest_App_Icon.svg"))

        # Apply the central application stylesheet.
        app = QApplication.instance()
        if app is not None:
            apply_stylesheet(app)

        # Show the QuESt logo in the ribbon.
        self.ui.label_logo.setPixmap(
            QPixmap(":/logos/images/logo/Quest_App_Icon_50_transparent.png")
        )
        self.ui.label_logo.setFixedSize(48, 48)
        self.ui.label_logo.setScaledContents(True)

        # Build and place the pages into the stacked widget.
        self.pages = {}
        self.pages["page_landing"] = self._make_page(
            "page_landing", LandingPage()
        )
        self.pages["page_power_system"] = self._make_page(
            "page_power_system", PowerSystemPage()
        )
        self.pages["page_planning"] = self._make_page(
            "page_planning", PlanningModelPage()
        )
        self.pages["page_scenario"] = self._make_page(
            "page_scenario", ScenarioBuilderPage()
        )
        self.pages["page_execute"] = self._make_page(
            "page_execute", ExecuteModelPage()
        )
        self.pages["page_results"] = self._make_page(
            "page_results", ResultsViewerPage()
        )
        # Remaining pages are placeholders left as their empty widget forms.
        for name in ("page_large_load", "page_settings", "page_about"):
            placeholder = self.ui.stackedWidget.findChild(QWidget, name)
            self.pages[name] = placeholder

        # Land on the home page.
        self.ui.stackedWidget.setCurrentWidget(self.pages["page_landing"])

        # Wire the ribbon buttons and the prev/next navigation.
        self.page_buttons = {}
        for page_name, button_name in self.__pages__:
            button = getattr(self.ui, button_name)
            button.setCheckable(True)
            button.clicked.connect(
                lambda _=False, name=page_name: self.show_page(name)
            )
            self.page_buttons[page_name] = button

        # Start button on the landing page advances to Power System Data.
        self.pages["page_landing"].start_requested.connect(
            lambda: self.show_page("page_power_system")
        )

        self.ui.btn_prev.clicked.connect(self.go_previous)
        self.ui.next_prev.clicked.connect(self.go_next)

        # Initial selection state for the ribbon.
        self.select_page("page_landing")

    def _make_page(self, name, widget):
        """Replace the placeholder widget with a real page widget."""
        placeholder = self.ui.stackedWidget.findChild(QWidget, name)
        index = self.ui.stackedWidget.indexOf(placeholder)
        widget.setObjectName(name)
        self.ui.stackedWidget.removeWidget(placeholder)
        self.ui.stackedWidget.insertWidget(index, widget)
        self.ui.stackedWidget.setCurrentIndex(0)
        return widget

    def show_page(self, name):
        """Switch to the given page and highlight its ribbon button."""
        widget = self.pages.get(name)
        if widget is None:
            return
        self.ui.stackedWidget.setCurrentWidget(widget)
        self.select_page(name)

    def select_page(self, name):
        """Highlight the ribbon button matching the given page."""
        for page_name, button in self.page_buttons.items():
            button.setChecked(page_name == name)

    def go_next(self):
        """Advance to the next page in the wizard order."""
        index = self.ui.stackedWidget.currentIndex()
        count = self.ui.stackedWidget.count()
        if index < count - 1:
            self.ui.stackedWidget.setCurrentIndex(index + 1)
            self._sync_ribbon()

    def go_previous(self):
        """Step back to the previous page in the wizard order."""
        index = self.ui.stackedWidget.currentIndex()
        if index > 0:
            self.ui.stackedWidget.setCurrentIndex(index - 1)
            self._sync_ribbon()

    def _sync_ribbon(self):
        """Highlight the ribbon button for the current page."""
        current = self.ui.stackedWidget.currentWidget()
        for page_name, button in self.page_buttons.items():
            button.setChecked(self.pages[page_name] is current)


class SplashScreen(QMainWindow):
    """Splash screen that fades into the main window when ready."""

    def __init__(self):
        super().__init__()
        from quest_planning.gui.splash_screen_page.ui.ui_splash_screen import (
            Ui_SplashScreen,
        )

        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # remove window decorations
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)

        # Start timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)

        self.show()

    def progress(self):
        global time_count
        value = time_count

        if time_count > 100:
            self.timer.stop()
            self.main = QuestPlanning()
            self.main.show()
            self.close()
        else:
            self.load_status_graphic(value)
            time_count += 0.4

    def load_status_graphic(self, value):
        stylesheet = """
        QFrame {
            border-radius: 125px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90,
                stop:{STOP_V1} rgba(0, 0, 0, 0),
                stop:{STOP_V2} rgba(129, 194, 64, 255));
        }
        """
        progress = (100 - value) / 100.0
        stop_v1 = str(progress - 0.001)
        stop_v2 = str(progress)
        new_style = stylesheet.replace(
            "{STOP_V1}", stop_v1
        ).replace("{STOP_V2}", stop_v2)
        self.ui.load_status_graphic.setStyleSheet(new_style)
        self.ui.label.setText(str(int(value)) + " %")


def main():
    print("Opening QuESt Planning Tool")
    # Suppress Qt warnings
    Settings = QSettings()
    Settings.clear()
    QImageReader.setAllocationLimit(0)

    app = QApplication(sys.argv)

    # Apply the central consolidated stylesheet.
    apply_stylesheet(app)

    window = SplashScreen()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
