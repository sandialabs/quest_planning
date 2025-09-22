import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.cm as cm
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QListWidget, QProgressBar, QMessageBox, QComboBox
)
from PySide6.QtCore import Qt, QThread, Signal
import matplotlib.dates as mdates
from quest_planning.gui.scenario_viewer_page.ui.ui_scenario_widget import  Ui_scenario_view_widget
from quest_planning.paths import get_path
base_dir = get_path()

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
            'Therm (New) (0-2 hrs.)': '#ffe4e1', # MistyRose
            'Therm (New) (2-4 hrs.)': '#ffb6c1',# LightPink
            'Therm (New) (4-6 hrs.)': '#ffa07a',# LightSalmon
            'Therm (New) (6-8 hrs.)': '#fa8072', # Salmon
            'Therm (New) (8-10 hrs.)': '#e9967a',  # DarkSalmon
            'Therm (New) (10-15 hrs.)': '#cd5c5c',  # IndianRed
            'Therm (New) (15-24 hrs.)': '#b22222',  # FireBrick
            'Therm (New) (24+ hrs.)': '#8b0000',  # DarkRed
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
        # Define the order of technologies: thermal, renewables, storage
        thermal_techs = ['Coal','Nuclear','Oil_CT','Oil_ST','Gas_CT','Gas_CC','Hydro','Gas (New)']
        renewable_techs = ['Wind','Solar','Solar_RT','CSP','Wind (New)','Solar (New)']
        other_techs = sorted([tech for tech in techs if tech not in thermal_techs + renewable_techs])
        ordered_techs = [tech for tech in thermal_techs + renewable_techs + other_techs if tech in techs]
        

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
            included_techs = [p for p in ordered_techs if p in pivot.columns]
            for i, year in enumerate(all_years):
                x_left = i - (bar_width * num_scenarios / 2) + s_idx * bar_width
                bottom = 0
                for tech in ordered_techs:
                    if tech in pivot.columns:
                        value = pivot.loc[year, tech] if year in pivot.index and tech in pivot.columns else 0
                        if value > 0:
                            ax.bar(x_left, value, bar_width, bottom=bottom,
                                color=self.color_tech(tech),
                                edgecolor='black', hatch=hatches[s_idx % len(hatches)])
                            bottom += value

        ax.set_xticks(range(len(all_years)))
        ax.set_xticklabels(all_years, rotation=45, fontsize=14)
        ax.set_ylabel("Capacity (GW)", fontsize=16)
        ax.set_title("Stacked Grouped Bar Plot of Scenarios", fontsize=18)

        tech_patches = [mpatches.Patch(color=self.color_tech(t), label=t) for t in included_techs]
        scenario_patches = [mpatches.Patch(facecolor='white', edgecolor='black', hatch=h, label=name)
                            for h, name in zip(hatches, scenario_names)]
        ax.legend(handles=tech_patches + scenario_patches, loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        plt.show()

    def stacked_storage(self, scenarios, figsize):
        scenario_names = list(scenarios.keys())
        num_scenarios = len(scenarios)

        fig, ax = plt.subplots(figsize=figsize)

        all_years = sorted({int(y) for s in scenarios.values() for y in s['P_cap_total']['y'].unique()})
        bins = [0, 2, 4, 6, 8, 10, 15, 24, np.inf]
        labels = ['0-2 hrs.', '2-4 hrs.', '4-6 hrs.', '6-8 hrs.', '8-10 hrs.', '10-15 hrs.', '15-24 hrs.', '24+ hrs.']

        all_techs = set()
        tech_order = []

        for s in scenarios.values():
            df = s['P_cap_total'].copy()
            store = s['Store'].copy()

            df_es = df[df['Technology'].isin(store['Technology'])].copy()
            df_es = df_es.merge(store[['Technology', 'Value']], on='Technology', suffixes=('', '_energy'))

            df_es['Duration'] = df_es['Value_energy'] / df_es['Value']
            df_es['Duration_Bin'] = pd.cut(df_es['Duration'], bins=bins, labels=labels, right=False)

            df_es['Tech_Name'] = df_es.apply(
                lambda row: f"{row['Tech_Name']} ({row['Duration_Bin']})" if pd.notnull(row['Duration_Bin']) else row['Tech_Name'],
                axis=1
            )
            all_techs.update(df_es['Tech_Name'].unique())

        # Sort techs by duration bin order
        duration_sort = {label: i for i, label in enumerate(labels)}
        def sort_key(tech_name):
            if '(' in tech_name and ')' in tech_name:
                dur = tech_name.split('(')[-1].strip(')')
                return duration_sort.get(dur, -1)
            return -1
        techs = sorted(all_techs, key=sort_key)

        bar_width = 0.8 / num_scenarios
        hatches = ['///', 'xxx', '...', '\\\\\\', '++', 'oo', '**']

        for s_idx, (name, data) in enumerate(scenarios.items()):
            df = data['P_cap_total'].reset_index(drop=True)
            store = data['Store'].reset_index(drop=True)

            df_es = df[df['Technology'].isin(store['Technology'])].copy()
            df_es = df_es.merge(store[['Technology', 'Value']], on='Technology', suffixes=('', '_energy'))

            df_es['Duration'] = df_es['Value_energy'] / df_es['Value']
            df_es['Duration_Bin'] = pd.cut(df_es['Duration'], bins=bins, labels=labels, right=False)

            df_es['Tech_Name'] = df_es.apply(
                lambda row: f"{row['Tech_Name']} ({row['Duration_Bin']})" if pd.notnull(row['Duration_Bin']) else row['Tech_Name'],
                axis=1
            )

            pivot = df_es[df_es['Value'] != 0].pivot_table(
                index='y', columns='Tech_Name', values='Value', aggfunc='sum'
            ).fillna(0) / 1000

            for i, year in enumerate(all_years):
                x_left = i - (bar_width * num_scenarios / 2) + s_idx * bar_width
                bottom = 0
                for tech in techs:
                    value = pivot.loc[year, tech] if year in pivot.index and tech in pivot.columns else 0
                    if value > 0:
                        ax.bar(
                            x_left, value, bar_width, bottom=bottom,
                            color=self.color_tech(tech),
                            edgecolor='black', hatch=hatches[s_idx % len(hatches)]
                        )
                        bottom += value

        ax.set_xticks(range(len(all_years)))
        ax.set_xticklabels(all_years, rotation=45)
        ax.set_ylabel("Capacity (GW)")
        ax.set_title("Stacked Storage Capacity by Scenario")

        tech_patches = [mpatches.Patch(color=self.color_tech(t), label=t) for t in techs]
        scenario_patches = [
            mpatches.Patch(facecolor='white', edgecolor='black', hatch=h, label=name)
            for h, name in zip(hatches, scenario_names)
        ]
        ax.legend(handles=tech_patches + scenario_patches, loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        plt.show()

    def capacity_investment_bar(self, scenarios, gen_df, sto_df, figsize=(12, 6)):

        # # print("=== Starting capacity_investment_bar ===")

        # Build Gen_num → Tech maps
        gen_map = dict(zip(gen_df["Gen_num"], gen_df["Tech"]))
        sto_map = dict(zip(sto_df["Gen_num"], sto_df["Tech"]))

        # Collect all years
        all_years = sorted({int(y) for s in scenarios.values()
                            for sheet in s.values() if not sheet.empty
                            for y in sheet['y'].unique()})
        # # print("All years:", all_years)

        tech_data = {}  # scenario → (year, tech) → value
        all_techs = set()

        # Duration bin definitions
        bins = [0, 2, 4, 6, 8, 10, 15, 24, np.inf]
        labels = ['0-2 hrs.', '2-4 hrs.', '4-6 hrs.', '6-8 hrs.', '8-10 hrs.', '10-15 hrs.', '15-24 hrs.', '24+ hrs.']

        for scenario_name, sheets in scenarios.items():
            # Process generation investments
            g_df = sheets.get("G_inv", pd.DataFrame()).copy()
            if not g_df.empty:
                g_df['g'] = g_df['g'].ffill()
                g_df['y'] = g_df['y'].astype(int)
                g_df['Tech'] = g_df['g'].map(gen_map).apply(
                    lambda tech: tech.replace('_Cand', '').replace('Li_Ion', 'Li-Ion Battery') if 'Solar' in tech or 'Wind' in tech else f"{tech.replace('_Cand', '').replace('Li_Ion', 'Li-Ion Battery')} (New)"
                )
                g_df = g_df.dropna(subset=["Tech"])

            # Process storage investments
            s_df = sheets.get("Sto_inv", pd.DataFrame()).copy()
            if not s_df.empty:
                s_df['g'] = s_df['g'].ffill()
                s_df['y'] = s_df['y'].astype(int)
                s_df = s_df.dropna(subset=["b", "Value"])
                s_df = s_df[s_df['Value'] > 0]

                # print(f"  -> Storage rows before binning: {len(s_df)}")

                s_df['Tech'] = s_df['g'].map(sto_map)
                s_df = s_df.dropna(subset=["Tech"])

                # Compute duration and assign bins
                s_df['Duration'] = s_df['b'] / s_df['Value']
                s_df['Duration_Bin'] = pd.cut(s_df['Duration'], bins=bins, labels=labels, right=False)

                num_unbinned = s_df['Duration_Bin'].isna().sum()
                if num_unbinned > 0:
                    print(f"  !! Warning: {num_unbinned} storage rows couldn't be binned and will remain unbinned.")

                # Assign technology names with proper formatting

                def format_tech(row):
                    tech_name = row['Tech'].replace('_Cand', '').replace('Li_Ion', 'Li-Ion Battery (New)')
                    if pd.notnull(row['Duration_Bin']):
                        return f"{tech_name} ({row['Duration_Bin']})"
                    else:
                        print(f"  -> No duration bin for {tech_name}. Why? Check 'b'={row['b']} and 'Value'={row['Value']}")
                        return f"{tech_name} (New)"

                s_df['Tech'] = s_df.apply(format_tech, axis=1)

            # Merge G_inv and Sto_inv
            df = pd.concat([g_df, s_df], ignore_index=True)
            df = df[df["Value"] > 0]

            # Simplify label for grouping
            df["Tech_Simple"] = df["Tech"]
            all_techs.update(df["Tech_Simple"].unique())

            for _, row in df.iterrows():
                key = (scenario_name, row["y"], row["Tech_Simple"])
                tech_data[key] = tech_data.get(key, 0) + row["Value"] / 1000  # Convert to GW

        # Sort techs by duration bin if applicable
        def tech_sort_key(name):
            if '(' in name:
                for i, label in enumerate(labels):
                    if label in name:
                        return (name.split('(')[0], i)
            return (name, -1)

        techs_sorted = sorted(all_techs, key=tech_sort_key)
        # print("All unique techs:", techs_sorted)

        # Plotting
        fig, ax = plt.subplots(figsize=figsize)
        bar_width = 0.8 / len(scenarios)
        hatches = ['///', '...', 'xxx', '\\\\\\', '++', '**', 'oo']

        for s_idx, scenario_name in enumerate(scenarios.keys()):
            for y_idx, year in enumerate(all_years):
                x_left = y_idx - (bar_width * len(scenarios) / 2) + s_idx * bar_width
                bottom = 0
                for tech in techs_sorted:
                    val = tech_data.get((scenario_name, year, tech), 0)
                    if val > 0:
                        ax.bar(x_left, val, bar_width, bottom=bottom,
                            color=self.color_tech(tech),  # Use consistent color mapping
                            edgecolor='black',
                            hatch=hatches[s_idx % len(hatches)],
                            label=f"{scenario_name} | {tech}")
                        # print(f"Plotting: Scenario={scenario_name}, Year={year}, Tech={tech}, Value={val:.3f}, X={x_left:.2f}")
                        bottom += val

        ax.set_xticks(range(len(all_years)))
        ax.set_xticklabels(all_years, rotation=45)
        ax.set_ylabel("Capacity Investment (GW)")
        ax.set_title("Capacity Investment by Technology and Scenario")

        # Legend
        tech_patches = [mpatches.Patch(color=self.color_tech(t), label=t) for t in techs_sorted]
        scenario_patches = [mpatches.Patch(facecolor='white', edgecolor='black',
                                        hatch=hatches[i % len(hatches)],
                                        label=scenario)
                            for i, scenario in enumerate(scenarios.keys())]

        ax.legend(handles=tech_patches + scenario_patches, loc='center left', bbox_to_anchor=(1, 0.5))
        plt.tight_layout()
        plt.show()



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
        self.scenario_help.clicked.connect(self.show_scenario_help)

    def select_excel_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Excel Files", "", "Excel Files (*.xlsx *.xls)")
        if not files:
            return

        for f in files:
            name = os.path.splitext(os.path.basename(f))[0]
            if name not in self.file_paths:
                self.file_paths[name] = f
                if not any(self.loaded_files_list.item(i).text() == name for i in range(self.loaded_files_list.count())):
                    self.loaded_files_list.addItem(name)


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

        if plot_type == "Generation Capacity":
            if all('P_cap_total' in s and 'Store' in s for s in selected.values()):
                self.viewer.stacked_grouped_bar_with_hatching(selected, figsize=(18, 8))
            else:
                QMessageBox.warning(self, "Missing Sheets", "Each scenario must include 'P_cap_total' and 'Store'.")

        elif plot_type == "Capacity Investments":
            if all('G_inv' in s and 'Sto_inv' in s for s in selected.values()):
                try:
                    gen_path = os.path.join(base_dir, "data_explan", "rts_csv_data", "gen.csv")
                    store_path = os.path.join(base_dir, "data_explan", "rts_csv_data", "storage.csv")
                    # print(gen_path)
                    # print("##############################")
                    gen_map = pd.read_csv(gen_path)
                    sto_map = pd.read_csv(store_path)
                except Exception as e:
                    QMessageBox.critical(self, "Mapping Error", f"Could not load mapping files: {e}")
                    return
                self.viewer.capacity_investment_bar(selected, gen_map, sto_map, figsize=(14, 6))
            else:
                QMessageBox.warning(self, "Missing Sheets", "Each scenario must include 'G_inv' and 'Sto_inv'.")

        elif plot_type == "ESS Capacity":
            if all('P_cap_total' in s and 'Store' in s for s in selected.values()):
                self.viewer.stacked_storage(selected, figsize=(18, 8))
            else:
                QMessageBox.warning(self, "Missing Sheets", "Each scenario must include 'P_cap_total' and 'Store'.")


    def show_scenario_help(self):
        # Create a QMessageBox
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Scenario Viewer Help")
        msg_box.setText("How to Use the Scenario Viewer:")
        
        # Define the detailed instructions with formatting
        instructions = (
            "<b>Step 1:</b> Load in an Excel file that has been generated by the tool. "
            "You can save scenario results by clicking on the save icon in the menu bar on the left side of the screen.<br><br>"
            
            "<b>Step 2:</b> Select the Excel file. This will populate the center window with sheets.<br><br>"
            
            "<b>Step 3:</b> Select the sheets for the plot you would like to view.<br><br>"
            
            "You can load more than one Excel file and perform side-by-side comparisons by selecting the appropriate sheets from each file.<br><br>"
            
            "You can also remove sheets after they are added by right-clicking on them.<br><br>"
            
            "<b>There are 3 different plots:</b><br><br>"
            
            "<b>1. Generation Capacity:</b> "
            "If all selected sheets contain 'P_cap_total' and 'Store', the plot will be generated. "
            "Otherwise, a warning will be shown.<br><br>"
            
            "<b>2. Capacity Investments:</b> "
            "If all selected sheets contain 'G_inv' and 'Sto_inv', the plot will be generated. "
            "Otherwise, a warning will be shown.<br><br>"
            
            "<b>3. ESS Capacity:</b> "
            "If all selected sheets contain 'P_cap_total' and 'Store', the plot will be generated. "
            "Otherwise, a warning will be shown."
        )
        
        # Set the detailed instructions as the message box's informative text
        msg_box.setInformativeText(instructions)
        
        # Set the text format to HTML for better formatting
        msg_box.setTextFormat(Qt.TextFormat.RichText)
        
        # Add an OK button
        msg_box.setStandardButtons(QMessageBox.Ok)
        
        # Show the message box
        msg_box.exec()

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


