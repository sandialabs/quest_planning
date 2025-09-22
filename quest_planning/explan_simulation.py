# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:06:12 2024

@author: cjnewlu
"""
import os.path
import yaml
import argparse
from quest_planning.explan.explan_data_handler import ExplanDataHandler
from quest_planning.explan.explan_optimizer import ExplanOptimizer
from quest_planning.explan.explan_results_viewer import ExplanResultsViewer


class Explan:
    def __init__(self, config):
        '''
        Initialize Explan class with configuration dictionary

        Parameters
        ----------
        config : dict
            Configuration dictionary containing all necessary parameters.
        '''
        self.config = config
        #Define data handler
        self.data_handler = ExplanDataHandler()
        # Define Optimizer
        self.optimizer = None
        # Define results viewer
        self.results = None

    def setup_data_handler(self):
        ''' Initiate and setup data_handler'''
        # Define the data_handler
        d = self.data_handler
        # set the config file
        config = self.config

        # Assign the configuration options to the data_handler
        d.set_data_ls_index(config['data_ls'])
        d.data_dir = config['data_dir']
        
        #Time Horizon and scenario configuration
        d.set_start_year(config['start_year'])
        d.set_end_year(config['end_year'])
        #d.set_year_gap(config['year_gap'])
        d.set_scenario(config['scenario'])
        d.set_tx_model(config['tx_model'])
        d.set_transmission_expansion(config['trans_expansion'])
        d.set_years_hours(config['years'])
        d.set_block_selection(config['block_selection'])
        d.set_load_growth(config['load_growth'])
        d.set_es_cost(config['es_cost'])
        d.set_ldes_switch(config['ldes_switch'])
        d.set_load_profile(config['load_forecast'])
        
        # Economic parameters
        d.set_discount_rate(config['discount_rate'])
        d.set_base_currency_year(config['base_curr_year'])
        d.set_end_effects(config['end_effects'])
        d.set_voll(config['voll'])
        d.set_tax_credit_end_year(config['tax_credit_end_year'])
            
        #Modeling options
        d.set_reserves_option(config['reserves_option'])
        d.set_tax_credits_option(config['tax_credits_option'])
        d.set_es_lifetime_cost_option(config['es_lifetime_cost_option'])
        d.set_solver(config['solver'])
        d.set_system_name(config['system'])
        d.set_mva_base(config['mva_base'])
        
        #System-wide resource limits
        d.set_system_wide_wind_max(config['system_wide_wind_max'])
        d.set_system_wide_solar_max(config['system_wide_solar_max'])
        d.set_system_wide_tx_expansion_max(config['system_wide_tx_expansion_max'])
        d.set_system_wide_gas_max(config['system_wide_gas_max'])
        
        #set reserve parameters
        d.set_reserve_params(config['prm'],config['reg_res_req'],config['spin_res_req'],config['flex_res_w_req'],config['flex_res_s_req'])
        
        #ES min and max SOC %
        d.set_es_soc_min_max(config['soc_min'],config['soc_max'],config['ini_level'])
        
        #Custom retirement schedule
        d.set_custom_retirement_years(config['custom_retirement'],
                                      config['ng_retirement_year'],
                                      config['coal_retirement_year'],
                                      config['nuclear_retirement_year'],
                                      config['oil_retirement_year'])
        #RPS policy flag
        d.set_rps_policy(config['rps_policy'])
        #Co2 policy flag
        d.set_co2_policy(config['co2_policy'])
        d.set_co2_intensity_policy(config['co2_intensity_policy'])
        
        d.set_es_lifetime_extension(config['es_lifetime_extension'])
        
        d.set_resource_bus_limits(config['limit_by_buses'])
        
    def load_data(self):
        self.data_handler.get_data()
    
    def construct_load_blocks(self):
        self.data_handler.construct_load_blocks()
        

    def run_optimizer(self):
        ''' Run the optimization model'''
        self.optimizer = ExplanOptimizer(
            self.data_handler, solver=self.config['solver'])
        self.var_dict, self.par_dict, self.timestamp = self.optimizer.run()

    def view_results(self):
        ''' Process and visualize results'''
        self.results = ExplanResultsViewer(self.data_handler)
        self.results.stacked_bar_by_bus_option = self.config['stacked_bar_by_bus']
        self.results.policy_plot_option = self.config['policy_plot_option']
        self.results.process_results(
            self.var_dict, self.par_dict, self.timestamp, self.optimizer.report)


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
    # Ensure the file path is relative to the current working directory
    if not os.path.isabs(yaml_file):
        yaml_file = os.path.join(os.getcwd(), yaml_file)

    with open(yaml_file, 'r') as f:
        return yaml.safe_load(f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Explan simulation with specified YAML configuration file.')
    parser.add_argument('yaml_file', type=str, help='Path to the input YAML file.')
    args = parser.parse_args()

    current_dir = os.getcwd()
    input_dict = read_input_yaml(args.yaml_file)

    data_file = os.path.join(current_dir, 'quest_planning','data_explan', input_dict['data_folder'])
    input_dict['data_dir'] = data_file
    input_dict['data_ls'] = ['bus','branch','capex_es','capex_l_es','capex_h_es','capex_tech','fuel','gen','gen_viz','load','scalars','solar','storage','tech','wind','policy','solar_cand','wind_cand']#'disfact',
    

    exp = Explan(input_dict)
    exp.setup_data_handler()
    exp.load_data()
    exp.construct_load_blocks()
    exp.run_optimizer()
    exp.view_results()
    
    
    
    
    
