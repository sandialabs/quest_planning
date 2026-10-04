import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QListWidget, QProgressBar, QMessageBox, QComboBox
)
from PySide6.QtCore import Qt, QThread, Signal
import matplotlib.dates as mdates
from quest_planning.gui.scenario_viewer_page.ui.ui_scenario_widget import  Ui_scenario_view_widget
class GraphBuilder:
    def __init__(self):
        self.tech_colors = {
            'Nuclear': 'darkred',
            'Coal': 'black',
            'Oil_CT': 'slategrey',
            'Oil_ST': 'lightslategrey',
            'Hydro': 'steelblue',
            'Gas': 'darkgrey',
            'Gas_CC': 'silver',
            'Gas_CT': 'dimgray',
            'Gas (New)': 'silver',
            'Geothermal': 'rosybrown',
            'Wind PPA': 'darkgreen',
            'Wind_PPA': 'darkgreen',
            'Wind': 'darkgreen',
            'Solar': 'yellow',
            'Solar_PPA': 'yellow',
            'Solar_RT': 'khaki',
            'CSP': 'darkgoldenrod',
            'Solar PPA': 'goldenrod',
            'ES PPA': 'lightsteelblue',
            'ES_PPA': 'lightsteelblue',
            'ES': 'lightsteelblue',
            'Nat. Gas H2 Conv. (New)': 'lightgrey',
            'Wind (New)': 'lime',
            'Solar (New)': 'gold',
            'ES 4hr (New)': 'royalblue',
            'ES 6hr (New)': 'blue',
            'ES 8hr (New)': 'slateblue',
            'ES 10hr (New)': 'darkviolet',
            'ES 100hr (New)': 'deeppink',
            'ES (2-4 hrs.)': 'royalblue',
            'Li-Ion Battery (New)': 'royalblue',
            'Li-Ion Battery (New) (0-2 hrs.)': '#add8e6',
            'Li-Ion Battery (New) (2-4 hrs.)': '#87ceeb',
            'Li-Ion Battery (New) (4-6 hrs.)': '#4682b4',
            'Li-Ion Battery (New) (6-8 hrs.)': '#4169e1',
            'Li-Ion Battery (New) (8-10 hrs.)': '#0000ff',
            'Li-Ion Battery (New) (10-15 hrs.)': '#0000cd',
            'Li-Ion Battery (New) (15-24 hrs.)': '#00008b',
            'Li-Ion Battery (New) (24+ hrs.)': '#000080',
            'Flow Battery (New)': 'darkviolet',
            'Grav (New)': 'orangered',
            'PSH (New)': 'darkblue',
            'Therm (New)': 'salmon',
            'CAES (New)': 'chocolate',
            'Demand Response (New)': 'cyan',
            'LDES (New)': 'deeppink',
            'Zinc (New)': 'darkturquoise',
            'Hydrogen (New)': 'pink',
            'Iron Air (New)': 'white',
            'ES PPA-charge': 'lightblue',
            'ES-discharge': 'lightblue',
            'ES 4hr (New)-charge': 'lightskyblue',
            'ES 6hr (New)-charge': 'deepskyblue',
            'ES 8hr (New)-charge': 'steelblue',
            'ES 10hr (New)-charge': 'darkslateblue',
            'ES 100hr (New)-charge': 'darkblue',
            'Li-Ion Battery (New)-charge': 'royalblue',
            'Li-Ion Battery 1 (New)-charge': 'royalblue',
            'Li-Ion Battery 2 (New)-charge': 'royalblue',
            'Li-Ion Battery 3 (New)-charge': 'royalblue',
            'Li-Ion Battery 4 (New)-charge': 'royalblue',
            'Li-Ion Battery 5 (New)-charge': 'royalblue',
            'Li-Ion Battery 6 (New)-charge': 'royalblue',
            'Li-Ion Battery 7 (New)-charge': 'royalblue',
            'Li-Ion Battery 8 (New)-charge': 'royalblue',
            'Li-Ion Battery 9 (New)-charge': 'royalblue',
            'Li-Ion Battery 10 (New)-charge': 'royalblue',
            'Flow Battery (New)-charge': 'darkviolet',
            'Grav (New)-charge': 'orangered',
            'PSH (New)-charge': 'darkblue',
            'Therm (New)-charge': 'salmon',
            'CAES (New)-charge': 'chocolate',
            'LDES (New)-charge': 'darkblue',
            'Zinc (New)-charge': 'darkturquoise',
            'Hydrogen (New)-charge': 'pink',
            'ES PPA-discharge': 'lightpink',
            'ES-charge': 'lightpink',
            'ES 4hr (New)-discharge': 'hotpink',
            'ES 6hr (New)-discharge': 'deeppink',
            'ES 8hr (New)-discharge': 'mediumvioletred',
            'ES 10hr (New)-discharge': 'mediumorchid',
            'ES 100hr (New)-discharge': 'purple',
            'Li-Ion Battery (New)-discharge': 'hotpink',
            'Li-Ion Battery 1 (New)-discharge': 'hotpink',
            'Li-Ion Battery 2 (New)-discharge': 'hotpink',
            'Li-Ion Battery 3 (New)-discharge': 'hotpink',
            'Li-Ion Battery 4 (New)-discharge': 'hotpink',
            'Li-Ion Battery 5 (New)-discharge': 'hotpink',
            'Li-Ion Battery 6 (New)-discharge': 'hotpink',
            'Li-Ion Battery 7 (New)-discharge': 'hotpink',
            'Li-Ion Battery 8 (New)-discharge': 'hotpink',
            'Li-Ion Battery 9 (New)-discharge': 'hotpink',
            'Li-Ion Battery 10 (New)-discharge': 'hotpink',
            'Flow Battery (New)-discharge': 'mediumorchid',
            'Grav (New)-discharge': 'lightsalmon',
            'PSH (New)-discharge': 'lightblue',
            'Therm (New)-discharge': 'salmon',
            'CAES (New)-discharge': 'sandybrown',
            'LDES (New)-discharge': 'purple',
            'Zinc (New)-discharge': 'aquamarine',
            'Hydrogen (New)-discharge': 'plum',
            'Curtailment': 'moccasin'
        }

    def color_tech(self, tech_name):
        return self.tech_colors.get(tech_name, '#7f7f7f')


    def stacked_grouped_bar_with_hatching(self, scenarios, figsize):
        import matplotlib.patches as mpatches

        scenario_names = list(scenarios.keys())
        num_scenarios = len(scenarios)
        fig, ax = plt.subplots(figsize=figsize)

        all_years = sorted({int(y) for s in scenarios.values() for y in s['P_cap_total']['y'].unique()})

        # Gather all techs including duration-binned storage names
        techs = set()
        for s in scenarios.values():
            techs.update(s['P_cap_total']['Tech_Name'].unique())

            df = s['P_cap_total'].copy()
            store = s['Store'].copy()

            df_es = df[df['Technology'].isin(store['Technology'])].copy()
            df_es.loc[:, 'Energy'] = store['Value'].values
            df_es.loc[:, 'Duration'] = df_es['Energy'] / df_es['Value']
            bins = [0, 2, 4, 6, 8, 10, 15, 24, np.inf]
            labels = ['0-2 hrs.', '2-4 hrs.', '4-6 hrs.', '6-8 hrs.', '8-10 hrs.', '10-15 hrs.', '15-24 hrs.', '24+ hrs.']
            df_es.loc[:, 'Duration_Bin'] = pd.cut(df_es['Duration'], bins=bins, labels=labels, right=False)
            df_es.loc[:, 'Tech_Name'] = df_es.apply(
                lambda row: f"{row['Tech_Name']} ({row['Duration_Bin']})"
                if pd.notnull(row['Duration_Bin']) else row['Tech_Name'],
                axis=1
            )
            techs.update(df_es['Tech_Name'].unique())

        techs = sorted(techs)
        bar_width = 0.8 / num_scenarios
        hatches = ['///', 'xxx', '...', '\\\\\\', '++', 'oo', '**']

        for s_idx, (name, data) in enumerate(scenarios.items()):
            df = data['P_cap_total'].reset_index(drop=True)
            store = data['Store'].reset_index(drop=True)

            df_es = df[df['Technology'].isin(store['Technology'])].copy()
            df_es.loc[:, 'Energy'] = store['Value'].values
            df_es.loc[:, 'Duration'] = df_es['Energy'] / df_es['Value']
            bins = [0, 2, 4, 6, 8, 10, 15, 24, np.inf]
            labels = ['0-2 hrs.', '2-4 hrs.', '4-6 hrs.', '6-8 hrs.', '8-10 hrs.', '10-15 hrs.', '15-24 hrs.', '24+ hrs.']
            df_es.loc[:, 'Duration_Bin'] = pd.cut(df_es['Duration'], bins=bins, labels=labels, right=False)
            df_es.loc[:, 'Tech_Name'] = df_es.apply(
                lambda row: f"{row['Tech_Name']} ({row['Duration_Bin']})"
                if pd.notnull(row['Duration_Bin']) else row['Tech_Name'],
                axis=1
            )

            df.update(df_es)
            pivot = df[df['Value'] != 0].pivot_table(index='y', columns='Tech_Name', values='Value', aggfunc='sum').fillna(0) / 1000

            for i, year in enumerate(all_years):
                x_left = i - (bar_width * num_scenarios / 2) + s_idx * bar_width
                bottom = 0
                for tech in techs:
                    value = pivot.loc[year, tech] if year in pivot.index and tech in pivot.columns else 0
                    if value > 0:
                        ax.bar(x_left, value, bar_width, bottom=bottom,
                            color=self.color_tech(tech),
                            edgecolor='black', hatch=hatches[s_idx % len(hatches)])
                        bottom += value

        ax.set_xticks(range(len(all_years)))
        ax.set_xticklabels(all_years, rotation=45)
        ax.set_ylabel("Capacity (GW)")
        ax.set_title("Stacked Grouped Bar Plot of Scenarios")

        tech_patches = [mpatches.Patch(color=self.color_tech(t), label=t) for t in techs]
        scenario_patches = [mpatches.Patch(facecolor='white', edgecolor='black', hatch=h, label=name)
                            for h, name in zip(hatches, scenario_names)]
        ax.legend(handles=tech_patches + scenario_patches, loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        plt.show()



    def timeseries_plot(self, scenarios, sheet_name=None, figsize=(18, 6)):
        fig, ax = plt.subplots(figsize=figsize)

        for scenario_name, sheets in scenarios.items():
            for s_name, df in sheets.items():
                if sheet_name is not None and s_name != sheet_name:
                    continue  # only plot the matching sheet, if specified

                df = df.copy()
                hour_cols = [col for col in df.columns if str(col).isdigit() or isinstance(col, int)]

                long_df = df.melt(id_vars=['y'], value_vars=hour_cols, var_name='Hour', value_name='Value')
                long_df['Hour'] = long_df['Hour'].astype(int)
                long_df = long_df.groupby(['y', 'Hour'])['Value'].sum().reset_index()
                long_df['TimeIndex'] = long_df['y'].astype(str) + '-' + long_df['Hour'].astype(str)

                label = f"{scenario_name} - {s_name}"
                ax.plot(long_df['TimeIndex'], long_df['Value'], label=label)

        ax.set_title("Time-Series Comparison")
        ax.set_xlabel("Year-Hour")
        ax.set_ylabel("Value")
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    


    # def curtailment_comparison_plot(self, scenarios, figsize):
    #     fig, ax = plt.subplots(figsize=figsize)
    #     for name, data in scenarios.items():
    #         if 'Curt' not in data:
    #             continue
    #         df = data['Curt']
    #         hour_cols = [col for col in df.columns if isinstance(col, int) or str(col).isdigit()]
    #         long_df = df.melt(id_vars=['y'], value_vars=hour_cols, var_name='Hour', value_name='Curtailment')
    #         long_df = long_df.groupby(['y', 'Hour'])['Curtailment'].sum().reset_index()
    #         long_df['TimeIndex'] = long_df['y'].astype(str) + '-' + long_df['Hour'].astype(str)
    #         ax.plot(long_df['TimeIndex'], long_df['Curtailment'], label=name)

    #     ax.set_title("Curtailment Comparison")
    #     ax.set_xlabel("Year-Hour")
    #     ax.set_ylabel("Curtailment (MW or MWh)")
    #     ax.legend()
    #     plt.xticks(rotation=45)
    #     plt.tight_layout()
    #     plt.show()

    # def timeseries_line_plot(self, scenarios, figsize):
    #     fig, ax = plt.subplots(figsize=figsize)

    #     for scenario_name, sheets in scenarios.items():
    #         for sheet_name, df in sheets.items():
    #             hour_cols = [col for col in df.columns if isinstance(col, int) or str(col).isdigit()]
    #             long_df = df.melt(id_vars=['y'], value_vars=hour_cols, var_name='Hour', value_name='Value')
    #             long_df = long_df.groupby(['y', 'Hour'])['Value'].sum().reset_index()

    #             # Fix: parse year safely
    #             long_df['Datetime'] = pd.to_datetime(long_df['y'].astype(int).astype(str), format='%Y') + pd.to_timedelta(long_df['Hour'], unit='h')

    #             label = f"{scenario_name} - {sheet_name}"
    #             ax.plot(long_df['Datetime'], long_df['Value'], label=label)

    #     ax.set_title("Time-Series Comparison")
    #     ax.set_xlabel("Date")
    #     ax.set_ylabel("Value")
    #     ax.legend()

    #     ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    #     ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    #     plt.setp(ax.get_xticklabels(), rotation=45, ha='right', fontsize=9)

    #     plt.tight_layout()
    #     plt.show()

class SheetLoader(QThread):
    finished = Signal(str, str, pd.DataFrame)

    def __init__(self, scenario, path, sheet_name):
        super().__init__()
        self.scenario = scenario
        self.path = path
        self.sheet_name = sheet_name

    def run(self):
        xls = pd.ExcelFile(self.path)
        df = xls.parse(self.sheet_name)
        self.finished.emit(self.scenario, self.sheet_name, df)

class ScenarioSelectionWidget(QWidget, Ui_scenario_view_widget):

    def __init__(self, viewer):

        super().__init__()
        self.setupUi(self)
        self.viewer = viewer
        self.file_paths = {}
        self.loaded_scenarios = {}
        self.scenario_sheet_names = {}
        self.loaders = {}

        self.progbar.setValue(0)
        self.loaded_files_list = QListWidget()
        self.sheet_list = QListWidget()
        self.selected_sheets_list = QListWidget()

        self.loaded_files_list.itemClicked.connect(self.populate_sheet_list)
        self.sheet_list.itemDoubleClicked.connect(self.add_sheet)
        self.selected_sheets_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.selected_sheets_list.customContextMenuRequested.connect(self.remove_sheet)

        self.verticalLayout_excel.insertWidget(0, self.loaded_files_list)
        self.verticalLayout_select.insertWidget(0, self.sheet_list)
        self.verticalLayout_selected.insertWidget(0, self.selected_sheets_list)

        self.load_button.clicked.connect(self.select_excel_files)

        self.plot_button.clicked.connect(self.plot_selected)

    def select_excel_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Excel Files", "", "Excel Files (*.xlsx *.xls)")
        if not files:
            return
        self.file_paths = {os.path.splitext(os.path.basename(f))[0]: f for f in files}
        self.loaded_files_list.clear()
        for name in self.file_paths:
            self.loaded_files_list.addItem(name)
        self.loaded_scenarios.clear()
        self.scenario_sheet_names.clear()

    def populate_sheet_list(self, item):
        scenario = item.text()
        self.sheet_list.clear()

        if scenario not in self.scenario_sheet_names:
            self.progbar.setRange(0, 0)
            xls = pd.ExcelFile(self.file_paths[scenario])
            sheet_names = xls.sheet_names
            self.scenario_sheet_names[scenario] = sheet_names
            if scenario not in self.loaded_scenarios:
                self.loaded_scenarios[scenario] = {}
            self.progbar.setRange(0, 100)
            self.progbar.setValue(100)

        # Show all known sheets for this scenario
        self.sheet_list.addItems([f"{scenario}::{s}" for s in self.scenario_sheet_names[scenario]])

    def add_sheet(self, item):
        text = item.text()
        scenario, sheet = text.split("::")

        if sheet in self.loaded_scenarios.get(scenario, {}):
            if not any(self.selected_sheets_list.item(i).text() == text
                       for i in range(self.selected_sheets_list.count())):
                self.selected_sheets_list.addItem(text)
            return

        self.progbar.setRange(0, 0)
        loader = SheetLoader(scenario, self.file_paths[scenario], sheet)
        loader.finished.connect(self.on_sheet_loaded)
        loader.start()
        self.loaders[sheet] = loader

    def on_sheet_loaded(self, scenario, sheet, df):
        self.loaded_scenarios[scenario][sheet] = df
        item_text = f"{scenario}::{sheet}"
        if not any(self.selected_sheets_list.item(i).text() == item_text
                   for i in range(self.selected_sheets_list.count())):
            self.selected_sheets_list.addItem(item_text)
        self.progbar.setRange(0, 100)
        self.progbar.setValue(100)

    def remove_sheet(self, pos):
        item = self.selected_sheets_list.itemAt(pos)
        if item:
            self.selected_sheets_list.takeItem(self.selected_sheets_list.row(item))

    def plot_selected(self):
        selected = {}
        for i in range(self.selected_sheets_list.count()):
            text = self.selected_sheets_list.item(i).text()
            scenario, sheet = text.split("::")
            if scenario not in selected:
                selected[scenario] = {}
            selected[scenario][sheet] = self.loaded_scenarios[scenario][sheet]

        plot_type = self.graph_type_combo.currentText()

        if plot_type == "Stacked Capacity Duration":
            if all('P_cap_total' in s and 'Store' in s for s in selected.values()):
                self.viewer.stacked_grouped_bar_with_hatching(selected, figsize=(18, 8))
            else:
                QMessageBox.warning(self, "Missing Sheets", "Each scenario must include 'P_cap_total' and 'Store'.")

        elif plot_type == "Curtailment Comparison":
            if all('Curt' in s for s in selected.values()):
                self.viewer.timeseries_plot(selected, sheet_name="Curt", figsize=(18, 6))
            else:
                QMessageBox.warning(self, "Missing Curt Sheet", "Each scenario must include 'Curt'.")

        # elif plot_type == "Time-Series":
        #     if len(selected) < 1:
        #         QMessageBox.warning(self, "No Data", "Please select at least one sheet to plot.")
        #         return
        #     all_sheets = set(s for sheets in selected.values() for s in sheets)
        #     for sheet_name in all_sheets:
        #         self.viewer.timeseries_plot(selected, sheet_name=sheet_name, figsize=(18, 6))
        elif plot_type == "Time-Series":
            if len(selected) < 1:
                QMessageBox.warning(self, "No Data", "Please select at least one sheet to plot.")
                return
            # Pass all selected sheets into the same graph
            self.viewer.timeseries_plot(selected, sheet_name=None, figsize=(18, 6))

        else:
            QMessageBox.warning(self, "Unsupported Graph", f"The graph type '{plot_type}' is not implemented yet.")




    # def plot_selected(self):
    #     selected = {}
    #     for i in range(self.selected_sheets_list.count()):
    #         text = self.selected_sheets_list.item(i).text()
    #         scenario, sheet = text.split("::")
    #         if scenario not in selected:
    #             selected[scenario] = {}
    #         selected[scenario][sheet] = self.loaded_scenarios[scenario][sheet]

    #     plot_type = self.graph_type_combo.currentText()

    #     if plot_type == "Stacked Capacity Duration":
    #         if all('P_cap_total' in s and 'Store' in s for s in selected.values()):
    #             self.viewer.stacked_grouped_bar_with_hatching(selected, figsize=(18, 8))
    #         else:
    #             QMessageBox.warning(self, "Missing Sheets", "Each scenario must include 'P_cap_total' and 'Store'.")

    #     # elif plot_type == "Curtailment Comparison":
    #     #     if all('Curt' in s for s in selected.values()):
    #     #         self.viewer.curtailment_comparison_plot(selected, figsize=(18, 6))
    #     #     else:
    #     #         QMessageBox.warning(self, "Missing Curt Sheet", "Each scenario must include 'Curt'.")

    #     elif plot_type == "Time-Series":
    #         if len(selected) < 1:
    #             QMessageBox.warning(self, "No Data", "Please select at least one sheet to plot.")
    #             return
    #         self.viewer.timeseries_line_plot(selected, figsize=(18, 6))

    #     else:
    #         QMessageBox.warning(self, "Unsupported Graph", f"The graph type '{plot_type}' is not implemented yet.")

    # def plot_selected(self):
    #     selected = {}
    #     for i in range(self.selected_sheets_list.count()):
    #         text = self.selected_sheets_list.item(i).text()
    #         scenario, sheet = text.split("::")
    #         if scenario not in selected:
    #             selected[scenario] = {}
    #         selected[scenario][sheet] = self.loaded_scenarios[scenario][sheet]

    #     plot_type = self.graph_type_combo.currentText()

    #     if plot_type == "Stacked Capacity Duration":
    #         if all('P_cap_total' in s and 'Store' in s for s in selected.values()):
    #             self.viewer.stacked_grouped_bar_with_hatching(selected, figsize=(18, 8))
    #         else:
    #             QMessageBox.warning(self, "Missing Sheets", "Each scenario must include 'P_cap_total' and 'Store'.")
    #     elif plot_type == "Curtailment Comparison":
    #         if all('Curt' in s for s in selected.values()):
    #             self.viewer.curtailment_comparison_plot(selected, figsize=(18, 6))
    #         else:
    #             QMessageBox.warning(self, "Missing Curt Sheet", "Each scenario must include 'Curt'.")
    #     elif plot_type == "Time-Series":
    #         used_sheets = set()
    #         for i in range(self.selected_sheets_list.count()):
    #             _, sheet = self.selected_sheets_list.item(i).text().split("::")
    #             used_sheets.add(sheet)
    #         if len(used_sheets) != 1:
    #             QMessageBox.warning(self, "Multiple Sheets", "Please select exactly one same-named sheet from each scenario for Time-Series.")
    #             return
    #         sheet_name = used_sheets.pop()
    #         if all(sheet_name in s for s in selected.values()):
    #             self.viewer.timeseries_line_plot(selected, sheet_name=sheet_name, figsize=(18, 6))
    #         else:
    #             QMessageBox.warning(self, "Missing Sheet", f"Each scenario must include '{sheet_name}'.")
    #     else:
    #         QMessageBox.warning(self, "Unsupported Graph", f"The graph type '{plot_type}' is not implemented yet.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scenario Viewer")
        self.setGeometry(100, 100, 1200, 600)
        viewer = GraphBuilder()
        self.setCentralWidget(ScenarioSelectionWidget(viewer))

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    else:
        window = MainWindow()
        window.show()


