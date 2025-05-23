# -*- coding: utf-8 -*-
"""
Updated 3/24 - C.J. Newlun
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.text as mtext
import folium
import branca.colormap as cm
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
import os.path
import yaml
import glob
import argparse
import textwrap

from explan_simulation import Explan
from explan.explan_data_handler import ExplanDataHandler
from explan.explan_optimizer import ExplanOptimizer
from explan.explan_results_viewer import ExplanResultsViewer


class ExplanResultsViewer_Ex():

    def __init__(self, data_handler):
        self.data_handler = data_handler
        #TODO: Fix this
        self.system = None#self.data_handler.system#'PNM'#self.data_handler.scalars.loc['System']['Value']#TODO: change this
        self.rd = None
        
        # Plotting options - FALSE by default
        self.stacked_bar_by_bus_option = False
        self.policy_plot_option = False
        
        self.wind = None
        
        self.solar = None
        
        self.load = None
    
    def create_lookup_info(self):
        self.gen_map_info = self.data_handler.load_data[self.data_handler.data_ls.index('gen')][[
            'Gen_num', 'Bus_num', 'Bus', 'Tech', 'Tech_Num']]
        
        self.tech_map_info = self.data_handler.load_data[self.data_handler.data_ls.index('tech')][['Tech', 'Tech_Name', 'Tech_Num']]
        
        self.bus_list = self.data_handler.load_data[self.data_handler.data_ls.index('bus')]['Bus_number'].values
        self.bus_names = self.data_handler.load_data[self.data_handler.data_ls.index('bus')][[
            'Bus_number', 'Bus_name']]
    def load_scenarios(self, folder_path):
        """
        Load scenarios from Excel files in the specified folder.
        """
        scenario_files = glob.glob(f"{folder_path}/*.xls") + glob.glob(f"{folder_path}/*.xlsx")
        scenarios = {}
        for file in scenario_files:
            scenario_name = os.path.splitext(os.path.basename(file))[0]#file.split('/')[-1].split('.')[0]  # Extract scenario name from file name
           
            scenario = {}
            scenario['P_cap_total'] = pd.read_excel(file, sheet_name='P_cap_total')
            scenario['Store'] = pd.read_excel(file, sheet_name='Store')
            scenarios[scenario_name] = scenario
            
        return scenarios
    
    def stacked_resource_es_duration_bar(self, scenarios, figsize):
        """
        Plot stacked bar chart of installed capacity by year for multiple scenarios.
        """
        
        # Define the desired order of scenarios
        scenario_order = [
            "Baseline",
            "Baseline + High Load",
            #"Baseline + High ES Costs",
            
            #"Moderate Technology",
            "Advanced Tech + Low Econ. Growth",
            #"Baseline + Tx. Exp",
            "Advanced Tech + Tx. Exp. + High Load",
            "RPS80",
        ]
        
        # Filter and reorder the scenarios based on the desired order
        ordered_scenarios = {name: scenarios[name] for name in scenario_order if name in scenarios}
        
        num_scenarios = len(ordered_scenarios)
        
        fig, axes = plt.subplots(1, num_scenarios, figsize=figsize, sharey=True)
        
        all_handles = []
        all_labels = []
        seen_labels = set()
        
        for i, (scenario_name, scenario) in enumerate(ordered_scenarios.items()):
            # Load results for the scenario
            results = scenario['P_cap_total']
            results_en1 = scenario['Store']
            if np.size(results.index.names) > 1:
                results.reset_index(inplace=True)
            if np.size(results_en1.index.names) > 1:
                results_en1.reset_index(inplace=True)
        
            # Add tech name
            translate = {x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
            tech_num = [translate.get(x, x) for x in results['g']]
            results['Technology'] = tech_num
            tech_num = [translate.get(x, x) for x in results_en1['g']]
            results_en1['Technology'] = tech_num
        
            # Filter for ES tech
            results_es = results[results['Technology'].isin(np.unique(
                self.data_handler.load_data[self.data_handler.data_ls.index('storage')]['Tech_Num']))]
            results_es['Energy'] = results_en1['Value'].values
            results_es['Duration'] = results_es['Energy'] / results_es['Value']
        
            # Define duration bins and labels
            bins = [0, 2, 4, 6, 8, 10, 15, 24, np.inf]
            labels = ['0-2 hrs.', '2-4 hrs.', '4-6 hrs.', '6-8 hrs.', '8-10 hrs.', '10-15 hrs.','15-24 hrs.','24+ hrs.']
        
            # Create a new column for binned durations
            results_es['Duration_Bin'] = pd.cut(results_es['Duration'], bins=bins, labels=labels, right=False)
        
            # Ensure Duration_Bin includes all categories
            results_es['Duration_Bin'] = results_es['Duration_Bin'].cat.set_categories(labels)
            
            # Combine Technology and Duration_Bin into a new column
            results_es['Tech_Name'] = results_es.apply(
                lambda row: f"{row['Tech_Name']} ({row['Duration_Bin']})" if pd.notnull(row['Duration_Bin']) else row['Technology'], axis=1)
            
            # Replace entries in results with those in results_es based on generator number (g)
            results['Duration'] = 0
            
            results.update(results_es)
        
            # Pivot table based on the new Tech_Category column
            results_pivot = results[results['Value'] != 0].pivot_table(
                index=['y'], columns='Tech_Name', values='Value', aggfunc='sum')
          
            results_pivot = results_pivot / 1000
            
            # Rename columns
            translate1 = {x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
            cols = [translate1.get(x, x) for x in results_pivot.columns]
            results_pivot.columns = cols
            
            # Define the order of technologies: thermal, renewables, storage
            thermal_techs = ['Coal','Nuclear','Oil_CT','Oil_ST','Gas_CT','Gas_CC','Hydro','Gas (New)']
            renewable_techs = ['Wind','Solar','Solar_RT','CSP','Wind (New)','Solar (New)']
            other_techs = sorted([tech for tech in cols if tech not in thermal_techs + renewable_techs])
            ordered_cols = [tech for tech in thermal_techs + renewable_techs + other_techs if tech in cols]
            
            results_pivot = results_pivot[ordered_cols]
            
            # Assign colors
            color_array = [self.color_tech(c) for c in ordered_cols]
        
            ax = axes[i]
                   
            results_pivot.plot.bar(stacked=True, color=color_array, ax=ax, legend=False, linewidth=0.75,edgecolor="black", width=0.5)
            ax.set_ylabel('Capacity (GW)', fontsize=12)
            #ax.set_title(f'{scenario_name}', fontsize=14)
            ax.margins(x=0, y=0)
            ax.set_xlabel('')
            ax.tick_params(axis='y', labelsize=12)
            
            if i > 0:
                ax.set_facecolor('#f0f0f0')  # Light shade background color
            # Wrap and set the subplot title
            wrapped_title = "\n".join(textwrap.wrap(scenario_name, width=16))
            ax.set_title(wrapped_title, fontsize=14, fontweight='bold')
            
            # Collect handles and labels for the legend
            handles, labels = ax.get_legend_handles_labels()
            for handle, label in zip(handles, labels):
                if label not in seen_labels:
                    all_handles.append(handle)
                    all_labels.append(label)
                    seen_labels.add(label)
            
            # Set x-axis labels to be integers, larger font, and diagonal
            ax.set_xticklabels(results_pivot.index.astype(int), rotation=45, ha='right', fontsize=12)
            # Add faint separator line between scenarios
            if i < num_scenarios - 1:
                ax.axvline(x=ax.get_xlim()[1], color='gray', linestyle='--', linewidth=0.5)
            
        # Create a single legend for the entire figure
        fig.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.25), fontsize=12, ncol=5)
        
        plt.tight_layout()
        plt.show()
    
    def stacked_resource_es_duration_bar_gen_diff(self, scenarios, figsize):
        """
        Plot stacked bar chart of installed capacity by year for multiple scenarios.
        """
        baseline_scenario_name = "Baseline"
        
        # Define the desired order of scenarios
        scenario_order = [
            "Baseline",
            "Baseline + High Load",
            #"Baseline + High ES Costs",
            
            #"Moderate Technology",
            "Advanced Tech + Low Econ. Growth",
            #"Baseline + Tx. Exp",
            "Advanced Tech + Tx. Exp. + High Load",
            "RPS80",
        ]
        
        # Filter and reorder the scenarios based on the desired order
        ordered_scenarios = {name: scenarios[name] for name in scenario_order if name in scenarios}
        
        num_scenarios = len(ordered_scenarios)
        
        # Create subplots: one for the baseline and a grid for the rest
        fig = plt.figure(figsize=figsize)
        gs = fig.add_gridspec(1, num_scenarios, width_ratios=[1] + [1] * (num_scenarios - 1))
        
        ax_baseline = fig.add_subplot(gs[0, 0])
        ax_deltas = [fig.add_subplot(gs[0, i + 1], sharey=ax_baseline) for i in range(num_scenarios - 1)]
        
        all_handles = []
        all_labels = []
        seen_labels = set()
        
        baseline_results_pivot = None
        
        color_mapping = {}
        
        for i, (scenario_name, scenario) in enumerate(ordered_scenarios.items()):
            # Load results for the scenario
            
            
            results = scenario['P_cap_total']
            results_en1 = scenario['Store']
            if np.size(results.index.names) > 1:
                results.reset_index(inplace=True)
            if np.size(results_en1.index.names) > 1:
                results_en1.reset_index(inplace=True)
        
            # Add tech name
            translate = {x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
            tech_num = [translate.get(x, x) for x in results['g']]
            results['Technology'] = tech_num
            tech_num = [translate.get(x, x) for x in results_en1['g']]
            results_en1['Technology'] = tech_num
        
            # Filter for ES tech
            results_es = results[results['Technology'].isin(np.unique(
                self.data_handler.load_data[self.data_handler.data_ls.index('storage')]['Tech_Num']))]
            results_es['Energy'] = results_en1['Value'].values
            results_es['Duration'] = results_es['Energy'] / results_es['Value']
        
            # Define duration bins and labels
            bins = [0, 2, 4, 6, 8, 10, 15, 24, np.inf]
            labels = ['0-2 hrs.', '2-4 hrs.', '4-6 hrs.', '6-8 hrs.', '8-10 hrs.', '10-15 hrs.','15-24 hrs.','24+ hrs.']
        
            # Create a new column for binned durations
            results_es['Duration_Bin'] = pd.cut(results_es['Duration'], bins=bins, labels=labels, right=False)
        
            # Ensure Duration_Bin includes all categories
            results_es['Duration_Bin'] = results_es['Duration_Bin'].cat.set_categories(labels)
            
            # Combine Technology and Duration_Bin into a new column
            results_es['Tech_Name'] = results_es.apply(
                lambda row: f"{row['Tech_Name']} ({row['Duration_Bin']})" if pd.notnull(row['Duration_Bin']) else row['Technology'], axis=1)
            
            # Replace entries in results with those in results_es based on generator number (g)
            results['Duration'] = 0
            
            results.update(results_es)
        
            # Pivot table based on the new Tech_Category column
            results_pivot = results[results['Value'] != 0].pivot_table(
                index=['y'], columns='Tech_Name', values='Value', aggfunc='sum')
          
            results_pivot = results_pivot / 1000
            
            # Rename columns
            translate1 = {x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
            cols = [translate1.get(x, x) for x in results_pivot.columns]
            results_pivot.columns = cols
            
            # Define the order of technologies: thermal, renewables, storage
            thermal_techs = ['Coal','Nuclear','Oil_CT','Oil_ST','Gas_CT','Gas_CC','Hydro','Gas (New)']
            renewable_techs = ['Wind','Solar','Solar_RT','CSP','Wind (New)','Solar (New)']
            other_techs = sorted([tech for tech in cols if tech not in thermal_techs + renewable_techs])# + storage_techs]
            #print(other_techs)
            # Ensure ordered_cols are in cols
            ordered_cols = [tech for tech in thermal_techs + renewable_techs + other_techs if tech in cols]
            #ordered_cols = thermal_techs + renewable_techs + other_techs #+ storage_techs
            
            results_pivot = results_pivot[ordered_cols]
            
            # Assign colors# Assign colors
            for tech in ordered_cols:
                if tech not in color_mapping:
                    color_mapping[tech] = self.color_tech(tech)
            #print(color_mapping)
            color_array = [color_mapping[tech] for tech in ordered_cols]
            #color_array = [self.color_tech(c) for c in ordered_cols]
        
            if scenario_name == baseline_scenario_name:
                baseline_results_pivot = results_pivot.copy()
                results_pivot.plot.bar(stacked=True, color=color_array, ax=ax_baseline, legend=False, edgecolor="black", linewidth=0.75, width=0.5)
                ax_baseline.set_ylabel('Capacity (GW)', fontsize=15)
                ax_baseline.set_title('Baseline', fontsize=15, fontweight='bold')
                ax_baseline.axhline(y=0, color='k', linewidth=0.5)
                ax_baseline.set_xlabel('')
                ax_baseline.set_xticklabels(baseline_results_pivot.index.astype(int), rotation=45, ha='right', fontsize=15)
                
            else:
                results_pivot1 = results_pivot.fillna(0)
                baseline_results_pivot = baseline_results_pivot.fillna(0)
                
                # Calculate the change in energy storage investment compared to the baseline
                results_pivot1 = results_pivot1.subtract(baseline_results_pivot, fill_value=0)
                color_array = [self.color_tech(c) for c in results_pivot1.columns]
                ax=ax_deltas[i-1]
                results_pivot1.plot.bar(stacked=True, color=color_array, ax=ax, legend=False, edgecolor="black", linewidth=0.75, width=0.5)
                
                # Wrap and set the subplot title
                wrapped_title = "\n".join(textwrap.wrap(scenario_name, width=20))
                ax.set_title(wrapped_title, fontsize=15, fontweight='bold')
                #ax.set_ylabel('Change from Baseline (GW)', fontsize=15)
                
                y_min, y_max = ax.get_ylim()
                if i == 1:
                    y_min, y_max = ax.get_ylim()
                    ax.annotate('Decrease / Increase from Baseline (GW)', xy=(0, 0.25), xytext=(-0.06,1 / 2),
                                textcoords='axes fraction', va='center', ha='center', rotation=90, fontsize=15)
                    #ax.annotate('Decrease', xy=(0, y_min), xytext=(-0.06, y_min / 2),
                      #      textcoords='axes fraction', va='center', ha='center', rotation=90, fontsize=15, color='red')
                    #ax.annotate('Increase', xy=(0, y_max), xytext=(-0.06, y_max / 2),
                     #           textcoords='axes fraction', va='center', ha='center', rotation=90, fontsize=15, color='blue')
                    # Create custom text objects
                    decrease_text = mtext.Text(0.5, -37, "Decrease", color='red', fontsize=15, rotation=0, va='center', ha='center',weight = 'bold')
                    increase_text = mtext.Text(0.5, 37, "Increase", color='blue', fontsize=15, rotation=0, va='center', ha='center',weight = 'bold')
                    #combined_text = mtext.Text(0, 0, " / ", fontsize=15, rotation=90, va='center', ha='center')
                    
                    # Combine the texts
                    ax.annotate('', xy=(0, 0.25), xytext=(-0.06, 1 / 2),
                                textcoords='axes fraction', va='center', ha='center', rotation=90, fontsize=15)
                    # Position the combined text
                    #decrease_text.set_position((-0.06, 0.25))
                    #combined_text.set_position((-0.06, 0.5))
                    #increase_text.set_position((-0.06, 0.5))
                    
                    ax.add_artist(decrease_text)
                    #ax.add_artist(combined_text)
                    ax.add_artist(increase_text)
                
                # Collect handles and labels for the legend
                handles, labels = ax.get_legend_handles_labels()
                for handle, label in zip(handles, labels):
                    if label not in seen_labels:
                        all_handles.append(handle)
                        all_labels.append(label)
                        seen_labels.add(label)
                
                # Set x-axis labels to be integers, larger font, and diagonal
                ax.set_xticklabels(results_pivot.index.astype(int), rotation=45, ha='right', fontsize=15)
                ax.axhline(y=0, color='k', linewidth=0.5)
                ax.set_xlabel('')
                ax.set_facecolor('#f0f0f0')  # Light shade background color
                for spine in ax.spines.values():
                    spine.set_edgecolor('black')
                    spine.set_linewidth(1.5)
         # Set y-axis label for the delta subplots
        for ax in ax_deltas:
            ax.set_ylabel('Delta Baseline', fontsize=15)
            
        # Ensure all plots have the same y-axis scale
        y_limits = [ax.get_ylim() for ax in [ax_baseline] + ax_deltas]
        min_y, max_y = min(y[0] for y in y_limits), max(y[1] for y in y_limits)
        for ax in [ax_baseline] + ax_deltas:
            ax.set_ylim(-max_y, max_y)
            
        for ax in ax_deltas:
            # Fill the positive and negative areas with light colors
            ax.fill_between(ax.get_xlim(), 0, max_y, color='lightblue', alpha=0.15)
            ax.fill_between(ax.get_xlim(), -max_y, 0, color='lightcoral', alpha=0.15)
        
        
        # Create a single legend for the entire figure
        fig.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.25), fontsize=14, ncol=5)
        
        plt.tight_layout()
        plt.show()

    def stacked_es_duration_bar_es_diff(self, scenarios, figsize):
        """
        Plot stacked bar chart of installed energy storage capacity by year for multiple scenarios.
        """
        baseline_scenario_name = "Baseline"
        
        # Define the desired order of scenarios
        scenario_order = [
            "Baseline",
            "Baseline + High Load",
            #"Baseline + High ES Costs",
            
            #"Moderate Technology",
            "Advanced Tech + Low Econ. Growth",
            #"Baseline + Tx. Exp",
            "Advanced Tech + Tx. Exp. + High Load",
            "RPS80",
        ]
        
        # Filter and reorder the scenarios based on the desired order
        ordered_scenarios = {name: scenarios[name] for name in scenario_order if name in scenarios}
        
        num_scenarios = len(ordered_scenarios)
        
        # Create subplots: one for the baseline and a grid for the rest
        fig = plt.figure(figsize=figsize)
        #gs = fig.add_gridspec(1, num_scenarios, width_ratios=[1, 0.1] + [1] * (num_scenarios - 1))
        gs = fig.add_gridspec(1, num_scenarios, width_ratios=[1] + [1] * (num_scenarios - 1))
        
        ax_baseline = fig.add_subplot(gs[0, 0])
        ax_deltas = [fig.add_subplot(gs[0, i + 1], sharey=ax_baseline) for i in range(num_scenarios - 1)]
        
        all_handles = []
        all_labels = []
        seen_labels = set()
        
        baseline_results_pivot = None
        
        color_mapping = {}
        
        for i, (scenario_name, scenario) in enumerate(ordered_scenarios.items()):
            # Load results for the scenario
            results = scenario['P_cap_total']
            results_en1 = scenario['Store']
            if np.size(results.index.names) > 1:
                results.reset_index(inplace=True)
            if np.size(results_en1.index.names) > 1:
                results_en1.reset_index(inplace=True)
        
            # Add tech name
            translate = {x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
            tech_num = [translate.get(x, x) for x in results['g']]
            results['Technology'] = tech_num
            tech_num = [translate.get(x, x) for x in results_en1['g']]
            results_en1['Technology'] = tech_num
        
            # Filter for ES tech
            es_techs = np.unique(self.data_handler.load_data[self.data_handler.data_ls.index('storage')]['Tech_Num'])
            results_es = results[results['Technology'].isin(es_techs)]
            results_es['Energy'] = results_en1['Value'].values
            results_es['Duration'] = results_es['Energy'] / results_es['Value']
        
            # Define duration bins and labels
            bins = [0, 2, 4, 6, 8, 10, 15, 24, np.inf]
            labels = ['0-2 hrs.', '2-4 hrs.', '4-6 hrs.', '6-8 hrs.', '8-10 hrs.', '10-15 hrs.','15-24 hrs.','24+ hrs.']
        
            # Create a new column for binned durations
            results_es['Duration_Bin'] = pd.cut(results_es['Duration'], bins=bins, labels=labels, right=False)
        
            # Ensure Duration_Bin includes all categories
            results_es['Duration_Bin'] = results_es['Duration_Bin'].cat.set_categories(labels)
            
            # Combine Technology and Duration_Bin into a new column
            results_es['Tech_Name'] = results_es.apply(
                lambda row: f"{row['Tech_Name']} ({row['Duration_Bin']})" if pd.notnull(row['Duration_Bin']) else row['Technology'], axis=1)
            
            # Replace entries in results with those in results_es based on generator number (g)
            results['Duration'] = 0
            
            results.update(results_es)
            
            results_es1 = results[results['Technology'].isin(es_techs)]
        
            # Pivot table based on the new Tech_Category column
            results_pivot = results_es1[results_es1['Value'] != 0].pivot_table(
                index=['y'], columns='Tech_Name', values='Value', aggfunc='sum')
          
            results_pivot = results_pivot / 1000
            
            # Rename columns
            translate1 = {x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
            cols = [translate1.get(x, x) for x in results_pivot.columns]
            results_pivot.columns = cols
            
            # Assign colors
            for tech in cols:
                if tech not in color_mapping:
                    color_mapping[tech] = self.color_tech(tech)
            color_array = [color_mapping[tech] for tech in cols]
        
            if scenario_name == baseline_scenario_name:
                baseline_results_pivot = results_pivot.copy()
                results_pivot.plot.bar(stacked=True, color=color_array, ax=ax_baseline, legend=False, edgecolor="black", linewidth=0.75, width=0.5)
                ax_baseline.set_ylabel('Capacity (GW)', fontsize=15)
                ax_baseline.set_title('Baseline', fontsize=14, fontweight='bold')
                ax_baseline.axhline(y=0, color='k', linewidth=0.5)
                ax_baseline.set_xlabel('')
                ax_baseline.set_xticklabels(baseline_results_pivot.index.astype(int), rotation=45, ha='right', fontsize=15)
            else:
                results_pivot1 = results_pivot.fillna(0)
                baseline_results_pivot = baseline_results_pivot.fillna(0)
                
                # Calculate the change in energy storage investment compared to the baseline
                results_pivot1 = results_pivot1.subtract(baseline_results_pivot, fill_value=0)
                #color_array = [self.color_tech[tech] for tech in results_pivot1.columns]
                color_array = [self.color_tech(c) for c in results_pivot1.columns]
                ax = ax_deltas[i - 1]
                results_pivot1.plot.bar(stacked=True, color=color_array, ax=ax, legend=False, edgecolor="black", linewidth=0.75, width=0.5)
                
                # Wrap and set the subplot title
                wrapped_title = "\n".join(textwrap.wrap(scenario_name, width=20))
                ax.set_title(wrapped_title, fontsize=14, fontweight='bold')
                #ax.set_ylabel('Change from Baseline (GW)', fontsize=5)
                
                # Add y-axis labels for positive and negative values
                
                y_min, y_max = ax.get_ylim()
                if i == 1:
                    y_min, y_max = ax.get_ylim()
                    ax.annotate('Decrease / Increase from Baseline (GW)', xy=(0, 0.25), xytext=(-0.06,1 / 2),
                                textcoords='axes fraction', va='center', ha='center', rotation=90, fontsize=15)
                    #ax.annotate('Decrease', xy=(0, y_min), xytext=(-0.06, y_min / 2),
                      #      textcoords='axes fraction', va='center', ha='center', rotation=90, fontsize=15, color='red')
                    #ax.annotate('Increase', xy=(0, y_max), xytext=(-0.06, y_max / 2),
                     #           textcoords='axes fraction', va='center', ha='center', rotation=90, fontsize=15, color='blue')
                    # Create custom text objects
                    decrease_text = mtext.Text(0.5, -15, "Decrease", color='red', fontsize=15, rotation=0, va='center', ha='center',weight = 'bold')
                    increase_text = mtext.Text(0.5, 15, "Increase", color='blue', fontsize=15, rotation=0, va='center', ha='center',weight = 'bold')
                    #combined_text = mtext.Text(0, 0, " / ", fontsize=15, rotation=90, va='center', ha='center')
                    
                    # Combine the texts
                    ax.annotate('', xy=(0, 0.25), xytext=(-0.06, 1 / 2),
                                textcoords='axes fraction', va='center', ha='center', rotation=90, fontsize=15)
                    # Position the combined text
                    #decrease_text.set_position((-0.06, 0.25))
                    #combined_text.set_position((-0.06, 0.5))
                    #increase_text.set_position((-0.06, 0.5))
                    
                    ax.add_artist(decrease_text)
                    #ax.add_artist(combined_text)
                    ax.add_artist(increase_text)
                    
                    
                    
                    
                # Collect handles and labels for the legend
                handles, labels = ax.get_legend_handles_labels()
                for handle, label in zip(handles, labels):
                    if label not in seen_labels:
                        all_handles.append(handle)
                        all_labels.append(label)
                        seen_labels.add(label)
                
                # Set x-axis labels to be integers, larger font, and diagonal
                ax.set_xticklabels(results_pivot.index.astype(int), rotation=45, ha='right', fontsize=15)
                ax.axhline(y=0, color='k', linewidth=0.5)
                ax.set_xlabel('')
                
                ax.set_facecolor('#f0f0f0')  # Light shade background color
                for spine in ax.spines.values():
                    spine.set_edgecolor('black')
                    spine.set_linewidth(1.5)
        
        # Ensure all plots have the same y-axis scale
        y_limits = [ax.get_ylim() for ax in [ax_baseline] + ax_deltas]
        min_y, max_y = min(y[0] for y in y_limits), max(y[1] for y in y_limits)
        for ax in [ax_baseline] + ax_deltas:
            ax.set_ylim(-max_y, max_y)
            
        for ax in ax_deltas:
            # Fill the positive and negative areas with light colors
            ax.fill_between(ax.get_xlim(), 0, max_y, color='lightblue', alpha=0.15)
            ax.fill_between(ax.get_xlim(), -max_y, 0, color='lightcoral', alpha=0.15)
        
        
        # Create a single legend for the entire figure
        fig.legend(all_handles, all_labels, loc='lower center', bbox_to_anchor=(0.5, -0.2), fontsize=14, ncol=3)
        
        plt.tight_layout()
        plt.show()
        #del results_es,results

    def stacked_resource_dispatch(self, select_year):
        """


        Parameters
        ----------
        gen_map_info : TYPE
            DESCRIPTION.
        tech_map_info : TYPE
            DESCRIPTION.
        select_year : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """

        results = self.rd['P_gen']
        if np.size(results.index.names) > 1:
            results = results.reset_index()
        ES_cha = self.rd['Pcha']
        if np.size(ES_cha.index.names) > 1:
            ES_cha = ES_cha.reset_index()
        ES_dis = self.rd['Pdis']
        if np.size(ES_dis.index.names) > 1:
            ES_dis = ES_dis.reset_index()
        Curt = self.rd['Curt']
        if np.size(Curt.index.names) > 1:
            Curt = Curt.reset_index()
        PF = self.rd['PF']
        if np.size(PF.index.names) > 1:
            PF = PF.reset_index()
        SOC = self.rd['SOC']
        if np.size(SOC.index.names) > 1:
            SOC = SOC.reset_index()

        # Modify load dataframe
        #load_df_rs = load_df
        load_df = self.pd['load_full']
        ind_s = len(load_df.index.names)
        load_df_rs = load_df.stack().unstack(ind_s-1)
        load_df_rs = load_df_rs.droplevel(ind_s-1)

        if np.size(load_df_rs.index.names) > 1:
            load_df_rs = load_df_rs.reset_index()

        # investment results for screening purposes
        g_cap = self.rd['P_cap_total']
        if np.size(g_cap.index.names) > 1:
            g_cap = g_cap.reset_index()
        g_cap_y = g_cap[g_cap['y'] == select_year]
        gen_keep = g_cap_y[g_cap_y['Value'] > 0]['g']

        # filter the following dataframes
        results = results[results['g'].isin(gen_keep)]
        ES_cha = ES_cha[ES_cha['g'].isin(gen_keep)]
        ES_dis = ES_dis[ES_dis['g'].isin(gen_keep)]
        Curt = Curt[Curt['g'].isin(gen_keep)]
        SOC = SOC[SOC['g'].isin(gen_keep)]
        
        '''
        # Filter PF dataframe
        mkt_line = 2
        PF_mkt = PF[PF['l'] == mkt_line]
        
        # Select datetime for specific
        dt_select_year = pd.DataFrame()
        dt_select_year[str(select_year)] = dt[str(select_year)]
        dt_select_year['s'] = season_map_series(
            dt_select_year[str(select_year)])
        '''
        # add tech name
        translate = {
            x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
        tech_num = [translate.get(x, x)
                    for x in results['g']]
        results['Technology'] = tech_num
        ES_cha['Technology'] = [
            translate.get(x, x) for x in ES_cha['g']]
        ES_dis['Technology'] = [
            translate.get(x, x) for x in ES_dis['g']]
        Curt['Technology'] = [
            translate.get(x, x) for x in Curt['g']]
        # SOC
        SOC['Technology'] = [
            translate.get(x, x) for x in SOC['g']]

        #all_tech = np.unique(gen_map_info['Tech_ID'])
        # need to reorder for stack plots

        #nums = np.arange(1,np.size(re_order_tech)+1)
        # num_tech =

        # for y in np.unique(results['y']):
        if self.data_handler.block_selection.lower() == 'Full_Year'.lower():
            dispatch = results.loc[(
                results['y'] == select_year)].drop(['b', 'g', 'y', 's'], axis=1)
            dispatch_tech = dispatch.groupby(
                dispatch['Technology']).sum().T  #

            load_df_rs_y = load_df_rs.loc[(
                load_df_rs['y'] == select_year)].drop(['b', 'y', 's'], axis=1)
            load_df_rs_y = load_df_rs_y.sum(axis=0)
            #load_df_rs_y.column = ['Load']

            es_cha = ES_cha.loc[(
                ES_cha['y'] == select_year)].drop(['b', 'g', 'y', 's'], axis=1)
            es_cha_tech = es_cha.groupby(
                es_cha['Technology']).sum().T
            # season_es_cha_tech = season_es_cha_tech.drop(
            # ['index'], axis=0) 'level_4', 'level_0',

            es_dis = ES_dis.loc[(
                ES_dis['y'] == select_year)].drop(['b', 'g', 'y', 's'], axis=1)
            es_dis_tech = es_dis.groupby(
                es_dis['Technology']).sum().T
            # season_es_dis_tech = season_es_dis_tech.drop(
            # ['index'], axis=0) 'level_4', 'level_0',

            curt = Curt.loc[(
                Curt['y'] == select_year)].drop(['b', 'g', 'y', 's'], axis=1)
            curt_tech = curt.sum().T

            soc = SOC.loc[(
                SOC['y'] == select_year)].drop(['b', 'g', 'y', 's'], axis=1)
            soc_tech = soc.groupby(
                soc['Technology']).sum().T
            # season_curt_tech = season_curt_tech.drop(
            # ['index'], axis=0)

            # rename columns
            translate1 = {
                x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
            cols1 = [translate1.get(x, x)
                     for x in dispatch_tech.columns]
            dispatch_tech.columns = cols1
            cols2 = [translate1.get(x, x)+'-charge'
                     for x in es_cha_tech.columns]
            es_cha_tech.columns = cols2
            cols3 = [translate1.get(x, x)+'-discharge'
                     for x in es_dis_tech.columns]
            es_dis_tech.columns = cols3
            cols4 = [translate1.get(x, x)
                     for x in soc_tech.columns]
            soc_tech.columns = cols4

            # assign colors
            '''
            color_array = [color_tech(c) for c in cols1]
            color_array_esc = [color_tech(c) for c in cols2]
            color_array_esd = [color_tech(c) for c in cols3]
            color_array = np.concatenate(
                (color_array, color_array_esc, color_array_esd), axis=None)
            '''
            dispatch_tech[dispatch_tech < 0] = 0
            curt_tech[curt_tech < 0] = 0
            # season_es_cha_tech.columns
            #['ES', 'ES 4hr (New)', 'ES 6hr (New)', 'ES 8hr (New)', 'ES 10hr (New)', 'ES 100hr (New)', 'Li-Ion Battery (New)', 'Flow Battery (New)', 'LDES (New)']
            dispatch_tech[es_cha_tech.columns] = -es_cha_tech.clip(
                lower=0)
            dispatch_tech[es_dis_tech.columns] = es_dis_tech.clip(
                lower=0)

            dispatch_tech['Curtailment'] = - \
                curt_tech
            # Drop all zero columns
            dispatch_tech = dispatch_tech.loc[:, (
                dispatch_tech != 0).any(axis=0)]
            # season_dispatch_tech = season_dispatch_tech.drop(
            #   ['ES PPA', 'ES 4hr (New)', 'ES 8hr (New)', 'ES Flow 10hr (New)', 'ES 100hr (New)'], axis=1)

            color_array = [self.color_tech(
                c) for c in dispatch_tech.columns]
            # season_dispatch_tech = season_dispatch_tech.drop(
            # ['level_0'], axis=0)

            # set date time
            # season_dispatch_tech.index =
            #x = dt_select_year[dt_select_year['s'] == s][str(select_year)]
            fig, ax = plt.subplots(1, 1)
            # fig = season_dispatch_tech.plot.area(stacked=True, color=color_array, figsize=[
            # 16, 8], legend=False, linewidth=0).figure
            dispatch_tech.plot.area(stacked=True, color=color_array, figsize=[
                50, 8], legend=False, linewidth=0, ax=ax)
            # season_es_cha_tech.clip(lower=0).plot.area(stacked=True, color=color_array_esc, figsize=[
            # 16, 8], legend=False, linewidth=0, ax = ax)
            load_df_rs_y.plot(
                legend=False, color='k', linewidth=1, label='Load')
            # soc_tech.plot(
            #  legend=False, secondary_y=True, color='b', linestyle='--', ax=ax, linewidth=3, label='State-of-Charge')
            fig.legend(loc="center left",
                       bbox_to_anchor=(0.9, 0.5), fontsize=15)
            ax.set_ylabel('Capacity (MW)', fontsize=25)
            ax.set_xlabel('Time (hr)', fontsize=25)
            # ax.right_ax.set_ylim(-max(soc_tech.max(axis=1)),
            #                   max(soc_tech.max(axis=1)))

            # ax.set_xticklabels(fontsize=20)
            ax.set_title(str(select_year) +
                         ' Generation Dispatch', weight='bold', fontsize=30)
            ax.margins(x=0, y=0)
            # fig.tight_layout()
            plt.close(fig)
            fig.savefig(self.dispatch_folder_path+'/' + str(select_year)
                        + '.png', bbox_inches='tight')
            fig1, ax1 = plt.subplots(1, 1)
            color_array = [self.color_tech(
                c) for c in soc_tech.columns]
            soc_tech.plot(
                legend=False, figsize=[50, 8], color=color_array, linestyle='-', ax=ax1, linewidth=3, label='State-of-Charge')
            fig1.legend(loc="center left",
                        bbox_to_anchor=(0.9, 0.5), fontsize=15)
            ax1.set_ylabel('SOC (MWh)', fontsize=25)
            ax1.set_xlabel('Time (hr)', fontsize=25)
            # ax1.right_ax.set_ylim(-max(soc_tech.max(axis=1)),
            #                    max(soc_tech.max(axis=1)))

            # ax.set_xticklabels(fontsize=20)
            ax1.set_title(str(select_year) +
                          ' ES State-of-Charge', weight='bold', fontsize=30)
            ax1.margins(x=0, y=0)
            # fig.tight_layout()
            plt.close(fig1)
            fig1.savefig(self.dispatch_folder_path+'/SOC_' + str(select_year)
                         + '.png', bbox_inches='tight')
        else:
            for s in np.unique(results['s']):
                season_dispatch = results.loc[(
                    results['y'] == select_year) & (results['s'] == s)].drop(['b', 'g', 'y', 's'], axis=1)
                season_dispatch_tech = season_dispatch.groupby(
                    season_dispatch['Technology']).sum().T  #

                load_df_rs_y = load_df_rs.loc[(
                    load_df_rs['y'] == select_year) & (load_df_rs['s'] == s)].drop(['b', 'y', 's'], axis=1)
                load_df_rs_y = load_df_rs_y.sum(axis=0)
                #load_df_rs_y.column = ['Load']

                season_es_cha = ES_cha.loc[(
                    ES_cha['y'] == select_year) & (ES_cha['s'] == s)].drop(['b', 'g', 'y', 's'], axis=1)
                season_es_cha_tech = season_es_cha.groupby(
                    season_es_cha['Technology']).sum().T
                # season_es_cha_tech = season_es_cha_tech.drop(
                # ['index'], axis=0) 'level_4', 'level_0',

                season_es_dis = ES_dis.loc[(
                    ES_dis['y'] == select_year) & (ES_dis['s'] == s)].drop(['b', 'g', 'y', 's'], axis=1)
                season_es_dis_tech = season_es_dis.groupby(
                    season_es_dis['Technology']).sum().T
                # season_es_dis_tech = season_es_dis_tech.drop(
                # ['index'], axis=0) 'level_4', 'level_0',

                season_curt = Curt.loc[(
                    Curt['y'] == select_year) & (Curt['s'] == s)].drop(['b', 'g', 'y', 's'], axis=1)
                season_curt_tech = season_curt.sum().T
                # season_curt_tech = season_curt_tech.drop(
                # ['index'], axis=0)

                # rename columns
                translate1 = {
                    x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
                cols1 = [translate1.get(x, x)
                         for x in season_dispatch_tech.columns]
                season_dispatch_tech.columns = cols1
                cols2 = [translate1.get(x, x)+'-charge'
                         for x in season_es_cha_tech.columns]
                season_es_cha_tech.columns = cols2
                cols3 = [translate1.get(x, x)+'-discharge'
                         for x in season_es_dis_tech.columns]
                season_es_dis_tech.columns = cols3
                # cols4 = [translate1.get(x, x)
                # for x in season_curt_tech.columns]
                #season_curt_tech.columns = cols4

                # assign colors
                '''
                color_array = [color_tech(c) for c in cols1]
                color_array_esc = [color_tech(c) for c in cols2]
                color_array_esd = [color_tech(c) for c in cols3]
                color_array = np.concatenate(
                    (color_array, color_array_esc, color_array_esd), axis=None)
                '''
                season_dispatch_tech[season_dispatch_tech < 0] = 0
                season_curt_tech[season_curt_tech < 0] = 0
                # season_es_cha_tech.columns
                #['ES', 'ES 4hr (New)', 'ES 6hr (New)', 'ES 8hr (New)', 'ES 10hr (New)', 'ES 100hr (New)', 'Li-Ion Battery (New)', 'Flow Battery (New)', 'LDES (New)']
                season_dispatch_tech[season_es_cha_tech.columns] = -season_es_cha_tech.clip(
                    lower=0)
                season_dispatch_tech[season_es_dis_tech.columns] = season_es_dis_tech.clip(
                    lower=0)

                season_dispatch_tech['Curtailment'] = - \
                    season_curt_tech
                # Drop all zero columns
                season_dispatch_tech = season_dispatch_tech.loc[:, (
                    season_dispatch_tech != 0).any(axis=0)]
                # season_dispatch_tech = season_dispatch_tech.drop(
                #   ['ES PPA', 'ES 4hr (New)', 'ES 8hr (New)', 'ES Flow 10hr (New)', 'ES 100hr (New)'], axis=1)

                color_array = [self.color_tech(
                    c) for c in season_dispatch_tech.columns]
                # season_dispatch_tech = season_dispatch_tech.drop(
                # ['level_0'], axis=0)

                # set date time
                # season_dispatch_tech.index =
                #x = dt_select_year[dt_select_year['s'] == s][str(select_year)]
                fig, ax = plt.subplots(1, 1)
                # fig = season_dispatch_tech.plot.area(stacked=True, color=color_array, figsize=[
                # 16, 8], legend=False, linewidth=0).figure
                season_dispatch_tech.plot.area(stacked=True, color=color_array, figsize=[
                    16, 8], legend=False, linewidth=0, ax=ax)
                # season_es_cha_tech.clip(lower=0).plot.area(stacked=True, color=color_array_esc, figsize=[
                # 16, 8], legend=False, linewidth=0, ax = ax)
                load_df_rs_y.plot(
                    legend=False, color='k', linewidth=3.5, label='Load')
                fig.legend(loc="center left",
                           bbox_to_anchor=(0.925, 0.5), fontsize=15)
                if s == 1:
                    season = 'Winter'
                elif s == 2:
                    season = 'Spring'
                elif s == 3:
                    season = 'Summer'
                elif s == 4:
                    season = 'Fall'
                elif s == 5:
                    season = 'Peak Week'

                ax.set_ylabel('Capacity (MW)', fontsize=25)
                ax.set_xlabel('Time (hr)', fontsize=25)
                # ax.set_xticklabels(fontsize=20)
                ax.set_title(season+' ' + str(select_year) +
                             ' Generation Dispatch', weight='bold', fontsize=30)
                ax.margins(x=0, y=0)
                # fig.tight_layout()
                plt.close(fig)
                fig.savefig(self.dispatch_folder_path+'/'+season+'_' + str(select_year)
                            + '.png', bbox_inches='tight')
        
    
    def plot_time_series(self):
        """Plot an 8760 time series plot with wind, solar, and load data."""
        
        self.wind = self.data_handler.load_data[self.data_handler.data_ls.index('wind')]['66']
        
        self.solar = self.data_handler.load_data[self.data_handler.data_ls.index('solar')]['46']
        
        self.load = self.data_handler.load_data[self.data_handler.data_ls.index('load')]['system_wide']
        plt.style.use('default')
        fig, axs = plt.subplots(3, 1, figsize=(25, 12), sharex=True)
        
        date_range = pd.date_range(start='2024-01-01', periods=8760, freq='H')
      
        
        axs[0].plot(date_range, self.wind, color='green', label='Wind')
        axs[0].set_ylabel('Wind Power (MW)')
        axs[0].set_title('Wind',fontsize = 20)
        axs[0].grid(True)
        axs[0].margins(0)
        
        axs[1].plot(date_range, self.solar, color='orange', label='Solar')
        axs[1].set_ylabel('Solar Power (MW)')
        axs[1].set_title('Solar',fontsize = 20)
        axs[1].grid(True)
        axs[1].margins(0)
        
        axs[2].plot(date_range, self.load, color='blue', label='Load')
        axs[2].set_ylabel('Load (MW)')
        #axs[2].set_xlabel('Time (hours)')
        axs[2].set_title('Load',fontsize = 20)
        axs[2].grid(True)
        axs[2].margins(0)
        
        
        
        #fig.suptitle('8760 Time Series Plot of Wind, Solar, and Load')
        
        # Adjust layout to remove margins
        plt.subplots_adjust(hspace=0.1, top=0.95, bottom=0.05, left=0.05, right=0.95)
        # Format the x-axis to show months
        axs[2].xaxis.set_major_locator(mdates.MonthLocator())
        axs[2].xaxis.set_major_formatter(mdates.DateFormatter('%b'))
        axs[2].tick_params(axis='x', labelsize=14)
        
        plt.show()
        
    
    def create_results_folder(self,filepath):
        # Create Results folder
        if filepath is None:
            filepath = os.getcwd()
        else:
            filepath = filepath
        results_folder_path = os.path.join(
            filepath,'Results', self.data_handler.system+'_Results')
        if not os.path.exists(results_folder_path):
            os.mkdir(results_folder_path)
        
        # all results
        folder_name = str(self.data_handler.scenario)+'_LG' +str(self.data_handler.load_growth)+'_ESC'+str(self.data_handler.es_cost)+'_LDES'+str(self.data_handler.ldes_switch)+'_tx-'+ str(self.data_handler.tx_model)+str(self.data_handler.years[0])+'-'+str(self.data_handler.years[-1]) +'_'+str(self.timestamp)+'_'+str(self.data_handler.system)
        self.folder_path = os.path.join(results_folder_path, folder_name)
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)
            
        # bus expansion results folder
        self.bus_folder_path = os.path.join(
            self.folder_path, 'bus_exp_results')
        if not os.path.exists(self.bus_folder_path):
            os.mkdir(self.bus_folder_path)

        # cost results folder
        self.cost_folder_path = os.path.join(
            self.folder_path, 'cost_results')
        if not os.path.exists(self.cost_folder_path):
            os.mkdir(self.cost_folder_path)

        # dispatch results folder
        self.dispatch_folder_path = os.path.join(
            self.folder_path, 'dispatch_results')
        if not os.path.exists(self.dispatch_folder_path):
            os.mkdir(self.dispatch_folder_path)

        # map results folder
        self.map_folder_path = os.path.join(
            self.folder_path, 'map_results')
        if not os.path.exists(self.map_folder_path):
            os.mkdir(self.map_folder_path)

        # Tx results folder
        self.tx_folder_path = os.path.join(
            self.folder_path, 'Tx_results')
        if not os.path.exists(self.tx_folder_path):
            os.mkdir(self.tx_folder_path)

        # Policy folder
        self.policy_folder_path = os.path.join(
            self.folder_path, 'Policy_results')
        if not os.path.exists(self.policy_folder_path):
            os.mkdir(self.policy_folder_path)

        #print model stats to txt file
        txt_file = self.folder_path+'/model_stats.txt'
        
        with open(txt_file, "w") as text_file:
            print(self.report, file=text_file)

    def process_results_gui(self, rd, pd, timestamp, report,filepath):
        """Process the output of the optimizer - GUI only - filepath is provided as an option"""
        print('Process Results')
        self.rd = rd
        self.pd = pd
        self.timestamp = timestamp
        self.report = report
        
        self.create_results_folder(filepath=filepath)
        self.create_lookup_info()
        print("Model has solved to optimality and results have been processed. Please proceed to the Results page.")
        
    def process_results(self, rd, pd, timestamp, report):
        """Process the output of the optimizer - Command line only"""
        self.system = self.data_handler.system
        self.rd = rd
        self.pd = pd
        self.timestamp = timestamp
        self.report = report

        self.create_results_folder(filepath=None)

        self.create_lookup_info()
        self.plot_results()
        self.create_map()
        self.export_results()

    def plot_results(self):
        '''
        Create results plots and save in apprpriate folders
        '''
        
        fig, ax = plt.subplots(1, 1)
        self.stacked_resource_bar(fig,ax,figsize=[6,6])
        self.stacked_resource_area()
        
        if self.stacked_bar_by_bus_option:
            for b in self.bus_list:
                self.stacked_resource_bar_by_bus(b)
                self.stacked_resource_area_by_bus(b)
        else:
            print('Too many buses/zones for detailed buildout plots')
        
        self.plot_cost_bar()
        
        if self.data_handler.block_selection.lower() != 'Seasonal_Blocks'.lower():
            for y in self.data_handler.years:
                self.stacked_resource_dispatch(y)

            self.plot_tx_flow()
        
        if self.policy_plot_option:
            self.policy_plot()
            
        fig, ax = plt.subplots(1, 1)
        self.plot_es_system(fig,ax,figsize = [6,6])
        

    def create_map(self):
        '''
        Create map visualizations
        '''
        gen_map_info = self.data_handler.load_data[self.data_handler.data_ls.index('gen')][[
            'Gen_num', 'Bus_num', 'Bus', 'Tech', 'Tech_Num']]
        tech_map_info = self.data_handler.load_data[self.data_handler.data_ls.index('tech')][[
            'Tech', 'Tech_Name', 'Tech_Num']]

        self.map_results()

        self.map_es_results()
        
    def export_results(self):
        """
        Writes Excel file of optimizer's results

        Returns
        -------
        None.

        """

        filename = self.folder_path+'\\'+str(self.data_handler.scenario)+'_' + \
            str(self.data_handler.start_year)+'-' + str(self.data_handler.end_year) + \
            '_results_'+self.timestamp+'.xlsx'
        writer = pd.ExcelWriter(
            filename)  # , engine='xlsxwriter')

        for key in self.rd.keys():
            df = self.rd[key]  # pd.DataFrame()
            if df.empty == False:
                df.to_excel(writer, sheet_name=key)
        writer.close()
        # writer.save()
        print('Pyomo results exported to Excel')


    def color_tech(self,tech):#self,
        """
        
        Parameters
        ----------
        tech : technology

        Raises
        ------
        TypeError
            DESCRIPTION.

        Returns
        -------
        color : technology

        """

        global color
        #global fg
        
        tech_colors = {
        'Nuclear': 'darkred',
        'Coal': 'black',
        'Oil_CT': 'slategrey',
        'Oil_ST': 'lightslategrey',
        'Hydro': 'steelblue',
        'Gas': 'darkgrey',
        'Gas_CC': 'silver',
        'Gas_CT': 'dimgray',
        'Gas (New)': 'tan',
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
        'ES 6hr (New)': 'blue',
        'ES 8hr (New)': 'slateblue',
        'ES 10hr (New)': 'darkviolet',
        'ES 100hr (New)': 'deeppink',
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
        'Flow Battery (New) (0-2 hrs.)': '#f8bbee',  # LightPink
        'Flow Battery (New) (2-4 hrs.)': '#ee82ee',  # Violet
        'Flow Battery (New) (4-6 hrs.)': '#dda0dd',  # Plum
        'Flow Battery (New) (6-8 hrs.)': '#da70d6',  # Orchid
        'Flow Battery (New) (8-10 hrs.)': '#ba55d3', # MediumOrchid
        'Flow Battery (New) (10-15 hrs.)': '#9370db',# MediumPurple
        'Flow Battery (New) (15-24 hrs.)': '#8a2be2',# BlueViolet
        'Flow Battery (New) (24+ hrs.)': '#4b0082',  # Indigo
        'Grav (New)': 'orangered',
        'PSH (New)': 'darkblue',
        'Therm (New)': 'salmon',
        'Therm (New) (0-2 hrs.)': '#ffe4e1', # MistyRose
        'Therm (New) (2-4 hrs.)': '#ffb6c1',# LightPink
        'Therm (New) (4-6 hrs.)': '#ffa07a',# LightSalmon
        'Therm (New) (6-8 hrs.)': '#fa8072', # Salmon
        'Therm (New) (8-10 hrs.)': '#e9967a',  # DarkSalmon
        'Therm (New) (10-15 hrs.)': '#cd5c5c',  # IndianRed
        'Therm (New) (15-24 hrs.)': '#b22222',  # FireBrick
        'Therm (New) (24+ hrs.)': '#8b0000',  # DarkRed
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
        if tech not in tech_colors:
            raise TypeError(f"{tech} is not valid")
    
        return tech_colors[tech]

    def stacked_resource_bar(self,fig,ax,figsize):
        """
        Plot staked bar chart of installed capacity by year
        """

        results = self.rd['P_cap_total']
        if np.size(results.index.names) > 1:
            results.reset_index(inplace=True)
        # results.reset_index(inplace=True)
        # add tech name
        translate = {
            x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
        tech_num = [translate.get(x, x)
                    for x in results['g']]
        results['Technology'] = tech_num

        #all_tech = np.unique(gen_map_info['Tech_ID'])
        # need to reorder for stack plots

        #nums = np.arange(1,np.size(re_order_tech)+1)
        # num_tech =

        results_pivot = results[results['Value'] != 0].pivot_table(
            index=['y'], columns='Technology', values='Value', aggfunc='sum')

        # rename columns
        translate1 = {
            x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
        cols = [translate1.get(x, x)
                for x in results_pivot.columns]

        results_pivot.columns = cols
        
        # assign colors
        color_array = [self.color_tech(c) for c in cols]

        if figsize is None:
            results_pivot.plot.bar(stacked=True, color=color_array, ax=ax, legend=False, edgecolor="black", linewidth=0.75,width=0.5)
            ax.legend(loc="center left",
                      bbox_to_anchor=(1, 0.5),fontsize=7)
            ax.set_ylabel('Capacity (MW)')
            ax.set_xlabel('Years')
            ax.set_title('Installed capacity')
            #ax.tick_params(axis='both', which='major', labelsize=14)
            ax.margins(x=0, y=0)
        else:
            results_pivot.plot.bar(stacked=True, color=color_array, ax=ax, figsize=figsize, legend=False, edgecolor="black", linewidth=0.75,width=0.5)
            ax.legend(loc="center left",
                      bbox_to_anchor=(1, 0.5), fontsize=15)
            ax.set_ylabel('Capacity (MW)', fontsize=20)
            ax.set_xlabel('Years', fontsize=20)
            ax.set_title('Installed capacity', fontsize=25)
            ax.tick_params(axis='both', which='major', labelsize=14)
            ax.margins(x=0, y=0)
            plt.close(fig)
            fig.savefig(self.folder_path+'/'+str(self.data_handler.scenario) +
                        '_stacked_bar.png', bbox_inches='tight')
        # save legend as png for input into folium
    

    def stacked_resource_area(self):
        """

        Parameters
        ----------
        gen_map_info : TYPE
            DESCRIPTION.
        tech_map_info : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """

        results = self.rd['P_cap_total']
        if np.size(results.index.names) > 1:
            results = results.reset_index(inplace=True)
        # results.reset_index(inplace=True)
        # add tech name
        translate = {
            x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
        tech_num = [translate.get(x, x)
                    for x in results['g']]
        results['Technology'] = tech_num

        #all_tech = np.unique(gen_map_info['Tech_ID'])
        # need to reorder for stack plots

        #nums = np.arange(1,np.size(re_order_tech)+1)
        # num_tech =

        results_pivot = results[results['Value'] > 0].pivot_table(
            index=['y'], columns='Technology', values='Value', aggfunc='sum')

        results_pivot = results_pivot.fillna(0)
        # rename columns
        translate1 = {
            x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
        cols = [translate1.get(x, x)
                for x in results_pivot.columns]

        results_pivot.columns = cols
        # assign colors
        color_array = [self.color_tech(c) for c in cols]

        fig, ax = plt.subplots(1, 1)
        results_pivot.plot.area(stacked=True, color=color_array, figsize=[
            10, 8], legend=False, linewidth=0, ax=ax).figure
        ax.legend(loc="center left",
                  bbox_to_anchor=(1, 0.5), fontsize=15)
       
        ax.set_ylabel('Capacity (MW)', fontsize=20)
        ax.set_xlabel('Years', fontsize=20)
        ax.set_title('Installed capacity', fontsize=25)
        ax.tick_params(axis='both', which='major', labelsize=14)
        ax.margins(x=0, y=0)
        plt.close(fig)
        fig.savefig(self.folder_path+'/'+str(self.data_handler.scenario) +
                    '_stacked_area.png', bbox_inches='tight')

    def stacked_resource_bar_by_bus(self, bus):
        """


        Parameters
        ----------
        gen_map_info : TYPE
            DESCRIPTION.
        tech_map_info : TYPE
            DESCRIPTION.
        bus : TYPE
            DESCRIPTION.
        bus_names : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """

        results = self.rd['P_cap_total']
        results.reset_index(drop=True, inplace=True)
        # add tech name
        translate = {
            x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
        tech_num = [translate.get(x, x)
                    for x in results['g']]
        results['Technology'] = tech_num

        #all_tech = np.unique(gen_map_info['Tech_ID'])
        # need to reorder for stack plots

        #nums = np.arange(1,np.size(re_order_tech)+1)
        # num_tech =

        #bus_nums = np.unique(results['b'])
        #fig, axs = plt.subplots(int(np.size(bus_nums)/2)+1,int(np.size(bus_nums)/2))
        # for b in bus_nums:
        results_b = results.loc[results['b'] == bus]
        name = self.bus_names.loc[self.bus_names['Bus_number']
                             == bus]['Bus_name'].reset_index(drop=True)
        name = name[0]
        # np.size(results_b) != 0:
        results_pivot = results_b[results_b['Value'] != 0].pivot_table(
            index=['y'], columns='Technology', values='Value', aggfunc='sum')

        if results_pivot.empty == False:
            # rename columns
            translate1 = {
                x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
            cols = [translate1.get(x, x)
                    for x in results_pivot.columns]

            results_pivot.columns = cols
            # assign colors
            color_array = [self.color_tech(c) for c in cols]

            fig, ax = plt.subplots(1, 1)
            results_pivot.plot.bar(stacked=True, color=color_array, ax=ax, figsize=[
                10, 8], legend=False, edgecolor="black", linewidth=0)
            ax.legend(loc="center left",
                      bbox_to_anchor=(1, 0.5), fontsize=15)

            ax.set_ylabel('Capacity (MW)', fontsize=25)
            ax.set_xlabel('Years', fontsize=25)
            ax.set_title(
                'Installed capacity: Zone '+name, fontsize=30)
            ax.margins(x=0, y=0)
            plt.close(fig)
            fig.savefig(self.bus_folder_path+'/'+'_stacked_bar_' + str(name)
                        + '.png', bbox_inches='tight')
            # return fig
        else:
            fig, ax = plt.subplots(1, 1, figsize=[10, 8])
            ax.set_title(
                'Installed capacity: Zone '+name, fontsize=30)
            plt.close(fig)
            fig.savefig(self.bus_folder_path+'/'+'_stacked_bar_' + str(name)
                        + '.png', bbox_inches='tight')

    def stacked_resource_area_by_bus(self, bus):
        """


        Parameters
        ----------
        gen_map_info : TYPE
            DESCRIPTION.
        tech_map_info : TYPE
            DESCRIPTION.
        bus : TYPE
            DESCRIPTION.
        bus_names : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """

        results = self.rd['P_cap_total']
        results.reset_index(drop=True, inplace=True)
        # add tech name
        translate = {
            x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
        tech_num = [translate.get(x, x)
                    for x in results['g']]
        results['Technology'] = tech_num

        #all_tech = np.unique(gen_map_info['Tech_ID'])
        # need to reorder for stack plots

        #nums = np.arange(1,np.size(re_order_tech)+1)
        # num_tech =

        #bus_nums = np.unique(results['b'])
        #fig, axs = plt.subplots(int(np.size(bus_nums)/2)+1,int(np.size(bus_nums)/2))
        # for b in bus_nums:
        results_b = results.loc[results['b'] == bus]

        results_pivot = results_b[results_b['Value'] > 0].pivot_table(
            index=['y'], columns='Technology', values='Value', aggfunc='sum')
        results_pivot = results_pivot.fillna(0)

        name = self.bus_names[self.bus_names['Bus_number']
                         == bus]['Bus_name'].reset_index(drop=True)
        name = name[0]
        if results_pivot.empty == False:
            # rename columns
            translate1 = {
                x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
            cols = [translate1.get(x, x)
                    for x in results_pivot.columns]

            results_pivot.columns = cols
            # assign colors
            color_array = [self.color_tech(c) for c in cols]
            fig, ax = plt.subplots(1, 1)
            results_pivot.plot.area(stacked=True, color=color_array, figsize=[
                10, 8], legend=False, linewidth=0, ax=ax).figure
            ax.legend(loc="center left",
                      bbox_to_anchor=(1, 0.5), fontsize=15)

            ax.set_ylabel('Capacity (MW)', fontsize=25)
            ax.set_xlabel('Years', fontsize=25)
            ax.set_title(
                'Installed capacity: '+name, fontsize=30)
            ax.margins(x=0, y=0)
            plt.close(fig)
            fig.savefig(self.bus_folder_path+'/'+'_stacked_area_' + str(name)
                        + '.png', bbox_inches='tight')

            # return fig
        else:
            fig, ax = plt.subplots(1, 1, figsize=[10, 8])
            ax.set_title(
                'Installed capacity: Zone '+name, fontsize=30)
            plt.close(fig)
            fig.savefig(self.bus_folder_path+'/'+'_stacked_bar_' + str(name)
                        + '.png', bbox_inches='tight')

    def plot_cost_bar(self):
        """


        Returns
        -------
        None.

        """
        # gather cost data
        all_costs = pd.DataFrame()
        all_costs['FOM'] = self.rd['annual_fom_cost']
        all_costs['VOM'] = self.rd['annual_vom_cost']
        all_costs['Fuel'] = self.rd['annual_fuel_cost']
        all_costs['Penalty'] = self.rd['annual_ls_cost']
        all_inv_costs = pd.DataFrame()
        all_inv_costs['Generation Investment'] = self.rd['annual_gen_inv_cost']
        all_inv_costs['Transmission Investment'] = self.rd['annual_trans_inv_cost']
        all_inv_costs['ES Replacement Cost'] = self.rd['annual_es_replace_cost']

        colors = ['grey', 'mediumblue',
                  'saddlebrown', 'red']
        colors_inv = ['green', 'orange', 'salmon']
        fig, axs = plt.subplots(1, 2, figsize=[10, 4])
        all_costs.plot.bar(
            stacked=True, color=colors, ax=axs[0], title='Annual Operational Costs')
        all_inv_costs.plot.bar(
            stacked=True, color=colors_inv, ax=axs[1], title='Annual Investment Costs')
        plt.close(fig)
        fig.savefig(self.cost_folder_path +
                    '/'+'Total_Costs.png')

    def plot_tx_flow(self):
        """


        Returns
        -------
        None.

        """
        pf = self.rd['PF']
        if np.size(pf.index.names) > 1:
            pf = pf.reset_index()
        for y in self.data_handler.years:
            fig, axs = plt.subplots(
                len(np.unique(pf['s'])), 1, figsize=[12, 10], sharex=True)
            if self.data_handler.block_selection.lower() == 'Peak_Day'.lower():
                pf_y_s = pf.loc[(pf['y'] == y)].drop(
                    ['y', 's'], axis=1).set_index(['l'])
                pf_y_s.T.plot(
                    legend=False, ax=axs, title='Power Flow')
                axs.margins(x=0, y=0)
            else:
                for s in np.unique(pf['s']):
                    pf_y_s = pf.loc[(pf['y'] == y) & (pf['s'] == s)].drop(
                        ['y', 's'], axis=1).set_index(['l'])
                    if s == 1:
                        season = 'Winter'
                    elif s == 2:
                        season = 'Spring'
                    elif s == 3:
                        season = 'Summer'
                    elif s == 4:
                        season = 'Fall'
                    elif s == 5:
                        season = 'Peak Week'
                    ax = axs[s-1]
                    pf_y_s.T.plot(
                        legend=False, ax=ax, title=season)
                    ax.margins(x=0, y=0)
            fig.tight_layout()
            fig.suptitle(
                'Transmission Flow ('+str(y)+')', fontsize=20)
            fig.supxlabel('Time (h)')
            fig.supylabel('Power Flow (MW)')
            plt.close(fig)
            fig.savefig(self.tx_folder_path +
                        '/'+'Tx_Flow_'+str(y)+'.png')

    def plot_es_system(self,fig,ax,figsize):

        #bus_list = exp.data_handler.load_data['BUS']['Bus_number'].values
        # bus_names = exp.data_handler.load_data['BUS'][[
        #  'Bus_number', 'Bus_name']]

        results = self.rd['P_cap_total']
        results_en1 = self.rd['Store']
        if np.size(results.index.names) > 1:
            results.reset_index(inplace=True)#drop=True, inplace=True
        if np.size(results_en1.index.names) > 1:
            results_en1.reset_index(inplace=True)#drop=True,inplace=True
        #if np.size(results_en.index.names) > 1:
        #results_en.reset_index()#drop=True, inplace=True)
        # add tech name
        translate = {
            x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
        tech_num = [translate.get(x, x)
                    for x in results['g']]
        results['Technology'] = tech_num
        tech_num = [translate.get(x, x)
                    for x in results_en1['g']]
        results_en1['Technology'] = tech_num

        # filter for ES tech
        results = results[results['Technology'].isin(np.unique(
            self.data_handler.load_data[self.data_handler.data_ls.index('storage')]['Tech_Num']))]
        results['Energy'] = results_en1['Value'].values
        results['Duration'] = results['Energy'] / \
            results['Value']

        results_pivot = results.pivot_table(
            index=['y'], columns='Technology', values='Value', aggfunc='sum')
        results_pivot = results_pivot.fillna(0)
        translate1 = {
            x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
        cols = [translate1.get(x, x)
                for x in results_pivot.columns]
        results_pivot.columns = cols
        # filter out very small values - solver error
        results_pivot[results_pivot < 0.001] = 0
        # delete zero columns
        results_pivot = results_pivot.loc[:, (results_pivot != 0).any(
            axis=0)]

        # fig, ax = plt.subplots(1, 1, figsize=[
        # 10, 8])
        #ax2 = ax.twinx()
        color_array = [
            self.color_tech(c) for c in results_pivot.columns]
        #print(cols)
        #print(color_array)
        # results_pivot.plot.bar(
        #   stacked=True, color=color_array, legend=False, linewidth=3, ax=ax).figure

        results_en_pivot = results.pivot_table(
            index=['y'], columns='Technology', values='Energy', aggfunc='sum')
        results_en_pivot = results_en_pivot.fillna(0)
        translate1 = {
            x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
        cols = [translate1.get(x, x)
                for x in results_en_pivot.columns]
        results_en_pivot.columns = cols
        # filter out very small values - solver error
        results_en_pivot[results_en_pivot < 0.001] = 0
        # delete zero columns
        results_en_pivot = results_en_pivot.loc[:, (results_en_pivot != 0).any(
            axis=0)]
        # color_array = [
        #  self.color_tech(c) for c in cols]

        #results_pivot['Energy'] = results_en_pivot.values
        # ax2.plot(results_pivot.index,
        #       results_pivot['Energy'], linestyle='-', marker='o')
        # results_pivot['Energy'].plot(
        #   kind='line', marker='d', secondary_y=True, ax=ax2)
        # results_pivot.loc[:,results_pivot.columns != 'Energy'].plot.bar(
        #    stacked=True, color=color_array, legend=False, linewidth=3, ax=ax)
        if figsize is None:
            results_pivot.plot(kind='bar',stacked=True, align='edge', width=-0.4, color=color_array, legend=True, linewidth=0.3,ax=ax,edgecolor='black')
            results_en_pivot.plot(kind='bar',stacked=True, align='edge', width=0.4, color=color_array, legend=True, secondary_y=True,linewidth=0.3,ax=ax,edgecolor='black', hatch='///')
            ax.set_xlim(-.6,len(results_pivot.index)-1+.6)
            max_all= max([max(results_pivot.sum(axis=1)),max(results_en_pivot.sum(axis=1))])
            ax.set_ylim(0,max_all)
            h,l = ax.get_legend_handles_labels()
         
            
            l1 = ax.legend(loc="center left",
                      bbox_to_anchor=(1.2, 0.3), fontsize=7, ncol=1)
            
            
            patch_hatched = mpatches.Patch(facecolor='beige', hatch=' ', edgecolor="darkgrey", label='Power')
            patch_unhatched = mpatches.Patch(facecolor='beige', hatch='///', edgecolor="darkgrey", label='Energy')
            
            l2=fig.legend(handles=[patch_hatched, patch_unhatched], loc='center left', bbox_to_anchor=(1.06, 0.5))
    
            # as soon as a second legend is made, the first disappears and needs to be added back again
            fig.add_artist(l1) 
            
            ax.set_ylabel('Power Capacity (MW)')
            ax.right_ax.set_ylabel('Energy Capacity (MWh)')
            ax.set_xticklabels(results_pivot.index, rotation=75)
            #ax2.set_ylabel('Energy Capacity (MWh)', fontsize=25)
            ax.set_xlabel('Years')
            #ax.tick_params(axis='both',  labelsize=14)#
            #ax.right_ax.tick_params(axis='both',  labelsize=14)
            #secax = ax.secondary_yaxis('right')
            #secax.tick_params( labelsize=14)
            ax.set_title(
                'Installed ES capacity')
            ax.margins(x=0, y=0)
            #plt.yticks(14)
            
        else:
            results_pivot.plot(kind='bar',stacked=True, align='edge', width=-0.4, color=color_array, legend=True, linewidth=0.3,ax=ax,edgecolor='black',figsize=figsize)
            results_en_pivot.plot(kind='bar',stacked=True, align='edge', width=0.4, color=color_array, legend=True, secondary_y=True,linewidth=0.3,ax=ax,edgecolor='black', hatch='///')
            ax.set_xlim(-.6,len(results_pivot.index)-1+.6)
            max_all= max([max(results_pivot.sum(axis=1)),max(results_en_pivot.sum(axis=1))])
            ax.set_ylim(0,max_all)
            h,l = ax.get_legend_handles_labels()
         
            
            l1 = ax.legend(loc="center left",
                      bbox_to_anchor=(1.2, 0.3), fontsize=12, ncol=1)
            
            patch_hatched = mpatches.Patch(facecolor='beige', hatch=' ', edgecolor="darkgrey", label='Power')
            patch_unhatched = mpatches.Patch(facecolor='beige', hatch='///', edgecolor="darkgrey", label='Energy')
            
            l2=fig.legend(handles=[patch_hatched, patch_unhatched], loc='center left', bbox_to_anchor=(1.06, 0.5), fontsize=12)

            # as soon as a second legend is made, the first disappears and needs to be added back again
            fig.add_artist(l1) 
            
            ax.set_ylabel('Power Capacity (MW)', fontsize=20)
            ax.right_ax.set_ylabel('Energy Capacity (MWh)', fontsize=20)
            ax.set_xticklabels(results_pivot.index, rotation=75)
            #ax2.set_ylabel('Energy Capacity (MWh)', fontsize=25)
            ax.set_xlabel('Years', fontsize=20)
            ax.tick_params(axis='both',  labelsize=14)#
            ax.right_ax.tick_params(axis='both',  labelsize=14)
            #secax = ax.secondary_yaxis('right')
            #secax.tick_params( labelsize=14)
            ax.set_title(
                'Installed ES capacity', fontsize=24)
            ax.margins(x=0, y=0)
            #plt.yticks(14)
            # plt.close(fig)
            fig.savefig(self.folder_path+'/' +
                        'ES_inv_MWh'+'.png')
        
    # Policy results viewer

    def policy_plot(self):
        """


        Returns
        -------
        None.

        """
        CO2_int = self.rd['CO2_intensity']
        CO2_em = self.rd['CO2_emission']
        if np.size(CO2_em.index.names) > 1:
            results = CO2_em.reset_index()
        carbon_gen = self.rd['carbon_gen']
        if np.size(carbon_gen.index.names) > 1:
            results = carbon_gen.reset_index()
        ren_gen = self.rd['ren_gen']
        if np.size(ren_gen.index.names) > 1:
            results = ren_gen.reset_index()

        # make plots
        CO2_em_y = CO2_em.pivot_table(
            index=['y'], values='Value', aggfunc='sum')
        carbon_gen_y = carbon_gen.pivot_table(
            index=['y'], values='Value', aggfunc='sum')
        ren_gen_y = ren_gen.pivot_table(
            index=['y'], values='Value', aggfunc='sum')

        CO2_em_y.columns = ['CO2 Emissions']
        CO2_int.columns = ['CO2 Intensity']
        fig, ax = plt.subplots(1, 1)
        CO2_em_y.plot(ax=ax, figsize=[15, 8])
        CO2_int.plot(ax=ax, secondary_y=True,
                     figsize=[15, 8])
        ax.set_ylabel('Emissions (Tons)', fontsize=25)
        ax.right_ax.set_ylabel(
            'Intensity (Tons/MWh)', fontsize=25)
        ax.set_xlabel('Years', fontsize=25)
        ax.set_title('PNM Annual Emissions', fontsize=30)
        ax.margins(x=0, y=0)
        plt.close(fig)
        fig.savefig(self.policy_folder_path+'/' +
                    'CO2_emissions'+'.png')

        gen = pd.concat([carbon_gen_y, ren_gen_y], axis=1)
        gen.columns = ['CO2 Generation',
                       'Renewable Generation']
        fig, ax = plt.subplots(1, 1)
        gen.plot.bar(
            ax=ax, color=['grey', 'green'], figsize=[12, 8])
        ax.set_ylabel('Generation (MWh)', fontsize=25)
        ax.set_xlabel('Years', fontsize=25)
        ax.set_title('PNM Annual Generation', fontsize=30)
        ax.margins(x=0, y=0)
        plt.close(fig)
        fig.savefig(self.policy_folder_path+'/' +
                    'Annual_Generation'+'.png')
        # pd.DataFrame(columns=['CO2 Generation', 'Renewable Generation'],
        #                  index=ren_gen_y.index, data=[carbon_gen_y['Value'],ren_gen_y['Value']])

        #ax2 = carbon_gen_y.plot.bar(color='grey')
        #ren_gen_y.plot.bar(ax=ax2, color='green')

    def policy_resource_plot(self):
        """


        Returns
        -------
        None.

        """
        policy = self.data_handler.load_data[self.data_handler.data_ls.index('policy')]#['RPS']
        #CO2 = exp.data_handler.load_data['POLICY']#['CO2']
        
        gen = self.data_handler.load_data[self.data_handler.data_ls.index('gen')]
        
        gen_mx = pd.DataFrame(index = range(2021,2041),columns = ['Nuclear','Coal','Gas','Geothermal'])#'Solar','Wind_PPA','ES_PPA'
        gen_mx = gen_mx.fillna(0)
        for y in  gen_mx.index:
            for g in gen.index:
                gen_i = gen.iloc[g]
                #if gen_i['Tech']=='Nuclear':
                tech = gen_i['Tech']
                if tech in gen_mx.columns:
                    if y<gen_i['RetYr']:
                        gen_mx[tech][y] = gen_mx[tech][y]+gen_i['Cap']
                    elif y>=gen_i['RetYr']:
                        gen_mx[tech][y] = gen_mx[tech][y]+gen_i['Cap']-gen_i['RetCap']
        
        #make plot
        fig, ax = plt.subplots(1, 1)
       
        ax3 = ax.twinx()
        rspine = ax3.spines['right']
        rspine.set_position(('axes', 1.15))
        ax3.set_frame_on(True)
        ax3.patch.set_visible(False)
        fig.subplots_adjust(right=0.7)
        
        #df.A.plot(ax=ax, style='b-')
        gen_mx.plot.bar(stacked=True,ax=ax,color = ['darkred','black','darkgrey','rosybrown'],figsize=[12, 6])
        
        # same ax as above since it's automatically added on the right
        #df.B.plot(ax=ax, style='r-', secondary_y=True)
        #df.C.plot(ax=ax3, style='g-')
        policy['RPS'].plot(ax=ax,secondary_y=True,legend =False,color='green', linestyle='--',linewidth=4)
        policy['CO2_intensity'].plot(ax=ax3,legend =False,color='blue', linestyle='-.',linewidth=4)            
        ax.set_ylabel('Capacity (MW)', fontsize=12,fontweight='bold')
        ax.set_xlabel('Year',fontsize=12,fontweight='bold')
        ax.right_ax.set_ylabel('RPS (%)', fontsize=12,fontweight='bold',color='green')
        ax3.set_ylabel('CO2 Intensity (MM Ton/MWhr)', fontsize=12,fontweight='bold',color='blue')
        ax.set_xticklabels(gen_mx.index, rotation=75)
        #plt.tight_layout()
        ax.right_ax.tick_params(axis='y', colors='green')
        ax.right_ax.spines['right'].set_color('green')
        
        ax3.tick_params(axis='y', colors='blue')
        ax3.spines['right'].set_color('blue')
        plt.grid(True)
        
        #lns = ax+ax3#lns1+lns2+lns3
        #labs = [l.get_label() for l in lns]
        #ax.legend([ax.get_label(),ax3.get_label()], labs, loc=0)
        lines, labels = ax.get_legend_handles_labels()
        lines1, labels1 = ax.right_ax.get_legend_handles_labels()
        labels1 = ['RPS']
        lines2, labels2 = ax3.get_legend_handles_labels()
        ax.legend(lines + lines1+lines2, labels+labels1 + labels2, loc=1,bbox_to_anchor=(1.2, -0.152),ncol=6,fontsize=12)
        
        # add legend --> take advantage of pandas providing us access
        # to the line associated with the right part of the axis
        #ax3.legend([ax.get_lines()[0], ax.right_ax.get_lines()[0], ax3.get_lines()[0]],\
         #          ['A','B','C'], bbox_to_anchor=(1.5, 0.5))
         
    def energy_storage_cost(self):
        '''
        

        Returns
        -------
        None.

        '''
        es_pwr_en_cost = exp.data_handler.load_data[self.data_handler.data_ls.index('capex_es')]#['RPS']
        
        select_costs = es_pwr_en_cost[es_pwr_en_cost['Tech_name'].isin(['Li_Ion_Cand_1','Flow_Cand','Therm_Cand'])]
        
        select_power_costs = select_costs[select_costs['Cost']=='Power'].drop(['Tech_num','Cost'],axis=1).set_index('Tech_name').T
        select_energy_costs = select_costs[select_costs['Cost']=='Energy'].drop(['Tech_num','Cost'],axis=1).set_index('Tech_name').T
        
        select_power_costs.columns = ['Li-Ion (Base)','Flow (Base)','Thermal (Base)']
        select_energy_costs.columns = ['Li-Ion (Base)','Flow (Base)','Thermal (Base)']
        
        select_power_costs = select_power_costs[select_power_costs.index.isin(years)]
        select_energy_costs = select_energy_costs[select_energy_costs.index.isin(years)]
        
        years = range(2023,2051)
        
        #High
        es_h_pwr_en_cost = exp.data_handler.load_data['CAPEX_H_ES']#['RPS']
        
        select_costs_h = es_h_pwr_en_cost[es_h_pwr_en_cost['Tech_name'].isin(['Li_Ion_Cand','Flow_Cand','Therm_Cand'])]
        
        select_power_costs_h = select_costs_h[select_costs_h['Cost']=='Power'].drop(['Tech_num','Cost'],axis=1).set_index('Tech_name').T
        select_energy_costs_h = select_costs_h[select_costs_h['Cost']=='Energy'].drop(['Tech_num','Cost'],axis=1).set_index('Tech_name').T
        
        select_power_costs_h.columns = ['Li-Ion (High)','Flow (High)','Thermal (High)']
        select_energy_costs_h.columns = ['Li-Ion (High)','Flow (High)','Thermal (High)']
        
        select_power_costs_h = select_power_costs_h[select_power_costs_h.index.isin(years)]
        select_energy_costs_h = select_energy_costs_h[select_energy_costs_h.index.isin(years)]
        #Low
        es_l_pwr_en_cost = exp.data_handler.load_data['CAPEX_L_ES']#['RPS']
        
        select_costs_l = es_l_pwr_en_cost[es_l_pwr_en_cost['Tech_name'].isin(['Li_Ion_Cand','Flow_Cand','Therm_Cand'])]
        
        select_power_costs_l = select_costs_l[select_costs_l['Cost']=='Power'].drop(['Tech_num','Cost'],axis=1).set_index('Tech_name').T
        select_energy_costs_l = select_costs_l[select_costs_l['Cost']=='Energy'].drop(['Tech_num','Cost'],axis=1).set_index('Tech_name').T
        
        select_power_costs_l.columns = ['Li-Ion (Low)','Flow (Low)','Thermal (Low)']
        select_energy_costs_l.columns = ['Li-Ion (Low)','Flow (Low)','Thermal (Low)']
        
        select_power_costs_l = select_power_costs_l[select_power_costs_l.index.isin(years)]
        select_energy_costs_l = select_energy_costs_l[select_energy_costs_l.index.isin(years)]
        
        
        #make plot
        fig, ax = plt.subplots(1, 2,figsize=[8, 6])
        select_power_costs.plot(ax=ax[0],legend=False,color = ['royalblue','darkviolet','red'],figsize=[12, 6])
        select_energy_costs.plot(ax=ax[1],secondary_y = False,legend=False,color = ['royalblue','darkviolet','red'])
        
        select_power_costs_h.plot(ax=ax[0],legend=False,color = ['royalblue','darkviolet','red'],figsize=[12, 6], linestyle='--')
        select_energy_costs_h.plot(ax=ax[1],secondary_y = False,legend=False,color = ['royalblue','darkviolet','red'], linestyle='--')

        select_power_costs_l.plot(ax=ax[0],legend=False,color = ['royalblue','darkviolet','red'],figsize=[12, 6], linestyle='-.')
        select_energy_costs_l.plot(ax=ax[1],secondary_y = False,legend=False,color = ['royalblue','darkviolet','red'], linestyle='-.')
        
        ax[0].fill_between(years,select_power_costs_h['Thermal (High)'],select_power_costs_l['Thermal (Low)'],facecolor='red',alpha = 0.2)
        ax[0].fill_between(years,select_power_costs_h['Li-Ion (High)'],select_power_costs_l['Li-Ion (Low)'],facecolor='royalblue',alpha = 0.2)
        ax[0].fill_between(years,select_power_costs_h['Flow (High)'],select_power_costs_l['Flow (Low)'],facecolor='darkviolet',alpha = 0.2)

        ax[1].fill_between(years,select_energy_costs_h['Thermal (High)'],select_energy_costs_l['Thermal (Low)'],facecolor='red',alpha = 0.2)
        ax[1].fill_between(years,select_energy_costs_h['Li-Ion (High)'],select_energy_costs_l['Li-Ion (Low)'],facecolor='royalblue',alpha = 0.2)
        ax[1].fill_between(years,select_energy_costs_h['Flow (High)'],select_energy_costs_l['Flow (Low)'],facecolor='darkviolet',alpha = 0.2)

        ax[0].margins(x=0,y=0)
        ax[1].margins(x=0,y=0)
        ax[0].grid(True)
        ax[1].grid(True)
        
        ax[0].set_ylabel('Power Cost ($/kW)', fontsize=12,fontweight='bold')
        ax[1].set_ylabel('Energy Cost ($/kWh)', fontsize=12,fontweight='bold')
        fig.supxlabel('Year',fontsize=12,fontweight='bold')
        ax[0].legend(bbox_to_anchor=(1.75, -0.142),ncol=3,fontsize=12)
        #ax.right_ax.set_ylabel('Energy Cost ($/kWh)', fontsize=12,fontweight='bold')#,color='green')
        
    

    def map_results(self):
        """


        Parameters
        ----------
        gen_map_info : TYPE
            DESCRIPTION.
        tech_map_info : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        gen_lat_lon_df = self.data_handler.load_data[self.data_handler.data_ls.index('gen_viz')]

        # self.rd['P_cap_total']
        #results = exp.var_dict['P_cap_total']
        results = self.rd['P_cap_total']
        if np.size(results.index.names) > 1:
            results.reset_index(inplace=True)
        translate = {
            x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
        tech_num = [translate.get(x, x)
                    for x in results['g']]
        results['Technology'] = tech_num
        translate1 = {
            x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
        tech_name = [translate1.get(x, x)
                     for x in results['Technology']]
        results['Tech_Name'] = tech_name
        
        tx_expansion = self.rd['L_cap_total']
        if np.size(tx_expansion.index.names) > 1:
            tx_expansion.reset_index(inplace=True)
        
        line_data = self.data_handler.load_data[self.data_handler.data_ls.index('branch')]
        bus_data = self.data_handler.load_data[self.data_handler.data_ls.index('bus')]
        
        #TODO: Custom scaling options for viz purposes only
        if self.system == 'PNM':
            rad_div = 10
            line_div = 100
        elif self.system == 'RTS_GMLC_Nodal':
            rad_div = 16
            line_div = 100
        else:
            rad_div = 16
            line_div = 100
        
        for y in self.data_handler.years:  # self.data_handler.years:
            m = folium.Map(location=[34.41013879673766, -
                                     105.98914264797419], zoom_start=6.5, zoom_control=True,
                           scrollWheelZoom=True,
                           dragging=True)
            # Add lines to the map
            l_fg = folium.FeatureGroup(
                name='Tx', overlay=True)
            l_ex = folium.FeatureGroup(
                name='Tx_exp', overlay=True)
            
            for l in line_data['Line_Number']:
                line = line_data[line_data['Line_Number'] == l]
                from_bus = int(
                    line['From_Bus_Number'])
                to_bus = int(line['To_Bus_Number'])
                from_pt = tuple((float(bus_data[bus_data['Bus_number'] == from_bus]
                                ['LAT']), float(bus_data[bus_data['Bus_number'] == from_bus]['LON'])))
                to_pt = tuple((float(bus_data[bus_data['Bus_number'] == to_bus]
                              ['LAT']), float(bus_data[bus_data['Bus_number'] == to_bus]['LON'])))
                weight_y = tx_expansion[(tx_expansion['l']==l) & (tx_expansion['y']==y)]['Value'].values[0]
                #weight_y_l = weight_y[weight_y['l']==line]
                #print(weight_y)
                weight = float(weight_y)
            
                
                folium.PolyLine((from_pt, to_pt), color="black",
                                weight=2, opacity=1).add_to(l_fg)
                folium.PolyLine((from_pt, to_pt), color="blue",
                                weight=weight/line_div, opacity=1).add_to(l_ex)
                
            m.add_child(l_fg)
            m.add_child(l_ex)

            results_y = results[results['y'] == y]
            results_y = results_y[results_y['Value'] > 0]

            for tech in np.unique(results_y['Tech_Name']):
                results_y_t = results_y[results_y['Tech_Name'] == tech]
                color = self.color_tech(tech)
                fg = folium.FeatureGroup(
                    name=tech, overlay=True)

                for g in results_y_t['g']:
                    gen = results_y_t[results_y_t['g'] == g]
                    #t_name = gen['Tech_Name'].values[0]

                    # self.color_tech(t_name)
                    #fg = folium.FeatureGroup(name=t_name, overlay=True)
                    # Change...

                    lat = gen_lat_lon_df[gen_lat_lon_df['Gen_num']
                                         == g]['LAT']
                    lon = gen_lat_lon_df[gen_lat_lon_df['Gen_num']
                                         == g]['LON']
                    capacity = float(gen['Value'])
                    folium.CircleMarker((lat, lon), color=color, fill_color=color, opacity=1,
                                        fill_opacity=0.5,  radius=capacity/rad_div).add_to(fg)  # number_of_sides=4,
                m.add_child(fg)

            # Create a layer control object and add it to our map instance
            folium.LayerControl().add_to(m)
            map_title = 'Generation_'+str(y)+'.html'
            m.save(self.map_folder_path+"/"+map_title)

    def map_es_results(self):
        """


        Parameters
        ----------
        gen_map_info : TYPE
            DESCRIPTION.
        tech_map_info : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        gen_lat_lon_df = self.data_handler.load_data[self.data_handler.data_ls.index('gen_viz')]

        # self.rd['P_cap_total']
        #results = exp.var_dict['P_cap_total']
        results = self.rd['P_cap_total']
        results_en = self.rd['Store']
        if np.size(results.index.names) > 1:
            results.reset_index(inplace=True)
        if np.size(results_en.index.names) > 1:
            results_en.reset_index(inplace=True)

        translate = {
            x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
        tech_num = [translate.get(x, x)
                    for x in results['g']]
        results['Technology'] = tech_num
        translate1 = {
            x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
        tech_name = [translate1.get(x, x)
                     for x in results['Technology']]
        results['Tech_Name'] = tech_name

        # filter down into ES technologies only
        results = results[results['g'].isin(
            self.data_handler.tech_nums['storage'])]

        # Add energy components
        results = results.assign(
            energy=list(results_en['Value'].values))

        line_data = self.data_handler.load_data[self.data_handler.data_ls.index('branch')]
        bus_data = self.data_handler.load_data[self.data_handler.data_ls.index('bus')]

        if self.system == 'PNM':
            rad_div = 10
        elif self.system == 'RTS_GMLC_Nodal':
            rad_div = 16
        else:
            rad_div = 10
            line_div = 100

        # get min and max durations for bounds
        # min_duration = self.data_handler.load_data['STORAGE'][[
        #   'Tech_Num', 'Min_Duration']].pivot_table(index='Tech_Num', values='Min_Duration', aggfunc='min')
        # max_duration = self.data_handler.load_data['STORAGE'][[
        #   'Tech_Num', 'Max_Duration']].pivot_table(index='Tech_Num', values='Max_Duration', aggfunc='max')
        for y in self.data_handler.years:  # self.data_handler.years:
            m = folium.Map(location=[34.41013879673766, -
                                     105.98914264797419], zoom_start=6.5, zoom_control=True,
                           scrollWheelZoom=True,
                           dragging=True)
            # Add lines to the map
            l_fg = folium.FeatureGroup(
                name='Tx', overlay=True)
            for l in line_data['Line_Number']:
                line = line_data[line_data['Line_Number'] == l]
                from_bus = int(
                    line['From_Bus_Number'])
                to_bus = int(line['To_Bus_Number'])
                from_pt = tuple((float(bus_data[bus_data['Bus_number'] == from_bus]
                                ['LAT']), float(bus_data[bus_data['Bus_number'] == from_bus]['LON'])))
                to_pt = tuple((float(bus_data[bus_data['Bus_number'] == to_bus]
                              ['LAT']), float(bus_data[bus_data['Bus_number'] == to_bus]['LON'])))
                folium.PolyLine((from_pt, to_pt), color="black",
                                weight=2, opacity=1).add_to(l_fg)
            m.add_child(l_fg)

            results_y = results[results['y'] == y]
            results_y = results_y[results_y['Value'] > 0]

            duration = results_y['energy'] / \
                results_y['Value']
            min_d_t = 1  # int(min_duration.loc[tn])
            # int(max_duration.loc[tn])
            max_d_t = int(duration.max())

            # cm_opts = ['YlOrBr', 'PRGn', 'RdGy',
            #            'PuBu', 'PiYG', 'spectral']
            for tech in np.unique(results_y['Tech_Name']):
                
                results_y_t = results_y[results_y['Tech_Name'] == tech]
                # tn = int(
                #     np.unique(results_y_t['Technology'].values))
                # min_d_t = 1  # int(min_duration.loc[tn])
                # max_d_t = 10  # int(max_duration.loc[tn])
                # if min_d_t == max_d_t:
                #     min_d_t = 1
                # color = self.color_tech(tech)

                colormap = cm.LinearColormap(colors=['darkblue', 'lightblue', 'yellow', 'red'],  # 'yellow', 'orange', 'red'],
                                             vmin=min_d_t, vmax=max_d_t,
                                             caption=tech+' Duration (h)')  # index=[0, 25, 62.5, 156.25, 390.6, 1000],

                fg = folium.FeatureGroup(
                    name=tech, overlay=True)

                for g in results_y_t['g']:
                    gen = results_y_t[results_y_t['g'] == g]
                    #t_name = gen['Tech_Name'].values[0]

                    # self.color_tech(t_name)
                    #fg = folium.FeatureGroup(name=t_name, overlay=True)
                    # Change...

                    lat = gen_lat_lon_df[gen_lat_lon_df['Gen_num']
                                         == g]['LAT']
                    lon = gen_lat_lon_df[gen_lat_lon_df['Gen_num']
                                         == g]['LON']
                    power = float(gen['Value'])
                    energy = float(gen['energy'])
                    duration_g = energy/power

                    color = colormap(duration_g)
                    if tech == 'Therm (New)':#g in [132,133,134,135,136,137]:
                        folium.RegularPolygonMarker((lat, lon), color=color, fill_color=color, opacity=1,
                                        fill_opacity=0.5,  radius=power/rad_div,number_of_sides=5).add_to(fg)
                    else:
                        folium.CircleMarker((lat, lon), color=color, fill_color=color, opacity=1,
                                        fill_opacity=0.5,  radius=power/rad_div).add_to(fg)  # number_of_sides=4,
                m.add_child(fg)
                m.add_child(colormap)
                # colormap.add_to(m)

            # Create a layer control object and add it to our map instance
            folium.LayerControl().add_to(m)
            map_title = 'ES_'+str(y)+'.html'
            m.save(self.map_folder_path +
                   "/"+map_title)

    def map_ren_cf(self):
        """


        Parameters
        ----------
        gen_map_info : TYPE
            DESCRIPTION.
        tech_map_info : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        gen_lat_lon_df = self.data_handler.load_data[self.data_handler.data_ls.index('gen_viz')]

        # self.rd['P_cap_total']
        #results = exp.var_dict['P_cap_total']
        results = self.rd['P_cap_total']
        results_en = self.rd['Store']
        if np.size(results.index.names) > 1:
            results.reset_index(inplace=True)
        if np.size(results_en.index.names) > 1:
            results_en.reset_index(inplace=True)

        translate = {
            x: y for x, y in self.gen_map_info[['Gen_num', 'Tech_Num']].values}
        tech_num = [translate.get(x, x)
                    for x in results['g']]
        results['Technology'] = tech_num
        translate1 = {
            x: y for x, y in self.tech_map_info[['Tech_Num', 'Tech_Name']].values}
        tech_name = [translate1.get(x, x)
                     for x in results['Technology']]
        results['Tech_Name'] = tech_name

        # filter down into ES technologies only
        results = results[results['g'].isin(
            self.data_handler.tech_nums['storage'])]

        # Add energy components
        results = results.assign(
            energy=list(results_en['Value'].values))

        line_data = self.data_handler.load_data[self.data_handler.data_ls.index('branch')]
        bus_data = self.data_handler.load_data[self.data_handler.data_ls.index('bus')]

        if self.system == 'PNM':
            rad_div = 10
        elif self.system == 'RTS_GMLC_Nodal':
            rad_div = 16
        else:
            rad_div = 10
            

        # get min and max durations for bounds
        # min_duration = self.data_handler.load_data['STORAGE'][[
        #   'Tech_Num', 'Min_Duration']].pivot_table(index='Tech_Num', values='Min_Duration', aggfunc='min')
        # max_duration = self.data_handler.load_data['STORAGE'][[
        #   'Tech_Num', 'Max_Duration']].pivot_table(index='Tech_Num', values='Max_Duration', aggfunc='max')
        for y in self.data_handler.years:  # self.data_handler.years:
            m = folium.Map(location=[34.41013879673766, -
                                     105.98914264797419], zoom_start=6.5, zoom_control=True,
                           scrollWheelZoom=True,
                           dragging=True)
            # Add lines to the map
            l_fg = folium.FeatureGroup(
                name='Tx', overlay=True)
            for l in line_data['Line_Number']:
                line = line_data[line_data['Line_Number'] == l]
                from_bus = int(
                    line['From_Bus_Number'])
                to_bus = int(line['To_Bus_Number'])
                from_pt = tuple((float(bus_data[bus_data['Bus_number'] == from_bus]
                                ['LAT']), float(bus_data[bus_data['Bus_number'] == from_bus]['LON'])))
                to_pt = tuple((float(bus_data[bus_data['Bus_number'] == to_bus]
                              ['LAT']), float(bus_data[bus_data['Bus_number'] == to_bus]['LON'])))
                folium.PolyLine((from_pt, to_pt), color="black",
                                weight=2, opacity=1).add_to(l_fg)
            m.add_child(l_fg)

            results_y = results[results['y'] == y]
            results_y = results_y[results_y['Value'] > 0]

            cm_opts = ['YlOrBr', 'PRGn', 'RdGy',
                       'PuBu', 'PiYG', 'spectral']
            for tech in np.unique(results_y['Tech_Name']):
                results_y_t = results_y[results_y['Tech_Name'] == tech]
                tn = int(
                    np.unique(results_y_t['Technology'].values))
                min_d_t = 1  # int(min_duration.loc[tn])
                max_d_t = 10  # int(max_duration.loc[tn])
                if min_d_t == max_d_t:
                    min_d_t = 1
                color = self.color_tech(tech)
                colormap = cm.LinearColormap(colors=['darkblue', 'lightblue', 'yellow', 'red'],  # 'yellow', 'orange', 'red'],
                                             vmin=min_d_t, vmax=max_d_t,
                                             caption=tech+' Duration (h)')  # index=[0, 25, 62.5, 156.25, 390.6, 1000],

                fg = folium.FeatureGroup(
                    name=tech, overlay=True)

                for g in results_y_t['g']:
                    gen = results_y_t[results_y_t['g'] == g]
                    #t_name = gen['Tech_Name'].values[0]

                    # self.color_tech(t_name)
                    #fg = folium.FeatureGroup(name=t_name, overlay=True)
                    # Change...

                    lat = gen_lat_lon_df[gen_lat_lon_df['Gen_num']
                                         == g]['LAT']
                    lon = gen_lat_lon_df[gen_lat_lon_df['Gen_num']
                                         == g]['LON']
                    capacity = float(gen['Value'])
                    color = colormap(
                        float(gen['energy'])/capacity)
                    folium.CircleMarker((lat, lon), color=color, fill_color=color, opacity=1,
                                        fill_opacity=0.5,  radius=capacity/rad_div).add_to(fg)  # number_of_sides=4,
                m.add_child(fg)
                m.add_child(colormap)
                # colormap.add_to(m)

            # Create a layer control object and add it to our map instance
            folium.LayerControl().add_to(m)
            map_title = 'ES_'+str(y)+'.html'
            m.save(self.map_folder_path +
                   "/"+map_title)


def read_input_yaml(yaml_file):
    '''
    Read input YAML file

    Parameters
    ----------
    yaml_file : str
        Path to the input YAML file.

    Returns
    -------
    dict
        Dictionary of input parameters.
    '''
    with open(yaml_file, 'r') as f:
        return yaml.safe_load(f)
    
if __name__ == '__main__':
    #parser = argparse.ArgumentParser(description='Run Explan simulation with specified YAML configuration file.')
    #parser.add_argument('yaml_file', type=str, help='Path to the input YAML file.')
    #args = parser.parse_args()

    current_dir = os.getcwd()
    input_dict = read_input_yaml('input_rts_test.yaml')
    #current_dir = os.getcwd()
    #input_dict = read_input_yaml('input.yaml')

    data_file = os.path.join(current_dir, 'Data', input_dict['data_folder'])
    input_dict['data_dir'] = data_file
    input_dict['data_ls'] = ['bus','branch','capex_es','capex_l_es','capex_h_es','capex_tech','fuel','gen','gen_viz','load','scalars','solar','storage','tech','wind','policy','disfact','solar_cand','wind_cand']
    

    exp = Explan(input_dict)
    exp.setup_data_handler()
    exp.load_data()
    exp.results = ExplanResultsViewer_Ex(exp.data_handler)
    exp.results.create_lookup_info()
    #exp.results.plot_time_series()
    
    scenarios = exp.results.load_scenarios('C:/Users/cjnewlu/Desktop/PNM-CRADA_CJN/quest-planning/Results/RTS_GMLC_Results/PESGM/Scenario')
    #exp.results.stacked_resource_es_duration_bar(scenarios,figsize=[20,6])
    exp.results.stacked_resource_es_duration_bar_gen_diff(scenarios,figsize=[20,6])
    #exp.results.stacked_es_duration_bar_es_diff(scenarios,figsize=[20,6])
    
    #exp.results.stacked_bar_by_bus_option = self.config['stacked_bar_by_bus']
    #exp.results.policy_plot_option = self.config['policy_plot_option']
    #exp.results.process_results(
        #self.var_dict, self.par_dict, self.timestamp, self.optimizer.report)

'''ARCHIVE

fig, ax = plt.subplots(1, 1)
for b in bus_list:
    results_b = results[results['b'] == b]
    results_b_pivot = results_b[results_b['Value'] > 0].pivot_table(
        index=['y'], columns='Technology', values='Value', aggfunc='sum')
    results_b_pivot = results_b_pivot.fillna(0)
    translate1 = {
        x: y for x, y in tech_map_info[['Tech_Num', 'Tech_Name']].values}
    cols = [translate1.get(x, x)
            for x in results_b_pivot.columns]
    results_b_pivot.columns = cols

    color_array = [
        self.color_tech(c) for c in cols]

    if results_b_pivot.empty == False:
        results_b_pivot.plot(stacked=True, color=color_array, figsize=[
            10, 8], legend=False, linewidth=3, ax=ax).figure

ax.legend(loc="center left",
          bbox_to_anchor=(1, 0.5), fontsize=15)

ax.set_ylabel('Capacity (MW)', fontsize=25)
ax.set_xlabel('Years', fontsize=25)
ax.set_title(
    'Installed ES capacity', fontsize=30)
ax.margins(x=0, y=0)
plt.close(fig)
fig.savefig(self.policy_folder_path+'/' +
            'ES_inv_MWh'+'.png')

   'Li-Ion Battery 1 (New)': 'royalblue',
   'Li-Ion Battery 2 (New)': 'royalblue',
   'Li-Ion Battery 3 (New)': 'royalblue',
   'Li-Ion Battery 4 (New)': 'royalblue',
   'Li-Ion Battery 5 (New)': 'royalblue',
   'Li-Ion Battery 6 (New)': 'royalblue',
   'Li-Ion Battery 7 (New)': 'royalblue',
   'Li-Ion Battery 8 (New)': 'royalblue',
   'Li-Ion Battery 9 (New)': 'royalblue',
   'Li-Ion Battery 10 (New)': 'royalblue',

def stacked_resource_es_duration_bar1(self,fig,ax,figsize):
    """
    Plot stacked bar chart of installed capacity by year
    """
    
    results = exp.results.rd['P_cap_total']
    results_en1 = exp.results.rd['Store']
    if np.size(results.index.names) > 1:
        results.reset_index(inplace=True)
    if np.size(results_en1.index.names) > 1:
        results_en1.reset_index(inplace=True)

    # Add tech name
    translate = {x: y for x, y in exp.results.gen_map_info[['Gen_num', 'Tech_Num']].values}
    tech_num = [translate.get(x, x) for x in results['g']]
    results['Technology'] = tech_num
    tech_num = [translate.get(x, x) for x in results_en1['g']]
    results_en1['Technology'] = tech_num

    # Filter for ES tech
    results_es = results[results['Technology'].isin(np.unique(
        exp.results.data_handler.load_data[exp.results.data_handler.data_ls.index('storage')]['Tech_Num']))]
    results_es['Energy'] = results_en1['Value'].values
    results_es['Duration'] = results_es['Energy'] / results_es['Value']

    # Define duration bins and labels
    bins = [0, 2, 4, 6, 8, 10, 15, 24, np.inf]
    labels = ['0-2 hrs.', '2-4 hrs.', '4-6 hrs.', '6-8 hrs.', '8-10 hrs.', '10-15 hrs.','15-24 hrs.','24+ hrs.']

    # Create a new column for binned durations
    results_es['Duration_Bin'] = pd.cut(results_es['Duration'], bins=bins, labels=labels, right=False)

    # Ensure Duration_Bin includes all categories
    results_es['Duration_Bin'] = results_es['Duration_Bin'].cat.set_categories(labels)
    
    # Combine Technology and Duration_Bin into a new column
    results_es['Tech_Name'] = results_es.apply(
        lambda row: f"{row['Tech_Name']} ({row['Duration_Bin']})" if pd.notnull(row['Duration_Bin']) else row['Technology'], axis=1)
    
    # Replace entries in results with those in results_es based on generator number (g)
    results['Duration'] = 0
    
    results.update(results_es)

    # Pivot table based on the new Tech_Category column
    results_pivot = results[results['Value'] != 0].pivot_table(
        index=['y'], columns='Tech_Name', values='Value', aggfunc='sum')
  
    
    # Rename columns
    translate1 = {x: y for x, y in exp.results.tech_map_info[['Tech_Num', 'Tech_Name']].values}
    cols = [translate1.get(x, x) for x in results_pivot.columns]
    results_pivot.columns = cols

    # Assign colors
    color_array = [exp.results.color_tech(c) for c in cols]

    if figsize is None:
        results_pivot.plot.bar(stacked=True, color=color_array, ax=ax, legend=False, edgecolor="black", linewidth=0.75, width=0.5)
        ax.legend(loc="center left", bbox_to_anchor=(1, 0.5), fontsize=7)
        ax.set_ylabel('Capacity (MW)')
        ax.set_xlabel('Years')
        ax.set_title('Installed capacity')
        ax.margins(x=0, y=0)
        plt.show(fig)
    else:
        results_pivot.plot.bar(stacked=True, color=color_array, ax=ax, figsize=figsize, legend=False, edgecolor="black", linewidth=0.75, width=0.5)
        ax.legend(loc="center left", bbox_to_anchor=(1, 0.5), fontsize=15)
        ax.set_ylabel('Capacity (MW)', fontsize=20)
        ax.set_xlabel('Years', fontsize=20)
        ax.set_title('Installed capacity', fontsize=25)
        ax.tick_params(axis='both', which='major', labelsize=14)
        ax.margins(x=0, y=0)
        plt.close(fig)
        fig.savefig(self.folder_path + '/' + str(self.data_handler.scenario) + '_stacked_es_duration_bar.png', bbox_inches='tight')
        
'''