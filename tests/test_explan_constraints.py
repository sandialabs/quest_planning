import pytest
import pyomo.environ as pm
import pandas as pd
import numpy as np
from quest_planning.explan.explan_data_handler import ExplanDataHandler
from quest_planning.explan.explan_optimizer import ExplanOptimizer
from quest_planning.explan.explan_constraints import ExplanConstraints

@pytest.fixture
def mock_data_handler(tmp_path):
    # Setup minimal required CSVs for a valid ExplanDataHandler
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    # Scalars
    pd.DataFrame({'Scalar': ['load_growth', 'soc_max', 'soc_min', 'reg_res_req', 'spin_res_req', 'flex_res_req', 'voll', 'prm'],
                  'Value': [1.5, 1.0, 0.2, 0.01, 0.01, 0.01, 10000, 0.15]}).to_csv(data_dir / "scalars.csv", index=False)

    # Tech
    # Tech_Num: 1=Nuclear, 2=Gas, 3=Wind, 4=Solar, 5=Storage
    pd.DataFrame({
        'Tech_Num': [1, 2, 3, 4, 5],
        'Tech': ['Nuclear', 'Gas', 'Wind', 'Solar', 'Storage'],
        'Tech_Name': ['Nuclear', 'Gas', 'Wind', 'Solar', 'Storage'],
        'Lead_Time': [10, 2, 2, 2, 2],
        'CandCap': [1000, 1000, 1000, 1000, 1000],
        'RampRate': [0.1, 0.5, 1.0, 1.0, 1.0],
        'FOM': [10, 10, 10, 10, 10],
        'VOM': [2, 2, 2, 2, 2],
        'PTC': [0, 0, 0.01, 0.01, 0],
        'ITC': [0, 0, 0.1, 0.1, 0.1],
        'CapCred': [0.9, 0.9, 0.3, 0.2, 0.9],
        'Lifetime': [40, 30, 20, 20, 15]
    }).to_csv(data_dir / "tech.csv", index=False)

    # Gen
    pd.DataFrame({
        'Gen_num': [1, 2, 3, 4, 5],
        'Gen_name': ['Gen1', 'Gen2', 'Gen3', 'Gen4', 'Gen5'],
        'Tech': ['Nuclear', 'Gas', 'Wind', 'Solar', 'Storage'],
        'Bus_num': [101, 101, 101, 101, 101],
        'Bus': ['Bus101']*5,
        'Cap': [1000, 1000, 1000, 1000, 1000],
        'MinCap': [200, 100, 0, 0, 0],
        'CandCap': [0, 0, 0, 0, 0],
        'PlannedYr': [2020, 2020, 2020, 2020, 2020],
        'RetYr': [2060, 2060, 2060, 2060, 2060],
        'CapCred': [0.9, 0.9, 0.3, 0.2, 0.9],
        'LeadTime': [10, 2, 2, 2, 2],
        'YearAvail': [2020, 2020, 2020, 2020, 2020],
        'HR': [10, 10, 0, 0, 0],
        'FOM': [2, 2, 2, 2, 2],
        'VOM': [1, 1, 1, 1, 1],
        'PTC': [0, 0, 0.01, 0.01, 0],
        'ITC': [0, 0, 0.1, 0.1, 0.1],
        'Lifetime': [40, 30, 20, 20, 15],
        'Ramp': [0.1, 0.5, 1.0, 1.0, 1.0],
        'FOR': [0.05, 0.05, 0.05, 0.05, 0.05],
        'CO2': [0, 500, 0, 0, 0],
        'SO2': [0, 1, 0, 0, 0],
        'NO2': [0, 1, 0, 0, 0],
        'SystCap': [1000, 1000, 1000, 1000, 1000],
        'RetCap': [0, 0, 0, 0, 0],
        'TransAdder': [0, 0, 0, 0, 0],
        'Tech_Num': [1, 2, 3, 4, 5]
    }).to_csv(data_dir / "gen.csv", index=False)

    # Branch
    pd.DataFrame({
        'Line_Number': [1, 2],
        'From_Bus_Number': [101, 101],
        'To_Bus_Number': [102, 102],
        'From_Bus_Name': ['Bus101', 'Bus101'],
        'To_Bus_Name': ['Bus102', 'Bus102'],
        'Capacity': [1000, 1000],
        'X': [0.1, 0.1],
        'Rating_F': [1000, 1000],
        'Rating_B': [1000, 1000],
        'Tx_cost': [100, 100],
        'Tx_limit': [1000, 1000],
        'Lead_Time': [2, 2]
    }).to_csv(data_dir / "branch.csv", index=False)

    # Bus
    pd.DataFrame({
        'Bus_num': [101, 102],
        'Bus_number': [101, 102],
        'Bus_name': ['Bus101', 'Bus102'],
        'LAT': [30, 31],
        'LON': [-90, -91],
        'Load_share': [0.6, 0.4],
        'Region': [1, 1]
    }).to_csv(data_dir / "bus.csv", index=False)

    # Policy
    pd.DataFrame({'Years': [2020], 'RPS': [0.1], 'CO2': [50], 'CO2_intensity': [0.5]}).to_csv(data_dir / "policy.csv", index=False)

    # Load
    load_df = pd.DataFrame({
        'datetime': pd.date_range(start='2020-01-01', periods=24, freq='h'),
        'year': [2020]*24,
        'day': pd.date_range(start='2020-01-01', periods=24, freq='h').date,
        'load_forecast': np.random.rand(24) * 1000
    })
    load_df.to_csv(data_dir / "load.csv", index=False)

    # Renewable profiles
    ren_cols = {'datetime': pd.date_range(start='2020-01-01', periods=24, freq='h'), 'val': np.random.rand(24)}
    for key in ['solar_cand', 'solar', 'wind_cand', 'wind']:
        pd.DataFrame(ren_cols).to_csv(data_dir / f"{key}.csv", index=False)

    # Storage
    pd.DataFrame({
        'Gen_num': [5],
        'RTE': [0.9],
        'Charge_Eff': [0.95],
        'Discharge_Eff': [0.95],
        'Duration': [4],
        'Min_Duration': [1],
        'Max_Duration': [10]
    }).to_csv(data_dir / "storage.csv", index=False)

    for key in ['prm', 'gen_viz', 'capex_es', 'capex_h_es', 'capex_l_es', 'capex_tech', 'fuel', 'cap_cred']:
        pd.DataFrame({'Column1': [0]}).to_csv(data_dir / f"{key}.csv", index=False)

    handler = ExplanDataHandler()
    handler.data_dir = str(data_dir)
    handler.set_data_ls_index(None)
    handler.get_data()
    handler.start_year = 2020
    handler.end_year = 2020
    handler.years = [2020]
    handler.year_gap_array = [1]
    handler.set_block_selection('Peak_Day')
    handler.discount_rate = 5.0
    handler.base_currency_year = 2020
    handler.M = 24
    handler.S = 1
    handler.hour_duration = [365]
    handler.season_time_duration = {(1, i): 365 for i in range(24)}
    handler.line_bus_num = [(1, 101, 102), (2, 101, 102)]
    handler.large_load_option = False
    handler.tx_model = 'dc'
    handler.reserves_option = True
    handler.rps_policy = True
    handler.co2_policy = True
    handler.co2_intensity_policy = True
    handler.tax_credits_option = True
    handler.custom_retirement = False
    handler.trans_expansion = True
    handler.resource_bus_limit_dict = None
    handler.regional_load_growth = None
    handler.es_lifetime_cost_option = False
    handler.load_blocks = pd.DataFrame(np.random.rand(24, 1), columns=['2020'])
    handler.load_forecast = 'load_forecast'
    handler.system = 'TestSystem'
    handler.ini_level = 0.5
    handler.year_gap = 1
    handler.tax_credit_end_year = 2030
    handler.dt_info = {'2020': pd.date_range(start='2020-01-01', periods=8760, freq='h')}
    handler.bus_upv_ex_num = [101]
    handler.bus_solar_can_num = [101]
    handler.bus_wind_ex_num = [101]
    handler.bus_wind_can_num = [101]
    handler.tech_nums = {
        'renewables': [3, 4],
        'storage': [5],
        'storage_cand': [5],
        'storage_cand_year': [],
        'candidates': [2, 3, 4, 5],
        'upv_ex': [4],
        'upv_can': [4],
        'wind_ex': [3],
        'wind_can': [3],
        'dr': [],
        'exist': [1, 3, 4],
        'thermal': [1, 2],
        'nuclear': [1],
        'coal': [],
        'oil': [],
        'ng': [2],
        'ldes': [],
        'large_load_gen': [],
        'large_load_sto': []
    }

    return handler

def test_explan_constraints_initialization(mock_data_handler):
    """Test if ExplanConstraints initializes correctly with a data handler."""
    constraints = ExplanConstraints(mock_data_handler)
    assert constraints.data_handler == mock_data_handler
    assert constraints.system == mock_data_handler.system
    assert hasattr(constraints, 'storage_tuple')
    assert hasattr(constraints, 'thermal_tuple')

def test_explan_constraints_set_expressions(mock_data_handler):
    """Test if instantiate_model correctly sets up the model structure with all required sets."""
    optimizer = ExplanOptimizer(mock_data_handler, solver={'solver': 'cbc'})
    optimizer.instantiate_model()

    model = optimizer.model

    # Check if key sets were created on the model
    assert hasattr(model, 'B')
    assert hasattr(model, 'G')
    assert hasattr(model, 'Y')
    assert hasattr(model, 'S_I')
    assert hasattr(model, 'L')

    # Check bus-gen pair sets created by instantiate_model
    assert hasattr(model, 'B_G')
    assert hasattr(model, 'B_G_thermal')
    assert hasattr(model, 'B_G_sto')
    assert hasattr(model, 'B_G_ren')
    assert hasattr(model, 'B_G_ldes')
    assert hasattr(model, 'B_G_ng')

    # Verify dimensions based on mock data
    assert len(model.B) == 2  # 2 buses
    assert len(model.G) == 5  # 5 generators
    assert len(model.Y) == 1  # 1 year
    assert len(model.L) == 2  # 2 branches

def test_explan_constraints_logic_skip(mock_data_handler):
    """Test that constraints return pm.Constraint.Skip when not applicable."""
    constraints = ExplanConstraints(mock_data_handler)
    model = pm.ConcreteModel()

    # Mock some minimal model attributes needed for the rule
    model.B_G = pm.Set(initialize=[(101, 1)]) # A nuclear gen
    model.B_G_sto = pm.Set(initialize=[]) # No storage

    # cSOCmax should skip for non-storage gen
    result = constraints.cSOCmax(model, 101, 1, 2020, 1, 0)
    assert result == pm.Constraint.Skip

def test_explan_constraints_thermal_max(mock_data_handler):
    """Test the logic of the thermal generation limit constraint."""
    constraints = ExplanConstraints(mock_data_handler)
    model = pm.ConcreteModel()

    # Setup mock model attributes
    b, g, y, s, i = 101, 2, 2020, 1, 0 # Gen 2 is Gas (thermal)
    model.B_G = pm.Set(initialize=[(b, g)])
    # Use tuple-based indexing so Pyomo creates the right multi-dimensional entries
    idx_5 = [(b, g, y, s, i)]
    idx_3 = [(b, g, y)]
    model.P_gen = pm.Var(idx_5, initialize=100)
    model.P_Reg = pm.Var(idx_5, initialize=10)
    model.P_Spin = pm.Var(idx_5, initialize=10)
    model.P_Flex = pm.Var(idx_5, initialize=10)
    model.P_cap_total = pm.Var(idx_3, initialize=200)

    # Make sure (b, g) is in the thermal tuple
    constraints.thermal_tuple = ((101, 2),)

    result = constraints.cThermMax(model, b, g, y, s, i)
    assert result is not None
    assert "P_gen" in str(result)
    assert "P_cap_total" in str(result)

def test_explan_constraints_power_balance_rule(mock_data_handler):
    """Test the power balance constraint rule (cPwrBal)."""
    constraints = ExplanConstraints(mock_data_handler)
    model = pm.ConcreteModel()

    b, y, s, i = 101, 2020, 1, 0
    model.B = pm.Set(initialize=[101, 102])
    model.Y = pm.Set(initialize=[2020])
    model.S_I = pm.Set(initialize=[(1, 0)])

    # Mock data handler attributes used in cPwrBal
    mock_data_handler.line_bus_num = [(1, 101, 102)] # line 1 from 101 to 102
    mock_data_handler.bus_gen_num = pd.DataFrame({'Bus_num': [101], 'Gen_num': [1]})
    mock_data_handler.tech_nums['renewables'] = [1]
    mock_data_handler.tech_nums['storage'] = []

    # Mock model variables with tuple-based indices
    model.P_gen = pm.Var([(101, 1, 2020, 1, 0)], initialize=100)
    model.Pdis = pm.Var([(101, 1, 2020, 1, 0)], initialize=0)
    model.Pcha = pm.Var([(101, 1, 2020, 1, 0)], initialize=0)
    model.Curt = pm.Var([(101, 1, 2020, 1, 0)], initialize=0)
    model.PF = pm.Var([(1, 2020, 1, 0)], initialize=10)
    model.load_full = pm.Param([(101, 2020, 1, 0)], initialize=110)
    model.LNS = pm.Var([(101, 2020, 1, 0)], initialize=0)

    result = constraints.cPwrBal(model, b, y, s, i)
    assert result is not None
    result_str = str(result)
    assert "P_gen" in result_str
    assert "PF" in result_str
    # load_full is a Param which may render as a numeric value in the expression;
    # verify that LNS (a Var) appears and the expression is an equality
    assert "LNS" in result_str
    assert "==" in result_str

def test_explan_constraints_investment_cap(mock_data_handler):
    """Test the cumulative generation capacity constraint (cPCapTotal)."""
    constraints = ExplanConstraints(mock_data_handler)
    model = pm.ConcreteModel()

    b, g, y = 101, 1, 2020
    model.Y = pm.Set(initialize=[2020])
    model.P_cap = pm.Param([1], initialize=1000)
    model.G_inv = pm.Var([(101, 1, 2020)], initialize=100)
    model.P_cap_total = pm.Var([(101, 1, 2020)], initialize=1100)

    # Mock data handler
    constraints.candidate_tuple = ((101, 1),)
    mock_data_handler.block_selection = 'Full_Year'

    result = constraints.cPCapTotal(model, b, g, y)
    assert result is not None
    assert "P_cap_total" in str(result)
    assert "G_inv" in str(result)
