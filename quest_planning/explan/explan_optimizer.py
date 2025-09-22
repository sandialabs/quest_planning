# -*- coding: utf-8 -*-
"""
QuESt Planning - explan optimizer to set up the Pyomo model
Authors: C. Newlun and W. Olis
"""

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
        
        peak = self.data_handler.find_system_peak()
        energy = self.data_handler.find_system_energy()

        load_dict = self.data_handler.load_par_adjust()
        
        solar_ex_dict = self.data_handler.ren_profile_par_adj('upv_ex')
        wind_ex_dict = self.data_handler.ren_profile_par_adj('wind_ex')
        solar_can_dict = self.data_handler.ren_profile_par_adj('upv_can')
        wind_can_dict = self.data_handler.ren_profile_par_adj('wind_can')
                

        C_g_dict = self.data_handler.capex_par_adjust()

        C_g_es_pwr_dict = self.data_handler.capex_es_pwr_par_adjust()

        C_g_es_energy_dict = self.data_handler.capex_es_energy_par_adjust()

        G_fp_dict = self.data_handler.fp_par_adjust()

        par_index_labels = {}

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

        #Trnsmission params
        line_X_dict = {row.Line_Number: row.X for idx, row in BRANCH.iterrows()}
        line_fw_dict = {row.Line_Number: row.Rating_F for idx, row in BRANCH.iterrows()}
        line_bw_dict = {row.Line_Number: row.Rating_B for idx, row in BRANCH.iterrows()}
        line_cost_dict = {row.Line_Number: row.Tx_cost for idx, row in BRANCH.iterrows()}
        line_limit_dict = {row.Line_Number: row.Tx_limit for idx, row in BRANCH.iterrows()}
        line_lt_dict = {row.Line_Number: row.Lead_Time for idx, row in BRANCH.iterrows()}
        line_from_dict = {row.Line_Number: row.From_Bus_Number for idx, row in BRANCH.iterrows()}
        line_to_dict = {row.Line_Number: row.To_Bus_Number for idx, row in BRANCH.iterrows()}

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
        
        

        def line_cost_init(model, l):
            return line_cost_dict[l]

        model.line_cost = pm.Param(model.L, initialize=line_cost_init)
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

        #Check on this...ensure accuracy
        def co2_gen_init(model, g):
            co2_g = GEN[['Gen_num', 'CO2']
                        ].set_index('Gen_num')
            co2_g = co2_g['CO2']
            co2_g = co2_g.to_dict()
            # Divide by 2000  to convert lbs/MWh to tons/MWh??
            return co2_g[g]

        model.gen_CO2 = pm.Param(
            model.G, initialize=co2_gen_init)
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
        def existing_cap_init(model, g):
            exist_cap = GEN[['Gen_num', 'Cap']].set_index(
                'Gen_num')
            exist_cap.index = exist_cap.index.map(
                int)
            exist_cap = exist_cap.to_dict()['Cap']
            return exist_cap[g]
        model.P_cap = pm.Param(
            model.G, initialize=existing_cap_init)
        par_index_labels['P_cap'] = ['g']
        
        # Existing resource minimum stable level capacity
        def existing_min_cap_init(model, g):
            exist_cap = GEN[['Gen_num', 'MinCap']
                            ].set_index('Gen_num')
            exist_cap.index = exist_cap.index.map(
                int)
            exist_cap = exist_cap.to_dict()['MinCap']
            return exist_cap[g]
        model.P_cap_min = pm.Param(
            model.G, initialize=existing_min_cap_init)
        par_index_labels['P_cap_min'] = ['g']
        
        #Candidate resources candidate capacities per year
        def cand_cap_init(model, g):
            cand_cap = GEN[['Gen_num', 'CandCap']
                           ].set_index('Gen_num')
            cand_cap.index = cand_cap.index.map(
                int)  # .index.astype(str)
            cand_cap = cand_cap.to_dict()['CandCap']
            return cand_cap[g]

        model.P_cap_cand = pm.Param(
            model.G, initialize=cand_cap_init)
        par_index_labels['P_cap_cand'] = ['g']
        
        #Candidate resources candidate capacities max per simulation (whole planning horizon)
        def syst_cap_init(model, g):
            syst_cap = GEN[['Gen_num', 'SystCap']
                           ].set_index('Gen_num')
            syst_cap.index = syst_cap.index.map(
                int)
            syst_cap = syst_cap.to_dict()['SystCap']
            return syst_cap[g]

        model.P_cap_syst_max = pm.Param(
            model.G, initialize=syst_cap_init)
        par_index_labels['P_cap_syst_max'] = ['g']
        
        #Resource bus limits
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
        
        # Retirement years of generators - user input
        def gen_ret_yr_init(model, g):
            ret_yr = GEN[['Gen_num', 'RetYr']
                         ].set_index('Gen_num')
            ret_yr.index = ret_yr.index.map(
                int)
            ret_yr = ret_yr.to_dict()['RetYr']
            return ret_yr[g]

        model.gen_ret_yr = pm.Param(
            model.G, initialize=gen_ret_yr_init)
        par_index_labels['gen_ret_yr'] = ['g']
        
        #Planned years of candidate generators availability
        def gen_planned_yr_init(model, g):
            ret_yr = GEN[['Gen_num', 'PlannedYr']
                         ].set_index('Gen_num')
            ret_yr.index = ret_yr.index.map(
                int)
            ret_yr = ret_yr.to_dict()['PlannedYr']
            return ret_yr[g]

        model.gen_planned_yr = pm.Param(
            model.G, initialize=gen_planned_yr_init)
        par_index_labels['gen_planned_yr'] = ['g']

        # Retirement capacity of generators that are being retired
        def gen_ret_cap_init(model, g):
            ret_cap = GEN[['Gen_num', 'RetCap']
                          ].set_index('Gen_num')
            ret_cap.index = ret_cap.index.map(
                int)
            ret_cap = ret_cap.to_dict()['RetCap']
            return ret_cap[g]

        model.gen_ret_cap = pm.Param(
            model.G, initialize=gen_ret_cap_init)
        par_index_labels['gen_ret_cap'] = ['g']

        # FOM costs of generator
        def gen_fom_init(model, g):
            fom = GEN[['Gen_num', 'FOM']
                      ].set_index('Gen_num')
            fom.index = fom.index.map(
                int)  # .index.astype(str)
            fom = fom.to_dict()['FOM']
            return fom[g]

        model.G_fom = pm.Param(
            model.G, initialize=gen_fom_init)
        par_index_labels['G_fom'] = ['g']

        # VOM costs of generator
        def gen_vom_init(model, g):
            vom = GEN[['Gen_num', 'VOM']
                      ].set_index('Gen_num')
            vom.index = vom.index.map(
                int)  # .index.astype(str)
            vom = vom.to_dict()['VOM']
            return vom[g]

        model.G_vom = pm.Param(
            model.G, initialize=gen_vom_init)
        par_index_labels['G_vom'] = ['g']

        # Trans Adders - additional cost for transmission interconnection (if applicable)
        def gen_tx_add_init(model, g):
            tx_add = GEN[['Gen_num', 'TransAdder']
                         ].set_index('Gen_num')
            tx_add.index = tx_add.index.map(
                int)  # .index.astype(str)
            tx_add = tx_add.to_dict()['TransAdder']
            return tx_add[g]

        model.G_tx_add = pm.Param(
            model.G, initialize=gen_tx_add_init)
        par_index_labels['G_tx_add'] = ['g']

        # Production Tax credit (if applicable)
        def gen_ptc_init(model, g):
            ptc = GEN[['Gen_num', 'PTC']
                      ].set_index('Gen_num')
            ptc.index = ptc.index.map(
                int)  # .index.astype(str)
            ptc = ptc.to_dict()['PTC']
            return ptc[g]

        model.G_ptc = pm.Param(
            model.G, initialize=gen_ptc_init)
        par_index_labels['G_ptc'] = ['g']

        # Investment Tax credit (if applicable)
        def gen_itc_init(model, g):
            itc = GEN[['Gen_num', 'ITC']
                      ].set_index('Gen_num')
            itc.index = itc.index.map(
                int)
            itc = itc.to_dict()['ITC']
            return itc[g]
        model.G_itc = pm.Param(
            model.G, initialize=gen_itc_init)
        par_index_labels['G_itc'] = ['g']

        # Maximum heat rate of generator
        def gen_hr_init(model, g):
            hr = GEN[['Gen_num', 'HR']].set_index('Gen_num')
            hr.index = hr.index.map(
                int)  # .index.astype(str)
            hr = hr.to_dict()['HR']
            return hr[g]
        model.G_hr = pm.Param(
            model.G, initialize=gen_hr_init)
        par_index_labels['G_hr'] = ['g']

        # Capacity credit of generator
        def gen_cc_init(model, g):
            cc = GEN[['Gen_num', 'CapCred']
                     ].set_index('Gen_num')
            cc.index = cc.index.map(
                int)  # .index.astype(str)
            cc = cc.to_dict()['CapCred']
            return cc[g]
        model.G_cc = pm.Param(
            model.G, initialize=gen_cc_init)
        par_index_labels['G_cc'] = ['g']

        # Dynamic ELCC - TODO

        # Forced outage rate of generator; TODO: incorporate in model
        def gen_for_init(model, g):
            FOR = GEN[['Gen_num', 'FOR']
                      ].set_index('Gen_num')
            FOR.index = FOR.index.map(
                int)  # .index.astype(str)
            FOR = FOR.to_dict()['FOR']
            return FOR[g]
        model.G_for = pm.Param(
            model.G, initialize=gen_for_init)
        par_index_labels['G_for'] = ['g']

        # Lead times for gernation investment; TODO: incorporate in the model
        def gen_lt_init(model, g):
            LT = GEN[['Gen_num', 'LeadTime']
                     ].set_index('Gen_num')
            LT.index = LT.index.map(
                int)  # .index.astype(str)
            LT = LT.to_dict()['LeadTime']
            return LT[g]
        model.G_lt = pm.Param(
            model.G, initialize=gen_lt_init)
        par_index_labels['G_lt'] = ['g']

        # Generator ramp rates %/min;
        # TODO: check units
        def gen_ramp_init(model, g):
            Ramp = GEN[['Gen_num', 'Ramp']
                       ].set_index('Gen_num')
            Ramp.index = Ramp.index.map(
                int)  # .index.astype(str)
            Ramp = Ramp.to_dict()['Ramp']
            return Ramp[g]

        model.G_ramp = pm.Param(
            model.G, initialize=gen_ramp_init)
        par_index_labels['G_ramp'] = ['g']

        # Generator lifetime (y) - 
        # TODO: add automatic retirements
        def gen_lifetime_init(model, g):
            lt = GEN[['Gen_num', 'Lifetime']
                     ].set_index('Gen_num')
            lt.index = lt.index.map(
                int)  # .index.astype(str)
            lt = lt.to_dict()['Lifetime']
            return lt[g]
        model.G_lifetime = pm.Param(
            model.G, initialize=gen_lifetime_init)
        par_index_labels['G_lifetime'] = ['g']

        # Year technology is available to be invested
        def gen_year_avail_init(model, g):
            yav = GEN[['Gen_num', 'YearAvail']
                      ].set_index('Gen_num')
            yav.index = yav.index.map(
                int)
            yav = yav.to_dict()['YearAvail']
            return yav[g]
        model.G_y_avail = pm.Param(
            model.G, initialize=gen_year_avail_init)
        par_index_labels['G_y_avail'] = ['g']
        
        # Annual peak demand of system
        peak_dict = peak[self.data_handler.load_forecast].filter(
            items=self.data_handler.years, axis=0).to_dict()
        model.PEAK = pm.Param(model.Y, initialize=peak_dict)
        par_index_labels['PEAK'] = ['g']

        # Annual energy consumption of system
        energy_dict = energy[self.data_handler.load_forecast].filter(
            items=self.data_handler.years, axis=0).to_dict()
        model.ENERGY = pm.Param(
            model.Y, initialize=energy_dict)
        par_index_labels['ENERGY'] = ['g']

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

        self.par_index_labels = par_index_labels
        
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
        #%%
        # bus_gen pair-renewables only
        bus_gen_num = GEN[['Bus_num', 'Gen_num']]

        B_G_ren_df = bus_gen_num.loc[bus_gen_num['Gen_num'].isin(
            tech_nums['renewables'])]

        model.B_G_ren = pm.Set(dimen=2, initialize=tuple(
            zip(B_G_ren_df['Bus_num'].values, B_G_ren_df['Gen_num'].values)))

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
        self.report = build_model_size_report(self.model)
        print("Pyomo Model Successfully Built")
        print("Press the Solve Button")
        
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
                    self.model, tee=True, keepfiles=True)
                
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
        print('Model Statistics:')
        print(self.report)
        

    def _process_results(self):
        """A method for computing derived quantities of interest and creating the results DataFrame."""
        print('Unpack and process results')
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