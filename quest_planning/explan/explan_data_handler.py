# -*- coding: utf-8 -*-
"""
QuESt Planning - explan data handler used to process input data for the optimization model
Authors: C. Newlun and W. Olis
""" 

import pandas as pd
import numpy as np
import datetime
from datetime import date
import logging
import calendar
import networkx as nx
import matplotlib.dates as mdates
from sklearn.cluster import KMeans
#import plotly.graph_objects as go

from quest_planning.explan.explan_results_viewer import ExplanResultsViewer


class ExplanDataHandler():

    def __init__(self):
        self.block_selection = None
        self.tx_model = None
        self.trans_expansion = None
        self.load_growth = 1.5#None - Default value
        self.load_forecast = None
        self.es_cost = None
        self.ldes_switch = False
        self.data_ls = None
        self.index = None#self.data_ls.index
        
        self.data_file = None
        
        self.load_data = None
        self.scalars = None
        self.tech_nums = None
        self.load_blocks = None
        self.system_peak = None
        self.hour_duration = None
        self.season_time_duration = None
        self.dt_info = None
        self.season_map = None
        self.year_gap = None
        self.discount_rate = None
        self.base_currency_year = None
        self.reserves_option = None
        
        self.S = None
        self.start_year = None
        self.end_year = None
        self.start_hr = None
        self.end_hr = None
        self.last_hr = None
        self.first_hr = None

        self.solver = None
        self.rps_schedule = None
        self.rps_policy = False
        self.co2_policy = False
        self.co2_intensity_policy = False
        self.scenario = None
        
        self.years = None
        self.year_gap_array = None
        
        self.tech_categories=None
        
        #investment limits - system wide - default is none
        self.system_wide_wind_max = None
   
        self.system_wide_solar_max = None
        
        self.system_wide_gas_max = None
   
        self.system_wide_tx_expansion_max = None
        
        
        
        #Default values - if not changed in config file or missing
        self.load_growth = 1.5
        self.voll = 100000
        self.prm = 0.2
        self.reg_res_req = 0.01
        self.spin_res_req = 0.03
        self.flex_res_w_req = 0.1
        self.flex_res_s_req = 0.04
        self.soc_min = 0.2
        self.soc_max = 0.8
        self.ini_level = 0.5
        self.es_degradation = 0.03#annual degradation of ES technologies
        self.end_effects = 10
        self.tax_credit_end_year = 2032
        self.mva_base = 100
        # Custom retirement years - if user desires custom retirement schedule
        self.custom_retirement = False
        self.ng_retirement_year = None
        self.coal_retirement_year = None
        self.nuclear_retirement_year = None
        self.oil_retirement_year = None
        
        #modeling options
        self.reserves_option = True
        self.tax_credits_option = False
        self.es_lifetime_cost_option = False
        self.es_lifetime_extension = 50
        
        self.mva_base = 100
        
        self.resource_bus_limit_dict = None
        
        
    '''Functions to connect data_handler to front-end and define scalar values'''
    '''The following functions are connected to the GUI'''
    
    def set_data_ls_index(self,data_ls):
        if data_ls is not None:
            self.data_ls = data_ls
            self.index = self.data_ls.index
        else:
            self.data_ls = ['branch', 'bus', 'capex_es', 'capex_h_es', 'capex_l_es',
                             'capex_tech', 'fuel', 'gen_viz', 'gen',
                             'load', 'policy', 'scalars', 'solar_cand', 'solar', 
                             'storage', 'tech', 'wind_cand', 'wind']#'disfact',
            
            self.index = self.data_ls.index
            
    def set_start_year(self, year):
        """Set the start year of the simulation period"""
        self.start_year = year

    def set_end_year(self, year):
        """Set the end year of the simulation period"""
        self.end_year = year

    def set_year_gap(self, value):
        """Set the year gap of the simulation period"""
        self.year_gap = value
    
    def set_years_hours(self,years):
        '''Define years and year gap'''
        #self.years = [year for year in range(
            #self.start_year, self.end_year+1, self.year_gap)]
        self.years = years
        year_gap_array = []
        for i in range(len(years)):
            if i==0:
                dif = 1
                year_gap_array.append(dif)
            else:
                dif = years[i]-years[i-1]
                year_gap_array.append(dif)
            '''
            if i<len(years)-1:
                dif = years[i+1]-years[i]
                year_gap_array.append(dif)
            else:
                dif = 1
                year_gap_array.append(dif)
            '''
                
        self.year_gap_array = year_gap_array

    def set_tx_model(self, value):
        """Set the transmission model type"""
        if value == "Transportation (Pipe & Bubble)":
            v= 'Transportation'
            self.tx_model = v
        elif value == 'Copper Sheet':
            v = 'copper_sheet'
            self.tx_model = v
        else:
            self.tx_model = value
            
    def set_load_profile(self, value):
        """Set the load profile selection"""
        self.load_forecast = value
        
    def set_es_cost(self,value):
        """Set the annual load growth"""
        self.es_cost = value
    
    def set_scenario(self,value):
        """Set the scenario name"""
        self.scenario = value
    
    def set_block_selection(self, value):
        """Set the block selection type"""
        #print(value)
        self.block_selection = value
        
        if self.block_selection.lower() == 'Full_year'.lower() or self.block_selection.lower() == 'Full_year_MY'.lower():
            self.M = 8760
        elif self.block_selection.lower() == 'Peak_Day'.lower():
            self.M = 24
        elif self.block_selection.lower() == 'Seasonal_blocks'.lower():
            self.M = 5
        elif self.block_selection.lower() == 'Repr_3Days_Season'.lower():
            self.M = 72
        else:
            self.M = 168
    
    def set_discount_rate(self,value):
        """Set the discount rate"""
        self.discount_rate = value
    
    def set_base_currency_year(self,value):
        """Set base currency year"""
        self.base_currency_year = value
    
    def set_transmission_expansion(self, value):
        """Set the transmission expansion type"""
        
        #if value == "Transportation (Pipe & Bubble)":
            #v= 'Transportation'
        if value:#.lower() == "No":
            self.trans_expansion = True
        else:
            self.trans_expansion = False
    
    def set_rps_schedule(self, value,option):
        """Set the RPS schedule - GUI Only"""

        if option == 'Create New...':
            for year in value:
                self.load_data[self.index('policy')]['RPS'].loc[self.load_data[self.index('policy')]['Years'] == year] = float(value[year])/100
    
                #if value[year] is not None:
                 #   self.load_data[self.index('policy')]['RPS'].loc[self.load_data[self.index('policy')]['Years'] == year] = float(value[year])/100
                #else:
                #    print("no value")
        else:#do nothing - default
            pass
    
    def set_capital_cost_trend(self, value):
        """Set the capital cost trend for energy storage"""
        if value == "Moderate":
            self.es_cost = "Base"
        else:
            self.es_cost = value
    
    def set_retirements(self, value):
        """Set the retirement selections - GUI Only"""
        for gen in value:
            self.load_data[self.index('gen')]['RetYr'].loc[self.load_data[self.index('gen')]['Gen_name'] == gen] = int(value[gen])
    
    def set_system_name(self,value):
        self.system = value
        print(self.system)
        
    def set_solver(self, value):
        """Set the optimization solver"""
        self.solver = value.lower()

    '''The following methods are currently for the input.yaml file only'''
    def set_load_growth(self,value):
        """Set the annual load growth used if a full load forecast is not uploaded"""
        self.load_growth = float(value)/100
    
    def set_ldes_switch(self,value):
        """Set the ldes_switch"""
        self.ldes_switch = value
    
    def set_end_effects(self,value):
        '''Set end effects'''
        self.end_effects = value
    
    def set_voll(self,value):
        '''Set the value of lost load'''
        self.voll = value
    
    def set_mva_base(self,value):
        '''Set mva base'''
        self.mva_base = value
    
    def set_co2_policy(self,value):
        '''Enforce co2 policy'''
        self.co2_policy = value

    def set_rps_policy(self,value):
        '''Enforce rps policy'''
        self.rps_policy = value
    
    def set_co2_intensity_policy(self,value):
        '''Enforce co2 policy'''
        self.co2_intensity_policy = value
         
    def set_reserves_option(self,value):
        self.reserves_option = value
    
    def set_reserve_params(self,prm,reg_res_req,spin_res_req,flex_res_w_req,flex_res_s_req):
        '''Set reserves requirements (Convert to percent)'''
        self.prm = float(prm)/100
        self.reg_res_req = float(reg_res_req)/100
        self.spin_res_req = float(spin_res_req)/100
        self.flex_res_w_req = float(flex_res_w_req)/100
        self.flex_res_s_req = float(flex_res_s_req)/100
    
    def set_custom_retirement_years(self,custom_retirement,ng_retirement_year,coal_retirement_year,nuclear_retirement_year,oil_retirement_year):
        '''
        Sets custom retirement options based on fuel type
        Parameters
        ----------
        custom_retirement : Custom retirement option TRUE or FALSE
        ng_retirement_year : Retirement year of natural gas
        coal_retirement_year : Retirement year of coal
        nuclear_retirement_year : Retirement year of nuclear
        oil_retirement_year : Retirement year of oil
        '''
        self.custom_retirement = custom_retirement
        self.ng_retirement_year = ng_retirement_year #None if ng_retirement_year.lower() == 'none' else ng_retirement_year
        self.coal_retirement_year = coal_retirement_year #None if coal_retirement_year.lower() == 'none' else coal_retirement_year
        self.nuclear_retirement_year =nuclear_retirement_year # None if nuclear_retirement_year.lower() == 'none' else nuclear_retirement_year
        self.oil_retirement_year = oil_retirement_year #None if oil_retirement_year.lower() == 'none' else oil_retirement_year
    
    def set_tax_credits_option(self,value):
        '''Set option to enforce tax credits'''
        
        self.tax_credits_option = value
    def set_tax_credit_end_year(self,value):
        '''Set tax credit end year'''
        self.tax_credit_end_year = value
         
    def set_es_lifetime_cost_option(self,value):
        '''Set option to evaluate ES lifetime extension (replacement) cost'''
        self.es_lifetime_cost_option = value
    def set_es_lifetime_extension(self,value):
        '''Set number of years to asses lifetime extension of new ES assets'''
        self.es_lifetime_extension = value
            
    def set_system_wide_wind_max(self,value):
        '''Set system-wide maximum wind investment'''
        if value == 'Default':
            v = None
            self.system_wide_wind_max = v
        else:
            self.system_wide_wind_max = value
    def set_system_wide_solar_max(self,value):
        '''Set system-wide maximum solar investment'''
        if value == 'Default':
            v = None
            self.system_wide_solar_max = v
        else:
            self.system_wide_solar_max = value
    def set_system_wide_tx_expansion_max(self,value):
        '''Set system wide maximum transmission expansion'''
        if value == 'Default':
            v = None
            self.system_wide_tx_expansion_max = v
        else:
            self.system_wide_tx_expansion_max = value
    
    def set_system_wide_gas_max(self,value):
        '''Set system-wide maximum gas expansion'''
        if value == 'Default':
            v = None
            self.system_wide_gas_max = v
        else:
            self.system_wide_gas_max = value
    
    def set_es_soc_min_max(self,soc_min,soc_max,ini_level):
        '''Set ES SOC minimum, maximum, and initial level'''
        self.soc_min = soc_min/100
        self.soc_max = soc_max/100
        self.ini_level = ini_level/100
    
    def set_resource_bus_limits(self,d):
        self.resource_bus_limit_dict = d
    '''************************************************************************'''

    def get_data(self):
        """
        Load all data from csv files for input into the model.
        """
        print("Import data from Excel")
        #Load csv data
        self.load_data = {self.index(key): pd.read_csv(self.data_dir + f"/{key}.csv") for key in self.data_ls}
       
        #Set scalars and index        
        self.scalars = self.load_data[self.index('scalars')].set_index('Scalar')
        # Get tech_nums and bus nums
        self.get_tech_nums()
        self.define_bus_nums()

    def get_tech_nums(self):
        
        '''
        Develop generator tech number sets - Improved process flow
        TODO: move to csv files for improved usability
        '''
        #define gen dataframe
        df = self.load_data[self.index('gen')]

        # Define technology categories
        self.tech_categories = {
            'thermal': ['Nuclear', 'Coal', 'Gas', 'Gas_CT', 'Gas_CC', 'Geothermal', 'Oil_CT', 'Oil_ST', 'Hydro', 'Gas_Cand'],
            'nuclear': ['Nuclear'],
            'coal' : ['Coal'],
            'oil' : ['Oil_CT','Oil_St'],
            'retire': ['Coal', 'Gas', 'Gas_CT', 'Gas_CC', 'Oil_CT', 'Oil_ST'],
            'upv_ex': ['Solar', 'Solar_PPA', 'Solar_RT', 'CSP'],
            'wind_ex': ['Wind', 'Wind_PPA'],
            'upv_can': ['Solar_Cand'],
            'wind_can': ['Wind_Cand'],
            'ng': ['Gas', 'Gas_CC', 'Gas_CT', 'Gas_Cand'],
            'storage': ['ES', 'ES_PPA', 'ES_4hr_Cand', 'ES_6hr_Cand', 'ES_8hr_Cand', 'ES_10hr_Cand', 'ES_100hr_Cand', 'Li_Ion_Cand', 'Li_Ion_Cand_1', 'Li_Ion_Cand_2', 'Li_Ion_Cand_3', 'Li_Ion_Cand_4', 'Li_Ion_Cand_5', 'Li_Ion_Cand_6', 'Li_Ion_Cand_7', 'Li_Ion_Cand_8', 'Li_Ion_Cand_9', 'Li_Ion_Cand_10', 'Flow_Cand', 'Grav_Cand', 'PSH_Cand', 'Therm_Cand', 'CAES_Cand', 'Hydrogen_Cand', 'Zinc_Cand', 'Iron_Air_Cand'],
            'storage_cand': ['ES_4hr_Cand', 'ES_6hr_Cand', 'ES_8hr_Cand', 'ES_10hr_Cand', 'ES_100hr_Cand', 'Li_Ion_Cand', 'Li_Ion_Cand_1', 'Li_Ion_Cand_2', 'Li_Ion_Cand_3', 'Li_Ion_Cand_4', 'Li_Ion_Cand_5', 'Li_Ion_Cand_6', 'Li_Ion_Cand_7', 'Li_Ion_Cand_8', 'Li_Ion_Cand_9', 'Li_Ion_Cand_10', 'Flow_Cand', 'Grav_Cand', 'PSH_Cand', 'Therm_Cand', 'CAES_Cand', 'Hydrogen_Cand', 'Zinc_Cand', 'Iron_Air_Cand'],
            #'storage_cand_year': ['Li_Ion_Cand_2', 'Li_Ion_Cand_3', 'Li_Ion_Cand_4', 'Li_Ion_Cand_5', 'Li_Ion_Cand_6', 'Li_Ion_Cand_7', 'Li_Ion_Cand_8', 'Li_Ion_Cand_9', 'Li_Ion_Cand_10'],
            'ldes': ['ES_100hr_Cand', 'Grav_Cand', 'PSH_Cand', 'Therm_Cand', 'CAES_Cand', 'Hydrogen_Cand', 'Zinc_Cand', 'Flow_Cand', 'Iron_Air_Cand'],
            'dr': ['DR_Cand'],
            'renewables': ['Solar', 'Solar_RT', 'CSP', 'Solar_PPA', 'Hydro', 'Wind', 'Wind_PPA', 'Solar_Cand', 'Wind_Cand'],
            'candidates': ['Solar_Cand', 'Wind_Cand', 'Gas_Cand', 'ES_4hr_Cand', 'ES_6hr_Cand', 'ES_8hr_Cand', 'ES_10hr_Cand', 'ES_100hr_Cand', 'Li_Ion_Cand', 'Li_Ion_Cand_1', 'Li_Ion_Cand_2', 'Li_Ion_Cand_3', 'Li_Ion_Cand_4', 'Li_Ion_Cand_5', 'Li_Ion_Cand_6', 'Li_Ion_Cand_7', 'Li_Ion_Cand_8', 'Li_Ion_Cand_9', 'Li_Ion_Cand_10', 'Flow_Cand', 'Grav_Cand', 'PSH_Cand', 'Therm_Cand', 'CAES_Cand', 'Hydrogen_Cand', 'Zinc_Cand', 'DR_Cand', 'Iron_Air_Cand'],
            'exist': ['Nuclear', 'Coal', 'Gas', 'Gas_CT', 'Gas_CC', 'Geothermal', 'Oil_CT', 'Oil_ST', 'Hydro', 'Wind_PPA', 'Wind', 'Solar_PPA', 'ES_PPA', 'Solar', 'Solar_RT', 'CSP', 'ES']
        }

        # Initialize dictionary to hold generator numbers
        tech_nums = {}

        # Populate the dictionary with generator numbers for each technology category
        for category, techs in self.tech_categories.items():
            tech_nums[category] = df.loc[df['Tech'].isin(techs), 'Gen_num'].values

        self.tech_nums = tech_nums
        
    def round_params(self,data_dict):
        '''
        Optional function to round parameter values
        '''
        for k, v in data_dict.items():
            data_dict[k] = round(v, 2)
        #data_df = data_df[0].apply(lambda x: 0 if x < 0.01 else x)
        return data_dict
         
    def define_bus_nums(self):
        '''
        Define bus numbers to be used in model to define sets
        '''
        gen_df = self.load_data[self.index('gen')]
        branch_df = self.load_data[self.index('branch')]

        # Define a helper function to extract bus numbers based on generator numbers
        def get_bus_nums(tech_key):
            return gen_df.loc[gen_df['Gen_num'].isin(self.tech_nums[tech_key]), 'Bus_num'].values

        # Utilize the helper function for each technology category
        self.bus_sto_num = get_bus_nums('storage')
        self.bus_therm_num = get_bus_nums('thermal')
        self.bus_ren_num = get_bus_nums('renewables')
        self.bus_cand_num = get_bus_nums('candidates')
        self.bus_exist_num = get_bus_nums('exist')
        self.bus_upv_ex_num = get_bus_nums('upv_ex')
        self.bus_solar_can_num = get_bus_nums('upv_can')
        self.bus_wind_ex_num = get_bus_nums('wind_ex')
        self.bus_wind_can_num = get_bus_nums('wind_can')
        self.bus_es_can_num = get_bus_nums('storage_cand')
        #self.bus_es_can_yr_num = get_bus_nums('storage_cand_year')

        # For line_bus_num, directly use pandas' capabilities to create the tuple
        self.line_bus_num = tuple(zip(branch_df['Line_Number'], branch_df['From_Bus_Number'], branch_df['To_Bus_Number']))

        # For bus_gen_num, directly assign the DataFrame slice
        self.bus_gen_num = gen_df[['Bus_num', 'Gen_num']]

    def plot_load_profile(self,fig,ax,load_forecast):
        '''Plot load profile for power system data page'''        
        load_df = self.load_data[self.index('load')]
        #fig, ax = plt.subplots(1, 1)
        #set index to datetime
        
        #load_df.set_index('datetime')
        # Convert 'datetime' column to datetime type
        load_df['datetime'] = pd.to_datetime(load_df['datetime'])
        
        # Filter load_df for first year
        all_years = np.unique(load_df['datetime'].dt.year)
        load_df = load_df[load_df['datetime'].dt.year == all_years[0]]
        
        load_df[load_forecast].plot(x='datetime', y=load_forecast, ax=ax, color='tab:green', linewidth=0.25)
                
        # Set title and labels
        ax.set_title("System-wide Load Profile", fontsize=9, fontweight='bold')
        #ax.set_xlabel("Time (h)", fontsize=12)
        ax.set_ylabel("Load (MW)", fontsize=7)
        
        # Improve x-axis date formatting
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
        fig.autofmt_xdate()  # Rotate date labels
        
        # Add grid lines
        ax.grid(True, which='both', linestyle='--', linewidth=0.15)
        
        # Remove margins
        ax.margins(0)
        
        # Set tighter layout
        # Set tighter layout
        ax.relim()  # Recalculate limits
        ax.autoscale_view()  # Autoscale the view
        fig.tight_layout()  # Adjust layout
        fig.tight_layout()
        
    def plot_load_profile_plotly(self, load_forecast):
        '''Plot load profile for power system data page using plotly (optional)'''        
        load_df = self.load_data[self.index('load')]
        
        # Convert 'datetime' column to datetime type
        load_df['datetime'] = pd.to_datetime(load_df['datetime'])
        
        # Filter load_df for first year
        all_years = np.unique(load_df['datetime'].dt.year)
        load_df = load_df[load_df['datetime'].dt.year == all_years[0]]
        
        # Create a Plotly figure
        fig = go.Figure()
        
        # Add the load forecast line to the figure
        fig.add_trace(go.Scatter(
            x=load_df['datetime'],
            y=load_df[load_forecast],
            mode='lines',
            name=load_forecast,
            line=dict(color='green', width=0.45)
        ))
        
        # Set title and labels
        fig.update_layout(
            title={
                'text': "System-wide Hourly Base Load Profile",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(size=14, family='Arial', color='black')
            },
            yaxis_title="Load (MW)",
            xaxis_title="Time (h)",
            xaxis=dict(
                tickformat='%b',
                title_font=dict(size=12),
                tickfont=dict(size=10)
            ),
            yaxis=dict(
                title_font=dict(size=12),
                tickfont=dict(size=10)
            ),
            margin=dict(l=40, r=40, t=40, b=40),
            plot_bgcolor='white'
        )
        
        # Add grid lines
        fig.update_xaxes(showgrid=True, gridwidth=0.35, gridcolor='lightgrey')
        fig.update_yaxes(showgrid=True, gridwidth=0.35, gridcolor='lightgrey')
        
        # Show the figure
        #fig.show()
    
    def current_generation_mix_piechart(self, fig, ax):
        '''Show current generation mix via piechart'''
        gen_df = self.load_data[self.index('gen')]
        gen_df = gen_df[gen_df['Cap'] != 0]
        
        pivot_gen_df = gen_df.pivot_table(index='Tech', values='Cap', aggfunc='sum')
        rv = ExplanResultsViewer(self)
        color_array = [rv.color_tech(c) for c in pivot_gen_df.index]
        
        # Plot the pie chart with percentages
        wedges, texts, autotexts = ax.pie(
            pivot_gen_df['Cap'], 
            colors=color_array, 
            startangle=90, 
            autopct='%1i%%',  # Format for percentages
            textprops=dict(color="k"),  # Text color for better visibility
            pctdistance=1.25
        )
        
        # Create a compact legend at the bottom
        ax.legend(wedges, pivot_gen_df.index, loc="center", bbox_to_anchor=(0.5, -0.3), 
                fontsize='small', ncol=3, frameon=False)

        ax.set_title('Current Generation Mix',fontsize='small',fontweight = 'bold')
        

        
    def create_network_diagram(self,fig,ax,use_map):
        # Create an empty graph
        G = nx.Graph()
    
        branch_df = self.load_data[self.index('branch')]
        bus_df = self.load_data[self.index('bus')]
        
        # Add nodes to the graph
        for bus in bus_df.index:
            bus_name =  bus_df['Bus_name'][bus]  
            latitude = bus_df['LAT'][bus]  
            longitude = bus_df['LON'][bus] 
    
            # Add branch as a node to the graph
            G.add_node(bus_name, pos=(longitude, latitude))
    
           # Add edges
        for branch in branch_df.index:
            from_node = branch_df['From_Bus_Name'][branch]
            to_node = branch_df['To_Bus_Name'][branch]
            
            G.add_edge(from_node, to_node, weight=10)
        
        if use_map:
            # Calculate the center of the map based on bus locations
            pass
            '''
            center_latitude = bus_df['LAT'].mean()
            center_longitude = bus_df['LON'].mean()
            
            # Create a basemap centered on the calculated center
            offset=6
            m = Basemap(
               projection='aea',
               lat_0=center_latitude,
               lon_0=center_longitude,
               llcrnrlon=center_longitude - offset,
               llcrnrlat=center_latitude - offset,
               urcrnrlon=center_longitude + offset,
               urcrnrlat=center_latitude + offset,
               resolution='i',
               suppress_ticks=True)
            
    
        
        
            # Create a figure and axis
            #fig, ax = plt.subplots()
        
            # Draw the basemap
            # Set the map style
            m.drawcoastlines(linewidth=0.5)
            m.drawcountries(linewidth=0.5)
            m.fillcontinents(color='lightgray', lake_color='white')
            # Draw state boundaries
            m.drawstates(linewidth=0.5)
            
            # Draw terrain
            m.etopo(scale=0.5, alpha=0.5)
        
            # Convert node positions to basemap coordinates
            pos = nx.get_node_attributes(G, 'pos')
            pos = {node: m(pos[node][0], pos[node][1]) for node in pos}
            '''
        else:
            # Use default positions if Basemap is not used
            pos = nx.spring_layout(G)
            
        # Draw the network diagram
        nx.draw_networkx(G, pos, with_labels=True, node_size=100, font_size=8, ax=ax)
        #fig.show()
        # Save the figure as a PNG file
        #plt.savefig('network_diagram.png', format='png')
        #plt.show()
        
    
    def add_candidate_tech(self, tech, storage):
        """
        Add candidate technology selection from user to the database
 
        tech - candidate tech characteristics in dict form
 
        """
 
        techF = pd.DataFrame(columns=self.load_data[self.index('tech')].columns)
        genF = pd.DataFrame(columns=self.load_data[self.index('gen')].columns)
        storageF = pd.DataFrame(columns=self.load_data[self.index('storage')].columns)
 
        existing_genF = self.load_data[self.index('gen')][~self.load_data[self.index('gen')]['Gen_name'].str.endswith('_Cand')]
 
        existing_genF['Gen_num'] = existing_genF['Gen_num'] + existing_genF['Gen_num'].iloc[-1]
        existing_genF['Gen_name'] = [f"{name.split('_')[0]}_{name.split('_')[1]}_{tech['Name']}_Cand"
                                     if '_' in name else name for name in existing_genF['Gen_name']]
        existing_genF['Tech'] = [f"{tech['Name']}_Cand"]*len(existing_genF.index)
        existing_genF['Cap'] = [0]*len(existing_genF.index)
        existing_genF['MinCap'] = [0]*len(existing_genF.index)
        existing_genF['CandCap'] = [tech['Candidate Capacity']]*len(existing_genF.index)
        existing_genF['PlannedYr'] = [0]*len(existing_genF.index)
        existing_genF['RetYr'] = [0]*len(existing_genF.index)
        existing_genF['CapCred'] = [tech['Capacity Credit']]*len(existing_genF.index)
        existing_genF['LeadTime'] = [tech['Lead Time']]*len(existing_genF.index)
        existing_genF['YearAvail'] = [tech['Deployable Year']]*len(existing_genF.index)
        existing_genF['HR'] = [0]*len(existing_genF.index)
        existing_genF['FOM'] = [0]*len(existing_genF.index)
        existing_genF['VOM'] = [0]*len(existing_genF.index)
        existing_genF['PTC'] = [tech['PTC Credit']]*len(existing_genF.index)
        existing_genF['ITC'] = [tech['ITC Credit']]*len(existing_genF.index)
        existing_genF['Lifetime'] = [tech['Lifetime']]*len(existing_genF.index)
        existing_genF['Ramp'] = [tech['Ramp Rate']]*len(existing_genF.index)
        existing_genF['FOR'] = [0]*len(existing_genF.index)
        existing_genF['CO2'] = [0]*len(existing_genF.index)
        existing_genF['SO2'] = [0]*len(existing_genF.index)
        existing_genF['NO2'] = [0]*len(existing_genF.index)
 
        tech_dict = {
            'Num': len(self.load_data[self.index('tech')]),
            'Tech': tech['Name'] + '_Cand',
            'Tech_Name': tech['Name'] + '(New)',
            'ID': f"{len(self.load_data[self.index('tech')])}_{tech['Name']}_Cand",
            'Tech_Num': len(self.load_data[self.index('tech')]),
            'Lead_Time': tech['Lead Time'],
            'CandCap': tech['Candidate Capacity'],
            'RampRate': tech['Ramp Rate'],
            'FOM': None,
            'VOM': None,
            'PTC': tech['PTC Credit'],
            'ITC': tech['ITC Credit'],
            'CapCred': tech['Capacity Credit'],
            'Lifetime': tech['Lifetime']
        }
 
        self.load_data[self.index('gen')] = pd.concat([self.load_data[self.index('gen')], existing_genF], ignore_index=True)
        self.load_data[self.index('tech')] = pd.concat([self.load_data[self.index('tech')], pd.DataFrame(tech_dict, index=[0])], ignore_index=True)
 
        if storage:
            storageF = existing_genF[['Gen_num', 'Gen_name', 'Tech', 'Tech_num']]
            storageF['RTE'] = [tech['RTE']]*len(existing_genF.index)
            storageF['Charge_Eff'] = [0]*len(existing_genF.index)
            storageF['Discharge_Eff'] = [0]*len(existing_genF.index)
            storageF['Duration'] = [0]*len(existing_genF.index)
            storageF['Min_Duration'] = [tech['Min Duration']]*len(existing_genF.index)
            storageF['Max_Duration'] = [tech['Max Duration']]*len(existing_genF.index)
 
            self.load_data['STORAGE'] = pd.concat([self.load_data[self.index('storage')], storageF])

        print(self.load_data[self.index('gen')]['Gen_name'])

        
    def construct_load_blocks(self):
        """
        Construct load blocks (time steps) based on user input 
        WARNING: Not all selections work!
        """
        load_df = self.load_data[self.index('load')]

        
        load_df["datetime"] = pd.to_datetime(
            load_df["datetime"], format='mixed')#, infer_datetime_format=True
        load_df["day"] = pd.to_datetime(
            load_df["day"], format='mixed').dt.date#, infer_datetime_format=True
        load_df["hour"] = pd.to_datetime(
            load_df["datetime"], format='mixed').dt.hour#, infer_datetime_format=True
        
        
        #load_df["day"] = load_df["datetime"].dt.date
        #load_df["hour"] = load_df["datetime"].dt.hour
        #load_df["day_of_week"] = load_df["datetime"].dt.weekday+1

        load_df['month'] = pd.DatetimeIndex(
            load_df["datetime"]).month

        years = np.unique(load_df['year'].values)
        self.set_years_hours(self.years)
        #If entire load forecast is provided (e.g. all years are provided)
        try:
            if len(years) > 1:
    
                if self.block_selection.lower() == 'Peak_day'.lower():
                    sim_block = pd.DataFrame()
                    dt_info = pd.DataFrame()
    
                    for y in self.years:
                        # load for year y
                        load_df_y = load_df.loc[load_df['year'] == y]
    
                        # find peak value & select the day                   
                        peak_day = load_df_y.loc[load_df_y[self.load_forecast] ==
                                                 np.max(load_df_y[self.load_forecast])]['day'].values[0]
    
                        peak_day_profile = load_df_y.loc[load_df_y['day'] == peak_day]
    
                        # RETURN the block(s) to be simulated
                        sim_block[str(
                            y)] = peak_day_profile[self.load_forecast].values
                        dt_info[str(
                            y)] = peak_day_profile['datetime'].values
                        season_num = 1
                        hour_duration=365
                        s_i_weight = {}
                        for s in range(season_num+1):
                            for i in range(24+1):
                                if s != 0:
                                    s_i_weight[s,i] = 365
                        season_time_duration = s_i_weight
                        #dt_info = None
    
                elif self.block_selection.lower() == 'Peak_week'.lower():
                    sim_block = pd.DataFrame()
                    dt_info = pd.DataFrame()
                    for y in years:
                        # load for year y
                        load_df_y = load_df.loc[load_df['year'] == y]
                        # find peak value & select the day 
                        peak_day = load_df_y.loc[load_df_y[self.load_forecast] ==
                                                 np.max(load_df_y[self.load_forecast])]['day'].values[0]
                        # find week number
                        weekday = peak_day.isoweekday()
    
                        start_of_week = peak_day - \
                            datetime.timedelta(days=weekday)
    
                        week_dates = [start_of_week +
                                      datetime.timedelta(days=d) for d in range(7)]
    
                        peak_week_profile = pd.concat(
                            [load_df_y.loc[load_df_y['day'] == week_dates[i]] for i in range(np.size(week_dates))])
    
                        sim_block[str(
                            y)] = peak_week_profile[self.load_forecast].values
                        dt_info[str(
                            y)] = peak_week_profile['datetime'].values
    
                elif self.block_selection.lower() == 'Peak_month'.lower():
                    sim_block = pd.DataFrame()
                    dt_info = pd.DataFrame()
                    for y in years:
                        # load for year y
                        load_df_y = load_df.loc[load_df['year'] == y]
                        # find peak value & select the day 
                        peak_day = load_df_y.loc[load_df_y[self.load_forecast] ==
                                                 np.max(load_df_y[self.load_forecast])]['day'].values[0]
                        # find month number
                        month_num = peak_day.month
    
                        peak_month_profile = load_df_y.loc[load_df_y['month'] == month_num]
    
                        sim_block[str(
                            y)] = peak_month_profile[self.load_forecast].values
                        dt_info[str(
                            y)] = peak_month_profile['datetime'].values
    
                elif self.block_selection.lower() == 'Typical_Week_Month'.lower():
                    print('TODO')
                elif self.block_selection.lower() == 'Peak_Week_Season'.lower():
                    # print('TODO')
                    sim_block = pd.DataFrame()
                    dt_info = pd.DataFrame()
                    seasons = [1, 1, 2, 2, 2,
                               3, 3, 3, 4, 4, 4, 1]
                    month_to_season = dict(
                        zip(range(1, 13), seasons))
                    load_df['s'] = load_df['month'].map(
                        month_to_season)
                    for y in years:
                        # load for year y
                        load_df_y = load_df.loc[load_df['year'] == y]
                        all_season_load = []
                        all_season_dtime = []
                        for s in np.unique(seasons):
                            load_df_y_s = load_df_y.loc[load_df_y['s'] == s]
                            # find peak value & select week
                            peak_day = load_df_y_s.loc[load_df_y_s[self.load_forecast] ==
                                                       np.max(load_df_y_s[self.load_forecast])]['day'].values[0]
                            # find week number
                            weekday = peak_day.isoweekday()
    
                            start_of_week = peak_day - \
                                datetime.timedelta(days=weekday)
    
                            week_dates = [start_of_week +
                                          datetime.timedelta(days=d) for d in range(7)]
    
                            peak_week_profile = pd.concat(
                                [load_df_y_s.loc[load_df_y_s['day'] == week_dates[i]] for i in range(np.size(week_dates))])
                            all_season_load.extend(
                                peak_week_profile[self.load_forecast].values)
                            all_season_dtime.extend(
                                peak_week_profile['datetime'].values)
    
                        sim_block[str(y)] = all_season_load
                        dt_info[str(y)] = all_season_dtime
                        hour_duration = [
                            13.0357, 13.0357, 13.0357, 13.0357]
                        season_num = 4
    
                elif self.block_selection.lower() == 'Repr_Weeks'.lower():
                    
                    sim_block = pd.DataFrame()
                    dt_info = pd.DataFrame()

                    load_df1 = load_df.set_index(
                        'datetime') 
                    self.set_years_hours(self.years)
                    for y in self.years: 
                        load_df_y = load_df1.loc[load_df1['year'] == y]
    
                        seasons = [1, 1, 2, 2, 2,
                                   3, 3, 3, 4, 4, 4, 1]
                        month_to_season = dict(
                            zip(range(1, 13), seasons))
                        
                        load_df_y['s'] = load_df_y['month'].map(
                            month_to_season)
    
                        load_df_y['day_of_week'] = load_df_y['day'].apply(
                            date.isoweekday)
    
                        load_df_y_pivot = load_df_y.pivot_table(index=['day_of_week', 'hour', 's'], values=[
                            self.load_forecast], aggfunc='mean')
                        # find peak summer week
                        load_df_y_summer = load_df_y.loc[load_df_y['s'] == 3]
    
                        # find peak value
                        peak_day_hr = load_df_y_summer.loc[load_df_y_summer[self.load_forecast]
                                                           == np.max(load_df_y_summer[self.load_forecast])].index
                        # select the day
                        peak_day = load_df_y_summer.loc[load_df_y_summer[self.load_forecast] ==
                                                        np.max(load_df_y_summer[self.load_forecast])]['day'].values[0]
                        # find week number
                        week_of_num = peak_day.isocalendar()
    
                        weekday = peak_day.isoweekday()
    
                        start_of_week = peak_day - \
                            datetime.timedelta(days=weekday)
    
                        week_dates = [start_of_week +
                                      datetime.timedelta(days=d) for d in range(7)]
                        peak_week_profile = pd.concat(
                            [load_df_y_summer.loc[load_df_y_summer['day'] == week_dates[i]] for i in range(np.size(week_dates))])
    
                        # put together peak week + average weeks
                        load_df_y_pivot = load_df_y_pivot.reset_index()
                        sim_block[str(y)] = pd.concat([load_df_y_pivot.loc[load_df_y_pivot['s'] == 1][self.load_forecast],
                                                       load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                           == 2][self.load_forecast],
                                                       load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                           == 3][self.load_forecast],
                                                       load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                           == 4][self.load_forecast],
                                                       peak_week_profile[self.load_forecast]], ignore_index=True)              
                    hour_duration = [
                        13.0357, 13.0357, 12.0357, 13.0357, 1]
                    season_num = 5
                    
                    s_i_weight = {}
                    for s in range(season_num+1):
                        for i in range(168+1):
                            if s==1 or s==2 or s==4:
                                s_i_weight[s,i] = 13.0357
                            elif s==3:
                                s_i_weight[s,i] = 12.0357
                            elif s==5:
                                s_i_weight[s,i] = 1
                    
                    season_time_duration = s_i_weight
                    
                    dt_info = None

                elif self.block_selection.lower() == 'Full_Year'.lower():
    
                    if len(self.years) == 1:
                        sim_block = pd.DataFrame()
                        dt_info = pd.DataFrame()
                        seasons = [1, 1, 2, 2, 2,
                                   3, 3, 3, 4, 4, 4, 1]
                        month_to_season = dict(
                            zip(range(1, 13), seasons))
                        load_df['s'] = load_df['month'].map(
                            month_to_season)
                        for y in self.years:
                            # load for year y
                            load_df_y = load_df.loc[load_df['year'] == y]
    
                            sim_block[str(
                                y)] = load_df_y[self.load_forecast].values
                            # peak_week_profile['datetime'].values
                            dt_info[str(
                                y)] = load_df_y['datetime'].values
                            season_time_duration = 1 #weight is 1 hour
                    else:
                        raise Exception(
                            "Can only select one simulation year if 8760 time steps are chosen")
    
                    hour_duration = [1.0, 1, 1, 1]
                    season_num = 4
                elif self.block_selection.lower() == 'Full_Year_MY'.lower():
    
                    sim_block = pd.DataFrame()
                    dt_info = pd.DataFrame()
                    
                    # load_df = load_df.set_index(['datetime'])
                    # seasons = ['winter','spring','summer','fall']
                    seasons = [1, 1, 2, 2, 2,
                               3, 3, 3, 4, 4, 4, 1]
                    month_to_season = dict(
                        zip(range(1, 13), seasons))
                    load_df['s'] = load_df['month'].map(
                        month_to_season)
                    for y in self.years:
                        # load for year y
                        load_df_y = load_df.loc[load_df['year'] == y]
                        # remove leap day for now
                        load_df_y = load_df_y[~((load_df_y['datetime'].dt.day == 29) & (
                            load_df_y['datetime'].dt.month == 2))]
                        sim_block[str(
                            y)] = load_df_y[self.load_forecast].values
                        # peak_week_profile['datetime'].values
                        dt_info[str(
                            y)] = load_df_y['datetime'].values
    
                    hour_duration = [1.0, 1, 1, 1]
                    season_num = 4
                elif self.block_selection.lower() == 'Seasonal_blocks'.lower():
                    
                    '''
                    Develop seasonal blocks..
                    
                    for each season --> partition into 
                        12AM-6AM
                        6AM-10AM
                        10AM-2PM
                        2PM-6PM
                        6PM-12AM
                    then add one peak block...
                        12AM-6AM
                        6AM-10AM
                        10AM-2PM
                        2PM-6PM
                        6PM-12AM 
                    TOTAL: 25 operating conditions/year
                    
                    '''
                    sim_block = pd.DataFrame()
                    dt_info = pd.DataFrame()
                    
                    load_df1 = load_df.set_index(
                        'datetime') 
                    for y in self.years:
                        load_df_y = load_df1.loc[load_df1['year'] == y]
                        seasons = [1, 1, 2, 2, 2,
                                   3, 3, 3, 4, 4, 4, 1]
                        month_to_season = dict(
                            zip(range(1, 13), seasons))
                  
                        load_df_y['s'] = load_df_y['month'].map(
                            month_to_season)
                        
                        hours_b = [0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4]
                        hour_to_block = dict(
                            zip(range(0,24), hours_b))
                        load_df_y['block'] = load_df_y['hour'].map(
                            hour_to_block)
        
                        load_df_y['day_of_week'] = load_df_y['day'].apply(
                            date.isoweekday)
        
                        load_df_y_pivotc = load_df_y.pivot_table(index=['s','block'], values=[
                            self.load_forecast], aggfunc='count').to_dict()
                        peak_block = {(5,0):7,(5,1):4,(5,2):4,(5,3):4,(5,4):4}
                        s_i_weight = load_df_y_pivotc[self.load_forecast] | peak_block
                        
                        load_df_y_pivot = load_df_y.pivot_table(index=['block', 's'], values=[
                            self.load_forecast], aggfunc='mean') #'day_of_week'
                        
                        #now add peak conditions
                        # find peak summer week
                        load_df_y_summer = load_df_y.loc[load_df_y['s'] == 3]
                        # find peak value
                        peak_day_hr = load_df_y_summer.loc[load_df_y_summer[self.load_forecast]
                                                           == np.max(load_df_y_summer[self.load_forecast])].index
                        # select the day
                        peak_day = load_df_y_summer.loc[load_df_y_summer[self.load_forecast] ==
                                                        np.max(load_df_y_summer[self.load_forecast])]['day'].values[0]
                        #find hourly profile
                        peak_week_profile = pd.concat(
                            [load_df_y_summer.loc[load_df_y_summer['day'] == peak_day]])
                        peak_week_profile_pivot = peak_week_profile.pivot_table(index=['block', 's'], values=[
                            self.load_forecast], aggfunc='mean')
                        # put together peak block + season blocks
                          
                            #if y == self.years[0]:
                        load_df_y_pivot = load_df_y_pivot.reset_index()
                        sim_block[str(y)] = pd.concat([load_df_y_pivot.loc[load_df_y_pivot['s'] == 1][self.load_forecast],
                                                       load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                           == 2][self.load_forecast],
                                                       load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                           == 3][self.load_forecast],
                                                       load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                           == 4][self.load_forecast],
                                                       peak_week_profile_pivot[self.load_forecast]], ignore_index=True)
                       # else:
                          #  idx = np.where(
                           #     np.array(self.years) == y)[0][0]
                           # prev_y = self.years[idx-1]
                           # sim_block[str(y)] = (
                           #     1+(self.year_gap*self.load_growth/100))*sim_block[str(prev_y)]
    
                    hour_duration = [
                        13.0357, 13.0357, 12.0357, 13.0357, 1]#Check validity
                    season_time_duration = s_i_weight
                    #time_duration = [7,4,4,4,4,7,4,4,4,4,7,4,4,4,4,7,4,4,4,4,7,4,4,4,4]
                    season_num = 5
                    dt_info = None
                else:
                    raise Exception(
                        "Invalid selection")
                    
            else:
                # For RTS-GMLC only (or similar test case)...make the forecasted load profiles for future years
                if self.block_selection.lower() == 'Seasonal_blocks'.lower():
                    '''
                    Develop seasonal blocks..
                    
                    for each season --> partition into 
                        12AM-6AM
                        6AM-10AM
                        10AM-2PM
                        2PM-6PM
                        6PM-12AM
                    then add one peak block...
                        12AM-6AM
                        6AM-10AM
                        10AM-2PM
                        2PM-6PM
                        6PM-12AM 
                    TOTAL: 25 operating conditions/year
                    
                    '''
                    sim_block = pd.DataFrame()
                    dt_info = pd.DataFrame()
                    
                    load_df1 = load_df.set_index(
                        'datetime') 
                    load_df_y = load_df1
                    seasons = [1, 1, 2, 2, 2,
                               3, 3, 3, 4, 4, 4, 1]
                    month_to_season = dict(
                        zip(range(1, 13), seasons))
              
                    load_df_y['s'] = load_df_y['month'].map(
                        month_to_season)
                    
                    hours_b = [0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4]
                    hour_to_block = dict(
                        zip(range(0,24), hours_b))
                    load_df_y['block'] = load_df_y['hour'].map(
                        hour_to_block)
    
                    load_df_y['day_of_week'] = load_df_y['day'].apply(
                        date.isoweekday)
    
                    load_df_y_pivotc = load_df_y.pivot_table(index=['s','block'], values=[
                        self.load_forecast], aggfunc='count').to_dict()
                    peak_block = {(5,0):7,(5,1):4,(5,2):4,(5,3):4,(5,4):4}
                    s_i_weight = load_df_y_pivotc[self.load_forecast] | peak_block
                    
                    load_df_y_pivot = load_df_y.pivot_table(index=['block', 's'], values=[
                        self.load_forecast], aggfunc='mean') #'day_of_week', np.mean
                    
                    #now add peak conditions
                    # find peak summer week
                    load_df_y_summer = load_df_y.loc[load_df_y['s'] == 3]
                    # find peak value
                    peak_day_hr = load_df_y_summer.loc[load_df_y_summer[self.load_forecast]
                                                       == np.max(load_df_y_summer[self.load_forecast])].index
                    # select the day
                    peak_day = load_df_y_summer.loc[load_df_y_summer[self.load_forecast] ==
                                                    np.max(load_df_y_summer[self.load_forecast])]['day'].values[0]
                    #find hourly profile
                    peak_week_profile = pd.concat(
                        [load_df_y_summer.loc[load_df_y_summer['day'] == peak_day]])
                    peak_week_profile_pivot = peak_week_profile.pivot_table(index=['block', 's'], values=[
                        self.load_forecast], aggfunc='mean')
                    # put together peak block + season blocks
                    for y in self.years:  
                        if y == self.years[0]:
                            load_df_y_pivot = load_df_y_pivot.reset_index()
                            sim_block[str(y)] = pd.concat([load_df_y_pivot.loc[load_df_y_pivot['s'] == 1][self.load_forecast],
                                                           load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                               == 2][self.load_forecast],
                                                           load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                               == 3][self.load_forecast],
                                                           load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                               == 4][self.load_forecast],
                                                           peak_week_profile_pivot[self.load_forecast]], ignore_index=True)
                        else:
                            idx = np.where(
                                np.array(self.years) == y)[0][0]
                            prev_y = self.years[idx-1]

                            years_since_base = self.year_gap_array[self.years.index(y)]
                            sim_block[str(y)] = (1 + self.load_growth) ** years_since_base * sim_block[str(self.years[0])]

                            #sim_block[str(y)] = (
                                #1+(self.year_gap_array[self.years.index(y)]*self.load_growth))*sim_block[str(prev_y)]
    
                    hour_duration = [
                        13.0357, 13.0357, 12.0357, 13.0357, 1]#Check validity
                    season_time_duration = s_i_weight
                    #time_duration = [7,4,4,4,4,7,4,4,4,4,7,4,4,4,4,7,4,4,4,4,7,4,4,4,4]
                    season_num = 5
                    dt_info = None
                
                elif self.block_selection.lower() == 'Peak_day'.lower():
                    sim_block = pd.DataFrame()
                    dt_info = pd.DataFrame()
    
                    # find peak value & select the day
                    peak_day = load_df.loc[load_df[self.load_forecast] ==
                                             np.max(load_df[self.load_forecast])]['day'].values[0]
    
                    peak_day_profile = load_df.loc[load_df['day'] == peak_day]
                    
                    for y in self.years:
                        # RETURN the block(s) to be simulated
                        if y == self.years[0]:
                            sim_block[str(
                                y)] = peak_day_profile[self.load_forecast].values
                            dt_info[str(
                                y)] = peak_day_profile['datetime'].values
                        else:
                            sim_block[str(
                                y)] = (1+(self.year_gap_array[self.years.index(y)]*self.load_growth))*peak_day_profile[self.load_forecast].values
                            dt_info[str(
                                y)] = peak_day_profile['datetime'].values
                    season_num=1
                    hour_duration=365
                    s_i_weight = {}
                    for s in range(season_num+1):
                        for i in range(24+1):
                            if s != 0:
                                s_i_weight[s,i] = 365
                    
                    season_time_duration = s_i_weight
                elif self.block_selection.lower() == 'Repr_Weeks'.lower():
    
                    sim_block = pd.DataFrame()
                    dt_info = pd.DataFrame()
    
                    load_df1 = load_df.set_index(
                        'datetime') 
                    load_df_y = load_df1
    
                    seasons = [1, 1, 2, 2, 2,
                               3, 3, 3, 4, 4, 4, 1]
                    month_to_season = dict(
                        zip(range(1, 13), seasons))
    
                    load_df_y['s'] = load_df_y['month'].map(
                        month_to_season)
    
                    load_df_y['day_of_week'] = load_df_y['day'].apply(
                        date.isoweekday)
    
                    load_df_y_pivot = load_df_y.pivot_table(index=['day_of_week', 'hour', 's'], values=[
                        self.load_forecast], aggfunc='mean')
                    # find peak summer week
                    load_df_y_summer = load_df_y.loc[load_df_y['s'] == 3]
    
                    # find peak value - unused
                    peak_day_hr = load_df_y_summer.loc[load_df_y_summer[self.load_forecast]
                                                       == np.max(load_df_y_summer[self.load_forecast])].index
    
                    # select the day
                    peak_day = load_df_y_summer.loc[load_df_y_summer[self.load_forecast] ==
                                                    np.max(load_df_y_summer[self.load_forecast])]['day'].values[0]
    
                    # find week number
                    week_of_num = peak_day.isocalendar()
    
                    weekday = peak_day.isoweekday()
    
                    start_of_week = peak_day - \
                        datetime.timedelta(days=weekday)
    
                    week_dates = [start_of_week +
                                  datetime.timedelta(days=d) for d in range(7)]
                    peak_week_profile = pd.concat(
                        [load_df_y_summer.loc[load_df_y_summer['day'] == week_dates[i]] for i in range(np.size(week_dates))])
    
                    # put together peak week + average weeks
                    self.set_years_hours(self.years)
                    for y in self.years: 
                        if y == self.years[0]:
                            load_df_y_pivot = load_df_y_pivot.reset_index()
                            sim_block[str(y)] = pd.concat([load_df_y_pivot.loc[load_df_y_pivot['s'] == 1][self.load_forecast],
                                                           load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                               == 2][self.load_forecast],
                                                           load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                               == 3][self.load_forecast],
                                                           load_df_y_pivot.loc[load_df_y_pivot['s']
                                                                               == 4][self.load_forecast],
                                                           peak_week_profile[self.load_forecast]], ignore_index=True)
                        else:
                            idx = np.where(
                                np.array(self.years) == y)[0][0]
                            prev_y = self.years[idx-1]
                            
                            years_since_base = self.year_gap_array[self.years.index(y)]
                            sim_block[str(y)] = (1 + self.load_growth) ** years_since_base * sim_block[str(self.years[0])]

                            #sim_block[str(y)] = (
                              #  1+(self.year_gap_array[self.years.index(y)]*self.load_growth))*sim_block[str(prev_y)]#self.load_growth/100))*sim_block[str(prev_y)]
    
                    hour_duration = [
                        13.0357, 13.0357, 12.0357, 13.0357, 1]
                    
                    
                    season_num = 5
                    
                    s_i_weight = {}
                    for s in range(season_num+1):
                        for i in range(168+1):
                            if s==1 or s==2 or s==4:
                                s_i_weight[s,i] = 13.0357
                            elif s==3:
                                s_i_weight[s,i] = 12.0357
                            elif s==5:
                                s_i_weight[s,i] = 1
                    
                    season_time_duration = s_i_weight
                    dt_info = None
                    
                elif self.block_selection.lower() == 'Repr_3Days_Season'.lower():
                    sim_block = pd.DataFrame()
                    dt_info = pd.DataFrame()

                    # map months to seasons
                    seasons = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]
                    month_to_season = dict(zip(range(1, 13), seasons))
                    load_df['s'] = load_df['month'].map(month_to_season)

                    # --- build base year block ---
                    base_year = self.years[0]
                    load_df_base = load_df.copy() #load_df.loc[load_df['year'] == base_year].copy()
                    all_season_load = []
                    all_season_dtime = []

                    for s in sorted(np.unique(seasons)):
                        load_df_s = load_df_base.loc[load_df_base['s'] == s]
                        #print(load_df_s)
                        # build daily matrix (rows = days, cols = 24h)
                        daily = []
                        day_keys = []
                        for day, g in load_df_s.groupby('day'):
                            
                            if len(g) == 24:
                                daily.append(g.sort_values('datetime')[self.load_forecast].values)
                                day_keys.append(day)
                        daily = np.array(daily)

                        reps = []
                        print(f'Season {s}, found {daily.shape[0]} full days for base year {base_year}')
                        if daily.shape[0] >= 3:
                            print(f'Using KMeans to find representative days for season {s}')
                            try:
                                km = KMeans(n_clusters=3, random_state=0).fit(daily)
                                centers = km.cluster_centers_
                                for c in range(3):
                                    idx = int(np.argmin(np.linalg.norm(daily - centers[c], axis=1)))
                                    reps.append(day_keys[idx])
                            except Exception as e:
                                logging.warning(f"KMeans failed for season {s} (fallback): {e}")
                                # fall through to quantile/fallback logic below

                        # If we didn't get 3 reps from kmeans (or never ran it), use peak-based fallback.
                        if len(reps) < 3:
                            if len(day_keys) > 0:
                                # daily might be empty or small; compute peaks where possible
                                daily_peaks = pd.Series({day_keys[i]: daily[i].max() for i in range(len(day_keys))})
                                top = daily_peaks.sort_values(ascending=False).index.tolist()

                                if len(top) == 0:
                                    # no full days with 24h values — fall back to any available day_keys (even if partial)
                                    reps = (day_keys * 3)[:3]
                                else:
                                    # repeat top entries to ensure length 3, but avoid an infinite loop
                                    reps = (top * 3)[:3]
                            else:
                                # No days at all for this season — skip season (or choose a more aggressive fallback)
                                logging.warning(f"No candidate days found for season {s} (year {y}); skipping this season")
                                continue  # skip to next season

                        # Final safety: ensure exactly 3 reps
                        if len(reps) > 3:
                            reps = reps[:3]
                        elif len(reps) < 3:
                            reps = (reps * 3)[:3]

                        for d in reps:
                            d_profile = load_df_s.loc[load_df_s['day'] == d].sort_values('datetime').iloc[:24]
                            all_season_load.extend(d_profile[self.load_forecast].values)
                            all_season_dtime.extend(d_profile['datetime'].values)

                    # add annual peak day
                    peak_day = load_df_base.loc[load_df_base[self.load_forecast] ==
                                                np.max(load_df_base[self.load_forecast])]['day'].values[0]
                    peak_profile = load_df_base.loc[load_df_base['day'] == peak_day].sort_values('datetime').iloc[:24]
                    all_season_load.extend(peak_profile[self.load_forecast].values)
                    all_season_dtime.extend(peak_profile['datetime'].values)

                    # store base year block
                    sim_block[str(base_year)] = all_season_load
                    dt_info[str(base_year)] = all_season_dtime
                    season_num = 5
                    hour_duration = [30.431, 30.431, 28.107, 30.431, 2.333]
                    #(7/3)*[
                        #13.0357, 13.0357, 12.0357, 13.0357, 1]

                    # --- scale for future years using load growth ---
                    for y in self.years[1:]:
                        years_since_base = self.year_gap_array[self.years.index(y)]
                        growth_factor = (1 + self.load_growth) ** years_since_base
                        sim_block[str(y)] = growth_factor * sim_block[str(base_year)]
                        # keep same dt_info
                        dt_info[str(y)] = all_season_dtime
                    
                    s_i_weight = {}
                    for s in range(season_num+1):
                        for i in range(72+1):
                            if s==1 or s==2 or s==4:
                                s_i_weight[s,i] = 30.431
                            elif s==3:
                                s_i_weight[s,i] = 30.431
                            elif s==5:
                                s_i_weight[s,i] = 1
                    
                    season_time_duration = s_i_weight

                elif self.block_selection.lower() == 'Full_Year'.lower():
                    # CJN fixed temporarily - 7/3
                    if len(self.years) == 1:
                        sim_block = pd.DataFrame()
                        dt_info = pd.DataFrame()
                        seasons = [1, 1, 2, 2, 2,
                                   3, 3, 3, 4, 4, 4, 1]
                        month_to_season = dict(
                            zip(range(1, 13), seasons))
                        load_df['s'] = load_df['month'].map(
                            month_to_season)
                        #for y in self.years:
                            # load for year y
                            #load_df_y = load_df.loc[load_df['year'] == y]
    
                        sim_block[str(
                            self.years[0])] = load_df[self.load_forecast].values
                        dt_info[str(
                            self.years[0])] = load_df['datetime'].values
                        
                        season_time_duration = 1 

                    else:
                        raise Exception(
                            "Can only select one simulation year if 8760 time steps are chosen")
    
                    hour_duration = [1.0, 1, 1, 1]
                    season_num = 4
                else:
                    raise Exception(
                            "Invalid selection")
        except Exception as e:
                print(e)        

        self.load_blocks = sim_block
        self.dt_info = dt_info
        self.create_season_map()
        self.S = season_num
        self.hour_duration = hour_duration
        self.season_time_duration = season_time_duration

    def find_system_peak(self):
        '''
        Determines the annual system peak

        Returns
        -------
        peak_pivot : Dictionary of annual peak

        '''
        load_df = self.load_data[self.index('load')]
        years = np.unique(load_df['year'].values)
        if len(years) > 1:
            
            load_df["datetime"] = pd.to_datetime(
                load_df["datetime"], format='mixed')#, infer_datetime_format=True
            load_df["day"] = pd.to_datetime(
                load_df["day"], format='mixed').dt.date#, infer_datetime_format=True
            load_df["hour"] = pd.to_datetime(
                load_df["datetime"], format='mixed').dt.hour#, infer_datetime_format=True
    
            load_df['month'] = pd.DatetimeIndex(
                load_df["datetime"]).month
            self.set_years_hours(self.years)
            peak_pivot = load_df.pivot_table(index=['year'], values=[
                self.load_forecast], aggfunc=np.max)
        else:
            load_df = self.load_data[self.index('load')]
            peak = max(load_df[self.load_forecast])
            peak_pivot = pd.DataFrame(index = self.years,columns = [self.load_forecast])
            self.set_years_hours(self.years)
            
            for y in self.years:
                years_since_base = self.year_gap_array[self.years.index(y)]
                if y == self.years[0]:
                    peak_pivot.loc[y] = peak
                else:
                    peak_pivot.loc[y] = peak * (1 + self.load_growth) ** years_since_base
            #for y in self.years:
             #   if y == self.years[0]:
              #      peak_pivot.loc[y] = peak
               # else:
                    #TODO: fix load growth
                    
                    #print(self.years)
                    #print(self.year_gap_array[y])
                #    peak_pivot.loc[y] = peak*(1+self.year_gap_array[self.years.index(y)]*self.load_growth) #(self).year_gap*self.load_growth/100)

           
        return peak_pivot

    def find_system_energy(self):
        '''
        Determines the annual system energy

        Returns
        -------
        energy_pivot : Returns annual system energy

        '''
        load_df = self.load_data[self.index('load')]
       
        years = np.unique(load_df['year'].values)
        if len(years) > 1:

            load_df["datetime"] = pd.to_datetime(
                load_df["datetime"], format='mixed')#, infer_datetime_format=True
            load_df["day"] = pd.to_datetime(
                load_df["day"], format='mixed').dt.date#, infer_datetime_format=True
            load_df["hour"] = pd.to_datetime(
                load_df["datetime"], format='mixed').dt.hour#, infer_datetime_format=True
    
            load_df['month'] = pd.DatetimeIndex(
                load_df["datetime"]).month
    
            energy_pivot = load_df.pivot_table(index=['year'], values=[
                self.load_forecast], aggfunc=np.sum)
        else:
            load_df = self.load_data[self.index('load')]
            energy = sum(load_df[self.load_forecast])
            energy_pivot = pd.DataFrame(index = self.years,columns = [self.load_forecast])
            for y in self.years:
                if y == self.years[0]:
                    energy_pivot.loc[y] = energy
                else:
                    energy_pivot.loc[y] = energy*(1+self.year_gap_array[self.years.index(y)]*self.load_growth)#(self).year_gap*self.load_growth/100)
        return energy_pivot

    def create_season_map(self):
        '''
        Creates season map

        Returns
        -------
        None.

        '''
        seasons = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]
        month_to_season = dict(zip(range(1, 13), seasons))
        df = pd.DataFrame(columns=self.years)
        if self.block_selection.lower() != 'Repr_Weeks'.lower():
            if self.block_selection.lower() == 'Full_year'.lower():
                df = self.dt_info[str(self.years[0])].dt.month.map(
                    month_to_season)
                
            elif self.block_selection.lower() == 'Seasonal_blocks'.lower():
                for c in df.columns:
                    season_array = np.concatenate([np.ones(
                        5)*1, np.ones(5)*2, np.ones(5)*3, np.ones(5)*4, np.ones(5)*5])
                    df[c] = season_array
            elif self.block_selection.lower() == 'Repr_3Days_Season'.lower():
                # For each column (year) produce array: 3 days*24 hrs for s=1, ... s=4, then 24 hrs peak s=5
                for c in df.columns:
                    season_array = np.concatenate([
                        np.ones(3 * 24) * 1,
                        np.ones(3 * 24) * 2,
                        np.ones(3 * 24) * 3,
                        np.ones(3 * 24) * 4,
                        np.ones(24) * 5
                    ])
                    df[c] = season_array
            else:
                for c in self.dt_info.columns:
                    # print(c)
                    df[c] = self.dt_info[c].dt.month.map(
                        month_to_season)
                df = df.dropna(axis=1)
        
        else:
            # for Repr_Weeks only
            for c in df.columns:
                season_array = np.concatenate([np.ones(
                    168)*1, np.ones(168)*2, np.ones(168)*3, np.ones(168)*4, np.ones(168)*5])
                df[c] = season_array

        self.season_map = df
       

    def load_par_adjust(self):
        """

        Adjust the load parameter to be inputted into the pyomo models

        Parameters
        ----------
        df : input dataframe
        bus_frac : array of percenatages to distribute load
        block_selection: specify block selection

        Returns
        -------
        load_dict : dictionary containing input ready data

        """
        df = self.load_blocks
        bus_frac = list(
            self.load_data[self.index('bus')]['Load_share'].values)       
        years = self.years   
        df.columns = self.years
        time, year = np.shape(df)
        bus_num = np.size(bus_frac)
        bus_nums = list(
            self.load_data[self.index('bus')]['Bus_number'].values)
        
        if self.block_selection.lower() == 'Peak_day'.lower():
            time, year = np.shape(df)
            time_array = np.array(np.arange(0, 24))
            season_array = 1
            df1 = pd.DataFrame(data=df.unstack(level=0))

            df1['s'] = season_array
            df1 = df1.reset_index()
            df1.columns = ['y', 'i', 'total', 's']
            df1['i'] = np.concatenate([time_array]*year)
        if self.block_selection.lower() == 'Peak_Week_Season'.lower():
            # for Peak week only
            time, year = np.shape(df)
            time_array = np.concatenate(
                [np.array(np.arange(0, 168))]*4)
            season_array = self.season_map(
                self.dt_info).unstack(level=0)[years]
            season_array = season_array.values
            df1 = pd.DataFrame(data=df.unstack(level=0))

            df1['s'] = season_array
            df1 = df1.reset_index()
            df1.columns = ['y', 'i', 'total', 's']
            df1['i'] = time_array
        if self.block_selection.lower() == 'Seasonal_blocks'.lower():
            time, year = np.shape(df)
            time_array = np.concatenate(
                [np.array(np.arange(0, 5))]*5)
            season_array = np.concatenate([np.ones(
                5)*1, np.ones(5)*2, np.ones(5)*3, np.ones(5)*4, np.ones(5)*5])
            df1 = pd.DataFrame(data=df.unstack(level=0))

            df1['i'] = np.concatenate([time_array]*year)
            df1['s'] = np.concatenate([season_array]*year)

            df1 = df1.reset_index()
            df1.columns = ['y', 'drop', 'total', 'i', 's']
            df1 = df1.drop('drop', axis=1)
        if self.block_selection.lower() == 'Repr_weeks'.lower():
            # for Peak week only
            time, year = np.shape(df)
            time_array = np.concatenate(
                [np.array(np.arange(0, 168))]*5)
            season_array = np.concatenate([np.ones(
                168)*1, np.ones(168)*2, np.ones(168)*3, np.ones(168)*4, np.ones(168)*5])
            df1 = pd.DataFrame(data=df.unstack(level=0))

            df1['i'] = np.concatenate([time_array]*year)
            df1['s'] = np.concatenate([season_array]*year)

            df1 = df1.reset_index()
            df1.columns = ['y', 'drop', 'total', 'i', 's']
            df1 = df1.drop('drop', axis=1)
        if self.block_selection.lower() == 'Repr_3Days_Season'.lower():
            time, year = np.shape(df)
            # indices inside a year: 72 hours per season * 4 + 24 peak = 312
            time_array = np.concatenate([
                np.arange(0, 3 * 24),
                np.arange(0, 3 * 24),
                np.arange(0, 3 * 24),
                np.arange(0, 3 * 24),
                np.arange(0, 24)
            ])
            season_array = np.concatenate([
                np.ones(3 * 24) * 1,
                np.ones(3 * 24) * 2,
                np.ones(3 * 24) * 3,
                np.ones(3 * 24) * 4,
                np.ones(24) * 5
            ])
            df1 = pd.DataFrame(data=df.unstack(level=0))
            df1['i'] = np.concatenate([time_array] * year)
            df1['s'] = np.concatenate([season_array] * year)
            df1 = df1.reset_index()
            df1.columns = ['y', 'drop', 'total', 'i', 's']
            df1 = df1.drop('drop', axis=1)
        if self.block_selection.lower() == 'Full_year'.lower() or self.block_selection.lower() == 'Full_year_MY'.lower():
            time, year = np.shape(df)
            time_array = np.array(np.arange(0, time))
            # .unstack(level=0)
            season_array = self.season_map
            df1 = pd.DataFrame(data=df.unstack(level=0))

            df1['i'] = np.concatenate([time_array]*year)
            
            if self.block_selection.lower() == 'Full_Year_MY'.lower():
                df1['s'] = np.concatenate(
                    [season_array[season_array.columns[0]]]*year)
            else:
                df1['s'] = np.concatenate(
                    [season_array]*year)
            df1 = df1.reset_index()
            df1.columns = ['y', 'drop', 'total', 'i', 's']
            df1 = df1.drop('drop', axis=1)

            # Find season start hour and end hour for ES constraints
            if self.block_selection.lower() == 'Full_Year_MY'.lower():
                season_time_array = pd.DataFrame(
                    [season_array[season_array.columns[0]].values, time_array], index=['s', 'i']).T
            else:
                season_time_array = pd.DataFrame(
                    [season_array.values, time_array], index=['s', 'i']).T
            
            # Find the first and last hour of each season
            season_time_array['s'] = season_time_array['s'].astype(int)
            season_time_array['i'] = season_time_array['i'].astype(int)
            
            season_changes = season_time_array['s'].ne(season_time_array['s'].shift())
            season_starts = season_time_array.index[season_changes].tolist()
            season_ends = (season_time_array.index[season_changes.shift(-1, fill_value=False)]).tolist()
            #if season_ends[-1] != season_time_array.index[-1]:
                #season_ends.append(season_time_array.index[-1])

            self.start_hr = season_starts
            self.end_hr = season_ends

            #find last hour of one season and first hour of next
            
            #fh = np.array(season_time_array.index[season_changes])  # first hour of each season neglect t=0
            fh = np.array(season_time_array.index[season_changes])[1:]  # first hour of each season, skip the first
            lh = np.array(season_time_array.index[season_changes.shift(-1, fill_value=False)])  # last hour of each season

            self.last_hr = lh
            self.first_hr = fh

            '''
            lh = []#last hour
            fh = []#first hour
            for i in np.unique(season_time_array['i']):
                
                if i != 0:
                    s = season_time_array['s'][i]
                    s_1 = season_time_array['s'][i-1]
                    if s != s_1:  # and i != 0:
                        lh = np.concatenate(
                            (lh, i-1), axis=None)
                        fh = np.concatenate(
                            (fh, i), axis=None)
            '''
            
                        
            

        df1 = df1.set_index(['y', 's', 'i'])
        
        for b in np.arange(0, len(bus_nums)):
            df1[bus_nums[b]] = df1['total'] * (bus_frac[b]/100)#float(df1['total'])
            
        df1 = df1.drop(['total'], axis=1)
        df_final = pd.DataFrame(data=df1.stack(level=-1))
        df_final = df_final.rename_axis(
            ['y', 's', 'i', 'b'], axis=0)
        df_final = df_final.reset_index()
        df_final = df_final.set_index(['b', 'y', 's', 'i'])
        # df_final.index = df_final.index.map(str)
        all_bus_load = df_final.to_dict()[0]
        return all_bus_load


    def ren_profile_par_adj(self, tech_type):
        '''
        Renewable profile adjustment for model input
        
        Parameters
        ----------
        tech_type : Technology type
        
        Returns
        -------
        ren_df_all_years : dictionary for model input
        
        '''
        if tech_type == 'upv_ex':
            index = 'solar'
            bus_nums = self.bus_upv_ex_num
        elif tech_type == 'upv_can':
            index = 'solar_cand'
            bus_nums = self.bus_solar_can_num
        elif tech_type == 'wind_ex':
            index = 'wind'
            bus_nums = self.bus_wind_ex_num
        elif tech_type == 'wind_can':
            index = 'wind_cand'
            bus_nums = self.bus_wind_can_num
        else:
            logging.error(
                "Invalid renewable generator type: {error}".format(tech_type))
            
        ren_df = self.load_data[self.index(index)]
        
        tech_nums = self.tech_nums[tech_type]
        block_selection = self.block_selection
        years = self.years  
        ren_df['datetime'] = pd.to_datetime(ren_df['datetime'], format='mixed')#, infer_datetime_format=True
        ren_df['day'] = ren_df['datetime'].dt.strftime('%m-%d')
        #ren_df['day'] = pd.to_datetime(ren_df['datetime'], format='%m-%d', infer_datetime_format=False)#.strftime('%Y-%m-%d')
        
        
        
        if block_selection.lower() == 'Peak_Week_Season'.lower():
        
            date_selected = self.dt_info[str(
                years[0])].values
            if years[0] != ren_df['datetime'][0].year:
                ren_df['datetime'].year = years[0]
        
            ren_df_selected = ren_df[ren_df['datetime'].isin(
                date_selected)].drop(['datetime', 'year', 'day'], axis=1)
            # for Peak week only
            time, year = np.shape(ren_df_selected)
            time_array = np.concatenate(
                [np.array(np.arange(0, time/4))]*4)
            season_array = self.season_map[str(
                years[0])].values
        elif block_selection.lower() == 'Repr_Weeks'.lower():
            time_array = np.concatenate(
                [np.array(np.arange(0, 168))]*5)
            season_array = np.concatenate([np.ones(
                168)*1, np.ones(168)*2, np.ones(168)*3, np.ones(168)*4, np.ones(168)*5])
            seasons = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]
            month_to_season = dict(
                zip(range(1, 13), seasons))
            ren_df['month'] = pd.DatetimeIndex(
                ren_df['datetime']).month
            ren_df['hour'] = pd.DatetimeIndex(
                ren_df['datetime']).hour
            ren_df['s'] = ren_df['month'].map(
                month_to_season)
        
            ren_df['day_of_week'] = ren_df['datetime'].apply(
                date.isoweekday)
            ren_df_pivot = ren_df.pivot_table(
                index=['day_of_week', 'hour', 's'], values=ren_df.columns[3:3+len(tech_nums)], aggfunc='mean')
            ren_df_pivot = ren_df_pivot.reset_index()
            ren_df_selected = pd.concat([ren_df_pivot.loc[ren_df_pivot['s'] == 1],
                                           ren_df_pivot.loc[ren_df_pivot['s'] == 2],
                                           ren_df_pivot.loc[ren_df_pivot['s'] == 3],
                                           ren_df_pivot.loc[ren_df_pivot['s'] == 4],
                                           ren_df_pivot.loc[ren_df_pivot['s'] == 3]])
            ren_df_selected['y'] = years[0]
            ren_df_selected = ren_df_selected.drop(
                ['day_of_week', 'hour'], axis=1)
        
        elif block_selection.lower() == 'Repr_3Days_Season'.lower():
            # 3 representative days (72 hrs) per season for 4 seasons + 1 peak day (24 hrs) = 312 hrs
            # Extract date and hour
            ren_df['date'] = ren_df['datetime'].dt.date
            ren_df['hour'] = pd.DatetimeIndex(ren_df['datetime']).hour

            # Map months to seasons
            seasons_map = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 1]
            month_to_season = dict(zip(range(1, 13), seasons_map))
            ren_df['s'] = ren_df['datetime'].dt.month.map(month_to_season)

            rep_days_list = []
            avg_days = pd.DataFrame()
            # Select 3 representative days per season
            for s in [1, 2, 3, 4]:
                season_data = ren_df[ren_df['s'] == s]

                # Pivot to day × hour × tech
                pivot = season_data.pivot_table(
                    index=['date','hour','s'],
                    values=season_data.columns[3:3+len(tech_nums)],
                    aggfunc='mean'
                ).reset_index()

                # Split unique days into 3 chunks
                unique_days = pivot['date'].unique()
                day_chunks = np.array_split(unique_days, 3)

                avg_days1 = []
                for c, days in enumerate(day_chunks, start=1):
                    avg_day = (pivot[pivot['date'].isin(days)]
                            .groupby('hour')[pivot.columns[2:]].mean()
                            .reset_index())
                    avg_day = avg_day.drop('hour', axis=1)
                    avg_day['s'] = s
                    # avg_day['rep_day'] = c  # mark which of the 3 it is
                    #
                    avg_days1.append(avg_day)
                    
                avg_days = pd.concat(avg_days1, ignore_index=True)
                avg_days['i'] = np.arange(0, 72)
                avg_days = avg_days.set_index(['s','i'])
                #print('Average days')
                #print(avg_days)
                
                rep_days_list.append(avg_days)
                
            rep_days_df = pd.concat(rep_days_list, ignore_index=False)
            #print(rep_days_df)
            
            # Average day in July for peak
            july_data = ren_df[ren_df['datetime'].dt.month == 7]
            july_pivot = july_data.pivot_table(
                #index='date',
                index=['hour'],
                values=july_data.columns[3:3+len(tech_nums)],
                aggfunc='mean'
            )
            #print(july_pivot)
            #avg_july_day = july_pivot.mean(axis=0).to_frame().T.reset_index(drop=True)
            july_pivot['s'] = 5   
            july_pivot['i'] = np.arange(0, 24)
            july_pivot = july_pivot.set_index(['s','i'])
            # Combine with representative days
            ren_df_selected = pd.concat([rep_days_df, july_pivot], ignore_index=True)
            #print(ren_df_selected)
            # Create time and season arrays
            time_array = np.concatenate([np.arange(0, 72)]*4 + [np.arange(0, 24)])
            season_array = np.concatenate([np.ones(72)*1, np.ones(72)*2, np.ones(72)*3, np.ones(72)*4, np.ones(24)*5])

            # Assign arrays and year
            ren_df_selected['i'] = time_array
            ren_df_selected['s'] = season_array
            ren_df_selected['y'] = years[0]

            # Keep only columns in the format matching Repr_Weeks
            #ren_df_selected = ren_df_selected[ren_df_selected.columns[3:3+len(tech_nums)].tolist()]# + ['y','s','i']]
            
            #print(ren_df_selected)
            #ren_df_selected = ren_df_selected.drop(
                #['hour'], axis=1)
            

        elif self.block_selection.lower() == 'Seasonal_blocks'.lower():
            '''
            
            Develop seasonal blocks..
            
            for each season --> partition into 
                12AM-6AM
                6AM-10AM
                10AM-2PM
                2PM-6PM
                6PM-12AM
            then add one peak block...
                12AM-6AM
                6AM-10AM
                10AM-2PM
                2PM-6PM
                6PM-12AM 
            TOTAL: 25 operating conditions/year
            
            '''
            time_array = np.concatenate(
                [np.array(np.arange(0, 5))]*5)
            season_array = np.concatenate([np.ones(
                5)*1, np.ones(5)*2, np.ones(5)*3, np.ones(5)*4, np.ones(5)*5])
        
            seasons = [1, 1, 2, 2, 2,
                       3, 3, 3, 4, 4, 4, 1]
            month_to_season = dict(
                zip(range(1, 13), seasons))                 
            
            hours_b = [1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,5]
            hour_to_block = dict(
                zip(range(0,24), hours_b))
            ren_df['month'] = pd.DatetimeIndex(
                ren_df['datetime']).month
            ren_df['hour'] = pd.DatetimeIndex(
                ren_df['datetime']).hour
            ren_df['s'] = ren_df['month'].map(
                month_to_season)
            ren_df['block'] = ren_df['hour'].map(
                hour_to_block)
        
            ren_df['day_of_week'] = ren_df['datetime'].apply(
                date.isoweekday)
            ren_df_pivot = ren_df.pivot_table(
                index=['block', 's'], values=ren_df.columns[3:3+len(tech_nums)], aggfunc='mean')
            ren_df_pivot = ren_df_pivot.reset_index()
            ren_df_selected = pd.concat([ren_df_pivot.loc[ren_df_pivot['s'] == 1],
                                           ren_df_pivot.loc[ren_df_pivot['s'] == 2],
                                           ren_df_pivot.loc[ren_df_pivot['s'] == 3],
                                           ren_df_pivot.loc[ren_df_pivot['s'] == 4],
                                           ren_df_pivot.loc[ren_df_pivot['s'] == 3]])
            ren_df_selected['y'] = years[0]
            ren_df_selected = ren_df_selected.drop(
                ['block'], axis=1)
            
            
        elif block_selection.lower() == 'Full_Year'.lower() or self.block_selection.lower() == 'Full_year_MY'.lower():
        
            season_array = self.season_map
            if self.block_selection.lower() == 'Full_Year_MY'.lower():
                season_array = season_array[season_array.columns[0]].values
            else:
                season_array = season_array.values
        
            date_selected = self.dt_info[str(
                years[0])].values
            
            #Handle leap day if leap year is selected AND leap day is in the load data
            dates = pd.to_datetime(self.dt_info[str(years[0])].values)
            has_leap_day = any((d.month == 2 and d.day == 29) for d in dates)

            if calendar.isleap(self.years[0]) and has_leap_day:
                # Find the row for February 28th
                #print('yes')
                feb_28_row = ren_df[ren_df['day'] == "02-28"]
                #print(feb_28_row)
                if not feb_28_row.empty:
                    # Create a new row for February 29th with the same renewable profile as February 28th -quick fix for now
                    feb_29_row = feb_28_row.copy()
                    feb_29_row['day'] = "02-29"
                    
                    # Append the new row to the DataFrame
                    ren_df = pd.concat([ren_df, feb_29_row], ignore_index=True)
                    
            ren_df_selected = ren_df.drop(
                ['datetime', 'year', 'day'], axis=1)
            
            time, year = np.shape(ren_df_selected)
            time_array = np.array(np.arange(0, time))
        elif self.block_selection.lower() == 'Peak_day'.lower():
            '''Only used for testing'''
            date_selected = self.dt_info[str(
                years[0])].values
            date_selected = pd.to_datetime(date_selected).strftime('%m-%d')
            #print(ren_df['day'])
            #print(date_selected)
            
            if years[0] != ren_df['datetime'][0].year:
                ren_df['datetime'].year = years[0]
            
            ren_df_selected = ren_df[ren_df['day'].isin(
                date_selected)].drop(['datetime', 'year', 'day'], axis=1)
            time, year = np.shape(ren_df_selected)
            time_array = np.array(np.arange(0, time))
            season_array=1
            #print(ren_df_selected)
            
        
        ren_df_selected['i'] = time_array
    
        ren_df_selected['s'] = season_array

        ren_df_selected['y'] = years[0]
        
        ren_df_selected = ren_df_selected.set_index(
            ['y', 's', 'i'])
        
        bus_gen_num = tuple(zip(bus_nums, tech_nums))
        ren_df_selected.columns = pd.MultiIndex.from_tuples(
            bus_gen_num)
        
        ren_df_selected_us = ren_df_selected.unstack(
            level=['y', 's', 'i']).to_frame()
        ren_df_selected_us = ren_df_selected_us.rename_axis(
            ['b', 'g', 'y', 's', 'i'], axis=0)
        ren_df_selected_us = ren_df_selected_us.rename_axis(
            ['value'], axis=1)
        
        # now repeat for each year
        for y in years:
            if y == years[0]:
                ren_df_all_years = ren_df_selected_us
            else:
                new_y_df = ren_df_selected_us.reset_index(
                    ['b', 'g', 'y', 's', 'i'])
                new_y_df['y'] = y
                new_y_df = new_y_df.set_index(
                    ['b', 'g', 'y', 's', 'i'])
        
                ren_df_all_years = pd.concat(
                    [ren_df_all_years, new_y_df])
        
        ren_df_all_years.index = pd.MultiIndex.from_frame(
            pd.DataFrame(index=ren_df_all_years.index)
            .reset_index(['b', 'g', 'y', 's', 'i']).astype(int))
        
        ren_df_all_years = ren_df_all_years.dropna()
        
        ren_df_all_years = ren_df_all_years.to_dict()[0]
        
        ren_df_all_years = self.round_params(ren_df_all_years)
        #print(ren_df_all_years)
        
        return ren_df_all_years
            
    def capex_par_adjust(self):
        '''

        For non-energy storage technologies, adjust capex data

        Returns
        -------
        capex_df_dict : Dictionary of capex data with correct indices
        '''
        capex_t_df = self.load_data[self.index('capex_tech')]
        years = self.years
        bus_tech_nums = self.load_data[self.index('gen')][[
            'Bus_num', 'Gen_num', 'Gen_name', 'Tech_Num']]
        capex_df = pd.DataFrame(
            columns=capex_t_df.columns[2:np.shape(capex_t_df)[1]])
        
        new_rows = []
        for g in range(len(bus_tech_nums)):
            gen = bus_tech_nums.iloc[g]
            tn = gen['Tech_Num']
            gen_n = gen['Gen_num']
         
            if gen_n not in self.tech_nums['storage'] and gen_n in self.tech_nums['candidates']:
                capex_arr = capex_t_df[capex_t_df['Tech_num'] == tn].drop(
                    ['Tech_num', 'Tech_name'], axis=1)
                if not capex_arr.empty:
                    # Create a new row with the index set to gen_n
                    capex_arr.index = [gen_n]
                    new_rows.append(capex_arr)
                #capex_arr.index = [gen_n]
                #capex_df = pd.concat([capex_df, capex_arr])
        
        if new_rows:
            capex_df = pd.DataFrame(pd.concat(new_rows))
            #print(new_rows)
            #print(capex_df)

        capex_df.columns = capex_df.columns.astype(int)
        capex_df_us = capex_df.unstack(level=0).rename_axis(
            ['y', 'g'], axis=0).reset_index(['g', 'y']).set_index(['g', 'y'])
        
        # filter out years not used
        capex_df_us = capex_df_us[capex_df_us.index.isin(
            list(years), level=1)]
        capex_df_dict = capex_df_us.to_dict()[0]
        #capex_df_dict = self.round_params(capex_df_dict)
        return capex_df_dict

    def capex_es_pwr_par_adjust(self):
        '''
        For energy storage technologies power rating cost

        Returns
        -------
        capex_es_pwr_df_dict : Dictionary of capex data with correct indices

        '''

        if self.es_cost == 'Base':
            #print('Base ES Cost')
            capex_es_df = self.load_data[self.index('capex_es')]
        elif self.es_cost == 'Low':
            #print('Low ES Cost')
            capex_es_df = self.load_data[self.index('capex_l_es')]
        elif self.es_cost == 'High':
            #print('High ES Cost')
            capex_es_df = self.load_data[self.index('capex_h_es')]
        else:
            print('Invalid cost trajectory')
            
        capex_es_df = capex_es_df[capex_es_df['Cost'] == 'Power']
        capex_es_df = capex_es_df.drop(['Cost'],axis=1)
        years = self.years
        bus_tech_nums = self.load_data[self.index('gen')][[
            'Bus_num', 'Gen_num', 'Gen_name', 'Tech_Num']]
        capex_df = pd.DataFrame(
            columns=capex_es_df.columns[2:np.shape(capex_es_df)[1]])
        new_rows = []
        for g in range(len(bus_tech_nums)):
            gen = bus_tech_nums.iloc[g]
            tn = gen['Tech_Num']
            gen_n = gen['Gen_num']
            
            if gen_n in self.tech_nums['storage'] and gen_n in self.tech_nums['candidates']:
                capex_arr = capex_es_df[capex_es_df['Tech_num'] == tn].drop(
                    ['Tech_num', 'Tech_name'], axis=1)
                if not capex_arr.empty:
                    # Create a new row with the index set to gen_n
                    capex_arr.index = [gen_n]
                    new_rows.append(capex_arr)
                             
                #capex_arr.index = [gen_n]
                #capex_df = pd.concat([capex_df, capex_arr])

        if new_rows:
            capex_df = pd.DataFrame(pd.concat(new_rows))
        
        capex_df.columns = capex_df.columns.astype(int)
        capex_df_us = capex_df.unstack(level=0).rename_axis(
            ['y', 'g'], axis=0).reset_index(['g', 'y']).set_index(['g', 'y'])

        capex_df_us = capex_df_us[capex_df_us.index.isin(
            list(years), level=1)]
        capex_es_pwr_df_dict = capex_df_us.to_dict()[0]
        #capex_es_pwr_df_dict = self.round_params(capex_es_pwr_df_dict)
        return capex_es_pwr_df_dict

    def capex_es_energy_par_adjust(self):
        '''
        For energy storage technologies energy rating cost

        Returns
        -------
        capex_es_energy_df_dict : Dictionary of capex data with correct indices

        '''
        capex_es_df = self.load_data[self.index('capex_es')]
        capex_es_df = capex_es_df[capex_es_df['Cost']
                                  == 'Energy']
        capex_es_df = capex_es_df.drop(['Cost'],axis=1)
        years = self.years
        bus_tech_nums = self.load_data[self.index('gen')][[
            'Bus_num', 'Gen_num', 'Gen_name', 'Tech_Num']]
        capex_df = pd.DataFrame(
            columns=capex_es_df.columns[2:np.shape(capex_es_df)[1]])
        new_rows = []
        for g in range(len(bus_tech_nums)):
            gen = bus_tech_nums.iloc[g]
            tn = gen['Tech_Num']
            gen_n = gen['Gen_num']
            if gen_n in self.tech_nums['storage'] and gen_n in self.tech_nums['candidates']:
                capex_arr = capex_es_df[capex_es_df['Tech_num'] == tn].drop(
                    ['Tech_num', 'Tech_name'], axis=1)
                if not capex_arr.empty:
                    # Create a new row with the index set to gen_n
                    capex_arr.index = [gen_n]
                    new_rows.append(capex_arr)
                #capex_arr.index = [gen_n]
                #capex_df = pd.concat([capex_df, capex_arr])
        if new_rows:
            capex_df = pd.DataFrame(pd.concat(new_rows))
        
        capex_df.columns = capex_df.columns.astype(int)
        capex_df_us = capex_df.unstack(level=0).rename_axis(
            ['y', 'g'], axis=0).reset_index(['g', 'y']).set_index(['g', 'y'])
        capex_df_us = capex_df_us[capex_df_us.index.isin(
            list(years), level=1)]
        capex_es_energy_df_dict = capex_df_us.to_dict()[0]
        #capex_es_energy_df_dict = self.round_params(capex_es_energy_df_dict)
        return capex_es_energy_df_dict

    def fp_par_adjust(self):
        '''
        Adjust fuel price data for model input

        Returns
        -------
        fuel_df_dict : Dictionary of fuel price data

        '''
        fuel_df = self.load_data[self.index('fuel')]
        years = self.years
        fuel_df = fuel_df.set_index('Gen_num').drop(['Gen_name', 'Bus', 'Tech'], axis=1)
        fuel_df.columns = fuel_df.columns.astype(int)
        fuel_df_us = fuel_df.unstack(level=0).rename_axis(
            ['y', 'g'], axis=0).reset_index(['g', 'y']).set_index(['g', 'y'])
        fuel_df_us = fuel_df_us[fuel_df_us.index.isin(
            list(years), level=1)]
        fuel_df_dict = fuel_df_us.to_dict()[0]
        #fuel_df_dict = self.round_params(fuel_df_dict)
        return fuel_df_dict


