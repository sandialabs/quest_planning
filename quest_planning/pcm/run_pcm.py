"""
Utilities to export experiment results into the PCM data layout and to
invoke PCM simulations.

This module provides a PCM_Exporter class that converts an experiment
object (with data_handler, results, and config) into a directory structure
and CSV/YAML files consumable by QuEST PCM. It also supports copying or
reusing pre-generated site data and launching ProGRESS simulation runs.

Typical usage:
    exporter = PCM_Exporter(exp_obj)
    exporter.export_data([2030, 2040])
    exporter.run_PCM_simulation(exporter.main_path, [2030, 2040])
"""

import pandas as pd
import numpy as np
import os
import sys
import shutil
import tempfile
import copy
import yaml 
import json
import subprocess
import textwrap
from pathlib import Path
from quest_planning.paths import get_path
root_dir = Path(get_path())

class PCM_Exporter:
    """
    Export results and inputs from an experiment into the ProGRESS format.

    The exporter reads from an experiment object that must provide:
      - data_handler: input data and metadata (load, gen, locs, categories, years...)
      - results: runtime results (rd, bus_names, folder_path, etc.)
      - config: configuration for ProGRESS (paths, API keys, years, email, etc.)

    The class writes a ProGRESS_Data folder under results.folder_path with
    per-year subfolders containing network, generation, storage CSVs and a
    ProGRESS-compatible input.yaml. It can also prepare and copy solar and
    wind site data (using the ProGRESS python package) and run the sample
    Monte Carlo simulation wrapper.

    Parameters:
        exp_obj: object
            Experiment object with attributes `data_handler`, `results`, and
            `config` required by the exporter.
    """

    def __init__(self, exp_obj, config, venv_path = None):
        """
        Initialize exporter with an experiment object.

        The initializer extracts and caches commonly used inputs from the
        experiment, configures paths, and stores API credentials and year
        ranges required for external data generation.

        Parameters:
            exp_obj: Must contain `data_handler`, `results`, and `config`.
            venv_path (Path): Optional, path to ProGRESS venv python executable
        """
        self.data_inputs = exp_obj.data_handler
        self.results = exp_obj.results
        self.index = self.data_inputs.data_ls.index
        self.config = config
        if venv_path:
            self.pcm_path = venv_path
        else:
            if sys.platform == "win32":
                self.pcm_path = (root_dir / "pcm" / "env_pcm" / "Scripts" / "python.exe")
            else:  # macOS and Linux
                self.pcm_path = (root_dir / "pcm" / "env_pcm" / "bin" / "python")
        
        sys.path.append(self.pcm_path)
        self.data_mapper()


    def data_mapper(self):
        self.technology_mapper = {
                "Nuclear": {
            "type": "Thermal",
            "unit_type": "NUCLEAR",
            "category": "Nuclear",
            "fuel": "Nuclear",
            "min_down_time": 48,
            "min_up_time": 24,
            "agc": False,
            "fast_start": False,
        },

        "SMR_Cand": {
            "type": "Thermal",
            "unit_type": "NUCLEAR",
            "category": "Nuclear",
            "fuel": "Nuclear",
            "min_down_time": 8,
            "min_up_time": 8,
            "agc": False,
            "fast_start": False,
        },

        "Coal": {
            "type": "Thermal",
            "unit_type": "STEAM",
            "category": "Coal",
            "fuel": "Coal",
            "min_down_time": 4,
            "min_up_time": 8,
            "agc": True,
            "fast_start": False,
        },

        "Gas": {
            "type": "Thermal",
            "unit_type": "CC",
            "category": "Gas CC",
            "fuel": "NG",
            "min_down_time": 4.5,
            "min_up_time": 8,
            "agc": True,
            "fast_start": False,
        },

        "Gas_CC": {
            "type": "Thermal",
            "unit_type": "CC",
            "category": "Gas CC",
            "fuel": "NG",
            "min_down_time": 4.5,
            "min_up_time": 8,
            "agc": True,
            "fast_start": True,
        },

        "Gas_CT": {
            "type": "Thermal",
            "unit_type": "CT",
            "category": "Gas CT",
            "fuel": "NG",
            "min_down_time": 2.2,
            "min_up_time": 2.2,
            "agc": True,
            "fast_start": True,
        },

        "Gas_Cand": {
            "type": "Thermal",
            "unit_type": "CC",
            "category": "Gas CC",
            "fuel": "NG",
            "min_down_time": 4.5,
            "min_up_time": 8,
            "agc": True,
            "fast_start": True,
        },

        "Gas_CC_Cand": {
            "type": "Thermal",
            "unit_type": "CC",
            "category": "Gas CC",
            "fuel": "NG",
            "min_down_time": 4.5,
            "min_up_time": 8,
            "agc": True,
            "fast_start": True,
        },

        "Gas_CT_Cand": {
            "type": "Thermal",
            "unit_type": "CT",
            "category": "Gas CT",
            "fuel": "NG",
            "min_down_time": 2.2,
            "min_up_time": 2.2,
            "agc": True,
            "fast_start": True,
        },

        "Oil_CT": {
            "type": "Thermal",
            "unit_type": "CT",
            "category": "Oil CT",
            "fuel": "Oil",
            "min_down_time": 1,
            "min_up_time": 1,
            "agc": True,
            "fast_start": True,
        },

        "Oil_ST": {
            "type": "Thermal",
            "unit_type": "STEAM",
            "category": "Oil ST",
            "fuel": "Oil",
            "min_down_time": 2,
            "min_up_time": 4,
            "agc": True,
            "fast_start": False,
        },

        "Geothermal": {
            "type": "Thermal",
            "unit_type": "STEAM",
            "category": "Geothermal",
            "fuel": "Geothermal",
            "min_down_time": 0,
            "min_up_time": 0,
            "agc": False,
            "fast_start": False,
        },


        # ============================================================
        # HYDRO
        # ============================================================
        "Hydro": {
            "type": "Renewable",
            "unit_type": "HYDRO",
            "category": "Hydro",
            "fuel": "Hydro",
            "min_down_time": 0,
            "min_up_time": 0,
            "agc": True,
            "fast_start": True,
        },

        # ============================================================
        # SOLAR
        # ============================================================
        "Solar": {
            "type": "Renewable",
            "unit_type": "PV",
            "category": "Solar PV",
            "fuel": "Solar",
            "min_down_time": 0,
            "min_up_time": 0,
            "agc": False,
            "fast_start": False,
        },

        "Solar_PPA": {
            "type": "Renewable",
            "unit_type": "PV",
            "category": "Solar PV",
            "fuel": "Solar",
            "min_down_time": 0,
            "min_up_time": 0,
            "agc": False,
            "fast_start": False,
        },

        "Solar_RT": {
            "type": "Fixed Renewable",
            "unit_type": "RTPV",
            "category": "Solar RTPV",
            "fuel": "Solar",
            "min_down_time": 0,
            "min_up_time": 0,
            "agc": False,
            "fast_start": False,
        },

        "Solar_Cand": {
            "type": "Renewable",
            "unit_type": "PV",
            "category": "Solar PV",
            "fuel": "Solar",
            "min_down_time": 0,
            "min_up_time": 0,
            "agc": False,
            "fast_start": False,
        },

        "CSP": {
            "type": "Renewable",
            "unit_type": "CSP",
            "category": "CSP",
            "fuel": "Solar",
            "min_down_time": 1,
            "min_up_time": 1,
            "agc": False,
            "fast_start": False,
        },


        # ============================================================
        # WIND
        # ============================================================
        "Wind": {
            "type": "Renewable",
            "unit_type": "WIND",
            "category": "Wind",
            "fuel": "Wind",
            "min_down_time": 0,
            "min_up_time": 0,
            "agc": False,
            "fast_start": False,
        },

        "Wind_PPA": {
            "type": "Renewable",
            "unit_type": "WIND",
            "category": "Wind",
            "fuel": "Wind",
            "min_down_time": 0,
            "min_up_time": 0,
            "agc": False,
            "fast_start": False,
        },

        "Wind_Cand": {
            "type": "Renewable",
            "unit_type": "WIND",
            "category": "Wind",
            "fuel": "Wind",
            "min_down_time": 0,
            "min_up_time": 0,
            "agc": False,
            "fast_start": False,
        },
    }

    
    def rename_duplicates(self, df, index_col):
        """
        Ensure unique column names and unique values in a chosen index column.

        - Appends numeric suffixes to duplicate column names.
        - Appends numeric suffixes to duplicate values within `index_col`.

        Parameters:
            df: pandas.DataFrame
                DataFrame to process (modified in-place and returned).
            index_col: str
                Column name whose duplicate values should be renamed.

        Returns:
            pandas.DataFrame: DataFrame with unique column names and updated
                                values in index_col.
        """
        # Rename duplicate columns
        cols = pd.Series(df.columns)
        for dup in cols[cols.duplicated()].unique():
            cols[cols == dup] = [f"{dup}_{i}" if i != 0 else dup for i in range(sum(cols == dup))]
        df.columns = cols

        # Rename duplicates in the index column
        if index_col in df.columns:
            ids = pd.Series(df[index_col])
            for dup in ids[ids.duplicated()].unique():
                ids[ids == dup] = [f"{dup}_{i}" if i != 0 else dup for i in range(sum(ids == dup))]
            df[index_col] = ids

        return df
        
    def export_data(self, export_years):
        """
        Create PCM_Data folder and export per-year inputs.

        For each year in export_years, this method creates a year subfolder,
        exports input.yaml, network (bus, branch, load), generation and
        storage CSV files.

        Parameters:
            export_years: iterable of int
                Years to export under the PCM_Data folder.
        """
        
        pcm_folder_path = os.path.join(self.results.folder_path, "Production_Cost")
        self.main_path = pcm_folder_path
        os.makedirs(pcm_folder_path, exist_ok=True)

        for year in export_years:
            current_folder_path = os.path.join(pcm_folder_path, str(year))
            os.makedirs(current_folder_path, exist_ok=True)
            #Make the system folder
            syst_folder_path = os.path.join(current_folder_path, "Input Data")
            input_data_path = syst_folder_path
            os.makedirs(syst_folder_path, exist_ok=True)
            #export bus data
            self.export_network_data(syst_folder_path, year)
            #export_gen_data
            self.export_gen_data(syst_folder_path, year)
            #export storage_data
            self.export_storage_data(syst_folder_path, year)
            #export reserves 
            self.export_reserves(syst_folder_path, year) 
            #run pcm if user asks to
            if self.config.get("simulate_pcm", False):
                #Export config files
                yaml_dir = self.export_yaml_file(current_folder_path, year)
                self.export_PCM_json(current_folder_path, yaml_dir, syst_folder_path, year)
                self.run_PCM(current_folder_path, yaml_dir, syst_folder_path, year)

    def export_network_data(self, folder_path, current_year):
        """
        Export network CSV files (bus.csv, branch.csv, load.csv) for a year.

        Parameters:
            folder_path: str
                Directory where the CSV files will be written.
            current_year: int
                Year used to scale system-wide load and per-bus load shares.
        """
        bus_file_path = os.path.join(folder_path, "bus.csv")
        exp_bus_df = self.results.bus_names
        exp_bus_df = self.data_inputs.load_data[self.index('bus')]
        
        bus_df = pd.DataFrame({
            'Bus ID': exp_bus_df.get('Bus_number'),
            'Bus Name': exp_bus_df.get('Bus_name'),
            "Zone": exp_bus_df.get('Region'),
        })
        
        original_bus_numbers = bus_df["Bus ID"].tolist()
        # Mapping: old bus number -> new bus number (not necessary but from progress integration unchanged)
        bus_to_new_bus = dict(zip(original_bus_numbers, original_bus_numbers))
        bus_df["Bus ID"] = bus_df["Bus ID"].map(bus_to_new_bus)
        self.bus_newbus_mapper = bus_to_new_bus
        bus_to_zone = dict(zip(original_bus_numbers, bus_df["Zone"].values))
        self.bus_zone_mapper = bus_to_zone
        bus_df_export = bus_df
        bus_df_export.to_csv(bus_file_path, index=False)

        branch_file_path = os.path.join(folder_path, "branch.csv")
        explan_branch_df = self.data_inputs.load_data[self.index('branch')].set_index("Line_Number")
        n_branch = len(explan_branch_df)
        
        branch_inv = self.results.rd["LineCap"].reset_index()
        current_year_branch_inv = branch_inv[branch_inv["y"] == current_year].set_index("l")

        # Map from/to buses to zones if zonal model
        from_bus = explan_branch_df['From_Bus_Number'].map(bus_to_new_bus) if bus_to_new_bus else explan_branch_df['From_Bus_Number']
        to_bus = explan_branch_df['To_Bus_Number'].map(bus_to_new_bus) if bus_to_new_bus else explan_branch_df['To_Bus_Number']
        interzonal_flag = ["N" if bus_to_zone[f] == bus_to_zone[t] else "Y" for f, t in zip(from_bus.values, to_bus.values)]

        branch_dict = {
            'Line ID': [f"A{i}" for i in explan_branch_df.index],
            'From Bus': from_bus.values,
            'To Bus': to_bus.values,
            'R': explan_branch_df.get('R').values,
            'X': explan_branch_df.get('X').values,
            'B': explan_branch_df.get('B').values,
            'Cont Rating': explan_branch_df.get('Rating_B') + current_year_branch_inv.loc[explan_branch_df.index, "Value"].values
        }
        # Create DataFrame dynamically
        branch_df = pd.DataFrame(branch_dict)
        branch_df = branch_df[branch_df["Cont Rating"] != 0]

        # Save CSV
        branch_df.to_csv(branch_file_path, index=False)

        load_file_path = os.path.join(folder_path, "load.csv")
        explan_load_df = self.data_inputs.load_data[self.index('load')]
        base_load_year = int(self.data_inputs.load_data[self.index('load')].loc[0,'year'])
        if self.data_inputs.regional_load_growth is None: 
            system_wide_load = np.array(((1 + self.data_inputs.load_growth) ** (current_year - base_load_year)) * explan_load_df.loc[:, 'system_wide']) #New
        else:
            zonal_system_load = {}
            regional_base_share = (exp_bus_df.groupby("Region")["Load_share"].sum().astype(float) / 100)

            for zone, g in self.data_inputs.regional_load_growth.items():
                zonal_system_load[zone] = np.array(
                    regional_base_share.loc[zone]
                    * ((1 + g) ** (current_year - base_load_year))
                    * explan_load_df.loc[:, 'system_wide']
                ) 
            system_wide_load = sum(zonal_system_load.values())

        load_dict = {}
        load_dict["datetime"] = (pd.to_datetime(explan_load_df["datetime"]).map(lambda x: x.replace(year=current_year)).tolist())
        load_dict["system_wide"] = system_wide_load
        
        # Keep per-bus loads
        for idx, row in exp_bus_df.iterrows():
            bus_number = row["Bus_name"]
            load_share = row["Load_share"]
            load_dict[bus_number] = load_share / 100 * system_wide_load

        # Convert to DataFrame and save
        load_df = pd.DataFrame(load_dict)
        load_df.to_csv(load_file_path, index=False)

    def _initialize_gen_data_dict(self, gen_dict, n_gen):

        gen_dict["HR_avg_0"] = np.zeros(n_gen)
        gen_dict["HR_incr_1"] = np.zeros(n_gen)
        gen_dict["HR_incr_2"] = np.zeros(n_gen)
        gen_dict["HR_incr_3"] = np.zeros(n_gen)

        gen_dict["Output_pct_0"] = np.zeros(n_gen)
        gen_dict["Output_pct_1"] = np.zeros(n_gen)
        gen_dict["Output_pct_2"] = np.zeros(n_gen)
        gen_dict["Output_pct_3"] = np.zeros(n_gen)

        gen_dict["Start Time Cold Hr"] = np.zeros(n_gen)
        gen_dict["Start Time Warm Hr"] = np.zeros(n_gen)
        gen_dict["Start Time Hot Hr"] = np.zeros(n_gen)

        gen_dict["Start Heat Cold MBTU"] = np.zeros(n_gen)
        gen_dict["Start Heat Warm MBTU"] = np.zeros(n_gen)
        gen_dict["Start Heat Hot MBTU"] = np.zeros(n_gen)

        gen_dict["Min Up Time Hr"] = np.zeros(n_gen)
        gen_dict["Min Down Time Hr"] = np.zeros(n_gen)

        gen_dict["AGC capable"] = np.zeros(n_gen)
        gen_dict["Fast start"] = np.zeros(n_gen)

        gen_dict["Initial Power MW"] = np.zeros(n_gen)
        gen_dict["Initial Time Hr"] = np.zeros(n_gen)

        return gen_dict

    def export_gen_data(self, folder_path, current_year):
        """
        Export generation CSV (gen.csv) for thermal generators and renewable timeseries in a year.

        The method selects thermal techs, joins fuel costs and capacity from
        results, and writes a gen.csv file compatible with PCM inputs.

        Parameters:
            folder_path: str
                Folder under which gen.csv will be created (usually "System").
            current_year: int
                Year used to pick capacity and fuel cost columns.
        """
        storage_types = self.data_inputs.tech_categories["storage"]
        gen_file_path = os.path.join(folder_path, "gen.csv")
        gen_fuel_costs = self.data_inputs.load_data[self.index('fuel')].loc[:,["Gen_num",str(current_year)]].set_index("Gen_num")
        exp_gen_df = self.data_inputs.load_data[self.index('gen')]

        thermal_candidates = list(set(self.data_inputs.tech_categories["thermal"]) & set(self.data_inputs.tech_categories["candidates"]))
        gen_df_cand = exp_gen_df[exp_gen_df["Tech"].isin(thermal_candidates)].set_index("Gen_num")

        gen_mix = self.results.rd["P_cap_total"]
        current_year_gen_mix = gen_mix[gen_mix["y"] == current_year].set_index("g")

        gen_df = exp_gen_df[exp_gen_df["Tech"].isin(storage_types) == False].set_index("Gen_num")
        gen_df = gen_df.join(gen_fuel_costs, how="left").fillna(0)

        gen_dict = {}
        n_gen = len(gen_df)
        gen_dict["GEN UID"] =  gen_df.get("Gen_name").values
        gen_dict["Bus ID"] =  [self.bus_newbus_mapper.get(bus, bus) if self.bus_newbus_mapper else bus for bus in gen_df.get("Bus_num").values]
        gen_dict["Gen ID"] =  gen_df.index.values
        gen_dict["Type"] = [
        self.technology_mapper.get(tech, {}).get("type", "") for tech in gen_df["Tech"].values]
        gen_dict["Unit Type"] = [self.technology_mapper.get(tech, {}).get("unit_type", "") for tech in gen_df["Tech"].values]
        gen_dict["Category"] = [self.technology_mapper.get(tech, {}).get("category", tech) for tech in gen_df["Tech"].values]
        gen_dict["Fuel"] = [self.technology_mapper.get(tech, {}).get("fuel", "") for tech in gen_df["Tech"].values]
        max_cap_vals = current_year_gen_mix.loc[gen_df.index,"Value"].values
        gen_dict["Max Cap"] = max_cap_vals
        gen_dict["Min Cap"] = gen_df.get("MinCap").values.copy()
        candidate_thermal_mask = gen_df["Tech"].isin(thermal_candidates)
        gen_dict["Min Cap"][candidate_thermal_mask] = (
            0.20 * max_cap_vals[candidate_thermal_mask]
        )
        gen_dict["Fuel Price $/MMBTU"] = gen_df[str(current_year)].values
        gen_dict["Ramp Rate MW/Min"] = max_cap_vals*gen_df.get("Ramp").values

        detailed_gen_data = self.config.get("detailed_pcm_gen_data", False)
        self._initialize_gen_data_dict(gen_dict, n_gen)
        if detailed_gen_data:
            gen_df_pcm = pd.read_csv(os.path.join(self.config["data_dir"], "gen_pcm.csv")) 
            gen_num_to_idx = {uid: i for i, uid in enumerate(gen_df.index)}

            for _, row in gen_df_pcm.iterrows():
                gen_num_pcm = row["Gen_num"]
                
                this_gen_idx = gen_num_to_idx[gen_num_pcm]
                gen_dict["HR_avg_0"][this_gen_idx] = row["HR_avg_0"]
                gen_dict["HR_avg_0"][this_gen_idx] = row["HR_avg_0"]
                gen_dict["HR_incr_1"][this_gen_idx] = row["HR_incr_1"]
                gen_dict["HR_incr_2"][this_gen_idx] = row["HR_incr_2"]
                gen_dict["HR_incr_3"][this_gen_idx] = row["HR_incr_3"]

                gen_dict["Output_pct_0"][this_gen_idx] = row["Output_pct_0"]
                gen_dict["Output_pct_1"][this_gen_idx] = row["Output_pct_1"]
                gen_dict["Output_pct_2"][this_gen_idx] = row["Output_pct_2"]
                gen_dict["Output_pct_3"][this_gen_idx] = row["Output_pct_3"]

                gen_dict["Start Time Cold Hr"][this_gen_idx] = row["Start Time Cold Hr"]
                gen_dict["Start Time Warm Hr"][this_gen_idx] = row["Start Time Warm Hr"]
                gen_dict["Start Time Hot Hr"][this_gen_idx] = row["Start Time Hot Hr"]

                gen_dict["Min Up Time Hr"][this_gen_idx] = row["Min Up Time Hr"]
                gen_dict["Min Down Time Hr"][this_gen_idx] = row["Min Down Time Hr"]

                if gen_num_pcm in gen_df_cand.index:
                    gen_dict["Start Heat Cold MBTU"][this_gen_idx] = row["Start Heat Cold MBTU"]*max_cap_vals[this_gen_idx]
                    gen_dict["Start Heat Warm MBTU"][this_gen_idx] =  row["Start Heat Warm MBTU"]*max_cap_vals[this_gen_idx]
                    gen_dict["Start Heat Hot MBTU"][this_gen_idx] = row["Start Heat Hot MBTU"]*max_cap_vals[this_gen_idx]
                else:
                    gen_dict["Start Heat Cold MBTU"][this_gen_idx] = row["Start Heat Cold MBTU"]
                    gen_dict["Start Heat Warm MBTU"][this_gen_idx] =  row["Start Heat Warm MBTU"]
                    gen_dict["Start Heat Hot MBTU"][this_gen_idx] = row["Start Heat Hot MBTU"]

                gen_dict["AGC capable"][this_gen_idx] = row["AGC capable"]
                gen_dict["Fast start"][this_gen_idx] = row["AGC capable"]
        else:
            #If detailed data is not provided use linear heat curves based on heat rates
            gen_dict["HR_avg_0"]= gen_df["HR"].values*1000
            gen_dict["HR_incr_1"]= gen_df["HR"].values*1000
            gen_dict["HR_incr_2"]= gen_df["HR"].values*1000
            gen_dict["HR_incr_3"]= gen_df["HR"].values*1000
            gen_dict["Output_pct_0"] = np.ones(n_gen)*0.4
            gen_dict["Output_pct_1"] = np.ones(n_gen)*0.6
            gen_dict["Output_pct_2"] = np.ones(n_gen)*0.8
            gen_dict["Output_pct_3"] = np.ones(n_gen)*1.0
            gen_dict["Min Up Time Hr"] = np.array([self.technology_mapper.get(tech, {}).get("min_down_time", 0) for tech in gen_df["Tech"].values])
            gen_dict["Min Down Time Hr"] = np.array([self.technology_mapper.get(tech, {}).get("min_up_time", 1) for tech in gen_df["Tech"].values])
            gen_dict["AGC capable"] = np.array([self.technology_mapper.get(tech, {}).get("agc", False) for tech in gen_df["Tech"].values])
            gen_dict["Fast start"] = np.array([self.technology_mapper.get(tech, {}).get("fast_start", False) for tech in gen_df["Tech"].values])

        gen_dict["Initial Power MW"] = gen_dict["Min Cap"]
        gen_dict["Initial Time Hr"] = gen_dict["Min Up Time Hr"]

        gen_df_pcm = pd.DataFrame(gen_dict)
        column_order = ["GEN UID","Bus ID","Gen ID","Type","Unit Type","Category","Fuel","Max Cap","Min Cap","Fuel Price $/MMBTU",\
                        "Ramp Rate MW/Min","HR_avg_0","HR_incr_1","HR_incr_2","HR_incr_3","Output_pct_0","Output_pct_1","Output_pct_2",
                        "Output_pct_3","Start Time Cold Hr","Start Time Warm Hr","Start Time Hot Hr","Start Heat Cold MBTU",
                        "Start Heat Warm MBTU","Start Heat Hot MBTU","Min Up Time Hr","Min Down Time Hr","AGC capable","Fast start",
                        "Initial Power MW","Initial Time Hr"]
        gen_df_pcm = gen_df_pcm[column_order]
        gen_df_pcm = gen_df_pcm[gen_df_pcm["Max Cap"] != 0]
        gen_df_pcm = self.rename_duplicates(gen_df_pcm, "GEN UID")
        gen_df_pcm.to_csv(gen_file_path, index = False)

        renewable_file_path = os.path.join(folder_path, "renewable_timeseries_DA.csv")
        existing_solar_types = self.data_inputs.tech_categories.get("upv_ex")
        solar_df = exp_gen_df[exp_gen_df["Tech"].isin(existing_solar_types)].set_index("Gen_num")
        solar_timeseries = self.data_inputs.load_data[self.index('solar')]
        renewable_data = {}
        timestamps = pd.to_datetime(solar_timeseries["datetime"].values)
        renewable_data["Year"] = np.ones(len(timestamps))*current_year
        renewable_data["Month"] = timestamps.month.values
        renewable_data["Day"] = timestamps.day.values
        renewable_data["Period"] = timestamps.hour.values+1
        for gen_num in solar_df.index:
            current_max_cap = current_year_gen_mix.loc[gen_num,"Value"]
            rated_cap = solar_df.loc[gen_num, "Cap"]
            # In case the renewable gen is shut off or has zero capacity
            scaling_factor = current_max_cap / rated_cap if rated_cap != 0 else 0
            gen_name = gen_df_pcm.loc[gen_df_pcm["Gen ID"] == gen_num,"GEN UID"].iloc[0]
            renewable_data[f"{gen_name}"] = solar_timeseries[str(gen_num)].values * scaling_factor

        #candidate solar 
        candidate_solar_types = self.data_inputs.tech_categories.get("upv_can")
        candidate_solar_df = exp_gen_df[exp_gen_df["Tech"].isin(candidate_solar_types)].set_index("Gen_num")
        candidate_solar_timeseries = self.data_inputs.load_data[self.index('solar_cand')]
        for gen_num in candidate_solar_df.index:
            current_gen_value = current_year_gen_mix.loc[gen_num,"Value"]
            if current_gen_value == 0:
                continue
            gen_name = gen_df_pcm.loc[gen_df_pcm["Gen ID"] == gen_num,"GEN UID"].iloc[0]
            renewable_data[f"{gen_name}"] = candidate_solar_timeseries[str(gen_num)].values * current_gen_value
        #existing wind farms
        existing_wind_types = self.data_inputs.tech_categories.get("wind_ex")
        wind_df = exp_gen_df[exp_gen_df["Tech"].isin(existing_wind_types)].set_index("Gen_num")
        wind_timeseries = self.data_inputs.load_data[self.index('wind')]
        for gen_num in wind_df.index:
            current_max_cap = current_year_gen_mix.loc[gen_num,"Value"]
            rated_cap = wind_df.loc[gen_num, "Cap"]
            # In case the renewable gen is shut off or has zero capacity
            scaling_factor = current_max_cap / rated_cap if rated_cap != 0 else 0
            gen_name = gen_df_pcm.loc[gen_df_pcm["Gen ID"] == gen_num,"GEN UID"].iloc[0]
            renewable_data[f"{gen_name}"] = wind_timeseries[str(gen_num)].values * scaling_factor
        #candidate wind farms
        candidate_wind_types = self.data_inputs.tech_categories.get("wind_can")
        candidate_wind_df = exp_gen_df[exp_gen_df["Tech"].isin(candidate_wind_types)].set_index("Gen_num")
        candidate_wind_timeseries = self.data_inputs.load_data[self.index('wind_cand')]
        for gen_num in candidate_wind_df.index:
            current_gen_value = current_year_gen_mix.loc[gen_num,"Value"]
            if current_gen_value == 0:
                continue
            gen_name = gen_df_pcm.loc[gen_df_pcm["Gen ID"] == gen_num,"GEN UID"].iloc[0]
            renewable_data[f"{gen_name}"] = candidate_wind_timeseries[str(gen_num)].values * current_gen_value

        renewable_df = pd.DataFrame(renewable_data)
        renewable_df.to_csv(renewable_file_path, index = False)

    def export_storage_data(self, folder_path, current_year):
        """
        Export storage device CSV (storage.csv) for the given year.

        If no storage exist, the method returns immediately. Storage sizing is
        derived from results and the data handler storage metadata.

        Parameters:
            folder_path: str
                Destination folder (typically "Input Data").
            current_year: int
                Year used to read storage capacities and energy sizes.
        """
        storage_types = self.data_inputs.tech_categories["storage"]
        exp_gen_df = self.data_inputs.load_data[self.index('gen')]
        storage_df = exp_gen_df[exp_gen_df["Tech"].isin(storage_types)].set_index("Gen_num")
        storage_file_path = os.path.join(folder_path, "generic_storage.csv")

        if storage_df.empty:
            return
        
        gen_mix = self.results.rd["P_cap_total"]
        storage_energy = self.results.rd["Store"]
        storage_dat = self.data_inputs.load_data[self.index('storage')].set_index("Gen_num")
        current_year_gen_mix = gen_mix[gen_mix["y"] == current_year].set_index("g")
        current_year_storage_energy = storage_energy[storage_energy["y"] == current_year].set_index("g")
        
        storage_dict = {}
        n_storage = len(storage_df)
        storage_power_ratings = current_year_gen_mix.loc[storage_df.index,"Value"].values
        storage_energy_ratings = current_year_storage_energy.loc[storage_df.index,"Value"].values 
        storage_dict["Storage ID"] = storage_df.get("Gen_name").values
        storage_dict["Bus ID"] = [self.bus_newbus_mapper.get(bus, bus) if self.bus_newbus_mapper else bus 
                for bus in storage_df.get("Bus_num").values]
        storage_dict["In Service"] = np.ones(n_storage)
        storage_dict["Charge Rating MW"] = storage_power_ratings
        storage_dict["Discharge Rating MW"] = storage_power_ratings
        storage_dict["Min Charge Rating MW"] = np.zeros(n_storage)
        storage_dict["Min Discharge Rating MW"] = np.zeros(n_storage)
        storage_dict["Rated Capacity MWh"] = storage_energy_ratings
        duration_vals = storage_energy_ratings / (storage_power_ratings + 1e-15)
        storage_dict["Capacity Retention Rate"] = np.ones(n_storage)
        storage_dict["Discharging Efficiency"] = np.ones(n_storage)
        storage_dict["Charging Efficiency"] = storage_dat.loc[storage_df.index, "RTE"]
        
        storage_dict["Discharging Cost $/MWh"] = np.zeros(n_storage)
        storage_dict["Charging Cost $/MWh"] = np.zeros(n_storage)
        storage_dict["Maximum SoC"] = np.ones(n_storage)*self.data_inputs.soc_max
        storage_dict["Minimum SoC"] = np.ones(n_storage)*self.data_inputs.soc_min
        storage_dict["Initial SoC"] = np.ones(n_storage)*0.5

        storage_dict["Charging RampUP MW/min"] = storage_power_ratings*storage_df["Ramp"].values
        storage_dict["Charging RampDOWN MW/min"] = storage_power_ratings*storage_df["Ramp"].values
        storage_dict["Discharging RampUP MW/min"] = storage_power_ratings*storage_df["Ramp"].values
        storage_dict["Discharging RampDOWN MW/min"] = storage_power_ratings*storage_df["Ramp"].values
        storage_df = pd.DataFrame(storage_dict)
        storage_df = storage_df[storage_df["Rated Capacity MWh"] != 0]
        storage_df.to_csv(storage_file_path, index = False)

    
    def export_reserves(self, folder_path, export_years):
        """
        Prepare and export reserve requirements.

        Parameters:
            folder_path: str
                Path to the ProGRESS_Data folder where base/year subfolders
                will be created.
        """
        reserve_file_path = os.path.join(folder_path, "DA_reserves_fixed_percentage.csv")
        reserve_dict = {}
        reserve_dict["Reserve Type"] = []
        reserve_dict["System Percentage Requirement"] = []
        if self.data_inputs.reg_res_req:
            reserve_dict["Reserve Type"].append("Regulation Up")
            reserve_dict["Reserve Type"].append("Regulation Down")
            reserve_dict["System Percentage Requirement"].append(self.data_inputs.reg_res_req*100)
            reserve_dict["System Percentage Requirement"].append(self.data_inputs.reg_res_req*100)
        if self.data_inputs.spin_res_req:
            reserve_dict["Reserve Type"].append("Spinning Reserve")
            reserve_dict["System Percentage Requirement"].append(self.data_inputs.spin_res_req*100)
        if self.data_inputs.flex_res_req:
            reserve_dict["Reserve Type"].append("Flexible Ramp Up")
            reserve_dict["Reserve Type"].append("Flexible Ramp Down")
            reserve_dict["System Percentage Requirement"].append(self.data_inputs.flex_res_req*100)
            reserve_dict["System Percentage Requirement"].append(self.data_inputs.flex_res_req*100)
        reserve_dict["Eligible Areas"] = [None] * len(reserve_dict["Reserve Type"])
        reserve_df = pd.DataFrame(reserve_dict)
        reserve_df.to_csv(reserve_file_path, index = False)

    
    def export_yaml_file(self, folder_path, current_year):
        """
        Write input.yaml for PCM in the given folder.

        The YAML contains API credentials, year ranges for wind/solar data
        downloads, and Monte Carlo simulation parameters expected by the
        PCM tool.

        Parameters:
            folder_path: str
                Destination folder where input.yaml will be written.
        """
        
        # PCM Configuration File
        pcm_yaml = {}
        pcm_yaml["solver"] = self.data_inputs.solver
        pcm_yaml["mipgap"] = self.config.get("mipgap", 0.01)
        pcm_yaml["baseMVA"] = 100.0

        optional_date = self.config.get("pcm_start_date", "01/01")
        start_month, start_day = map(int, optional_date.split("/"))
        start_dt = pd.Timestamp(year=int(current_year), month=start_month, day=start_day)
        pcm_hours = int(self.config.get("pcm_hours", 24))
        lookahead_pad_hours = int(np.ceil(self.config.get("lookahead_hours", 0) / 24) * 24)
        total_hours = pcm_hours + lookahead_pad_hours
        end_dt = start_dt + pd.Timedelta(hours=total_hours - 1)
        pcm_yaml["start_date"] = start_dt.strftime("%m/%d/%Y")
        pcm_yaml["end_date"] = end_dt.strftime("%m/%d/%Y")

        pcm_yaml["simulate_DA_only"] = True
        pcm_yaml["DA_lookahead_periods"] = self.config.get("lookahead_hours", 0)
        
        pcm_yaml["RT_resolution"] = 60 
        pcm_yaml["RT_lookahead_periods"] = 1 
        pcm_yaml["run_RTSCED_as"] = "MILP" 
        pcm_yaml["branch_contingency"] = False
        pcm_yaml["solve_pricing_problem"] = self.config.get("solve_pricing_problem", False)
        pcm_yaml["load_timeseries_aggregation_level"] = "node"
        
        pcm_yaml["System Reserve"] = "None"
        if self.data_inputs.reg_res_req:
            pcm_yaml["Regulation Up"] = "percentage"
            pcm_yaml["Regulation Down"] = "percentage"
        else:
            pcm_yaml["Regulation Up"] = "None"
            pcm_yaml["Regulation Down"] = "None"
        if self.data_inputs.spin_res_req:
            pcm_yaml["Spinning Reserve"] = "percentage"
        else:
            pcm_yaml["Spinning Reserve"] = "None"
        if self.data_inputs.flex_res_req:
            pcm_yaml["Flexible Ramp Up"] = "percentage"
            pcm_yaml["Flexible Ramp Down"] = "percentage"
        else:
            pcm_yaml["Flexible Ramp Up"] = "None"
            pcm_yaml["Flexible Ramp Down"] = "None"
        pcm_yaml["NonSpinning Reserve"] = "None"
        pcm_yaml["Supplemental Reserve"] = "None"

        pcm_yaml["storage_AS_participation_level"] = 4 if self.config.get("storage_AS_mode", False) else 0 
        pcm_yaml["evaluate_degradation"] = False

        pcm_yaml["output_interval"] = self.config.get("pcm_output_frequency","at_once")
        pcm_yaml["plotly_plots"] = False 
        pcm_yaml["plot_ancillary_services"] = True
        pcm_yaml["plot_storage_details"] = False

        input_yaml_dir = os.path.join(folder_path, "input_pcm.yaml")
        
        class QuotedDumper(yaml.SafeDumper):
            pass

        def str_representer(dumper, data):
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

        QuotedDumper.add_representer(str, str_representer)

        with open(input_yaml_dir, "w") as file:
            yaml.dump(pcm_yaml, file, Dumper=QuotedDumper, default_flow_style=False)

        return input_yaml_dir

    def export_PCM_json(self,  folder_path, input_yaml_path, input_data_path, current_year):
        """Generate PCM JSON input files from the exported YAML configuration.

        A temporary Python script is executed in the PCM virtual environment to
        invoke PCM's DataManager and export the DA input JSON files.
        """
        code = textwrap.dedent(f"""
        import logging
        from egret.common.log import logger as egret_logger
        from pcm.data_manager.data_main import DataManager

        egret_logger.setLevel(logging.ERROR)

        main_data_path = r"{input_data_path}"
        yaml_path = r"{input_yaml_path}"
        output_dir = r"{folder_path}"

        input_manager = DataManager(main_data_path, yaml_path, optional_json_dir=output_dir)
        input_manager.export_input_json()
        """)

        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
            f.write(code.encode("utf-8"))
            temp_script = f.name

        print(f"Generating PCM JSON input files for year {current_year}...")
        env = os.environ.copy()
        env["PYTHONUNBUFFERED"] = "1"
        proc = subprocess.Popen(
            [self.pcm_path, temp_script],
            env=env
        )
        proc.wait()
        os.remove(temp_script)

    def run_PCM(self, folder_path, input_yaml_path, input_data_path, current_year):
        """Run the PCM market simulation and export results.

        A temporary Python script is executed in the PCM virtual environment to
        run the PCM market simulator and save results to the output directory.
        """
        code = textwrap.dedent(f"""
        import os
        import json
        import logging
        from egret.common.log import logger as egret_logger
        from pcm.data_manager.data_main import DataManager
        from pcm.market_manager.market_main import MarketSimulator
        from pcm.result_manager.result_main import ResultManager# %%

        egret_logger.setLevel(logging.ERROR)

        main_data_path = r"{input_data_path}"
        yaml_path = r"{input_yaml_path}"
        output_dir = r"{folder_path}"

        input_manager = DataManager(main_data_path, yaml_path, optional_json_dir = output_dir)
        simulator = MarketSimulator(input_manager)
        simulator.create_DA_RT_models()
        simulator.simulate_market() 

        result_processor = ResultManager(simulator, output_dir)
        result_processor.export_results()
        """)

        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
            f.write(code.encode("utf-8"))
            temp_script = f.name

        print(f"Running PCM market simulation for year {current_year}...")
        env = os.environ.copy()
        env["PYTHONUNBUFFERED"] = "1"
        proc = subprocess.Popen(
            [self.pcm_path, temp_script],
            text=True,
            env=env
        )
        
        proc.wait()
        os.remove(temp_script)
        print(f"PCM market simulation for year {current_year} complete")
