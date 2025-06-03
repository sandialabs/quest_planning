import sys
import pandas as pd
from collections import defaultdict
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget,
    QPushButton, QCheckBox, QScrollArea, QLabel, QFileDialog,
    QListWidgetItem, QTreeWidget, QTreeWidgetItem
)

class CSVScenarioSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSV Scenario Selector")
        self.resize(1000, 500)

        # Data containers
        self.csv_data = {}  # filename -> dataframe
        self.scenarios = defaultdict(list)

        # Layout setup
        layout = QHBoxLayout(self)

        # Panel 1: File list
        self.file_list = QListWidget()
        self.file_list.itemClicked.connect(self.display_columns)
        layout.addWidget(self.file_list, 1)

        # Panel 2: Column selector
        mid_panel = QVBoxLayout()
        self.column_area = QScrollArea()
        self.column_area.setWidgetResizable(True)
        self.column_widget = QWidget()
        self.column_layout = QVBoxLayout(self.column_widget)
        self.column_area.setWidget(self.column_widget)
        mid_panel.addWidget(QLabel("Columns"))
        mid_panel.addWidget(self.column_area)

        self.add_button = QPushButton("Add to Scenarios")
        self.add_button.clicked.connect(self.add_to_scenarios)
        mid_panel.addWidget(self.add_button)

        self.submit_button = QPushButton("Submit to Plotting Method")
        self.submit_button.clicked.connect(self.submit_scenarios)
        mid_panel.addWidget(self.submit_button)

        layout.addLayout(mid_panel, 2)

        # Panel 3: Scenario summary
        right_panel = QVBoxLayout()
        right_panel.addWidget(QLabel("Selected Scenarios"))
        self.scenario_view = QTreeWidget()
        self.scenario_view.setHeaderLabels(["File", "Category"])
        right_panel.addWidget(self.scenario_view)
        layout.addLayout(right_panel, 2)

        # Top Button to Load Files
        self.load_button = QPushButton("Load CSV Files")
        self.load_button.clicked.connect(self.load_files)
        layout.insertWidget(0, self.load_button)

    def load_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select CSV Files", "", "CSV Files (*.csv)")
        for file in files:
            if file not in self.csv_data:
                df = pd.read_csv(file)
                self.csv_data[file] = df
                item = QListWidgetItem(file)
                self.file_list.addItem(item)

    def display_columns(self, item):
        filename = item.text()
        df = self.csv_data.get(filename)
        if df is None:
            return

        # Clear current column layout
        for i in reversed(range(self.column_layout.count())):
            self.column_layout.itemAt(i).widget().setParent(None)

        # Add checkboxes
        for col in df.columns:
            cb = QCheckBox(col)
            cb.setObjectName(f"{filename}::{col}")
            self.column_layout.addWidget(cb)

    def add_to_scenarios(self):
        for i in range(self.column_layout.count()):
            cb = self.column_layout.itemAt(i).widget()
            if cb.isChecked():
                filename, col = cb.objectName().split("::")
                if col not in self.scenarios[filename]:
                    self.scenarios[filename].append(col)
                    self.update_scenario_view()

    def update_scenario_view(self):
        self.scenario_view.clear()
        for file, columns in self.scenarios.items():
            file_item = QTreeWidgetItem([file])
            for col in columns:
                col_item = QTreeWidgetItem([file, col])
                file_item.addChild(col_item)
            self.scenario_view.addTopLevelItem(file_item)

    def get_scenarios(self):
        """Returns the scenarios dictionary for external use"""
        return dict(self.scenarios)

    def submit_scenarios(self):
        scenarios = self.get_scenarios()
        self.handle_submit(scenarios)

    def handle_submit(self, scenarios):
        # 🚧 Replace this with your actual plotting or processing function
        print("Submitting scenarios to plot:")
        for file, columns in scenarios.items():
            print(f"{file} -> {columns}")
        # Example: self.my_custom_plot(scenarios)

def main():
    app = QApplication(sys.argv)
    window = CSVScenarioSelector()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


