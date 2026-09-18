"""
Utilities to export experiment results into the ProGRESS data layout and to
invoke ProGRESS site-data generation and simulations.

This module provides a ProGRESS_Exporter class that converts an experiment
object (with data_handler, results, and config) into a directory structure
and CSV/YAML files consumable by the ProGRESS tools (solar and wind data
generators and the Monte Carlo simulation). It also supports copying or
reusing pre-generated site data and launching ProGRESS simulation runs.

Typical usage:
    exporter = ProGRESS_Exporter(exp_obj)
    exporter.export_data([2030, 2040])
    exporter.run_ProgRESS_simulation(exporter.main_path, [2030, 2040])
"""

import pandas as pd
import numpy as np
import os
import sys
import shutil
import tempfile
import copy
import yaml 
import subprocess
import textwrap
from pathlib import Path
from quest_planning.paths import get_path
root_dir = Path(get_path())

class ProGRESS_Exporter:
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

    def __init__(self, exp_obj, venv_path = None):
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

        if venv_path:
            self.progress_path = venv_path
        else:
            if sys.platform == "win32":
                self.progress_path = (root_dir / "progress" / "env_progress" / "Scripts" / "python.exe")
            else:  # macOS and Linux
                self.progress_path = (root_dir / "progress" / "env_progress" / "bin" / "python")
        
        sys.path.append(self.progress_path)
       
        self.sim_option = exp_obj.config.get("progress_sim_mode", "Nodal")
        
        if exp_obj.config.get("ren_data_dir", None):
            self.existing_wind_dir = os.path.join(exp_obj.config.get("ren_data_dir"), "windspeed_data.csv")
            self.existing_solar_dir = os.path.join(exp_obj.config.get("ren_data_dir"), "gen_all_sites.csv")
        else:
            self.existing_wind_dir = None
            self.existing_solar_dir = None
        self.num_sample_paths = exp_obj.config.get("num_sample_paths", 1)
        self.num_hours = exp_obj.config.get('num_hours', 8760)
        self.num_mpi_processes = exp_obj.config.get("num_mpi_processes", 0)

    def export_data(self, export_years):
        """
        Create ProGRESS_Data folder and export per-year inputs.

        For each year in export_years, this method creates a year subfolder,
        exports input.yaml, network (bus, branch, load), generation and
        storage CSV files, and prepares Solar and Wind directories (copied
        from generated base folders or existing directories).

        Parameters:
            export_years: iterable of int
                Years to export under the ProGRESS_Data folder.
        """
        
        progress_folder_path = os.path.join(self.results.folder_path, "Reliability_Assessment")
        self.main_path = progress_folder_path
        os.makedirs(progress_folder_path, exist_ok=True)

        for year in export_years:
            current_folder_path = os.path.join(progress_folder_path, str(year))
            os.makedirs(current_folder_path, exist_ok=True)
            #Export config files
            self.export_yaml_file(current_folder_path)
            #Make the system folder
            syst_folder_path = os.path.join(current_folder_path, "System")
            os.makedirs(syst_folder_path, exist_ok=True)
            #export bus data
            self.export_network_data(syst_folder_path, year)
            #export_gen_data
            self.export_gen_data(syst_folder_path, year)
            #export storage_data
            self.export_storage_data(syst_folder_path, year)

        self.export_solar_data(progress_folder_path, export_years)
        self.export_wind_data(progress_folder_path, export_years)

    def export_yaml_file(self, folder_path):
        """
        Write input.yaml for ProGRESS in the given folder.

        The YAML contains API credentials, year ranges for wind/solar data
        downloads, and Monte Carlo simulation parameters expected by the
        ProGRESS tools.

        Parameters:
            folder_path: str
                Destination folder where input.yaml will be written.
        """
        yaml_file_path = os.path.join(folder_path, "input.yaml")
        config_dict = {}
        # ProGRESS Configuration File

        # Data file directory
        config_dict["data"] = folder_path

        # Inputs for Wind
        if self.existing_wind_dir:
            config_dict["download_w"] = "No"
        else:
            config_dict["download_w"] = "Yes"
        config_dict["year_start_w"] = 2007
        config_dict["year_end_w"] = 2007

        # Inputs for Solar
        if self.existing_solar_dir:
            config_dict["download_s"] = "No"
        else:
            config_dict["download_s"] = "Yes"
        config_dict["year_start_s"] = 2020
        config_dict["year_end_s"] = 2020
        config_dict["n_clusters"] = 8

        # Monte Carlo simulation parameters
        config_dict["samples"] = self.num_sample_paths
        config_dict["sim_hours"] = self.num_hours
        config_dict["load_factor"] = 1
        config_dict["model"] = self.sim_option
        config_dict["optimization_period"] = 24
        config_dict["evaluate_degradation"] = False
        config_dict["degradation_interval"] = 168
        config_dict["detailed_thermal_model"] = False
        config_dict["use_pcm"] = False
        
        class QuotedDumper(yaml.SafeDumper):
            pass

        def str_representer(dumper, data):
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

        QuotedDumper.add_representer(str, str_representer)

        with open(yaml_file_path, "w") as file:
            yaml.dump(config_dict, file, Dumper=QuotedDumper, default_flow_style=False)

    def export_network_data(self, folder_path, current_year):
        """
        Export network CSV files (bus.csv, branch.csv, load.csv) for a year.

        Parameters:
            folder_path: str
                Directory where the CSV files will be written (typically
                the "System" folder inside the per-year ProGRESS directory).
            current_year: int
                Year used to scale system-wide load and per-bus load shares.
        """
        bus_file_path = os.path.join(folder_path, "bus.csv")
        exp_bus_df = self.results.bus_names
        exp_bus_df = self.data_inputs.load_data[self.index('bus')]
        
        bus_df = pd.DataFrame({
            'Bus Name': exp_bus_df.get('Bus_name'),
            'Bus No.': exp_bus_df.get('Bus_number'),
            "Zone": exp_bus_df.get('Region'),
        })
        
        original_bus_numbers = bus_df["Bus No."].tolist()
        # Create new sequential numbering
        new_bus_numbers = list(range(1, len(bus_df) + 1))
        # Mapping: old bus number -> new bus number
        bus_to_new_bus = dict(zip(original_bus_numbers, new_bus_numbers))
        bus_df["Bus No."] = bus_df["Bus No."].map(bus_to_new_bus)
        self.bus_newbus_mapper = bus_to_new_bus
        bus_to_zone = dict(zip(new_bus_numbers, bus_df["Zone"].values))
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
            'Branch ID': explan_branch_df.index.values,
            'From Bus': from_bus.values,
            'To Bus': to_bus.values,
            'R': explan_branch_df.get('R').values,
            'X': explan_branch_df.get('X').values,
            'B': explan_branch_df.get('B').values,
            'Rating': explan_branch_df.get('Rating_B') + current_year_branch_inv.loc[explan_branch_df.index, "Value"].values,
            'MTTF': explan_branch_df.get('MTTF', pd.Series([10000]*n_branch)).values,
            'MTTR': explan_branch_df.get('MTTR', pd.Series([10]*n_branch)).values,
            'Tran OutRate': explan_branch_df.get('Tran_OutRate', pd.Series([2]*n_branch)).values,
            'Interzonal': interzonal_flag
        }
        # Create DataFrame dynamically
        branch_df = pd.DataFrame(branch_dict)
        branch_df = branch_df[branch_df["Rating"] != 0]

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
        load_dict["datetime"] = list(explan_load_df.loc[:,"datetime"])
        load_dict["system_wide"] = system_wide_load
        
        # Keep per-bus loads
        for idx, row in exp_bus_df.iterrows():
            bus_number = row["Bus_name"]
            load_share = row["Load_share"]
            load_dict[bus_number] = load_share / 100 * system_wide_load

        # Convert to DataFrame and save
        load_df = pd.DataFrame(load_dict)
        load_df.to_csv(load_file_path, index=False)

    def export_gen_data(self, folder_path, current_year):
        """
        Export generation CSV (gen.csv) for thermal generators in a year.

        The method selects thermal techs, joins fuel costs and capacity from
        results, and writes a gen.csv file compatible with ProGRESS inputs.

        Parameters:
            folder_path: str
                Folder under which gen.csv will be created (usually "System").
            current_year: int
                Year used to pick capacity and fuel cost columns.
        """
        thermal_types = self.data_inputs.tech_categories["thermal"]
        gen_file_path = os.path.join(folder_path, "gen.csv")
        gen_fuel_costs = self.data_inputs.load_data[self.index('fuel')].loc[:,["Gen_num",str(current_year)]].set_index("Gen_num")
        exp_gen_df = self.data_inputs.load_data[self.index('gen')]
        
        gen_mix = self.results.rd["P_cap_total"]
        current_year_gen_mix = gen_mix[gen_mix["y"] == current_year].set_index("g")

        thermal_gen_df = exp_gen_df[exp_gen_df["Tech"].isin(thermal_types)].set_index("Gen_num")
        thermal_gen_df = thermal_gen_df.join(gen_fuel_costs, how="inner") 

        gen_dict = {}
        n_gen = len(thermal_gen_df)
        gen_dict["Gen No."] = thermal_gen_df.index.values
        gen_dict["Gen Name"] = thermal_gen_df.get("Gen_name").values
        gen_dict["Bus Name"] = thermal_gen_df.get("Bus").values
        gen_dict["Bus No."] =  [self.bus_newbus_mapper.get(bus, bus) if self.bus_newbus_mapper else bus for bus in thermal_gen_df.get("Bus_num").values]
        gen_dict["Zone"] = [self.bus_zone_mapper.get(bus, bus) for bus in gen_dict["Bus No."]]
        gen_dict["Type"] = ['Thermal']*len(thermal_gen_df.iloc[:,0])
        gen_dict["Fuel"] =  thermal_gen_df.get("Tech").values
        gen_dict["Max Cap"] = current_year_gen_mix.loc[thermal_gen_df.index,"Value"].values
        gen_dict["Min Cap"] = pd.Series([0]*n_gen).values
        gen_dict["FOR"] =  thermal_gen_df.get("FOR", pd.Series([0.02]*n_gen)).replace(0,0.02).values
        gen_dict["MTTR"] = thermal_gen_df.get("MTTR", pd.Series([50]*n_gen)).values
        alternate_MTTF =  np.array(gen_dict["MTTR"])*(1-np.array(gen_dict["FOR"]))/np.array(gen_dict["FOR"] )
        gen_dict["MTTF"] =  thermal_gen_df.get("MTTF", pd.Series(alternate_MTTF)).values
        gen_dict["Cost"] = (thermal_gen_df["HR"]*thermal_gen_df[str(current_year)]).values

        gen_df = pd.DataFrame(gen_dict)
        column_order = ["Gen No.", "Gen Name", "Bus Name", "Bus No.","Zone","Type","Fuel","Max Cap","Min Cap","FOR","MTTR","MTTF","Cost"]
        gen_df = gen_df[gen_df["Max Cap"] != 0]
        gen_df.to_csv(gen_file_path, index = False)

    def export_storage_data(self, folder_path, current_year):
        """
        Export storage device CSV (storage.csv) for the given year.

        If no storage exist, the method returns immediately. Storage sizing is
        derived from results and the data handler storage metadata.

        Parameters:
            folder_path: str
                Destination folder (typically "System").
            current_year: int
                Year used to read storage capacities and energy sizes.
        """
        storage_types = self.data_inputs.tech_categories["storage"]
        exp_gen_df = self.data_inputs.load_data[self.index('gen')]
        storage_df = exp_gen_df[exp_gen_df["Tech"].isin(storage_types)].set_index("Gen_num")
        storage_file_path = os.path.join(folder_path, "storage.csv")

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
        storage_dict["Name"] = storage_df.get("Gen_name").values
        storage_dict["Bus No."] = [self.bus_newbus_mapper.get(bus, bus) if self.bus_newbus_mapper else bus 
                for bus in storage_df.get("Bus_num").values]
        storage_dict["Zone"] = [self.bus_zone_mapper.get(bus, bus) for bus in storage_dict["Bus No."]]
        storage_dict["Pmax"] = storage_power_ratings
        storage_dict["Pmin"] = pd.Series([0]*n_storage).values
        storage_dict["Duration"] = storage_energy_ratings / (storage_power_ratings + 1e-15)
        storage_dict["max_SOC"] = pd.Series([1]*n_storage).values
        storage_dict["min_SOC"] = pd.Series([0]*n_storage).values
        storage_dict["Efficiency"] = storage_dat.loc[storage_df.index, "RTE"]
        storage_dict["Discharge Cost"] = pd.Series([20]*n_storage).values
        storage_dict["Charge Cost"] = pd.Series([0]*n_storage).values
        storage_dict["Units"] = np.maximum(np.ceil(storage_power_ratings / 5).astype(int), 1)
        storage_dict["MTTF"] =  storage_df.get("MTTF", pd.Series([2000]*n_storage)).values
        storage_dict["MTTR"] = storage_df.get("MTTR", pd.Series([30]*n_storage)).values

        storage_df = pd.DataFrame(storage_dict)
        storage_df = storage_df[storage_df["Pmax"] != 0]
        storage_df.to_csv(storage_file_path, index = False)

    
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

    def export_solar_data(self, folder_path, export_years):
        """
        Prepare and export solar site data for ProGRESS.

        If existing_solar_dir is None the method:
          - Creates a Base_solar_data folder,
          - Writes solar_sites.csv and invokes ProGRESS Solar methods to download
            irradiance and run k-means clustering to create cluster files.

        Then, for each model year it copies the base directory into the
        per-year Solar folder and writes a year-specific solar_sites.csv
        reflecting the generator mix for that year.

        Parameters:
            folder_path: str
                Path to the ProGRESS_Data folder where base/year subfolders
                will be created.
        """
        solar_types = self.data_inputs.tech_categories["upv_ex"] + self.data_inputs.tech_categories["upv_can"]
        exp_gen_df = self.data_inputs.load_data[self.index('gen')]
        gen_loc = self.data_inputs.load_data[self.index('gen_viz')]

        solar_data_df = exp_gen_df[exp_gen_df["Tech"].isin(solar_types)]
        solar_data_locations = gen_loc[gen_loc["Tech"].isin(solar_types)].loc[solar_data_df.index,:]

        if solar_data_df.empty:
            return
        
        solar_data_df_reset = solar_data_df.reset_index(drop=True)
        solar_data_locations_reset = solar_data_locations.reset_index(drop=True)

        solar_buses = [self.bus_newbus_mapper.get(bus, bus) for bus in solar_data_df_reset.get("Bus_num").values]
        solar_zones = [self.bus_zone_mapper.get(bus, bus) for bus in solar_buses]
        solar_dict = {}
        n_solar = len(solar_data_df_reset)
        solar_dict["Site Name"] = solar_data_df_reset["Gen_name"]
        solar_dict["Latitude"] = solar_data_locations_reset["LAT"]
        solar_dict["Longitude"] = solar_data_locations_reset["LON"]
        solar_dict["MW_Capacity"] = solar_data_df_reset["Cap"]
        solar_dict["Tracking"] = pd.Series([1]*n_solar)
        solar_dict["Bus No."] = solar_buses
        solar_dict["Zone"] = solar_zones

        for year in export_years:
            
            current_folder_path = os.path.join(folder_path, str(year))
            os.makedirs(current_folder_path, exist_ok=True)

            current_solar_directory = os.path.join(current_folder_path, "Solar")
            os.makedirs(current_solar_directory, exist_ok=True)
            if self.existing_solar_dir:
                shutil.copy2(self.existing_solar_dir, current_solar_directory)

            gen_mix = self.results.rd["P_cap_total"]
            current_year_gen_mix = gen_mix[gen_mix["y"] == year].set_index("g")
            solar_mix = current_year_gen_mix.loc[solar_data_df.loc[:,"Gen_num"].values,"Value"]

            current_solar_data = copy.deepcopy(solar_dict)
            current_solar_data["MW_Capacity"] = solar_mix.values
            current_solar_df = pd.DataFrame(current_solar_data)
            current_solar_df = self.rename_duplicates(current_solar_df , index_col = "Site Name")
            current_solar_df = current_solar_df[current_solar_df["MW_Capacity"] != 0]

            current_solar_site_path = os.path.join(current_solar_directory, "solar_sites.csv")
            current_solar_df.to_csv(current_solar_site_path, index = False)
            
    def export_wind_data(self, folder_path, export_years):
        """
        Prepare and export wind site data for ProGRESS.

        If existing_wind_dir is None the method:
          - Creates a Base_wind_data folder,
          - Writes wind_sites.csv and basic power-curve CSVs,
          - Invokes ProGRESS Wind methods to download wind speed data and
            calculate transition/truncation rates.

        Then, for each model year it copies the base directory into the
        per-year Wind folder and writes a year-specific wind_sites.csv
        reflecting the per-year generator mix.

        Parameters:
            folder_path: str
                Path to the ProGRESS_Data folder where base/year subfolders
                will be created.
        """
        wind_types = self.data_inputs.tech_categories["wind_ex"] + self.data_inputs.tech_categories["wind_can"]
        exp_gen_df = self.data_inputs.load_data[self.index('gen')]
        gen_loc = self.data_inputs.load_data[self.index('gen_viz')]

        wind_data_df = exp_gen_df[exp_gen_df["Tech"].isin(wind_types)]
        wind_data_locations = gen_loc[gen_loc["Tech"].isin(wind_types)].loc[wind_data_df.index,:]

        if wind_data_df.empty:
            return
        wind_data_df_reset = wind_data_df.reset_index(drop=True)
        wind_data_locations_reset = wind_data_locations.reset_index(drop=True)
        
        wind_buses = [self.bus_newbus_mapper.get(bus, bus) for bus in wind_data_df_reset.get("Bus_num").values]
        wind_zones = [self.bus_zone_mapper.get(bus, bus) for bus in wind_buses]
        
        wind_columns = ["Site Name","Bus No.","Zone","Type","MW_Capacity","Power","Class","Latitude","Longitude","Hub Height","Turbine Rating"]
        wind_dict = {}
        n_wind = len(wind_data_df_reset)
        wind_dict["Site Name"] = wind_data_df_reset["Gen_name"]
        wind_dict["Bus No."] = wind_buses
        wind_dict["Zone"] = wind_zones
        wind_dict["Type"] = pd.Series(["Wind_PPA"]*n_wind)
        wind_dict["MW_Capacity"] = wind_data_df_reset["Cap"]
        wind_dict["Power Class"] = pd.Series([2]*n_wind)
        wind_dict["Latitude"] = wind_data_locations_reset["LAT"]
        wind_dict["Longitude"] = wind_data_locations_reset["LON"]
        wind_dict["Hub Height"] = pd.Series([100]*n_wind)
        wind_dict["Turbine Rating"] = pd.Series([8]*n_wind)

        for year in export_years:
            
            current_folder_path = os.path.join(folder_path, str(year))
            os.makedirs(current_folder_path, exist_ok=True)

            current_wind_directory = os.path.join(current_folder_path, "Wind")
            os.makedirs(current_wind_directory, exist_ok=True)
            
            if self.existing_wind_dir:
                shutil.copy2(self.existing_wind_dir, current_wind_directory)

            gen_mix = self.results.rd["P_cap_total"]
            current_year_gen_mix = gen_mix[gen_mix["y"] == year].set_index("g")
            wind_mix = current_year_gen_mix.loc[wind_data_df.loc[:,"Gen_num"].values,"Value"]

            current_wind_data = copy.deepcopy(wind_dict)
            current_wind_data["MW_Capacity"] = wind_mix.values
            current_wind_df = pd.DataFrame(current_wind_data)
            current_wind_df = self.rename_duplicates(current_wind_df , index_col = "Site Name")

            current_wind_site_path = os.path.join(current_wind_directory, "wind_sites.csv")
            current_wind_df.to_csv(current_wind_site_path, index = False)

            # Create the DataFrame
            df_power_curves = pd.DataFrame({
                "Start (m/s)": [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 22, 25],
                "End (m/s)":   [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 22, 25, 1000],
                "Class 2":     [0, 0.0052, 0.0423, 0.1031, 0.1909, 0.3127, 0.4731, 0.6693,
                                0.8554, 0.9641, 0.9942, 0.9994, 1, 1, 0],
                "Class 3":     [0, 0.0054, 0.053, 0.1351, 0.2508, 0.4033, 0.5952, 0.7849,
                                0.9178, 0.9796, 1, 1, 1, 0, 0]
            })
            wind_pcurve_path = os.path.join(current_wind_directory, "w_power_curves.csv")
            df_power_curves.to_csv(wind_pcurve_path, index = False)

    def run_ProgRESS_simulation(self, folder_path, sim_years):
        """
        Run ProGRESS Monte Carlo simulation wrapper for each year.

        This method imports the MCS simulation entrypoint from ProGRESS and
        invokes it with the per-year input.yaml and data directory created by
        export_data. The MCS function returns simulation records which are
        currently not processed further here.

        Parameters:
            folder_path: str
                Path to the ProGRESS_Data folder containing per-year data.
            sim_years: iterable of int
                Years for which to run the ProGRESS simulation.
        """
        ## First run the data_downloader process to create necessary clusters for solar and wind
        for year in sim_years:
            current_data_path = os.path.join(folder_path, str(year))
            current_yaml_file = os.path.join(current_data_path, "input.yaml")
            
            print(f"Running reliability assessment using ProGRESS for year {year}...")
            results_subdir = os.path.join(current_data_path, 'Results')
            os.makedirs(results_subdir, exist_ok=True)
            
            code = textwrap.dedent(f"""
                                    from progress.data_download_process import DataProcess
                                    data = DataProcess(r"{current_yaml_file}")
                                    data.ProcessWindData()
                                    data.ProcessSolarData()
                                    """)
            with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
                f.write(code.encode("utf-8"))
                temp_script = f.name
            subprocess.run([self.progress_path, temp_script], check=True)
            os.remove(temp_script)
            # run MCS
            if self.num_mpi_processes == 0:
               
               subprocess.run([self.progress_path, 
                               "-m", 
                               "progress.example_simulation", 
                               "--config", current_yaml_file, 
                               "--out", results_subdir], check=True)
            else:
                # Run with MPI
                cmd = [
                    "mpiexec",
                    "-n", str(self.num_mpi_processes),
                    self.progress_path,
                    "-m",
                    "progress.example_simulation_mult_proc",
                    "--config", current_yaml_file,
                    "--out", results_subdir
                ]
                subprocess.run(cmd, check=True)

