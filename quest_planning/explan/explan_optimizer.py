# -*- coding: utf-8 -*-
"""
QuESt Planning - explan optimizer to set up the Pyomo model
Authors: C. Newlun and W. Olis
"""

from pyexpat import model

import pyomo.environ as pm
import numpy as np
import pandas as pd
import time
import pyutilib 
import logging
from pyomo.util.model_size import build_model_size_report
from quest_planning.explan.optimizer import Optimizer
from quest_planning.explan.explan_constraints import ExplanConstraints
from pyomo.opt import TerminationCondition
from pyomo.environ import value
from pyomo.common.timing import report_timing
import io
from typing import Dict, List


class ExplanOptimizer(Optimizer):
    
    def __init__(self, data_handler, **kwargs):
        super().__init__(kwargs['solver'])

        self.data_handler = data_handler
        self.var_index_labels = None
        self.par_index_labels = None
        self.index = None
        
    @property
    def solver(self):
        return self._solver
    
    @solver.setter
    def solver(self,value):
        self._solver = value
        

    def _set_model_param(self):
        """A method for assigning model parameters and their default values to the model."""
        model = self.model
        
        self.index = self.data_handler.data_ls.index
        
        BUS = self.data_handler.load_data[self.index('bus')]
        GEN = self.data_handler.load_data[self.index('gen')]
        BRANCH = self.data_handler.load_data[self.index('branch')]
        POLICY = self.data_handler.load_data[self.index('policy')]
        POLICY = POLICY.set_index('Years')
        STORAGE = self.data_handler.load_data[self.index('storage')]
        discount_rate = self.data_handler.discount_rate/100#float(self.data_handler.scalars.loc['Discount Rate']['Value'])/100
        base_currency_year = self.data_handler.base_currency_year
        #TODO:replace with calculation below..
        #disc_fact = self.data_handler.load_data[self.index('disfact')].set_index(
            #'year')
        tech_nums = self.data_handler.tech_nums
        
        # Build generator-year capacity credit dictionary
        gen_tech = GEN[['Gen_num', 'Tech_Num']].copy()
        gen_tech['Gen_num'] = gen_tech['Gen_num'].astype(int)
        gen_tech['Tech_Num'] = gen_tech['Tech_Num'].astype(int)
        
        if bool(getattr(self.data_handler, 'varying_CC_mode', None)):      
            CAPCRED = self.data_handler.load_data[self.index('cap_cred')]
            capcred = CAPCRED[['Tech_Num', 'Year', 'Cap_Cred']].copy()
            capcred['Tech_Num'] = capcred['Tech_Num'].astype(int)
            capcred['Year'] = capcred['Year'].astype(int)

            gen_cc_df = gen_tech.merge(capcred, on='Tech_Num', how='left')
            gen_cc_dict = gen_cc_df.set_index(['Gen_num', 'Year'])['Cap_Cred'].to_dict()
        else:
            gen_cc_df = GEN[['Gen_num', 'CapCred']].copy()
            gen_cc_df['Gen_num'] = gen_cc_df['Gen_num'].astype(int)

            years = self.data_handler.years  # replace with your actual modeled years

            gen_cc_df = (gen_cc_df.merge(pd.DataFrame({'Year': years}), how='cross'))

            gen_cc_dict = (gen_cc_df.set_index(['Gen_num', 'Year'])['CapCred'].to_dict())

        # Old
        # peak = self.data_handler.find_system_peak()
        # energy = self.data_handler.find_system_energy()
        # load_dict = self.data_handler.load_par_adjust()
        

        # To include regional load growth
        use_regional = bool(getattr(self.data_handler, 'regional_load_growth', None))
        
        if use_regional:
            # regional blocks → per-bus dict
            load_dict = self.data_handler.load_par_adjust_regional()

            # regional peaks/energies (DataFrames: cols = regions)
            reg_peak   = self.data_handler.find_regional_peak()
            reg_energy = self.data_handler.find_regional_energy()

            # make system-wide equivalents by summing across regions (REGIONAL PATH ONLY)
            years = [int(y) for y in self.data_handler.years]
            col   = str(self.data_handler.load_forecast)

            peak_sum   = reg_peak.sum(axis=1)   # Series indexed by year
            energy_sum = reg_energy.sum(axis=1)

            # normalize index dtype and order to exactly match model.Y
            peak_sum.index   = peak_sum.index.astype(int)
            energy_sum.index = energy_sum.index.astype(int)

            peak   = peak_sum.reindex(years).astype(float).to_frame(col)
            energy = energy_sum.reindex(years).astype(float).to_frame(col)

            # (optional) keep regionals to use later
            #self.data_handler.regional_peak_df   = reg_peak
            #self.data_handler.regional_energy_df = reg_energy
        else:
            load_dict = self.data_handler.load_par_adjust()
            peak   = self.data_handler.find_system_peak()  
            energy = self.data_handler.find_system_energy()
        
        solar_ex_dict = self.data_handler.ren_profile_par_adj('upv_ex')
        wind_ex_dict = self.data_handler.ren_profile_par_adj('wind_ex')
        solar_can_dict = self.data_handler.ren_profile_par_adj('upv_can')
        wind_can_dict = self.data_handler.ren_profile_par_adj('wind_can')
        par_index_labels = {}
        if self.data_handler.large_load_option:

            ll_load_dict = self.data_handler.load_dict_ll

            model.large_load = pm.Param(
                model.B,
                model.Y,
                model.S_I,
                initialize=ll_load_dict,
                default=0
            )

            par_index_labels['large_load'] = [
                'b','y','s','i'
            ]

        C_g_dict = self.data_handler.capex_par_adjust()

        C_g_es_pwr_dict = self.data_handler.capex_es_pwr_par_adjust()

        C_g_es_energy_dict = self.data_handler.capex_es_energy_par_adjust()

        G_fp_dict = self.data_handler.fp_par_adjust()

        

        #print("Set up parameters")
        '''
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        3.) Parameters
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        '''
        #Load
        model.load_full = pm.Param(
            model.B, model.Y, model.S_I, initialize=load_dict)
        par_index_labels['load_full'] = ['b', 'y', 's', 'i']
        #Existing solar
        model.solar_ex = pm.Param(model.B, model.G, model.Y, model.S_I,
                                  initialize=solar_ex_dict)  
        par_index_labels['solar_ex'] = [
            'b', 'g', 'y', 's', 'i']
        #Existing wind
        model.wind_ex = pm.Param(
            model.B, model.G, model.Y, model.S_I, initialize=wind_ex_dict)
        par_index_labels['wind_ex'] = [
            'b', 'g', 'y', 's', 'i']

        # Candidate renewable profiles
        model.solar_can_cf = pm.Param(model.B, model.G, model.Y,
                                      model.S_I, initialize=solar_can_dict)
        par_index_labels['solar_can_cf'] = [
            'b', 'g', 'y', 's', 'i']
        
        model.wind_can_cf = pm.Param(model.B, model.G, model.Y,
                                     model.S_I, initialize=wind_can_dict)
        par_index_labels['wind_can_cf'] = [
            'b', 'g', 'y', 's', 'i']

        #Transmission params
        # Vectorized: one set_index then cheap column .to_dict() calls.
        # Replaces 7 separate iterrows() passes over BRANCH.
        _branch = BRANCH.set_index('Line_Number')
        line_X_dict       = _branch['X'].to_dict()
        line_fw_dict      = _branch['Rating_F'].to_dict()
        line_bw_dict      = _branch['Rating_B'].to_dict()
        line_cost_dict    = _branch['Tx_cost'].to_dict()
        line_limit_dict   = _branch['Tx_limit'].to_dict()
        line_lt_dict      = _branch['Lead_Time'].to_dict()
        line_from_dict    = _branch['From_Bus_Number'].to_dict()
        line_to_dict      = _branch['To_Bus_Number'].to_dict()
        #Region definitions (new by GCP)
        model.R = pm.Set(initialize=list(BUS['Region'].dropna().unique()))
        bus_region_dict = BUS.set_index('Bus_number')['Region'].to_dict()
        model.bus_region = pm.Param(model.B, initialize=bus_region_dict)
        par_index_labels['bus_region'] = ['b']

        # turn off market sharing for specific scenario - Not used now..
        if self.data_handler.scenario == 'No Market Share':
            BRANCH['Rating_F'][1] = self.data_handler.market_share_max
            BRANCH['Rating_B'][1] = self.data_handler.market_share_max
        
        def line_ex_imp_init(model, l):
            x_raw = line_X_dict[l]
            x_min = 0.0005
            if x_raw < x_min:
                print(f"Warning: line {l} X={x_raw:.4f} p.u. clipped to {x_min} p.u.")
            return max(x_raw, x_min)
        
        model.line_X = pm.Param(model.L, initialize=line_ex_imp_init)
        par_index_labels['line_X'] = ['l']

        scale_factor = 1.0  # double all line ratings temporarily
        #model.line_ex_fw_cap[l] *= scale_factor
        #model.line_ex_bw_cap[l] *= scale_factor
        def line_ex_fw_cap_init(model, l):
            return line_fw_dict[l]*scale_factor

        model.line_ex_fw_cap = pm.Param(model.L, initialize=line_ex_fw_cap_init)
        par_index_labels['line_ex_fw_cap'] = ['l']

        def line_ex_bw_cap_init(model, l):
            return line_bw_dict[l]*scale_factor

        model.line_ex_bw_cap = pm.Param(model.L, initialize=line_ex_bw_cap_init)
        par_index_labels['line_ex_bw_cap'] = ['l']
        
        

        # line_cost_dict already built above; use it directly to avoid the
        # positional-index bug (BRANCH['Tx_cost'].values[l-1] assumed 1-indexed
        # sequential Line_Numbers, which breaks for non-contiguous numbering).
        model.line_cost = pm.Param(
            model.L, initialize=line_cost_dict)
        par_index_labels['line_cost'] = ['l']

        def line_ex_limit_init(model, l):
            return line_limit_dict[l]

        model.line_ex_limit = pm.Param(model.L, initialize=line_ex_limit_init)
        par_index_labels['line_ex_limit'] = ['l']

        def line_lt_init(model, l):
            return line_lt_dict[l]

        model.line_lt = pm.Param(model.L, initialize=line_lt_init)
        par_index_labels['line_lt'] = ['l']

        # Precompute from/to buses as Params
        model.from_bus = pm.Param(model.L, initialize=line_from_dict)
        model.to_bus = pm.Param(model.L, initialize=line_to_dict)
        
        '''
        print("\n=== Line parameters check ===")
        for l in model.L:
            print(f"Line {l}: X={value(model.line_X[l]):.4f}, "
                f"PF_fw={value(model.line_ex_fw_cap[l]):.1f}, "
                f"PF_bw={value(model.line_ex_bw_cap[l]):.1f}, "
                f"Cost={value(model.line_cost[l])}, "
                f"Limit={value(model.line_ex_limit[l])}, "
                f"LeadTime={value(model.line_lt[l])}, "
                f"From={value(model.from_bus[l])}, To={value(model.to_bus[l])}")
        '''
        if self.data_handler.large_load_option:

            ll_data = self.data_handler.processed_ll

            ll_ids = [ll["id"] for ll in ll_data]

            model.LL = pm.Set(
                initialize=ll_ids
            )
            
            ll_ng_df = GEN.loc[
                GEN['Tech'] == 'Gas_LL_Cand'
            ]
            

            model.G_LL_NG = pm.Set(
                initialize=list(ll_ng_df['Gen_num'].values)
            )

            ll_bess_df = GEN.loc[
                GEN['Tech'] == 'Li_Ion_Cand_LL_Cand'
            ]

            model.G_LL_BESS = pm.Set(
                initialize=list(ll_bess_df['Gen_num'].values)
            )

            ll_bus_dict = {
                ll["id"]: ll["bus"]
                for ll in ll_data
            }

            model.LL_bus = pm.Param(
                model.LL,
                initialize=ll_bus_dict
            )


            ll_deploy_dict = {
                ll["id"]: ll["deploy_year"]
                for ll in ll_data
            }

            model.LL_deploy_year = pm.Param(
                model.LL,
                initialize=ll_deploy_dict
            )
            model.LL_NG_Max = pm.Param(
                model.LL,
                initialize={
                    ll["id"]: ll["ng_max_capacity_mw"]
                    for ll in ll_data
                },
                default=0
            )

            model.LL_BESS_Power_Max = pm.Param(
                model.LL,
                initialize={
                    ll["id"]: ll["bess_max_power_mw"]
                    for ll in ll_data
                },
                default=0
            )

            model.LL_BESS_Energy_Max = pm.Param(
                model.LL,
                initialize={
                    ll["id"]: ll["bess_max_energy_mwh"]
                    for ll in ll_data
                },
                default=0
            )
            par_index_labels["LL_bus"] = ["ll"]
            
            par_index_labels["LL_deploy_year"] = ["ll"]

            par_index_labels["LL_NG_Max"] = ["ll"]

            par_index_labels["LL_BESS_Power_Max"] = ["ll"]

            par_index_labels["LL_BESS_Energy_Max"] = ["ll"]


        #RPS policy
        rps = POLICY['RPS'].filter(items=self.data_handler.years, axis=0)
        rps = rps.to_dict()
        model.RPS = pm.Param(model.Y, initialize=rps)
        par_index_labels['RPS'] = ['y']

        # CO2 policy
        co2 = POLICY['CO2'].filter(items=self.data_handler.years, axis=0)
        co2 = co2.to_dict()
        model.CO2 = pm.Param(model.Y, initialize=co2)
        par_index_labels['CO2'] = ['y']
        # CO2 intensity policy 
        co2_int = POLICY['CO2_intensity'].filter(
            items=self.data_handler.years, axis=0)
        co2_int = co2_int.to_dict()
        model.CO2_int = pm.Param(
            model.Y, initialize=co2_int)
        par_index_labels['CO2_int'] = ['y']

        # ------------------------------------------------------------------
        # Pre-compute all generator scalar parameter dicts in one pass.
        # Previously each param used a callback that rebuilt the full GEN
        # DataFrame (set_index + map int + to_dict) on every element call,
        # resulting in ~9 500 redundant DataFrame operations for 500 generators.
        # Now: one set_index, then one cheap .to_dict() per column.
        # Note: gen_lt_dict_gen is named to avoid shadowing line_lt_dict.
        # ------------------------------------------------------------------
        _gen = GEN.set_index('Gen_num')
        _gen.index = _gen.index.astype(int)

        gen_co2_dict        = _gen['CO2'].to_dict()
        p_cap_dict          = _gen['Cap'].to_dict()
        p_cap_min_dict      = _gen['MinCap'].to_dict()
        cand_cap_dict       = _gen['CandCap'].to_dict()
        syst_cap_dict       = _gen['SystCap'].to_dict()
        gen_ret_yr_dict     = _gen['RetYr'].to_dict()
        gen_planned_yr_dict = _gen['PlannedYr'].to_dict()
        gen_ret_cap_dict    = _gen['RetCap'].to_dict()
        gen_fom_dict        = _gen['FOM'].to_dict()
        gen_vom_dict        = _gen['VOM'].to_dict()
        gen_tx_add_dict     = _gen['TransAdder'].to_dict()
        gen_ptc_dict        = _gen['PTC'].to_dict()
        gen_itc_dict        = _gen['ITC'].to_dict()
        gen_hr_dict         = _gen['HR'].to_dict()
        gen_for_dict        = _gen['FOR'].to_dict()
        gen_lt_dict_gen     = _gen['LeadTime'].to_dict()
        gen_ramp_dict       = _gen['Ramp'].to_dict()
        gen_lifetime_dict   = _gen['Lifetime'].to_dict()
        gen_y_avail_dict    = _gen['YearAvail'].to_dict()

        #Check on this...ensure accuracy
        model.gen_CO2 = pm.Param(
            model.G, initialize=gen_co2_dict)
        par_index_labels['gen_CO2'] = ['g']
        
        # Discount factor with end effects 
        def discount_factor_end_eff_init(model, y):
            money_years = np.arange(base_currency_year,self.data_handler.years[-1]+1)
            if self.data_handler.block_selection.lower() == 'Full_Year'.lower():
                df_array = {self.data_handler.years[0]: 1}
            else:
                #df_array = {self.data_handler.years[n]: 1/((1+discount_rate) ** (n))
                  #          for n in np.arange(0, np.size(self.data_handler.years)-1)}
                df_array = {money_years[n]: 1/((1+discount_rate) ** (n))
                            for n in np.arange(0, np.size(money_years)-1)}
                df_array[money_years[-1]] = (sum(1/((1+discount_rate) ** (n))
                                                for n in np.arange(np.size(money_years), np.size(money_years)+float(self.data_handler.end_effects))))
            #self.data_handler.scalars.loc['end_effects']['Value']
            return df_array[y]
        
            # elif y == np.size(all_years):  # end effects
        '''    
        df_ee = disc_fact['df_ee'].filter(
            items=self.data_handler.years, axis=0)
        df_ee_array = df_ee.to_dict()
        '''
        model.dis_factor_end_eff = pm.Param(
            model.Y, initialize=discount_factor_end_eff_init)
        par_index_labels['dis_factor_end_eff'] = ['y']

        # Discount factor without end effects TODO: fix the calculation and disregard csv
        def discount_factor_init(model, y):
            money_years = np.arange(base_currency_year,self.data_handler.years[-1]+1)
            if self.data_handler.block_selection.lower() == 'Full_Year'.lower():
                df_array = {self.data_handler.years[0]: 1}
            else:
                df_array = {money_years[n]: 1/((1+discount_rate) ** (n))
                            for n in np.arange(0, np.size(money_years))}
            return df_array[y]

        '''
        df = disc_fact['df'].filter(
            items=self.data_handler.years, axis=0)
        df_array = df.to_dict()
        '''

        model.dis_factor = pm.Param(
            model.Y, initialize=discount_factor_init)
        par_index_labels['dis_factor'] = ['y']
        
        # Existing resource capacity
        model.P_cap = pm.Param(
            model.G, initialize=p_cap_dict)
        par_index_labels['P_cap'] = ['g']
        
        # Existing resource minimum stable level capacity
        model.P_cap_min = pm.Param(
            model.G, initialize=p_cap_min_dict)
        par_index_labels['P_cap_min'] = ['g']
        
        # Candidate resources candidate capacities per year
        model.P_cap_cand = pm.Param(
            model.G, initialize=cand_cap_dict)
        par_index_labels['P_cap_cand'] = ['g']
        
        # Candidate resources candidate capacities max per simulation (whole planning horizon)
        model.P_cap_syst_max = pm.Param(
            model.G, initialize=syst_cap_dict)
        par_index_labels['P_cap_syst_max'] = ['g']
        
        #Resource bus limits
        '''
        if self.data_handler.resource_bus_limit_dict is not None:
            d = self.data_handler.resource_bus_limit_dict
            
            solar_dict = {}
            wind_dict = {}
            storage_dict = {}
            if d is not None:
                for item in d:
                    b = item['bus_num']
                    solar_dict[b] = item['solar']
                    wind_dict[b] = item['wind']
                    storage_dict[b] = item['storage']
            
            model.solar_max = pm.Param(model.B,initialize = solar_dict)
            model.wind_max = pm.Param(model.B,initialize = wind_dict)
            model.storage_max = pm.Param(model.B,initialize = storage_dict)
            par_index_labels['solar_max'] = ['b']
            par_index_labels['wind_max'] = ['b']
            par_index_labels['storage_max'] = ['b']
        else:
            pass
        '''
        if self.data_handler.resource_bus_limit_dict is not None:
            d = self.data_handler.resource_bus_limit_dict
            
            solar_dict = {}
            wind_dict = {}
            storage_dict = {}
            gas_dict={}
            if d is not None:
                for item in d:
                    solar_dict = item['solar']
                    wind_dict = item['wind']
                    storage_dict = item['storage']
                    gas_dict = item['gas']
            
            model.solar_max = pm.Param(model.B,initialize = solar_dict)
            model.wind_max = pm.Param(model.B,initialize = wind_dict)
            model.storage_max = pm.Param(model.B,initialize = storage_dict)
            model.gas_max = pm.Param(model.B,initialize = gas_dict)
            par_index_labels['solar_max'] = ['b']
            par_index_labels['wind_max'] = ['b']
            par_index_labels['storage_max'] = ['b']
            par_index_labels['gas_max'] = ['b']
        else:
            pass
        
        # Retirement years of generators - user input
        model.gen_ret_yr = pm.Param(
            model.G, initialize=gen_ret_yr_dict)
        par_index_labels['gen_ret_yr'] = ['g']
        
        # Planned years of candidate generators availability
        model.gen_planned_yr = pm.Param(
            model.G, initialize=gen_planned_yr_dict)
        par_index_labels['gen_planned_yr'] = ['g']

        # Retirement capacity of generators that are being retired
        model.gen_ret_cap = pm.Param(
            model.G, initialize=gen_ret_cap_dict)
        par_index_labels['gen_ret_cap'] = ['g']

        # FOM costs of generator
        model.G_fom = pm.Param(
            model.G, initialize=gen_fom_dict)
        par_index_labels['G_fom'] = ['g']

        # VOM costs of generator
        model.G_vom = pm.Param(
            model.G, initialize=gen_vom_dict)
        par_index_labels['G_vom'] = ['g']

        # Trans Adders - additional cost for transmission interconnection (if applicable)
        model.G_tx_add = pm.Param(
            model.G, initialize=gen_tx_add_dict)
        par_index_labels['G_tx_add'] = ['g']

        # Production Tax credit (if applicable)
        model.G_ptc = pm.Param(
            model.G, initialize=gen_ptc_dict)
        par_index_labels['G_ptc'] = ['g']

        # Investment Tax credit (if applicable)
        model.G_itc = pm.Param(
            model.G, initialize=gen_itc_dict)
        par_index_labels['G_itc'] = ['g']

        # Maximum heat rate of generator
        model.G_hr = pm.Param(
            model.G, initialize=gen_hr_dict)
        par_index_labels['G_hr'] = ['g']

        # Capacity credit of generator (Old version)
        # def gen_cc_init(model, g):
        #     cc = GEN[['Gen_num', 'CapCred']
        #              ].set_index('Gen_num')
        #     cc.index = cc.index.map(
        #         int)  # .index.astype(str)
        #     cc = cc.to_dict()['CapCred']
        #     return cc[g]
        # model.G_cc = pm.Param(
        #     model.G, initialize=gen_cc_init)
        # par_index_labels['G_cc'] = ['g']

        # New capacity credit based on generator technology and year - from separate csv by GCP
        def gen_cc_init(model, g, y):
            return gen_cc_dict[(g, y)]

        model.G_cc = pm.Param(model.G, model.Y, initialize=gen_cc_init)
        par_index_labels['G_cc'] = ['g', 'y']

        # Dynamic ELCC - TODO

        # Forced outage rate of generator; TODO: incorporate in model
        model.G_for = pm.Param(
            model.G, initialize=gen_for_dict)
        par_index_labels['G_for'] = ['g']

        # Lead times for generation investment; TODO: incorporate in the model
        model.G_lt = pm.Param(
            model.G, initialize=gen_lt_dict_gen)
        par_index_labels['G_lt'] = ['g']

        # Generator ramp rates %/min; TODO: check units
        model.G_ramp = pm.Param(
            model.G, initialize=gen_ramp_dict)
        par_index_labels['G_ramp'] = ['g']

        # Generator lifetime (y); TODO: add automatic retirements
        model.G_lifetime = pm.Param(
            model.G, initialize=gen_lifetime_dict)
        par_index_labels['G_lifetime'] = ['g']

        # Year technology is available to be invested
        model.G_y_avail = pm.Param(
            model.G, initialize=gen_y_avail_dict)
        par_index_labels['G_y_avail'] = ['g']
        
        # Old - Annual peak demand of system
        # peak_dict = peak[self.data_handler.load_forecast].filter(
        #     items=self.data_handler.years, axis=0).to_dict()
        # model.PEAK = pm.Param(model.Y, initialize=peak_dict)
        # par_index_labels['PEAK'] = ['y']

        # # Old - Annual energy consumption of system
        # energy_dict = energy[self.data_handler.load_forecast].filter(
        #     items=self.data_handler.years, axis=0).to_dict()
        # model.ENERGY = pm.Param(
        #     model.Y, initialize=energy_dict)
        # par_index_labels['ENERGY'] = ['y']

        # Build PEAK / ENERGY dicts and create Params (by GCP)
        years = [int(y) for y in self.data_handler.years]

        if use_regional:
            # REGIONAL: sum across region columns -> Series indexed by year
            rp = reg_peak.copy()
            re = reg_energy.copy()
            rp.index = rp.index.astype(int)
            re.index = re.index.astype(int)
            rp = rp.reindex(years).fillna(0.0)
            re = re.reindex(years).fillna(0.0)

            peak_sum   = rp.sum(axis=1) 
            energy_sum = re.sum(axis=1)  

            # Explicit dicts for Pyomo
            peak_dict   = {y: float(peak_sum.loc[y])   for y in years}
            energy_dict = {y: float(energy_sum.loc[y]) for y in years}

            # Regional peak parameter
            peak_reg_dict = {
                (r, y): float(rp.loc[y, r])
                for y in years
                for r in rp.columns
            }

            def peak_reg_init(model, r, y):
                return peak_reg_dict[(r, y)]

            model.PEAK_REG = pm.Param(model.R, model.Y, initialize=peak_reg_init)
            par_index_labels['PEAK_REG'] = ['r', 'y']

            model.PEAK   = pm.Param(model.Y, initialize=peak_dict)
            model.ENERGY = pm.Param(model.Y, initialize=energy_dict)

            # Regional PRM parameter
            PRM = self.data_handler.load_data[self.index('prm')].copy()
            PRM['Region'] = PRM['Region'].astype(int)
            PRM['Year'] = PRM['Year'].astype(int)
            PRM['PRM'] = PRM['PRM'].astype(float) / 100.0

            prm_dict = PRM.set_index(['Region', 'Year'])['PRM'].to_dict()

            def prm_init(model, r, y):
                return prm_dict[(r, y)]

            model.PRM = pm.Param(model.R, model.Y, initialize=prm_init)
            par_index_labels['PRM'] = ['r', 'y']

        else:
            # SYSTEM-WIDE: keep prior behavior (unchanged)
            peak_dict = peak[self.data_handler.load_forecast].filter(
                items=self.data_handler.years, axis=0).to_dict()
            model.PEAK = pm.Param(model.Y, initialize=peak_dict)

            energy_dict = energy[self.data_handler.load_forecast].filter(
                items=self.data_handler.years, axis=0).to_dict()
            model.ENERGY = pm.Param(model.Y, initialize=energy_dict)

        # Register labels so post-processing doesn’t KeyError
        par_index_labels["PEAK"]   = ["y"]
        par_index_labels["ENERGY"] = ["y"]



        #Round trip efficiency of ES technologies
        def es_rt_eff_init(model, g):
            if g in tech_nums['storage']:
                rte_eff = STORAGE[['Gen_num', 'RTE']].set_index(
                    'Gen_num')
                rte_eff.index = rte_eff.index.map(
                    int)  # .index.astype(str)
                rte_eff = rte_eff.to_dict()['RTE']
                return rte_eff[g]

        rte_eff = STORAGE[['Gen_num', 'RTE']].set_index(
            'Gen_num')
        rte_eff.index = rte_eff.index.map(
            int)
        rte_eff = rte_eff.to_dict()['RTE']
        model.rte_eff = pm.Param(
            model.G, initialize=rte_eff)
        par_index_labels['rte_eff'] = ['g']
        #Charging efficiency of ES technologies
        def es_cha_eff_init(model, g):
            if g in tech_nums['storage']:
                cha_eff = STORAGE[['Gen_num', 'Charge_Eff']].set_index(
                    'Gen_num')
                cha_eff.index = cha_eff.index.map(
                    int)  # .index.astype(str)
                cha_eff = cha_eff.to_dict()['Charge_Eff']
                return cha_eff[g]

        cha_eff = STORAGE[['Gen_num', 'Charge_Eff']
                          ].set_index('Gen_num')
        cha_eff.index = cha_eff.index.map(
            int)
        cha_eff = cha_eff.to_dict()['Charge_Eff']
        model.cha_eff = pm.Param(
            model.G, initialize=cha_eff)
        par_index_labels['cha_eff'] = ['g']
        #Discharge efficiency of ES technologies
        def es_dis_eff_init(model, g):
            if g in tech_nums['storage']:
                dis_eff = STORAGE[['Gen_num', 'Discharge_Eff']].set_index(
                    'Gen_num')
                dis_eff.index = dis_eff.index.map(
                    int)  # .index.astype(str)
                dis_eff = dis_eff.to_dict()['Discharge_Eff']
                return dis_eff[g]

        dis_eff = STORAGE[['Gen_num', 'Discharge_Eff']].set_index(
            'Gen_num')
        dis_eff.index = dis_eff.index.map(
            int)  # .index.astype(str)
        dis_eff = dis_eff.to_dict()['Discharge_Eff']
        model.dis_eff = pm.Param(
            model.G, initialize=dis_eff)
        par_index_labels['dis_eff'] = ['g']
        #Duration of ES technologies
        def es_duration_init(model, g):
            if g in tech_nums['storage']:
                es_duration = STORAGE[['Gen_num', 'Duration']].set_index(
                    'Gen_num')
                es_duration.index = es_duration.index.map(
                    int)  # .index.astype(str)
                es_duration = es_duration.to_dict()[
                    'Duration']
                return es_duration[g]

        es_duration = STORAGE[['Gen_num', 'Duration']].set_index(
            'Gen_num')
        es_duration.index = es_duration.index.map(
            int)  
        es_duration = es_duration.to_dict()['Duration']
        model.es_duration = pm.Param(
            model.G, initialize=es_duration)
        par_index_labels['es_duration'] = ['g']

        #Minimum duration of ES candidate technologies
        es_min_duration = STORAGE[['Gen_num', 'Min_Duration']].set_index(
            'Gen_num')
        es_min_duration.index = es_min_duration.index.map(
            int)  # .index.astype(str)
        es_min_duration = es_min_duration.to_dict()[
            'Min_Duration']
        model.es_min_duration = pm.Param(
            model.G, initialize=es_min_duration)
        par_index_labels['es_min_duration'] = ['g']
        #Maximum duration of ES candidate technologies
        es_max_duration = STORAGE[['Gen_num', 'Max_Duration']].set_index(
            'Gen_num')
        es_max_duration.index = es_max_duration.index.map(
            int) 
        es_max_duration = es_max_duration.to_dict()[
            'Max_Duration']
        model.es_max_duration = pm.Param(
            model.G, initialize=es_max_duration)
        par_index_labels['es_max_duration'] = ['g']

        # CAPEX

        model.C_g = pm.Param(
            model.G, model.Y, initialize=C_g_dict)
        par_index_labels['C_g'] = ['g', 'y']

        model.C_g_es_pwr = pm.Param(
            model.G, model.Y, initialize=C_g_es_pwr_dict)
        par_index_labels['C_g_es_pwr'] = ['g', 'y']

        model.C_g_es_energy = pm.Param(
            model.G, model.Y, initialize=C_g_es_energy_dict)
        par_index_labels['C_g_es_energy'] = ['g', 'y']

        # FUEL Price

        model.G_fp = pm.Param(
            model.G, model.Y, initialize=G_fp_dict)
        par_index_labels['G_fp'] = ['g', 'y']
        
        if self.data_handler.block_selection.lower() == 'Peak_Day'.lower():
            hour_duration_dict = 365
        else:
            hour_duration_dict = dict(
                zip(np.arange(1, self.data_handler.S+1), self.data_handler.hour_duration))
        model.hour_weight = pm.Param(
            model.S, initialize=hour_duration_dict)
        par_index_labels['hour_weight'] = ['s']
        # Weight of each time step based on load blocks selection
        model.season_time_weight = pm.Param(
            model.S,model.I, initialize=self.data_handler.season_time_duration)
        par_index_labels['season_time_weight'] = ['s','i']
        # Year gap - based on user input
        #print(self.data_handler.years)
        #print(self.data_handler.year_gap_array)
        model.year_gap_array = pm.Param(
            model.Y, initialize=dict(zip(self.data_handler.years, self.data_handler.year_gap_array)))
        par_index_labels['year_gap_array'] = ['y']

        # Grab branch data once
        branch_df = self.data_handler.load_data[self.index('branch')]

        # Create mapping dicts (line index -> bus number)
        from_bus_map = {l+1: branch_df.loc[l, 'From_Bus_Number'] for l in branch_df.index}
        to_bus_map   = {l+1: branch_df.loc[l, 'To_Bus_Number']   for l in branch_df.index}

        model.from_bus = pm.Param(model.L, initialize=from_bus_map)
        par_index_labels['from_bus'] = ['y']
        model.to_bus   = pm.Param(model.L, initialize=to_bus_map)
        par_index_labels['to_bus'] = ['y']

        model.CostScale = pm.Param(initialize=1e-6)
        par_index_labels['CostScale'] = ['i']

        model.LL_Curt_MaxFrac = pm.Param(
            initialize=0.25,
            mutable=True
        )
        par_index_labels['LL_Curt_MaxFrac'] = ['i']

        model.ll_self_sufficiency = pm.Param(
            initialize=self.data_handler.ll_self_sufficiency,
            mutable=True
        )
        par_index_labels['ll_self_sufficiency'] = ['i']

        self.par_index_labels = par_index_labels


    def add_large_loads_to_model(self, model):

        ll_data = self.data_handler.processed_ll

        ll_ids = [ll["id"] for ll in ll_data]

        model.LL = pm.Set(
            initialize=ll_ids
        )

        self.par_index_labels["LL"] = ["ll"]

        ll_bus_dict = {
            ll["id"]: ll["bus"]
            for ll in ll_data
        }

        model.LL_bus = pm.Param(
            model.LL,
            initialize=ll_bus_dict
        )

        self.par_index_labels["LL_bus"] = ["ll"]

        ll_deploy_dict = {
            ll["id"]: ll["deploy_year"]
            for ll in ll_data
        }

        model.LL_deploy_year = pm.Param(
            model.LL,
            initialize=ll_deploy_dict
        )

        self.par_index_labels["LL_deploy_year"] = ["ll"]

        ll_load_dict = self.data_handler.load_dict_ll

        model.large_load = pm.Param(
            model.B,
            model.Y,
            model.S_I,
            initialize=ll_load_dict,
            default=0
        )
       

        self.par_index_labels["large_load"] = [
            "b",
            "y",
            "s",
            "i"
        ]

        model.large_load_net = pm.Var(
            model.B_LL,
            model.Y,
            model.S_I,
            domain=pm.Reals
        )

        self.var_index_labels["large_load_net"] = [
            "b",
            "y",
            "s",
            "i"
        ]

        model.LL_Curt = pm.Var(
            model.B_LL,
            model.Y,
            model.S_I,
            domain=pm.NonNegativeReals
        )
        self.var_index_labels['LL_Curt'] = ['b','y','s','i']

        ll_bess_power = {
                ll["id"]: ll["bess_max_power_mw"]
                for ll in ll_data
            }

        ll_bess_energy = {
            ll["id"]: ll["bess_max_energy_mwh"]
            for ll in ll_data
        }

        model.LL_BESS_Power_Max = pm.Param(
            model.LL,
            initialize=ll_bess_power,
            default=0
        )

        model.LL_BESS_Energy_Max = pm.Param(
            model.LL,
            initialize=ll_bess_energy,
            default=0
        )
        

        

    def _set_model_var(self):
        """A method for initializing model decision variables for the model."""
        #print("Set up variables")
        model = self.model
        var_index_labels = {}
        # annual generation investment var
        model.G_inv = pm.Var(model.B_G_can, model.Y,
                             domain=pm.NonNegativeReals)
        var_index_labels['G_inv'] = ['b', 'g', 'y']
        model.Sto_inv = pm.Var(model.B_G_sto_cand, model.Y,
                               domain=pm.NonNegativeReals)
        var_index_labels['Sto_inv'] = ['b', 'g', 'y']
        # cumulative generation investment var
        # model.G_inv_total = Var(model.B, model.G, model.Y, domain=NonNegativeReals)

        # Total capacity existing + invested
        model.P_cap_total = pm.Var(
            model.B_G, model.Y, domain=pm.NonNegativeReals)
        var_index_labels['P_cap_total'] = ['b', 'g', 'y']
        # Operational variables
        '''
        def gen_filter(model,b,g):
            if(b,g) is in list():
            return
        '''

        # Generation Dispatch
        model.P_gen = pm.Var(model.B_G, model.Y,
                             model.S_I, domain=pm.NonNegativeReals)
        var_index_labels['P_gen'] = [
            'b', 'g', 'y', 's', 'i']

        model.P_Reg = pm.Var(model.B_G, model.Y,
                             model.S_I, domain=pm.NonNegativeReals)
        var_index_labels['P_Reg'] = [
            'b', 'g', 'y', 's', 'i']

        model.P_Spin = pm.Var(model.B_G, model.Y,
                              model.S_I, domain=pm.NonNegativeReals)
        var_index_labels['P_Spin'] = [
            'b', 'g', 'y', 's', 'i']

        model.P_Flex = pm.Var(model.B_G, model.Y,
                              model.S_I, domain=pm.NonNegativeReals)
        var_index_labels['P_Flex'] = [
            'b', 'g', 'y', 's', 'i']

        model.CO2_emission = pm.Var(model.B_G,
                                    model.Y, domain=pm.NonNegativeReals)
        var_index_labels['CO2_emission'] = ['b', 'g', 'y']

        model.CO2_intensity = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['CO2_intensity'] = ['y']

        model.ren_gen = pm.Var(
            model.B_G_ren, model.Y, domain=pm.NonNegativeReals)
        var_index_labels['ren_gen'] = ['b', 'g', 'y']

        model.carbon_gen = pm.Var(
            model.B_G_carbon, model.Y, domain=pm.NonNegativeReals)
        var_index_labels['carbon_gen'] = ['b', 'g', 'y']
        # Energy Storage Variables
        model.SOC = pm.Var(model.B_G_sto, model.Y, model.soc_s_i,
                           domain=pm.NonNegativeReals)  # state of charge
        var_index_labels['SOC'] = ['b', 'g', 'y', 's', 'i']

        model.Pcha = pm.Var(model.B_G_sto, model.Y, model.S_I,
                            domain=pm.NonNegativeReals)  # charge capacity
        var_index_labels['Pcha'] = ['b', 'g', 'y', 's', 'i']

        # discharge capacity
        model.Pdis = pm.Var(model.B_G_sto, model.Y,
                            model.S_I, domain=pm.NonNegativeReals)
        var_index_labels['Pdis'] = ['b', 'g', 'y', 's', 'i']
        # energy capacity
        model.Store = pm.Var(model.B_G_sto, model.Y,
                             domain=pm.NonNegativeReals)
        var_index_labels['Store'] = ['b', 'g', 'y']

        # Renewable Curtailment
        model.Curt = pm.Var(model.B_G_ren, model.Y, model.S_I,
                            domain=pm.NonNegativeReals)  # Curtailment
        var_index_labels['Curt'] = ['b', 'g', 'y', 's', 'i']

        # Power flow variables
        model.PF = pm.Var(model.L, model.Y, model.S_I,
                          domain=pm.Reals, initialize=0)
        var_index_labels['PF'] = ['l', 'y', 's', 'i']
        
        '''
        # Spin, reg, flex for market trades - not used...
        model.PF_spin = pm.Var(model.L_mkt, model.Y, model.S_I,
                               domain=pm.Reals, initialize=0)
        model.PF_reg = pm.Var(model.L_mkt, model.Y, model.S_I,
                              domain=pm.Reals, initialize=0)
        model.PF_flex = pm.Var(model.L_mkt, model.Y, model.S_I,
                               domain=pm.Reals, initialize=0)
        var_index_labels['PF_spin'] = ['l', 'y', 's', 'i']
        var_index_labels['PF_reg'] = ['l', 'y', 's', 'i']
        var_index_labels['PF_flex'] = ['l', 'y', 's', 'i']
        '''
        
        # line expansion in MW
        model.LineCap = pm.Var(
            model.L, model.Y, domain=pm.NonNegativeReals)
        var_index_labels['LineCap'] = ['l', 'y']
        # Cumulative line expansion
        model.L_cap_total = pm.Var(
            model.L, model.Y, domain=pm.NonNegativeReals)
        var_index_labels['L_cap_total'] = ['l', 'y']
        #Bus angle for DC power flow calculation
        model.theta = pm.Var(model.B, model.Y, model.S_I, domain=pm.Reals, bounds=(-np.pi/3,
                                                                        np.pi/3))  # power flow angle - set the bounds
        #set slack bus angle to 0
        if self.data_handler.tx_model == 'dc':
            for y in model.Y:
                for (s,i) in model.S_I:
                        model.theta[113, y, s, i].fix(0)

        var_index_labels['theta'] = ['b','y', 's', 'i']

        # Load not served
        model.LNS = pm.Var(model.B, model.Y, model.S_I,
                           domain=pm.NonNegativeReals)
        var_index_labels['LNS'] = ['b', 'y', 's', 'i']
        
        if self.data_handler.large_load_option:
            model.large_load_net = pm.Var(
                model.B_LL,
                model.Y,
                model.S_I,
                domain=pm.NonNegativeReals
            )

            var_index_labels['large_load_net'] = [
                'b','y','s','i'
            ]

            model.LL_Curt = pm.Var(
                model.B_LL,
                model.Y,
                model.S_I,
                domain=pm.NonNegativeReals
            )
            var_index_labels['LL_Curt'] = ['b','y','s','i']

        #model.dummy = pm.Var(model.B, model.Y, model.S_I,
                           #domain=pm.NonNegativeReals)
        #var_index_labels['dummy'] = ['b', 'y', 's', 'i']
      
        # Binaries - not used for now; but will keep for record keeping
        '''
        model.acha = pm.Var(model.B_G_sto, model.Y,
                            model.S_I, domain=pm.Binary)  # Binary charge
        var_index_labels['acha'] = ['b', 'g', 'y', 's', 'i']
        model.adis = pm.Var(model.B_G_sto, model.Y,
                            model.S_I, domain=pm.Binary)  # Binary discharge
        var_index_labels['adis'] = ['b', 'g', 'y', 's', 'i']
        
        # model.retire = Var(model.G,model.Y, domain=Binary)# Retirement decision of generator g
        '''
        
        # Cost variables
        model.annual_gen_inv_cost = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['annual_gen_inv_cost'] = ['y']
        model.ng_h2_conv_cost = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['ng_h2_conv_cost'] = ['y']
        model.annual_trans_inv_cost = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['annual_trans_inv_cost'] = ['y']
        model.annual_es_replace_cost = pm.Var(
            domain=pm.NonNegativeReals)
        var_index_labels['annual_es_replace_cost'] = ['y']
        model.annual_es_replace_cost_gen = pm.Var(model.B_G_sto_cand,
                                                  domain=pm.NonNegativeReals)
        var_index_labels['annual_es_replace_cost_gen'] = [
            'b', 'g']
        model.annual_fom_cost = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['annual_fom_cost'] = ['y']
        model.annual_vom_cost = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['annual_vom_cost'] = ['y']
        model.annual_fuel_cost = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['annual_fuel_cost'] = ['y']
        model.annual_ls_cost = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['annual_ls_cost'] = ['y']
        model.annual_itc = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['annual_itc'] = ['y']
        model.annual_ptc = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['annual_ptc'] = ['y']
        model.annual_total_cost = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['annual_total_cost'] = ['y']
        model.annual_ll_curt_cost = pm.Var(
            model.Y, domain=pm.NonNegativeReals)
        var_index_labels['annual_ll_curt_cost'] = ['y']
        # Objective Value
        model.objective_value = pm.Var(
            domain=pm.NonNegativeReals)
        var_index_labels['objective_value'] = ['n']

        

        self.var_index_labels = var_index_labels

    def instantiate_model(self):
        """A method for instantiating the model and assigning Optimizer attributes to model attributes."""

        print("Instantiate Pyomo model")
        model = self.model
        self.index = self.data_handler.data_ls.index
        
        BUS = self.data_handler.load_data[self.index('bus')]
        GEN = self.data_handler.load_data[self.index('gen')]
        BRANCH = self.data_handler.load_data[self.index('branch')]
        tech_nums = self.data_handler.tech_nums
        # Timestep parameters
        # Create parameter
        model.m = pm.Param(initialize=self.data_handler.M)
        model.I = pm.RangeSet(
            0, model.m)  # Create parameter

        # Season parameter
        model.s = pm.Param(initialize=self.data_handler.S)
        model.S = pm.RangeSet(1, model.s)

        # model.S_I is the season and time step dynamic block
        s_i = []
        soc_s_i = []
        if self.data_handler.block_selection.lower() == 'Peak_Week_Season'.lower() or self.data_handler.block_selection.lower() == 'Repr_Weeks'.lower() or self.data_handler.block_selection.lower() == 'Seasonal_blocks'.lower():
            for s in np.arange(1, self.data_handler.S+1):
                for i in np.arange(0, self.data_handler.M):
                    s_i.append((s, i))
                    soc_s_i.append((s, i))
                soc_s_i.append((s, self.data_handler.M))

        elif self.data_handler.block_selection.lower() == 'Repr_3Days_Season'.lower():
            for s in np.arange(1, self.data_handler.S+1):
                if s != 5:  # for all seasons except peak summer
                    for i in np.arange(0, self.data_handler.M):
                        s_i.append((s, i))
                        soc_s_i.append((s, i))
                    soc_s_i.append((s, self.data_handler.M))
                else:  # for peak summer, include an extra day
                    for i in np.arange(0, 24):
                        s_i.append((s, i))
                        soc_s_i.append((s, i))
                    soc_s_i.append((s, 24))
                  
        elif self.data_handler.block_selection.lower() == 'Full_Year'.lower() or self.data_handler.block_selection.lower() == 'Full_Year_MY'.lower():
            for i in self.data_handler.season_map.index:              
                s = self.data_handler.season_map
                if self.data_handler.block_selection.lower() == 'Full_Year_MY'.lower():
                    s1 = s[s.columns[0]].values[i]
                else:
                    s1 = s.values[i]
                s_i.append((s1, i))
                soc_s_i.append((s1, i))
            soc_s_i.append((s1, len(self.data_handler.season_map.index)))

        elif self.data_handler.block_selection.lower() == 'Peak_Day'.lower():
            s=1
            for i in np.arange(0, self.data_handler.M):
                s_i.append((s, i))
                soc_s_i.append((s, i))
            soc_s_i.append((s, self.data_handler.M))


        model.S_I = pm.Set(dimen=2, initialize=s_i)
        model.soc_s_i = pm.Set(dimen=2, initialize=soc_s_i)

        # Define bus indices
        bpoints = np.size(BUS.Bus_number)
        model.c = pm.Param(initialize=bpoints)
        model.B = pm.Set(initialize=list(
            BUS['Bus_number'].values))
        # an alias 
        model.B_i = pm.Set(initialize=list(
            BUS['Bus_number'].values))
        
        #print(self.data_handler.large_load_buses)
        if self.data_handler.large_load_option:
            model.B_LL = pm.Set(
                initialize=self.data_handler.large_load_buses
            )

        # generator indices
        model.G = pm.Set(
            initialize=list(GEN['Gen_num'].values))

        # bus_gen pair
        model.B_G = pm.Set(dimen=2, initialize=tuple(
            zip(GEN['Bus_num'].values, GEN['Gen_num'].values)))
        
     
        model.Y = pm.Set(initialize=self.data_handler.years)
        # an alias of Y
        model.Y1 = pm.SetOf(model.Y)

        # Define line indices

        model.L = pm.Set(initialize=list(
            BRANCH['Line_Number'].values))
        # market line - if applicable
        model.L_mkt = pm.Set(within=model.L, initialize=[2])

        # line - to-bus pair
        #model.L_tb = pm.Set(initialize = tuple(zip(BRANCH['Line_Number'].values,BRANCH['To_Bus'].values)))
        # line - from-bus pair
        #model.L_fb = pm.Set(initialize = tuple(zip(BRANCH['Line_Number'].values,BRANCH['From_Bus'].values)))
        #line - L_tfb
        
        model.L_tfb = pm.Set(within = model.L*model.B*model.B_i, initialize = self.data_handler.line_bus_num)
        
        # bus_gen pair-renewables only
        bus_gen_num = GEN[['Bus_num', 'Gen_num']]

        B_G_ren_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['renewables'])]

        

        model.B_G_ren = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_ren_df['Bus_num'].values, B_G_ren_df['Gen_num'].values)))
        
        B_G_LL_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['large_load_gen'])]
        
        
        model.B_G_LL = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_LL_df['Bus_num'].values, B_G_LL_df['Gen_num'].values)))

      
        B_G_LL_sto_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['large_load_sto'])]
        
        model.B_G_LL_sto = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_LL_sto_df['Bus_num'].values, B_G_LL_sto_df['Gen_num'].values)))

        B_G_carbon_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            list(set(tech_nums['thermal'])-set(tech_nums['nuclear'])))]

        model.B_G_carbon = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_carbon_df['Bus_num'].values, B_G_carbon_df['Gen_num'].values)))
        
        B_G_thermal_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            list(set(tech_nums['thermal'])))]

        model.B_G_thermal = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_thermal_df['Bus_num'].values, B_G_thermal_df['Gen_num'].values)))
        
        # bus_gen pair-storage only

        B_G_sto_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['storage'])]

        model.B_G_sto = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_sto_df['Bus_num'].values, B_G_sto_df['Gen_num'].values)))

        # bus_gen pair-storage candidates only

        B_G_sto_cand_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['storage_cand'])]

        model.B_G_sto_cand = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_sto_cand_df['Bus_num'].values, B_G_sto_cand_df['Gen_num'].values)))

        # bus_gen pair-storage candidates only

        #B_G_sto_cand_y_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
          #  tech_nums['storage_cand_year'])]

        #model.B_G_sto_cand_y = pm.Set(dimen=2, initialize=tuple(
        #    zip(B_G_sto_cand_y_df['Bus_num'].values, B_G_sto_cand_y_df['Gen_num'].values)))
        # bus_gen pair-candidates only

        B_G_can_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['candidates'])]
        
        model.B_G_can = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_can_df['Bus_num'].values, B_G_can_df['Gen_num'].values)))

        # bus_gen pair-candidates with no storage tech only

        B_G_can_no_es_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            list(set(tech_nums['candidates'])-set(tech_nums['storage_cand'])))]

        model.B_G_can_no_es = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_can_no_es_df['Bus_num'].values, B_G_can_no_es_df['Gen_num'].values)))

        # bus_gen pair-solar only

        B_G_pv_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            np.concatenate((tech_nums['upv_ex'], tech_nums['upv_can'])))]

        model.B_G_pv = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_pv_df['Bus_num'].values, B_G_pv_df['Gen_num'].values)))

        # bus_gen pair-wind only

        B_G_wind_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            np.concatenate((tech_nums['wind_ex'], tech_nums['wind_can'])))]

        model.B_G_wind = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_wind_df['Bus_num'].values, B_G_wind_df['Gen_num'].values)))

        # bus_gen pair-ldes only

        B_G_ldes_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['ldes'])]

        model.B_G_ldes = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_ldes_df['Bus_num'].values, B_G_ldes_df['Gen_num'].values)))

        # bus_gen pair-ng only

        B_G_ng_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['ng'])]

        model.B_G_ng = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_ng_df['Bus_num'].values, B_G_ng_df['Gen_num'].values)))

        # bus_gen pair-ng cand only
        B_G_ng_can_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            np.intersect1d(tech_nums['candidates'], tech_nums['ng']))]

        model.B_G_ng_can = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_ng_can_df['Bus_num'].values, B_G_ng_can_df['Gen_num'].values)))
        # bus_gen pair-renewables cand only

        B_G_ren_can_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            np.intersect1d(tech_nums['candidates'], tech_nums['renewables']))]

        model.B_G_ren_can = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_ren_can_df['Bus_num'].values, B_G_ren_can_df['Gen_num'].values)))

        # bus_gen pair-nuclear only

        B_G_nuc_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['nuclear'])]

        model.B_G_nuc = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_nuc_df['Bus_num'].values, B_G_nuc_df['Gen_num'].values)))
        
        # bus_gen pair-coal only

        B_G_coal_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['coal'])]

        model.B_G_coal = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_coal_df['Bus_num'].values, B_G_coal_df['Gen_num'].values)))
        
        # bus_gen pair-oil only

        B_G_oil_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['oil'])]

        model.B_G_oil = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_oil_df['Bus_num'].values, B_G_oil_df['Gen_num'].values)))

        # bus_gen pair-dr only

        B_G_dr_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['dr'])]

        model.B_G_dr = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_dr_df['Bus_num'].values, B_G_dr_df['Gen_num'].values)))

        # bus_gen pair — wind candidates only.
        # Used as the sparse index for cWindCan, replacing the full B × G
        # Cartesian product (200 × 500 = 100 000 pairs → ~50 actual pairs).
        B_G_wind_can_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['wind_can'])]
        model.B_G_wind_can = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_wind_can_df['Bus_num'].values,
                B_G_wind_can_df['Gen_num'].values)))

        # ------------------------------------------------------------------
        # Sparse bus-gen sets for renewable and thermal constraints (Fix E).
        # Replacing full B_G iteration in cPVExist, cPVCand, cWindExist,
        # cThermMax/Min/Rup/Rdwn, and the cNonES split.
        # Each set contains only the actual (bus, gen) pairs relevant to that
        # constraint family — eliminating the 84–99% Constraint.Skip overhead
        # that occurs when these constraints are indexed over all of B_G.
        # ------------------------------------------------------------------

        # Existing PV (upv_ex) generators only — for cPVExist
        B_G_pv_ex_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['upv_ex'])]
        model.B_G_pv_ex = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_pv_ex_df['Bus_num'].values,
                B_G_pv_ex_df['Gen_num'].values)))

        # Existing wind (wind_ex) generators only — for cWindExist
        B_G_wind_ex_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['wind_ex'])]
        model.B_G_wind_ex = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_wind_ex_df['Bus_num'].values,
                B_G_wind_ex_df['Gen_num'].values)))

        # Solar candidate (upv_can) generators only — for cPVCand
        B_G_solar_can_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['upv_can'])]
        model.B_G_solar_can = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_solar_can_df['Bus_num'].values,
                B_G_solar_can_df['Gen_num'].values)))

        # Non-storage bus-gen pairs — complement of B_G_sto within B_G.
        # Used for cPFlexMaxGen / cPSpinMaxGen / cPRegMaxGen (reserve constraints
        # for non-storage generators).
        _sto_bg_set = frozenset(
            zip(B_G_sto_df['Bus_num'].values, B_G_sto_df['Gen_num'].values))
        B_G_non_sto_pairs = [
            (int(b), int(g))
            for b, g in zip(bus_gen_num['Bus_num'].values,
                            bus_gen_num['Gen_num'].values)
            if (b, g) not in _sto_bg_set
        ]
        model.B_G_non_sto = pm.Set(dimen=2, initialize=tuple(B_G_non_sto_pairs))
        #%%
    
        
    def populate_model(self):
        """A method for setting model parameters, variables, and an ExpressionsBlock object for defining objectives and constraints."""

        print('Populate Pyomo model')
        print('Define Parameters')
        self._set_model_param()
        print('Define Variables')
        self._set_model_var()
        #Define constraints and build
        self.constraints = ExplanConstraints(
            self.data_handler)
        print('Build Constraints')
        self.constraints.set_expressions(self.model)
        
        #Report out model size and stats (used for informational purposes - prints to txt file)
        #self.report = build_model_size_report(self.model)
        print("Pyomo Model Successfully Built")
        print("Model will begin solving. If using the GUI, press the Solve Button")
        
        #self.log_report_timing(self.model)# - only used for testing and model setup time logging; let's keep for now
    
    def log_report_timing(self,model, logger=logging.getLogger(__name__)):
        buf = io.StringIO()
        report_timing(model, ostream=buf)   # capture timing into buffer
        logger.info("\n" + buf.getvalue())  # dump into log file
    
    def solve_model(self):
        """Solves the model using the specified solver."""

        if self.solver == "neos":
            opt = pm.SolverFactory("cbc")
            solver_manager = pm.SolverManagerFactory("neos")
            results = solver_manager.solve(
                self.model, opt=opt)
        elif self.solver == "gurobi":
            solver = pm.SolverFactory(self.solver)

            try:
                solver.available()
            except pyutilib.common._exceptions.ApplicationError as e:
                logging.error(
                    "Optimizer: {error}".format(error=e))
            else:
                # Set gurobi solver options
                solver.options["NumericFocus"]= 0#cjn add
                solver.options["BarHomogeneous"]= 1#cjn add
                solver.options["ScaleFlag"]= 2#cjn add
                results = solver.solve(
                    self.model, tee=True, keepfiles=True)
        elif self.solver == "HiGHs":
            #Solver Factory does not work with HiGHs
            solver = Highs()
            results = solver.solve(
                self.model)
            print(results)
        else:
            solver = pm.SolverFactory(self.solver)

            try:
                solver.available()
            except pyutilib.common._exceptions.ApplicationError as e:
                logging.error(
                    "Optimizer: {error}".format(error=e))
            else:
                
                results = solver.solve(
                    self.model, tee=True, keepfiles=True, symbolic_solver_labels=True)
                
                #logger = logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
                #log_infeasible_constraints(self.model, log_expression=True, log_variables=True,logger = logger)        
        try:
            assert results.solver.termination_condition == TerminationCondition.optimal
        except AssertionError:
            logging.error(
                "Optimizer: An optimal solution could not be obtained. (solver termination condition: {0})".format(
                    results.solver.termination_condition
                )
            )
            raise (
                AssertionError(
                    "An optimal solution could not be obtained. (solver termination condition: {0})".format(
                        results.solver.termination_condition
                    )
                )
            )
        else:
            self._process_results()

        self.print_model_stats()
        

        return self.get_results()
    
    def print_model_stats(self):
        ''' Print model statistics'''
        print('Model Statistics: Skipped!')
        #print(self.report)
        

    def _process_results(self):
        """A method for computing derived quantities of interest and creating the results DataFrame."""
        print('Unpack and process results')
        for b,y in [(211,2024),(107,2024)]:
            if not self.data_handler.large_load_option:
                break
            c = self.model.cLLResourceRequirement[b,y]

            print("\nConstraint", b, y)
            print("Lower:", c.lower)
            print("Body :", value(c.body))
            print("Upper:", c.upper)
        
        for b,y in [(211,2024),(107,2024)]:
            if not self.data_handler.large_load_option:
                break

            gen_nums = self.data_handler.bus_gen_num.loc[
                self.data_handler.bus_gen_num['Bus_num'] == b
            ]['Gen_num'].values.astype(int)

            ll_ng = np.intersect1d(gen_nums, list(self.model.G_LL_NG))
            ll_bess = np.intersect1d(gen_nums, list(self.model.G_LL_BESS))

            ng_energy = sum(
                value(self.model.P_gen[b,g,y,s,i])
                for g in ll_ng
                for (s,i) in self.model.S_I
            )

            bess_energy = sum(
                value(self.model.Pdis[b,g,y,s,i])
                for g in ll_bess
                for (s,i) in self.model.S_I
            )

            curt_energy = sum(
                value(self.model.LL_Curt[b,y,s,i])
                for (s,i) in self.model.S_I
            )

            print(
                f"Bus={b} Year={y}"
                f" NG={ng_energy:.2f}"
                f" BESS={bess_energy:.2f}"
                f" CURT={curt_energy:.2f}"
            )
        for y in self.model.Y:
            if not self.data_handler.large_load_option:
                break
            for b in self.model.B_LL:
                gen_nums = self.data_handler.bus_gen_num.loc[
                    self.data_handler.bus_gen_num['Bus_num'] == b
                ]['Gen_num'].values.astype(int)

                ll_bess = np.intersect1d(
                    gen_nums,
                    list(self.model.G_LL_BESS)
                )

                lhs = sum(
                    value(self.model.Pdis[b,g,y,s,i])
                    for g in ll_bess
                    for (s,i) in self.model.S_I
                )

                rhs = 0.8 * value(
                    sum(
                        self.model.large_load[b,y,s,i]
                        for (s,i) in self.model.S_I
                    )
                )

                print(
                    f"Bus={b} Year={y}"
                    f"  LHS={lhs:.2f}"
                    f"  RHS={rhs:.2f}"
                )
        instance = self.model
        all_vars = {}
        for v in instance.component_objects(pm.Var, active=True):
            # str(v))  # str(v))
            varobject = getattr(instance, str(v))
            keys = list(varobject.extract_values().keys())
            names = self.var_index_labels[str(v)]
            if type(keys[0]) is tuple:
                index = pd.MultiIndex.from_tuples(
                    keys, names=names)
            else:
                index = keys
            data = list(varobject.extract_values().values())
            # Set data and drop nans from results
            varF = pd.DataFrame(
                data=data, index=index).dropna()
            varF.columns = ['Value']

            all_vars[str(v)] = varF

        all_pars = {}
        for p in instance.component_objects(pm.Param, active=True):
            parobject = getattr(instance, str(p))
            keys = list(parobject.extract_values().keys())
            #print(parobject)
            #print(keys)
            if type(keys[0]) is tuple and keys[0] is not None:
                names = self.par_index_labels[str(p)]
                index = pd.MultiIndex.from_tuples(
                    keys, names=names)
                parF = pd.DataFrame(
                    index=index, data=parobject.extract_values().values())
            elif keys[0] is not None:
                names = self.par_index_labels[str(
                    p)][0]
                index = pd.Index(keys, name=names)
                parF = pd.DataFrame(
                    index=index, data=parobject.extract_values().values())
            else:
                parF = parobject.extract_values().values()

            all_pars[str(p)] = parF

        self.all_vars = all_vars
        self.all_pars = all_pars
        self.get_timestamp()

    def get_results(self):
        """A method for returning the results DataFrame plus any other quantities of interest."""
        dispatch_dicts = ['P_gen', 'P_Reg', 'P_Flex', 'P_Spin', 'Pcha',
                          'Pdis', 'PF', 'SOC', 'Curt', 'theta', 'LNS']
        for key in self.all_vars.keys():
            if key in dispatch_dicts:
                d = self.all_vars[key]
                ind_s = len(d.index.names)
                d_new = d.stack().unstack(ind_s-1)
                d_new = d_new.droplevel(ind_s-1)
                self.all_vars[key] = d_new

        return self.all_vars, self.all_pars, self.timestamp

    def get_timestamp(self):
        t = time.localtime()
        self.timestamp = time.strftime('%b-%d-%Y_%H%M', t)