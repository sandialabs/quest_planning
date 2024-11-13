# -*- coding: utf-8 -*-
"""
Control of the main window for the Quest Planning Application.
"""
import sys
import ctypes
from PySide6.QtGui import (
    QIcon,
    QGuiApplication,
    QPixmap,
    QColor,
    QImageReader
)

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QVBoxLayout,
    QSizeGrip,
    QSplashScreen,
)

from PySide6.QtCore import Qt, QThread, Signal,QRect,QTimer,QSettings

from quest_planning.gui.main.ui.ui_main import Ui_MainWindow
from quest_planning.gui.start_page.start_screen import StartScreen
from quest_planning.gui.power_system_data_page.power_system_data import PowerSystemDataPage
from quest_planning.gui.planning_model_page.planning_model import PlanningModelPage
from quest_planning.gui.scenario_builder_page.scenario_builder import ScenarioBuilderPage
from quest_planning.gui.build_run_page.build_run import BuildRunPage
from quest_planning.gui.results_page.results import ResultsPage

from quest_planning.explan.explan_data_handler import ExplanDataHandler
from quest_planning.explan.explan_optimizer import ExplanOptimizer
from quest_planning.explan.explan_results_viewer import ExplanResultsViewer

from quest_planning.gui.tools.tools import TabAnimator

from quest_planning.gui.splash_screen_page.ui.ui_splash_screen import Ui_SplashScreen
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="PIL.Image")


time_count = 0

class QuestPlanning(QMainWindow):
    """The main window that contains the tab widget for the separate pages."""

    def __init__(self, *args, **kwargs):
        """Initialize the app and load in the widgets."""
        super().__init__()

        self.data_handler = ExplanDataHandler()
        self.optimizer = ExplanOptimizer(self.data_handler, solver=self.data_handler.solver)#solver will be set in build-run page
        self.results_viewer = ExplanResultsViewer(self.data_handler)

        # Set ui and main window attributes
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)#self.main_win)
        self.ui.tabWidget.setCurrentWidget(self.ui.start)
        
        #self.ui.max_resize_button.clicked.connect(lambda: self.main_win.showFullScreen())
        #self.ui.exit_app_button.clicked.connect(lambda: self.main_win.close())
        #self.ui.norm_resize_button.clicked.connect(lambda: self.main_win.showNormal())
        #self.ui.min_resize_button.clicked.connect(lambda: self.main_win.showMinimized())

        self.ui.max_resize_button.clicked.connect(self.showFullScreen)
        self.ui.exit_app_button.clicked.connect(self.close)
        self.ui.norm_resize_button.clicked.connect(self.showNormal)
        self.ui.min_resize_button.clicked.connect(self.showMinimized)
        
        self.setWindowFlag(Qt.CustomizeWindowHint,True)
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.Window, False)

        self.setWindowTitle("QuESt Planning")
        self.setWindowIcon(QIcon(":/logos/images/logo/Quest_App_Icon.svg"))
        
        
        self.ui.home_button.clicked.connect(lambda: self.ui.tabWidget.setCurrentWidget(self.ui.start))
        
        # Add widgets to their respective layouts
        self.ui.start_page_layout.addWidget(StartScreen(self.ui.tabWidget))
        self.ui.power_system_data_page_layout.addWidget(PowerSystemDataPage(self.ui.tabWidget,self.data_handler))
        self.ui.planning_model_page_layout.addWidget(PlanningModelPage(self.ui.tabWidget,self.data_handler))
        self.ui.scenario_builder_page_layout.addWidget(ScenarioBuilderPage(self.ui.tabWidget,self.data_handler,self.ui.power_system_data_page_layout.itemAt(0).widget(),self.ui.planning_model_page_layout.itemAt(0).widget(), self.optimizer, self.results_viewer))
        self.ui.build_run_page_layout.addWidget(BuildRunPage(self.ui.tabWidget,self.data_handler, self.optimizer, self.results_viewer,self.ui.planning_model_page_layout.itemAt(0).widget(),
                                                             self.ui.scenario_builder_page_layout.itemAt(0).widget()))
        self.ui.results_page_layout.addWidget(ResultsPage(self.ui.tabWidget,self.data_handler, self.optimizer, self.results_viewer))

        # Set signal to load profile box when tab is opened. This could be used in other applications to improve workflow.
        self.ui.tabWidget.currentChanged.connect(self.ui.scenario_builder_page_layout.itemAt(0).widget().on_tab_opened)
        self.ui.tabWidget.currentChanged.connect(self.ui.planning_model_page_layout.itemAt(0).widget().on_tab_opened)
        self.ui.tabWidget.currentChanged.connect(self.ui.build_run_page_layout.itemAt(0).widget().on_tab_opened)
        
        # TODO-not working, secondary feature
        self.animator = TabAnimator(self.ui.tabWidget)
        self.ui.tabWidget.currentChanged.connect(lambda index: self.animator.fade_in_tab_widget(index))
        
    def show(self):
        """Show the main window."""
        #self.showMaximized()       
        #self.main_win.show()
        self.showNormal()
        # Set initial window size
        initial_width = 750
        initial_height = 500
        #self.setGeometry(100, 100, initial_width, initial_height)

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        #remove window
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)

        
        # Start timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)#record every 15ms

        self.show()


    def progress(self):
        global time_count
        value = time_count

        if time_count > 100: #Stop when reaches 100%
            # stop timer
            self.timer.stop()

            # Show QuestPlanning
            self.main = QuestPlanning()
            self.main.show()

            # Close Splash Screen
            self.close()
        else:
            self.load_status_graphic(value)
            time_count += 0.4


    def load_status_graphic(self, value):
        stylesheet = """
        QFrame {
            border-radius: 125px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_V1} rgba(0, 0, 0, 0), stop:{STOP_V2} rgba(129, 194, 64, 255));
        }
        """#rgb(129, 194, 64);

        # Calculate load status (%) 
        progress = (100 - value) / 100.0

        # Get the stop value for display
        stop_v1 = str(progress - 0.001)
        stop_v2 = str(progress)

        #Update load status by changing style sheet color
        newStyleSheet = stylesheet.replace("{STOP_V1}", stop_v1).replace("{STOP_V2}", stop_v2)

        # update stylesheet
        self.ui.load_status_graphic.setStyleSheet(newStyleSheet)
        self.ui.label.setText(str(int(value)) + " %")


def main():
    print('Opening QuESt Planning Tool')
    # Suppress Qt warnings
    Settings = QSettings()
    Settings.clear()
    QImageReader.setAllocationLimit(0)

    app = QApplication(sys.argv)

    # Apply dark theme
    windows_default_stylesheet = """
        * {
            background-color: #f0f0f0;
            color: #000000;
        }
        
    """
    app.setStyleSheet(windows_default_stylesheet)

    # Print the current stylesheet
    #print("Current Stylesheet:")
    #print(app.styleSheet())

    window = SplashScreen()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

    '''
    QMainWindow {
        background-color: rgb(200,200,200);
    }
    QTabWidget::pane {
        border: 1px solid rgb(255,255,255);
    }
    QTabBar::tab {
        background: rgb(255,255,255);
        border: 1px solid rgb(255,255,255);
        padding: 10px;
    }
    QTabBar::tab:selected {
        background: rgb(255,255,255);
        border-bottom: 2px solid rgb(255,255,255);
    }
    QPushButton {
        background-color: rgb(255,255,255);
        border: 1px solid ;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #555555;
    }
    QPushButton:pressed {
        background-color: #666666;
    }

    #label_5 {
            background-color: rgb(129, 194, 64);
        }
        #top_right_frame{
            background-color: rgb(129, 194, 64);
        }
    '''