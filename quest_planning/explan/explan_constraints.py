# -*- coding: utf-8 -*-
"""
QuESt Planning - explan constraints to be considered in the model
Authors: C. Newlun and W. Olis
"""

import pyomo.environ as pm
import numpy as np
from pyomo.environ import inequality


class ExplanConstraints:

    def __init__(self, data_handler):
        '''
        Initialize ExplanConstraints class
        '''
        
        self._scenario = data_handler.scenario
        #Define data_handler
        self.data_handler = data_handler
        self.index = self.data_handler.data_ls.index
        
        if data_handler.block_selection.lower() == 'Full_year'.lower() or data_handler.block_selection.lower() == 'Full_year_MY'.lower():
            self.start_hr = data_handler.start_hr
            self.end_hr = data_handler.end_hr
            self.last_hr = data_handler.last_hr
            self.first_hr = data_handler.first_hr
            print('start_hr:', self.start_hr, 'end_hr:', self.end_hr)
            print('last_hr:', self.last_hr, 'first_hr:', self.first_hr)
        else:
            self.start_hr = 0  
            self.end_hr = 167#can we just make this data_handler.end_hr
            
        # ES min SOC (%)
        self.ini_level = data_handler.ini_level
        
        #Define year gap for weighting
        self.year_gap = data_handler.year_gap
        self.year_gap_array = data_handler.year_gap_array
        # Tax crediit final year & initialize ITC and PTC
        self.tax_credit_end_year = data_handler.tax_credit_end_year
        self.total_itc = 0
        self.total_ptc = 0
        #System name
        self.system = data_handler.system
        
        
        
        #Can remove tuple with other bus_gen sets 
        self.storage_tuple = tuple(zip(
            data_handler.bus_sto_num, data_handler.tech_nums['storage']))
        self.thermal_nuclear_tuple = tuple(zip(
            data_handler.bus_therm_num, data_handler.tech_nums['nuclear']))
        self.thermal_tuple = tuple(zip(
            data_handler.bus_therm_num, data_handler.tech_nums['thermal']))
        self.candidate_tuple = tuple(zip(
            data_handler.bus_cand_num, data_handler.tech_nums['candidates']))
        self.upv_tuple = tuple(zip(
            data_handler.bus_upv_ex_num, data_handler.tech_nums['upv_ex']))
        self.solar_can_tuple = tuple(zip(
            data_handler.bus_solar_can_num, data_handler.tech_nums['upv_can']))
        self.wind_ex_tuple = tuple(zip(
            data_handler.bus_wind_ex_num, data_handler.tech_nums['wind_ex']))
        self.wind_can_tuple = tuple(zip(
            data_handler.bus_wind_can_num, data_handler.tech_nums['wind_can']))
        self.es_can_tuple = tuple(zip(
            data_handler.bus_es_can_num, data_handler.tech_nums['storage_cand']))
        self.ren_tuple = tuple(zip(
            data_handler.bus_ren_num, data_handler.tech_nums['renewables']))
        self.exist_tuple = tuple(zip(
            data_handler.bus_exist_num, data_handler.tech_nums['exist']))
        self.cand_tuple = tuple(zip(
            data_handler.bus_cand_num, data_handler.tech_nums['candidates']))
        self.dr_tuple = tuple(zip(
            data_handler.bus_cand_num, data_handler.tech_nums['dr']))
        
        # Gen_nm to Bus_num to Bus_name to Tech
        self.gen_map_info = data_handler.load_data[self.index('gen')][['Gen_num',
                                                           'Bus_num', 'Bus', 'Tech', 'Tech_Num']]
        self.tech_map_info = data_handler.load_data[self.index('tech')][[
            'Tech', 'Tech_Name', 'Tech_Num']]
        
        # MVA Base
        self.mva_base = data_handler.mva_base
        # hour weight
        self.hour_duration = data_handler.hour_duration
        # Transmission expansion sum
        self.trans_sum = 0
        
        
    @property
    def scenario(self):
        '''
        Define scenario - check if we need
        '''
        return self._scenario

    @scenario.setter
    def scenario(self, value):
        '''
        Set scenario to user-defined value - check if we need
        '''
        self._scenario = value

    def set_expressions(self, model):
        '''
        Set expressions for optimization model
        '''
        self.energy_storage_constraints(model)
        self.thermal_generator_constraints(model)
        self.renewable_generator_constraints(model)
        self.policy_constraints(model)
        self.transmission_constraints(model)
        self.power_balance_constraints(model)
        self.investment_constraints(model)
        self.reliability_and_resilience_constraints(model)
        self.dr_and_ee_constraints(model)
        self.obj_and_cost_breakdown(model)

        
    def energy_storage_constraints(self, model):
        '''
        Define the energy storage constraints of the optimization model
        '''
               
        model.cSOC_old = pm.Constraint(model.B_G_sto, model.Y, model.S_I, rule=self.cSOC_old)
        
        model.cChDsch = pm.Constraint(
            model.B_G_sto, model.Y, model.S_I, rule=self.cChDsch)
        model.cSOCmax = pm.Constraint(
            model.B_G_sto, model.Y, model.S_I, rule=self.cSOCmax)
        model.cSOCmin = pm.Constraint(
            model.B_G_sto, model.Y, model.S_I, rule=self.cSOCmin)
        model.cStoremax = pm.Constraint(
            model.B_G_sto, model.Y, rule=self.cStoremax)
        model.cStoremin = pm.Constraint(
            model.B_G_sto, model.Y, rule=self.cStoremin)
        model.cNonES = pm.Constraint(
            model.B_G_sto, model.Y, model.S_I, rule=self.cNonES)

        

        
    def thermal_generator_constraints(self, model):
        '''
        Define the thermal generation constraints of the optimization model
        '''
        model.cThermMax = pm.Constraint(
            model.B_G, model.Y, model.S_I, rule=self.cThermMax)
        model.cThermMin = pm.Constraint(
            model.B_G, model.Y, model.S_I, rule=self.cThermMin)
        #add reserves option flag
        if self.data_handler.reserves_option:
            model.cPRegMax = pm.Constraint(
                model.B_G, model.Y, model.S_I, rule=self.cPRegMax)
            model.cPSpinMax = pm.Constraint(
                model.B_G, model.Y, model.S_I, rule=self.cPSpinMax)
            model.cPFlexMax = pm.Constraint(
                model.B_G, model.Y, model.S_I, rule=self.cPFlexMax)
            model.cPRegMin = pm.Constraint(
                model.Y, model.S_I, rule=self.cPRegMin)
            model.cPSpinMin = pm.Constraint(
                model.Y, model.S_I, rule=self.cPSpinMin)
            model.cPFlexMin = pm.Constraint(
                model.Y, model.S_I, rule=self.cPFlexMin)
            
        #if not self.data_handler.reserves_option:
            #Fix reserve variables to 0
            #model.P_Reg[model.l, model.y, model.S_I].fix(0)
            #model.P_Spin[model.l, model.y, model.S_I].fix(0)
            #model.P_Flex[model.l, model.y, model.S_I].fix(0)
            
        if self.data_handler.block_selection.lower() != 'seasonal_blocks': 
            model.cThermRup = pm.Constraint(
                model.B_G, model.Y, model.S_I, rule=self.cThermRup)
            model.cThermRdwn = pm.Constraint(
                model.B_G, model.Y, model.S_I, rule=self.cThermRdwn)

    def renewable_generator_constraints(self, model):
        '''
        Define the renewable generation constraints of the optimization model
        '''
        model.cPVExist = pm.Constraint(
            model.B_G, model.Y, model.S_I, rule=self.cPVExist)
        model.cPVCand = pm.Constraint(
            model.B_G, model.Y, model.S_I, rule=self.cPVCand)
        model.cWindExist = pm.Constraint(
            model.B_G, model.Y, model.S_I, rule=self.cWindExist)
        model.cWindCan = pm.Constraint(
            model.B, model.G, model.Y, model.S_I, rule=self.cWindCan)

    def policy_constraints(self, model):
        '''
        Define the policy constraints of the optimization model
        '''
        model.cRenAnnual = pm.Constraint(model.B_G_ren,
                                              model.Y, rule=self.cRenAnnual)

        if self.data_handler.rps_policy:
            model.cRPS = pm.Constraint(model.Y, rule=self.cRPS)

        if self.data_handler.co2_policy:
            model.cCO2emm = pm.Constraint(
                model.B_G_carbon, model.Y,  rule=self.cCO2emm)
            model.cCO2emmLimit = pm.Constraint(
                model.Y, rule=self.cCO2emmLimit)
            
        if self.data_handler.co2_intensity_policy:
            model.cCO2int = pm.Constraint(
                model.Y,  rule=self.cCO2int)
            model.cCO2intLimit = pm.Constraint(
                model.Y,  rule=self.cCO2intLimit)
            

    def transmission_constraints(self, model):
        '''
        Define the transmission constraints of the optimization model
        '''
        if self.data_handler.tx_model != 'copper_sheet':
            #model.cTxFlwBounds = pm.Constraint(
                #model.L, model.Y, model.S_I, rule=self.cTxFlwBounds)
            model.cTxFlwUpper = pm.Constraint(
                model.L, model.Y, model.S_I, rule=self.cTxFlwUpper)
            model.cTxFlwLower = pm.Constraint(
                model.L, model.Y, model.S_I, rule=self.cTxFlwLower)
            #model.cTxFlwFw = pm.Constraint(model.L, model.Y, model.S_I, rule=self.cTxFlwFw)
            #model.cTxFlwBw = pm.Constraint(model.L, model.Y, model.S_I, rule=self.cTxFlwBw)
            
            if self.data_handler.tx_model == 'dc':#Only use if DC power flow is modeled
                model.cDCPF = pm.Constraint(model.L,model.Y, model.S_I, rule=self.cDCPF)
                model.cThetaDiffMax = pm.Constraint(model.L,model.Y, model.S_I, rule=self.cThetaDiffMax)
                model.cThetaDiffMin = pm.Constraint(model.L,model.Y, model.S_I, rule=self.cThetaDiffMin)
                #model.cSlackBus =pm.Constraint(model.Y, model.S_I, rule=self.cSlackBus)
        
        #if self.data_handler.tx_model == 'copper_sheet':
            #fix PF to 0
            #model.PF[model.L, model.Y, model.S_I].fix(0)

    def power_balance_constraints(self, model):
        '''
        Define the power balance constraints of the optimization model
        '''
        model.cPwrBal = pm.Constraint(model.B, model.Y, model.S_I, rule=self.cPwrBal)
        model.cLNSMax = pm.Constraint(model.B, model.Y, model.S_I, rule=self.cLNSMax)
        if self.data_handler.tx_model == 'copper_sheet':
            model.cPwrBal_CopperSheet = pm.Constraint(model.Y, model.S_I, rule=self.cPwrBal_CopperSheet)

    def investment_constraints(self, model):
        '''
        Define the investement constraints for generation and transmission of the optimization model
        '''
        model.cPCapTotal = pm.Constraint(model.B_G, model.Y, rule=self.cPCapTotal)
        model.cStoreCapTotal = pm.Constraint(model.B_G, model.Y, rule=self.cStoreCapTotal)

        model.cRetirements = pm.Constraint(
            model.B_G, model.Y, rule=self.cRetirements)
        
        #if self.data_handler.tx_model != 'copper_sheet':
        model.cBusInvMaxAnnual = pm.Constraint(
                model.B_G_can, model.Y, rule=self.cBusInvMaxAnnual)
        model.cBusInvMaxTotal = pm.Constraint(
                model.B_G_can, rule=self.cBusInvMaxTotal)
            
        model.cSystWindMax = pm.Constraint(
            rule=self.cSystWindMax)
        model.cSystPVMax = pm.Constraint(
            rule=self.cSystPVMax)
        model.cSystGasMax = pm.Constraint(
            rule=self.cSystGasMax)
        
        if self.data_handler.resource_bus_limit_dict is not None:
            model.cResourceByBus = pm.Constraint(
                model.B_G_can, rule=self.cResourceByBus)
        
        '''
        keep for now...'
        
        model.cTxCapTotalwDelay = pm.Constraint(
            model.L, model.Y, rule=self.cTxCapTotalwDelay)
        '''
        
        model.cTxCapTotalnoDelay = pm.Constraint(
            model.L, model.Y,model.Y1, rule=self.cTxCapTotalnoDelay)
        model.cTxCapInvMax = pm.Constraint(
            model.L, rule=self.cTxCapInvMax)
        model.cTxCapSystMax = pm.Constraint(
            rule=self.cTxCapSystMax)
        model.cTechAvail = pm.Constraint(
            model.B_G_can, model.Y, rule=self.cTechAvail)


    def reliability_and_resilience_constraints(self, model):
        '''
        Define the reliability and resilience constraints of the optimization model
        '''
        model.cPRM = pm.Constraint(
            model.Y, rule=self.cPRM)
        

    def dr_and_ee_constraints(self, model):
        '''
        Define the demand response and energy efficiency constraints of the optimization model
        '''
        model.cDRMax = pm.Constraint(
            model.B_G_dr, model.Y, model.S_I, rule=self.cDRMax)
        model.cDRgenMax = pm.Constraint(
            model.B_G_dr, model.Y, model.S_I, rule=self.cDRgenMax)
        model.cDRnoAnc = pm.Constraint(
            model.B_G_dr, model.Y, model.S_I, rule=self.cDRnoAnc)
        model.cDRopMax = pm.Constraint(
            model.B_G_dr, model.Y, rule=self.cDRopMax)
        model.cDRSystMax = pm.Constraint(
            model.B_G_dr, rule=self.cDRSystMax)
        model.cDRnoInv = pm.Constraint(
            model.B_G_dr, model.Y, rule=self.cDRnoInv)

    def obj_and_cost_breakdown(self, model):
        '''
        Define the objective and cost breakdown constraints of the optimization model
        '''
        model.cGenInvCostAnnual = pm.Constraint(
            model.Y, rule=self.cGenInvCostAnnual)
        #model.cNGH2Costconv = pm.Constraint(
            #model.Y, rule=self.cNGH2Costconv)
        model.cTxInvCostAnnual = pm.Constraint(
            model.Y, rule=self.cTxInvCostAnnual)
        
        model.cFOMCostAnnual = pm.Constraint(
            model.Y, rule=self.cFOMCostAnnual)
        model.cVOMCostAnnual = pm.Constraint(
            model.Y, rule=self.cVOMCostAnnual)
        model.cFuelCostAnnual = pm.Constraint(
            model.Y, rule=self.cFuelCostAnnual)
        model.cLNSCostAnnual = pm.Constraint(
            model.Y, rule=self.cLNSCostAnnual)
        
        model.cTotalCostAnnual = pm.Constraint(
            model.Y, rule=self.cTotalCostAnnual)
        model.OBJ = pm.Objective(rule=self.cOBJ)
                
        model.cESReplaceCostSum = pm.Constraint(
                rule=self.cESReplaceCostSum)
        model.cESReplaceCost = pm.Constraint(model.B_G_sto_cand,
                                                           rule=self.cESReplaceCost)
                    
        model.cITCAnnual = pm.Constraint(
                model.Y, rule=self.cITCAnnual)
        model.cPTCAnnual = pm.Constraint(
                model.Y, rule=self.cPTCAnnual)
        
                 

    def cSOC_old(self, model, b, g, y, s, i):
        '''
        Energy Storage SOC calculation
        
        TODO: add regulating reserves into this calculation
        '''
        if (b, g) in self.storage_tuple: 
            if self.data_handler.block_selection.lower() == 'Full_Year'.lower() or self.data_handler.block_selection.lower() == 'Full_Year_MY'.lower():
                delta = 1#hr
                if (b, g) in model.B_G_ldes:
                    
                    if i == 0:  # self.start_hr:
                        # Start at 50% state of charge (S0C) on first hour in time range
                        SOCpre = self.ini_level * \
                            model.Store[b, g, y]
                        return model.SOC[b, g, y, s, i] == (SOCpre)
                    elif i == self.data_handler.M:  # in self.end_hr:
                        return model.SOC[b, g, y, s, i] >= self.ini_level * model.Store[b, g, y]
                    elif i in np.array(self.first_hr):
                        if s != 1:
                            SOCpre = model.SOC[b,
                                               g, y, s - 1, i - 1]
                            return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i] )*delta
                        elif i == self.first_hr[-1]:
                            SOCpre = model.SOC[b,
                                               g, y, 4, i - 1]
                            return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*delta
                    else:
                        # SOCpre is the starting state of charge for this time step
                        SOCpre = model.SOC[b,
                                           g, y, s, i - 1]
                        return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*delta
                    '''
                    elif i in self.last_hr:
                        if s != 1: #i != self.end_hr[-1] and
                            SOCpre = model.SOC[b,
                                               g, y, s - 1, i - 1]
                            return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*delta

                        elif i == self.end_hr[-1]:
                            SOCpre = model.SOC[b,
                                               g, y, 4, i - 1]
                            return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*delta
                    '''
                    
                else:
                    
                    if i in self.start_hr or i == 0:
                        # Start at 50% state of charge (S0C) on first hour in time range
                        SOCpre = self.ini_level * \
                            model.Store[b, g, y]
                        return model.SOC[b, g, y, s, i] == (SOCpre)
                    elif i in self.last_hr:
                        return model.SOC[b, g, y, s, i] >= self.ini_level * model.Store[b, g, y]
                    elif i in np.array(self.first_hr):
                        if s != 1:
                            SOCpre = model.SOC[b,
                                               g, y, s - 1, i - 1]
                            return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i] )*delta
                        
                        elif i == self.first_hr[-1]:
                            SOCpre = model.SOC[b,
                                               g, y, 4, i - 1]
                            return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*delta
                    else:
                        # SOCpre is the starting state of charge for this time step
                        SOCpre = model.SOC[b,g, y, s, i - 1]
                        return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*delta
            if self.data_handler.block_selection.lower() == 'Peak_Week_Season'.lower() or self.data_handler.block_selection.lower() == 'Repr_Weeks'.lower():
                delta = 1#hr
                if (b, g) in model.B_G_ldes:
                    if i == self.start_hr:
                        # Start at 50% state of charge (S0C) on first hour in time range
                        SOCpre = self.ini_level * \
                            model.Store[b, g, y]
                        return model.SOC[b, g, y, s, i] == (SOCpre)
                    elif i == self.end_hr:
                        return model.SOC[b, g, y, s, i] >= self.ini_level * model.Store[b, g, y]
                    else:
                        # SOCpre is the starting state of charge for this time step
                        SOCpre = model.SOC[b, g, y, s, i - 1]
                        return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*delta
                else:
                    if i in [0,24,48,72,96,120,144]:#== self.start_hr:
                        # Start at 50% state of charge (S0C) on first hour in time range
                        SOCpre = self.ini_level * \
                            model.Store[b, g, y]
                        return model.SOC[b, g, y, s, i] == (SOCpre)
                    elif i in [23,47,71,95,119,143,167]:
                        return model.SOC[b, g, y, s, i] >= self.ini_level * model.Store[b, g, y]
                    else:
                        # SOCpre is the starting state of charge for this time step
                        SOCpre = model.SOC[b, g, y, s, i - 1]
                        return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*delta
            if self.data_handler.block_selection.lower() == 'Repr_3Days_Season'.lower():
                delta = 1  # 1 hour resolution

                if (b, g) in model.B_G_ldes:
                    # long-duration storage: enforce continuity across the whole horizon
                    if i == 0:  # very first hour
                        SOCpre = self.ini_level * model.Store[b, g, y]
                        return model.SOC[b, g, y, s, i] == SOCpre
                    elif i == self.data_handler.M:  # very last hour
                        return model.SOC[b, g, y, s, i] >= self.ini_level * model.Store[b, g, y]
                    else:
                        SOCpre = model.SOC[b, g, y, s, i - 1]
                        return model.SOC[b, g, y, s, i] == SOCpre + (
                            model.rte_eff[g] * model.Pcha[b, g, y, s, i] -
                            model.Pdis[b, g, y, s, i]
                        ) * delta
                else:
                    # short-duration storage (daily-cycling): enforce reset at start of each representative day
                    if i % 24 == 0:  # start of a rep-day
                        SOCpre = self.ini_level * model.Store[b, g, y]
                        return model.SOC[b, g, y, s, i] == SOCpre
                    elif (i + 1) % 24 == 0:  # end of a rep-day
                        return model.SOC[b, g, y, s, i] >= self.ini_level * model.Store[b, g, y]
                    else:
                        SOCpre = model.SOC[b, g, y, s, i - 1]
                        return model.SOC[b, g, y, s, i] == SOCpre + (
                            model.rte_eff[g] * model.Pcha[b, g, y, s, i] -
                            model.Pdis[b, g, y, s, i]
                        ) * delta
            if self.data_handler.block_selection.lower() == 'Seasonal_blocks'.lower():
                
                if (b, g) in model.B_G_ldes:
                    if i == 0 and s==1:#self.start_hr:
                        # Start at 50% state of charge (S0C) on first hour in time range
                        SOCpre = self.ini_level * \
                            model.Store[b, g, y]
                        return model.SOC[b, g, y, s, i] == (SOCpre)
                    elif i == 4 and s==4:#self.end_hr:
                        return model.SOC[b, g, y, s, i] >= self.ini_level * model.Store[b, g, y]
                    if i == 0 and s!=1:
                        SOCpre = model.SOC[b, g, y, s-1, 4]
                        return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*model.season_time_weight[s,i]               
                    else:
                        # SOCpre is the starting state of charge for this time step
                        SOCpre = model.SOC[b, g, y, s, i - 1]
                        return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*model.season_time_weight[s,i]  
                else:
                    if i ==0:
                        # Start at 50% state of charge (S0C) on first hour in time range
                        SOCpre = self.ini_level * \
                            model.Store[b, g, y]
                        return model.SOC[b, g, y, s, i] == (SOCpre)
                    elif i ==5:
                        return model.SOC[b, g, y, s, i] >= self.ini_level * model.Store[b, g, y]
                    else:
                        # SOCpre is the starting state of charge for this time step
                        SOCpre = model.SOC[b, g, y, s, i - 1]
                        return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*model.season_time_weight[s,i]  
            
            if self.data_handler.block_selection.lower() == 'Peak_Day'.lower():
                delta = 1
                if (b, g) in model.B_G_ldes:
                    if i == self.start_hr:
                        # Start at 50% state of charge (S0C) on first hour in time range
                        SOCpre = self.ini_level * \
                            model.Store[b, g, y]
                        return model.SOC[b, g, y, s, i] == (SOCpre)
                    elif i == self.end_hr:
                        return model.SOC[b, g, y, s, i] >= self.ini_level * model.Store[b, g, y]
                    else:
                        # SOCpre is the starting state of charge for this time step
                        SOCpre = model.SOC[b, g, y, s, i - 1]
                        return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*delta
                else:
                    if i in [0]:#== self.start_hr:
                        # Start at 50% state of charge (S0C) on first hour in time range
                        SOCpre = self.ini_level * \
                            model.Store[b, g, y]
                        return model.SOC[b, g, y, s, i] == (SOCpre)
                    elif i in [23]:#== self.end_hr:
                        return model.SOC[b, g, y, s, i] >= self.ini_level * model.Store[b, g, y]
                    else:
                        # SOCpre is the starting state of charge for this time step
                        SOCpre = model.SOC[b, g, y, s, i - 1]
                        return model.SOC[b, g, y, s, i] == (SOCpre) + (model.rte_eff[g] * model.Pcha[b, g, y, s, i] - model.Pdis[b, g, y, s, i])*delta
        else:
            return pm.Constraint.Skip


    def cChDsch(self, model, b, g, y, s, i):
        '''
        This enforces that the sum of the charge/discharge power and reserves does not exceed the cumulative invested power size of the ES
        '''

        if (b, g) in self.storage_tuple:
            return model.Pcha[b, g, y, s, i] + model.Pdis[b, g, y, s, i] + model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i] + model.P_Flex[b, g, y, s, i] <= model.P_cap_total[b, g, y]
        else:
            return pm.Constraint.Skip


    def cSOCmax(self, model, b, g, y, s, i):
        '''
        SOC has to be less than or equal to the battery's upper limit- KEEP CJN
        '''
        if (b, g) in self.storage_tuple:
           
            return model.SOC[b, g, y, s, i] <= float(self.data_handler.soc_max) * model.Store[b, g, y]
            # self.data_handler.scalars.loc['SOC_up_limit']['Value'])/100
        else:
            return pm.Constraint.Skip

    def cSOCmin(self, model, b, g, y, s, i):
        '''
        SOC has to be greater than or equal to the battery's lower limit
        '''
        if (b, g) in self.storage_tuple:
            # * delta
            return model.SOC[b, g, y, s, i] >= float(self.data_handler.soc_min) * model.Store[b, g, y]
            # self.data_handler.scalars.loc['SOC_down_limit']['Value'])/100
        else:
            return pm.Constraint.Skip


    def constraint1_i(self, model, b, g, y):
        '''
        Define model.Store -- the energy capacity
        **Optional constraint**
        '''
        if (b, g) in self.storage_tuple:
            return model.Store[b, g, y] == model.es_duration[g] * model.P_cap_total[b, g, y]
        else:
            return pm.Constraint.Skip

    
    def cStoremax(self, model, b, g, y):
        '''
        Define Max energy storage capacity
        '''
        if (b, g) in self.storage_tuple:

            return model.Store[b, g, y] <= model.es_max_duration[g] * model.P_cap_total[b, g, y]
        else:
            return pm.Constraint.Skip

    def cStoremin(self, model, b, g, y):
        '''
        Define minimum energy storage capacity
        '''
        if (b, g) in self.storage_tuple:
            # print((str(b), str(g)))
            return model.Store[b, g, y] >= model.es_min_duration[g] * model.P_cap_total[b, g, y]
        else:
            return pm.Constraint.Skip
    
    def cNonES(self, model, b, g, y, s, i):
        '''
        Ensures ES has no P_gen and no gen has Pcha and Pdis
        **Optional constraint**
        '''
        if (b, g) in self.storage_tuple:
            return model.P_gen[b, g, y, s, i] == 0
        elif (b, g) not in self.storage_tuple:
            return model.Pdis[b, g, y, s, i] + model.Pcha[b, g, y, s, i] == 0
        else:
            return pm.Constraint.Skip
    
    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    2.) Thermal Generator Constraints
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''

    def cThermMax(self, model, b, g, y, s, i):
        '''
        Thermal generation limit - upper bound
        **thermal_tuple is optional**
        '''
        if (b, g) in self.thermal_tuple:
            return model.P_gen[b, g, y, s, i] + model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i] + model.P_Flex[b, g, y, s, i] <= model.P_cap_total[b, g, y]
        else:
            return pm.Constraint.Skip

    def cThermMin(self, model, b, g, y, s, i):
        '''
        Enforce thermal generation minimum stable level
        '''
       
        if (b, g) in self.thermal_tuple and y < model.gen_ret_yr[g] and ((b, g) not in self.candidate_tuple):
            return model.P_gen[b, g, y, s, i] + model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i]+model.P_Flex[b, g, y, s, i] >= model.P_cap_min[g]
        elif (b, g) in self.thermal_tuple and y >= model.gen_ret_yr[g]:
            if model.gen_ret_cap[g] < model.P_cap_min[g]:
                return model.P_gen[b, g, y, s, i]+ model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i]+model.P_Flex[b, g, y, s, i]  >= (model.P_cap_min[g]-model.gen_ret_cap[g])
            elif model.gen_ret_cap[g] >= model.P_cap_min[g]:
               return model.P_gen[b, g, y, s, i]+ model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i]+model.P_Flex[b, g, y, s, i]  >= 0
        else:
            return pm.Constraint.Skip
    
    def cThermRup(self, model, b, g, y, s, i):
        '''
        Ramping constraint for each generator - ensures adequate ramp up - only valid for hourly simulation
        '''
        if (b, g) in self.thermal_tuple:
            if self.data_handler.block_selection.lower() == 'Full_Year'.lower() or self.data_handler.block_selection.lower() == 'Full_Year_MY'.lower():
                if i != 0:
                    if i in self.last_hr and s != 4:
                        P_diff = model.P_gen[b, g, y, s, i] - model.P_gen[b, g, y, s+1, self.first_hr[s-1]]
                        return P_diff <= model.G_ramp[g]*model.P_cap_total[b, g, y]
                    elif i in self.last_hr and s == 4:
                        P_diff = model.P_gen[b, g, y, s, i] - model.P_gen[b, g, y, 1, self.last_hr[0]]
                        return P_diff <= model.G_ramp[g]*model.P_cap_total[b, g, y]
                    elif i in self.first_hr and s != 1:
                        P_diff = model.P_gen[b, g, y, s-1, self.last_hr[s-1]] - model.P_gen[b, g, y, s, i]
                        return P_diff <= model.G_ramp[g]*model.P_cap_total[b, g, y]
                    else:
                        P_diff = model.P_gen[b, g, y, s, i] - model.P_gen[b, g, y, s, i-1]
                        return P_diff <= model.G_ramp[g]*model.P_cap_total[b, g, y]
                else:
                    return pm.Constraint.Skip
            else:
                if i != 0:
                    P_diff = model.P_gen[b, g, y, s, i] - model.P_gen[b, g, y, s, i-1]
                    return P_diff <= model.G_ramp[g]*model.P_cap_total[b, g, y]
                else:
                    return pm.Constraint.Skip
        else:
            return pm.Constraint.Skip
    def cThermRdwn(self, model, b, g, y, s, i):
        '''
        Ramping constraint for each generator - ensures adequate ramp down - only valid for hourly simulation
        '''
        if (b, g) in self.thermal_tuple:
            if i != 0:
                P_diff = model.P_gen[b, g, y, s, i-1]-model.P_gen[b, g, y, s, i]
                return P_diff <= model.G_ramp[g]*model.P_cap_total[b, g, y]
            else:
                return pm.Constraint.Skip
        else:
            return pm.Constraint.Skip

    def cPRegMax(self, model, b, g, y, s, i):
        '''
        Ramping constraints - Regulation - 5min -- Upper Bound  
        '''
        if (b, g) in self.storage_tuple:
            return model.P_Reg[b, g, y, s, i] <= model.Pdis[b, g, y, s, i]*5*model.G_ramp[g]
        else:
            return model.P_Reg[b, g, y, s, i] <= model.P_gen[b, g, y, s, i]*5*model.G_ramp[g]

    def cPSpinMax(self, model, b, g, y, s, i):
        '''
        Ramping constraints - Spinning - 10min -- Upper Bound
        '''

        if (b, g) in self.storage_tuple:
            return model.P_Spin[b, g, y, s, i] <= model.Pdis[b, g, y, s, i]*10*model.G_ramp[g]
        else:
            return model.P_Spin[b, g, y, s, i] <= model.P_gen[b, g, y, s, i]*10*model.G_ramp[g]

    def cPFlexMax(self, model, b, g, y, s, i):
        '''
        Ramping constraints - Flexibility -- Upper Bound
        '''
        if (b, g) in self.storage_tuple:
            return model.P_Flex[b, g, y, s, i] <= model.Pdis[b, g, y, s, i]*60*model.G_ramp[g]
        else:
            return model.P_Flex[b, g, y, s, i] <= model.P_gen[b, g, y, s, i]*60*model.G_ramp[g]

    def cPRegMin(self, model, y, s, i):
        '''
        Ramping constraints - Regulation - 5min -- Lower Bound
        '''
        if s == 5:# Peak block
            return sum(model.P_Reg[b, g, y, s, i] for (b, g) in model.B_G) == 0
        else:
            return sum(model.P_Reg[b, g, y, s, i] for (b, g) in model.B_G) >= sum(model.load_full[b, y, s, i] for b in model.B) * float(self.data_handler.reg_res_req)
            # self.data_handler.scalars.loc['Reg_Res_Req']['Value'])/100
    def cPSpinMin(self, model, y, s, i):
        '''
        Ramping constraints - Spinning - 10min -- Lower Bound
        '''
        if s == 5:#Peak block
            return sum(model.P_Spin[b, g, y, s, i] for (b, g) in model.B_G) == 0
        else:
            return sum(model.P_Spin[b, g, y, s, i] for (b, g) in model.B_G) >= sum(model.load_full[b, y, s, i] for b in model.B) * float(self.data_handler.spin_res_req)
            #float(self.data_handler.scalars.loc['Spin_Res_Req']['Value'])/100

    def cPFlexMin(self, model, y, s, i):
        '''
        Ramping constraints - Flexibility -- Lower Bound
        '''

        if s == 5:#Peak block
            return sum(model.P_Flex[b, g, y, s, i] for (b, g) in model.B_G) == 0
        else:
            return sum(model.P_Flex[b, g, y, s, i] for (b, g) in model.B_G) >= sum(model.P_gen[b, g, y, s, i] for (b, g) in model.B_G_wind) * float(self.data_handler.flex_res_w_req) + sum(model.P_gen[b, g, y, s, i] for (b, g) in model.B_G_pv) * float(self.data_handler.flex_res_s_req)
            # self.data_handler.scalars.loc['Flex_Res_W_Req']['Value'])/100
            # self.data_handler.scalars.loc['Flex_Res_S_Req']['Value'])/100
        
    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    3.) Renewable Generator Constraints
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''

    def cPVExist(self, model, b, g, y, s, i):
        '''
        Existing PV generator dispatch
        '''
        if (b, g) in self.upv_tuple:
            return model.P_gen[b, g, y, s, i] == model.solar_ex[b, g, y, s, i] - model.Curt[b, g, y, s, i]


        else:
            return pm.Constraint.Skip



    def cPVCand(self, model, b, g, y, s, i):
        '''
        Candidate PV generator dispatch
        '''
        if (b, g) in self.solar_can_tuple:

            return model.P_gen[b, g, y, s, i] == model.solar_can_cf[b, g, y, s, i]*model.P_cap_total[b, g, y] - model.Curt[b, g, y, s, i]

        else:
            return pm.Constraint.Skip

    def cWindExist(self, model, b, g, y, s, i):
        '''
        Existing Wind generator dispatch
        '''
        if (b, g) in self.wind_ex_tuple:
            return model.P_gen[b, g, y, s, i] == model.wind_ex[b, g, y, s, i] - model.Curt[b, g, y, s, i]

        else:
            return pm.Constraint.Skip

    def cWindCan(self, model, b, g, y, s, i):
        '''
        Candidate Wind generator dispatch
        '''
        if (b, g) in self.wind_can_tuple:

            return model.P_gen[b, g, y, s, i] == model.wind_can_cf[b, g, y, s, i]*model.P_cap_total[b, g, y] - model.Curt[b, g, y, s, i]

        else:
            return pm.Constraint.Skip

    def cCurtMax(self, model, b, g, y, s, i):
        '''
        Limit curtailment to only renewable generators 
        '''
        if (b, g) in self.ren_tuple:
            return model.Curt[b, g, y, s, i] <= model.P_gen[b, g, y, s, i]
        elif (b, g) not in self.ren_tuple:
            return model.Curt[b, g, y, s, i] == 0
        else:
            return pm.Constraint.Skip


    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    4.) Policy constraints
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''

    def cRenAnnual(self, model, b, g, y):
        '''
        Annual renewable generation calculation
        '''

        return model.ren_gen[b, g, y] == sum(model.season_time_weight[s,i]*(model.P_gen[b, g, y, s, i]-model.Curt[b, g, y, s, i])
                                             for (s, i) in model.S_I)


    def cRPS(self, model, y):
        '''
        Renewable portfolio standard constraint
        '''

        return sum(model.ren_gen[b, g, y] for (b, g) in model.B_G_ren) >= model.RPS[y]*(sum(model.season_time_weight[s,i]*model.load_full[b, y, s, i] for (s, i) in model.S_I for b in model.B))


    def cCO2emm(self, model, b, g, y):
        '''
        CO2 emission constraint - carbon intensity calculations
        '''
        if (b, g) in model.B_G_ng and (b, g) in model.B_G_can and y >= 2040:
            return model.CO2_emission[b, g, y] == 0
        else:
            #*(1-model.G_for[g])
            return model.CO2_emission[b, g, y] == sum(model.season_time_weight[s,i]*(model.gen_CO2[g]*(model.P_gen[b, g, y, s, i] + model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i]+model.P_Flex[b, g, y, s, i]))
                                                      for (s, i) in model.S_I)

    def cCO2int(self, model, y):
        '''
        CO2 emission constraint - carbon intensity calculations
        '''
        return model.CO2_intensity[y] == sum(model.CO2_emission[b, g, y] for (b, g) in model.B_G_carbon)/sum(model.season_time_weight[s,i]*(model.load_full[b, y, s, i]) for b in model.B for (s, i) in model.S_I)

    # Define constraint in model

    def cCO2intLimit(self, model, y):
        '''
        CO2 emission constraint - carbon intensity calculations
        '''

        return model.CO2_intensity[y] <= model.CO2_int[y]
        '''
        if y > all_years[0]:
            return sum(model.CO2_emission[b, g, y] for (b, g) in model.B_G) <= (1-model.CO2[y])*sum(model.CO2_emission[b, g, all_years[0]] for (b, g) in model.B_G)
        elif y == all_years[0]:
            return sum(model.CO2_emission[b, g, y] for (b, g) in model.B_G) <= 1.2*6197206
        '''
    

    def cCO2emmLimit(self, model, y):
        '''
        CO2 emission-free generation (% of generation)
        '''
        
        return sum(model.carbon_gen[b, g, y]for (b, g) in model.B_G_carbon) <= (1-model.CO2[y])*sum(model.season_time_weight[s,i]*(model.P_gen[b, g, y, s, i] + model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i]+model.P_Flex[b, g, y, s, i]) for (s, i) in model.S_I for (b, g) in model.B_G)


    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    5.) Transmission constraints
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''
    def cTxFlwBounds(self, model, l, y, s, i):
        fw_cap = model.line_ex_fw_cap[l] + model.L_cap_total[l, y]
        bw_cap = model.line_ex_bw_cap[l] + model.L_cap_total[l, y]

        if self.data_handler.tx_model == 'Transportation':
            if self.system == 'PNM':
                if l == 5 and y > 2033:
                    bw_cap += 1000
            # forward/backward unified
            return inequality(-bw_cap, model.PF[l, y, s, i], fw_cap)

        elif self.data_handler.tx_model == 'dc':
            return inequality(-bw_cap, model.PF[l, y, s, i], fw_cap)
    def cTxFlwUpper(self, model, l, y, s, i):
        fw_cap = model.line_ex_fw_cap[l]
        inv = model.L_cap_total[l, y]
        return model.PF[l, y, s, i] <= fw_cap + inv

    def cTxFlwLower(self, model, l, y, s, i):
        bw_cap = model.line_ex_bw_cap[l]
        inv = model.L_cap_total[l, y]
        return model.PF[l, y, s, i] >= - (bw_cap + inv)
    
    def cDCPF(self,model, l, y, s, i):
        fb = model.from_bus[l]
        tb = model.to_bus[l]
        theta_diff = model.theta[fb, y, s, i] - model.theta[tb, y, s, i]
        return ( (1e-3/self.mva_base) * model.PF[l, y, s, i]
            - (1e-3/model.line_X[l]) * theta_diff
            == 0 )
        
    def cThetaDiffMax(self,model, l, y, s, i):
        theta_diff = model.theta[model.from_bus[l], y, s, i] - model.theta[model.to_bus[l], y, s, i]
        return theta_diff <= np.pi/6

    def cThetaDiffMin(self,model, l, y, s, i):
        theta_diff = model.theta[model.from_bus[l], y, s, i] - model.theta[model.to_bus[l], y, s, i]
        return theta_diff >= -np.pi/6

    
                                            
    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    6.) Power balance
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''
    def cPwrBal(self, model, b, y, s, i):
        '''
        Power Balance constraint
        TODO: remove for and if statements as they are expensive in pyomo
        '''
        
        out_branches = [l[0] for l in self.data_handler.line_bus_num if l[1]==b]
        in_branches = [l[0] for l in self.data_handler.line_bus_num if l[2]==b]
    
        
        gen_nums = self.data_handler.bus_gen_num.loc[self.data_handler.bus_gen_num['Bus_num']
                                                     == b]['Gen_num'].values.astype(int)
        
        gen_ren_nums = np.intersect1d(
            gen_nums, self.data_handler.tech_nums['renewables'])

        gen_sto_nums = np.intersect1d(
            gen_nums, self.data_handler.tech_nums['storage'])
        
        return sum(model.P_gen[b, g, y, s, i] for g in gen_nums) + sum(model.Pdis[b, g, y, s, i]-model.Pcha[b, g, y, s, i] for g in gen_sto_nums)\
            - sum(model.Curt[b, g, y, s, i] for g in gen_ren_nums) + sum(model.PF[l, y, s, i] for l in in_branches) \
                - sum(model.PF[l, y, s, i] for l in out_branches) == model.load_full[b, y, s, i] - model.LNS[b, y, s, i]#-model.dummy[b, y, s, i] 

    def cPwrBal_CopperSheet(self, model, y, s, i):
        '''
        Power Balance constraint - copper sheet
        '''
        gen_nums = self.data_handler.bus_gen_num['Gen_num'].values.astype(int)
        
        gen_ren_nums = np.intersect1d(
            gen_nums, self.data_handler.tech_nums['renewables'])

        gen_sto_nums = np.intersect1d(
            gen_nums, self.data_handler.tech_nums['storage'])

        return sum(model.P_gen[b, g, y, s, i] for (b,g) in model.B_G) + sum(model.Pdis[b, g, y, s, i]-model.Pcha[b, g, y, s, i] for (b,g) in model.B_G_sto) - sum(model.Curt[b, g, y, s, i] for (b,g) in model.B_G_ren) == sum(model.load_full[b, y, s, i] - model.LNS[b, y, s, i] for b in model.B)

        
    def cLNSMax(self, model, b, y, s, i):
        '''
        Ensure load shed does not exceed the demand for that time step 
        '''
        
        return model.LNS[b, y, s, i] <= model.load_full[b, y, s, i]

    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    7.) Investment Constraints
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''

    def cPCapTotal(self, model, b, g, y):
        '''
        Cumulative  generation capacity
        TODO: address with lead times for technologies
        '''
        if (b, g) in self.candidate_tuple:
            if self.data_handler.block_selection.lower() == 'Full_Year'.lower() or self.data_handler.block_selection.lower() == 'Full_Year_MY'.lower():
                return model.P_cap_total[b, g, y] == model.P_cap[g] + model.G_inv[b, g, y]
            else:
                if np.size(self.data_handler.years) >= 20:
                    if y == model.Y.at(1):
                        return model.P_cap_total[b, g, y] == model.P_cap[g]
                    if y > model.Y.at(1) and model.year_gap_array[y] <= 1 and y != model.Y.at(-1):#TODO:check the logic here
                        return model.P_cap_total[b, g, y] == model.P_cap[g] + sum(model.G_inv[b, g, y1] for y1 in range(model.Y.at(1), y-model.G_lt[g]))
                else:
                    if y == model.Y.at(1):
                        return model.P_cap_total[b, g, y] == model.P_cap[g]
                    else:
                        index = self.data_handler.years.index(y)
                        if y == self.data_handler.years[-1]:
                            yrs = self.data_handler.years[0:index+1]
                        else:
                            yrs = self.data_handler.years[0:index]
                        return model.P_cap_total[b, g, y] == model.P_cap[g] + sum(model.G_inv[b, g, y1] for y1 in yrs)
        else:
            return pm.Constraint.Skip

    def cStoreCapTotal(self, model, b, g, y):
        '''
        Cumulative ES energy capacity
        TODO: address with lead times for technologies
        '''
        if (b, g) in self.es_can_tuple:

            if self.data_handler.block_selection.lower() == 'Full_Year'.lower():#TODO: fix this!!
                return model.Store[b, g, y] == model.P_cap[g]*model.es_min_duration[g]+model.Sto_inv[b, g, y]
            else:
                if model.year_gap_array[y] <= 1 and y != model.Y.at(-1):
                    return model.Store[b, g, y] == model.P_cap[g]*model.es_min_duration[g]+sum(model.Sto_inv[b, g, y1] for y1 in range(model.Y.at(1), y-model.G_lt[g]))
                else:
                    return model.Store[b, g, y] == model.P_cap[g]*model.es_min_duration[g]+sum(model.Sto_inv[b, g, y1] for y1 in self.data_handler.years[0:np.where(np.array(self.data_handler.years) == y)[0][0]])
        else:
            return pm.Constraint.Skip


    def cRetirements(self, model, b, g, y):
        '''
        P_cap_total calculations & generation retirements
        '''
        if (b, g) in self.exist_tuple:
            if self.data_handler.custom_retirement and (self.data_handler.ng_retirement_year is not None or self.data_handler.nuclear_retirement_year is not None or self.data_handler.coal_retirement_year is not None or self.data_handler.oil_retirement_year is not None):
                if (b, g) in model.B_G_ng and y>=self.data_handler.ng_retirement_year:
                    return model.P_cap_total[b, g, y] == 0
                elif (b, g) in model.B_G_nuc and y>=self.data_handler.nuclear_retirement_year:
                    return model.P_cap_total[b, g, y] == 0
                elif (b, g) in model.B_G_coal and y>=self.data_handler.coal_retirement_year:
                    return model.P_cap_total[b, g, y] == 0
                elif (b, g) in model.B_G_oil and y>=self.data_handler.oil_retirement_year:
                    return model.P_cap_total[b, g, y] == 0
                else:
                    if y >= model.gen_ret_yr[g] and y >= model.gen_planned_yr[g]:
                        return model.P_cap_total[b, g, y] == model.P_cap[g]-model.gen_ret_cap[g]
                    elif y >= model.gen_planned_yr[g] and y < model.gen_ret_yr[g]:
                        return model.P_cap_total[b, g, y] == model.P_cap[g]
                    elif y < model.gen_ret_yr[g]:
                        return model.P_cap_total[b, g, y] == model.P_cap[g]
                    elif y < model.gen_planned_yr[g]:
                        return model.P_cap_total[b, g, y] == 0
            else:
                if y >= model.gen_ret_yr[g] and y >= model.gen_planned_yr[g]:
                    return model.P_cap_total[b, g, y] == model.P_cap[g]-model.gen_ret_cap[g]
                elif y >= model.gen_planned_yr[g] and y < model.gen_ret_yr[g]:
                    return model.P_cap_total[b, g, y] == model.P_cap[g]
                elif y < model.gen_ret_yr[g]:
                    return model.P_cap_total[b, g, y] == model.P_cap[g]
                elif y < model.gen_planned_yr[g]:
                    return model.P_cap_total[b, g, y] == 0
        else:
            return pm.Constraint.Skip

    def cBusInvMaxAnnual(self, model, b, g, y):
        '''
        Planning horizon investment constraints
        '''
        if (b, g) in self.cand_tuple:
            if self.data_handler.block_selection.lower() == 'Full_Year'.lower():
                if self.data_handler.ldes_switch is False and (b, g) in model.B_G_ldes:
                    return model.G_inv[b, g, y] <= 0
                else:
                    return model.G_inv[b, g, y] <= 20*model.P_cap_cand[g]#relax constraint for now
            else:                
                if self.data_handler.ldes_switch is False and (b, g) in model.B_G_ldes:
                    return model.G_inv[b, g, y] <= 0
                else:
                    if y == model.Y.at(-1):
                        return model.G_inv[b, g, y] <= 20*model.P_cap_cand[g] #relax constraint for now...
                    else:
                        return model.G_inv[b, g, y] <= model.year_gap_array[y]*model.P_cap_cand[g]
        else:
            return pm.Constraint.Skip

    
    def cBusInvMaxTotal(self, model, b, g):#cjn - removed year index
        '''
        Maximum invested cumulative capacities of candidate technologies by bus
        '''
        return sum(model.G_inv[b, g, y] for y in model.Y) <= model.P_cap_syst_max[g]
    
    def cSystWindMax(self, model):
        '''
        Maximum system wind capacity
        '''
        if self.data_handler.system_wide_wind_max is not None:
            scale = 1000.0
            return sum(model.G_inv[b, g, y]/scale for (b, g) in self.wind_can_tuple for y in model.Y) <= self.data_handler.system_wide_wind_max/scale
        else:
            return pm.Constraint.Skip

    def cSystPVMax(self, model):
        '''
        Maximum system solar capacity
        
        '''
        if self.data_handler.system_wide_solar_max is not None:
            scale = 1000.0
            return sum(model.G_inv[b, g, y]/scale for (b, g) in self.solar_can_tuple for y in model.Y) <= self.data_handler.system_wide_solar_max/scale
        else:
            return pm.Constraint.Skip
     
    def cSystGasMax(self, model):
        '''
        Maximum system gas capacity
        
        '''
        if self.data_handler.system_wide_gas_max is not None:
            scale = 1000.0
            return sum(model.G_inv[b, g, y]/scale for (b, g) in model.B_G_ng_can for y in model.Y) <= self.data_handler.system_wide_gas_max/scale
        else:
            return pm.Constraint.Skip
        
    def cResourceByBus(self, model, b, g):
        '''Custom constraint'''
        if (b, g) in self.wind_can_tuple:
            return sum(model.G_inv[b, g, y] for y in model.Y) <= model.wind_max[b]
        elif (b, g) in self.solar_can_tuple:
            return sum(model.G_inv[b, g, y] for y in model.Y) <= model.solar_max[b]
        elif (b, g) in model.B_G_sto_cand:
            return sum(model.G_inv[b, g, y] for y in model.Y) <= model.storage_max[b]
        else:
            return pm.Constraint.Skip
    '''
    7b.) Cumulative  transmission capacity
    '''

    
    def cTxCapTotalnoDelay(self,model, l, y, y1):
        '''
        Transmission total invested capacity calculation
        '''
        if self.data_handler.trans_expansion is True:
            
            if y1 <= y:
                return model.L_cap_total[l, y] == sum(model.LineCap[l, y1] for y1 in model.Y1)
            elif y==self.data_handler.years[0]:
                return model.L_cap_total[l, y] == model.LineCap[l, y]
            else:
                return pm.Constraint.Skip
        else:
            return model.L_cap_total[l, y] == 0
    

    def cTxCapTotalwDelay(self, model, l, y):
        '''
        TODO: Optional constraint
        '''
     
        if np.size(self.data_handler.years) >= model.line_lt[l] and y-model.line_lt[l] in self.data_handler.years:
            # range(model.Y.at(1), y-model.line_lt[l]))
            return model.L_cap_total[l, y] == sum(model.LineCap[l, y1] for y1 in self.data_handler.years[0:np.where(np.array(self.data_handler.years) == y-model.line_lt[l])[0][0]])
        elif np.size(self.data_handler.years) <= model.line_lt[l]:
            return model.L_cap_total[l, y] == 0
        else:
            return pm.Constraint.Skip

    def cTxCapInvMax(self, model, l):
        """
        Enforce candidate line investment capacity
        """
        scale = 1000.0
        return sum(model.LineCap[l, y]/scale for y in model.Y) <= model.line_ex_limit[l]/scale
        

    def cTxCapSystMax(self, model):
        """
        Enforce system-wide transmission investment capacity
        """
        scale = 1000.0
        if self.data_handler.system_wide_tx_expansion_max is not None:
            if self.data_handler.trans_expansion is False:
                return sum(model.LineCap[l, y] for l in model.L for y in model.Y) <= 0
            elif self.data_handler.trans_expansion is True:
                return sum(model.LineCap[l, y]/scale for l in model.L for y in model.Y) <= self.data_handler.system_wide_tx_expansion_max/scale
            else:
                return pm.Constraint.Skip
        else:
            if self.data_handler.trans_expansion is False:
                return sum(model.LineCap[l, y] for l in model.L for y in model.Y) <= 0
            else:
                return pm.Constraint.Skip
            

    def cTechAvail(self, model, b, g, y):
        """
        Ensure technology is not invested before its availability year
        """
        if y < model.G_y_avail[g]:
            return model.G_inv[b, g, y] == 0
        else:
            return pm.Constraint.Skip


    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    8.) Reliability & Resilience constraints
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''

    def cPRM(self, model, y):
        """
        Planning reserve margin constraint
        TODO: Add piecewise ELCC or dynamic elcc curves for PRM calculations OR Seasonal ELCC 
        """
        scale = 1000.0
        return sum(model.G_cc[g]*model.P_cap_total[b, g, y]/scale for (b, g) in model.B_G) >= (1+float(self.data_handler.prm)) * model.PEAK[y]/scale
        # self.data_handler.scalars.loc['PRM']['Value'])/100
    
    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    9.) Demand Response & Energy Efficiency - this is a work in progress for later release
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''

    def cDRMax(self, model, b, g, y, s, i):
        """
        Demand response limits
        """
        if s == 3:
            if i in np.arange(24, 144):
                return model.P_gen[b, g, y, s, i] <= 0.1*model.load_full[b, y, s, i]
            else:
                return model.P_gen[b, g, y, s, i] == 0
        else:
            return model.P_gen[b, g, y, s, i] == 0


    def cDRgenMax(self, model, b, g, y, s, i):
        """
        Demand response limits
        TODO: fix constraint
        """
        return model.P_gen[b, g, y, s, i] <= model.P_cap_total[b, g, y]


    def cDRnoAnc(self, model, b, g, y, s, i):
        """
        Demand response limits
        TODO: fix constraint
        """
        return model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i] + model.P_Flex[b, g, y, s, i] == 0


    def cDRopMax(self, model, b, g, y):
        """
        Demand response limits
        TODO: fix constraint
        """
        # Only allowed to use DR in 100 hours per year
        return sum(model.P_gen[b, g, y, s, i] for (s, i) in model.S_I) <= (100/8760)*sum(model.load_full[b, y, s, i] for (s, i) in model.S_I)

    def cDRSystMax(self, model, b, g):
        """
        Demand response limits
        TODO: fix constraint
        """
        return sum(model.G_inv[b, g, y] for y in model.Y) <= 25

    def cDRnoInv(self, model, b, g, y):
        """
        Demand response limits
        TODO: fix constraint and remove hard code
        """
        if b in [3, 4, 5, 6, 7]:
            return model.P_cap_total[b, g, y] == 0
        else:
            return pm.Constraint.Skip
    '''
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    10.) Objective Function & Cost Breakdown
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    '''
    
    def cGenInvCostAnnual(self, model, y):
        """
        Define annual generation investment costs
        """
        
        return model.annual_gen_inv_cost[y] == model.CostScale*model.dis_factor[y]*(sum((model.C_g[g, y]+model.G_tx_add[g])*1000*model.G_inv[b, g, y] for (b, g) in model.B_G_can_no_es) +
                                                                    sum((model.C_g_es_pwr[g, y]+model.G_tx_add[g])*1000*model.G_inv[b, g, y] for (b, g) in model.B_G_sto_cand) +
                                                                    sum(model.C_g_es_energy[g, y]*1000*model.Sto_inv[b, g, y] for (b, g) in model.B_G_sto_cand))

    def cNGH2Costconv(self, model, y):
        '''
        Define hydrogen conversion costs
        **Optional cost**
        '''
        
        if y == model.Y.at(-1):
            return model.ng_h2_conv_cost[y] == model.CostScale*model.dis_factor[y]*1200*1000*sum(model.G_inv[b, g, y1] for (b, g) in model.B_G_ng_can for y1 in self.data_handler.years[0:np.where(np.array(self.data_handler.years) == y)[0][0]])
        elif y > model.Y.at(-1):
            return model.ng_h2_conv_cost[y] == model.CostScale*self.dis_factor[y]*1200*1000*sum(model.G_inv[b, g, y] for (b, g) in model.B_G_ng_can)
        else:
            return model.ng_h2_conv_cost[y] == 0

    def cTxInvCostAnnual(self, model, y):
        """
        Define annual transmission investment costs
        """
        
        return model.annual_trans_inv_cost[y] == model.CostScale*model.dis_factor[y]*sum(model.line_cost[l]*model.LineCap[l, y] for l in model.L)


    def cESReplaceCostSum(self, model):
        """
        Total energy storage lifetime costs
        """
        
        if self.data_handler.es_lifetime_cost_option == True:     
            return model.annual_es_replace_cost == sum(model.annual_es_replace_cost_gen[b, g] for (b, g) in model.B_G_sto_cand)
        else:
            return pm.Constraint.Skip
    def cESReplaceCost(self, model, b, g):
        """
        Energy storage lifetime extension costs for each storage device
        """
        
        if self.data_handler.es_lifetime_cost_option == True: 
            if model.G_lifetime[g] < self.data_handler.es_lifetime_extension :
                y1 = self.data_handler.years[-1]
                return model.annual_es_replace_cost_gen[b, g] == model.CostScale*int(self.data_handler.es_lifetime_extension/model.G_lifetime[g])*model.dis_factor[y1]*(sum((model.C_g_es_pwr[g, y]+model.G_tx_add[g])*1000*model.G_inv[b, g, y] for y in model.Y) +
                                                                                                                   sum(model.C_g_es_energy[g, y]*1000*model.Sto_inv[b, g, y] for y in model.Y))
            else:
                return model.annual_es_replace_cost_gen[b, g] == 0
        else:
            return model.annual_es_replace_cost_gen[b, g] == 0
    def cFOMCostAnnual(self, model, y):
        """
        Define annual fixed operating & maintenance costs
        """
        
        if y < model.Y.at(-1):
            return model.annual_fom_cost[y] == model.CostScale*model.year_gap_array[y]*model.dis_factor[y]*sum(model.P_cap_total[b, g, y]*model.G_fom[g] for (b, g) in model.B_G)
        elif y == model.Y.at(-1):
            return model.annual_fom_cost[y] == model.CostScale*model.dis_factor_end_eff[y]*sum(model.P_cap_total[b, g, y]*model.G_fom[g] for (b, g) in model.B_G)

    def cVOMCostAnnual(self, model, y):
        """
        Define annual variable operating & maintenance costs
        """
        
        if y < model.Y.at(-1):
            return model.annual_vom_cost[y] == model.CostScale*model.year_gap_array[y]*model.dis_factor[y]*(sum(model.season_time_weight[s,i]*(model.P_gen[b, g, y, s, i] + model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i] + model.P_Flex[b, g, y, s, i])*model.G_vom[g] for (b, g) in model.B_G for (s, i) in model.S_I)+
                                                                                            sum(model.season_time_weight[s,i]*(model.Pcha[b, g, y, s, i] +model.Pdis[b, g, y, s, i] + model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i] + model.P_Flex[b, g, y, s, i])*model.G_vom[g] for (b, g) in model.B_G_sto for (s, i) in model.S_I))
        elif y == model.Y.at(-1):
            return model.annual_vom_cost[y] == model.CostScale*model.dis_factor_end_eff[y]*(sum(model.season_time_weight[s,i]*(model.P_gen[b, g, y, s, i] + model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i] + model.P_Flex[b, g, y, s, i])*model.G_vom[g] for (b, g) in model.B_G for (s, i) in model.S_I)+
                                                                                sum(model.season_time_weight[s,i]*(model.Pcha[b, g, y, s, i] +model.Pdis[b, g, y, s, i] + model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i] + model.P_Flex[b, g, y, s, i])*model.G_vom[g] for (b, g) in model.B_G_sto for (s, i) in model.S_I))

    def cFuelCostAnnual(self, model, y):
        """
        Define annual fuel costs
        """
        
        if y < model.Y.at(-1):
            return model.annual_fuel_cost[y] == model.CostScale*model.year_gap_array[y]*model.dis_factor[y]*sum(model.season_time_weight[s,i]*(model.P_gen[b, g, y, s, i] + model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i] + model.P_Flex[b, g, y, s, i])*model.G_hr[g]*model.G_fp[g,y] for (b, g) in model.B_G_thermal for (s, i) in model.S_I)
        elif y == model.Y.at(-1):
            return model.annual_fuel_cost[y] == model.CostScale*model.dis_factor_end_eff[y]*sum(model.season_time_weight[s,i]*(model.P_gen[b, g, y, s, i] + model.P_Reg[b, g, y, s, i] + model.P_Spin[b, g, y, s, i] + model.P_Flex[b, g, y, s, i])*model.G_hr[g]*model.G_fp[g,y] for (b, g) in model.B_G_thermal for (s, i) in model.S_I)

    def cLNSCostAnnual(self, model, y):
        """
        Define load shed penalty cost
        """
        
        return model.annual_ls_cost[y] == model.CostScale*model.year_gap_array[y]*sum(model.season_time_weight[s,i]*model.LNS[b, y, s, i]*100*float(self.data_handler.voll) for b in model.B for (s, i) in model.S_I)#10000*
        # self.data_handler.scalars.loc['VOLL']['Value']
    def cITCAnnual(self, model, y):
        """
        Define investment tax credit incentives
        """
        
        if self.data_handler.tax_credits_option == True:
            if y <= self.tax_credit_end_year:
                return model.annual_itc[y] == model.CostScale*model.dis_factor[y]*(sum(model.G_itc[g]*model.C_g[g, y]*1000*model.G_inv[b, g, y] for (b, g) in model.B_G_ren_can)+sum(model.G_itc[g]*model.C_g_es_pwr[g, y]*1000*model.G_inv[b, g, y] for (b, g) in model.B_G_sto_cand) +
                                                                       sum(model.G_itc[g]*model.C_g_es_energy[g, y]*1000*model.Sto_inv[b, g, y] for (b, g) in model.B_G_sto_cand))
            else:
                return model.annual_itc[y] == 0
        else:
            return model.annual_itc[y] == 0

    def cPTCAnnual(self, model, y):
        """
        Define production tax credit incentives
        """
        
        if self.data_handler.tax_credits_option == True:
            return model.annual_ptc[y] == model.CostScale*model.year_gap_array[y]*model.dis_factor[y]*sum(model.season_time_weight[s,i]*(model.P_gen[b, g, y, s, i])*model.G_ptc[g] for (b, g) in model.B_G_ren_can for (s, i) in model.S_I)
        else:
            return model.annual_ptc[y] == 0
        
    def cTotalCostAnnual(self, model, y):
        """
        Define total annual costs
        """
        return model.annual_total_cost[y] == model.annual_gen_inv_cost[y]+ model.annual_trans_inv_cost[y] + model.annual_fom_cost[y] + model.annual_vom_cost[y] + model.annual_fuel_cost[y] + model.annual_ls_cost[y]-model.annual_itc[y]-model.annual_ptc[y]+model.ng_h2_conv_cost[y]

    def cOBJ(self, model):
        """
        Define objective function to mimimize
        """
        scale_factor = 1
        return (sum(model.annual_total_cost[y] for y in model.Y)+model.annual_es_replace_cost)/scale_factor

    
    
    
