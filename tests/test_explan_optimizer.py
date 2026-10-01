import pytest
import pyomo.environ as pm
import pandas as pd
import numpy as np
from quest_planning.explan.explan_data_handler import ExplanDataHandler
from quest_planning.explan.explan_optimizer import ExplanOptimizer

@pytest.fixture
def mock_data_handler(tmp_path):
    # Use the same mock setup as in test_explan_data_handler.py
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    # Minimal required CSVs
    pd.DataFrame({'Scalar': ['load_growth', 'soc_max', 'soc_min', 'reg_res_req', 'spin_res_req', 'flex_res_req', 'voll', 'prm'],
                  'Value': [1.5, 1.0, 0.2, 0.01, 0.01, 0.01, 10000, 0.15]}).to_csv(data_dir / "scalars.csv", index=False)
    pd.DataFrame({'Tech_Num': [1], 'Tech': ['Nuclear'], 'Tech_Name': ['Nuclear'], 'Lead_Time': [10], 'CandCap': [1000], 'RampRate': [0.1], 'FOM': [10], 'VOM': [2], 'PTC': [0], 'ITC': [0], 'CapCred': [0.9], 'Lifetime': [40]}).to_csv(data_dir / "tech.csv", index=False)
    pd.DataFrame({'Gen_num': [1], 'Gen_name': ['Gen1'], 'Tech': ['Nuclear'], 'Bus_num': [101], 'Bus': ['Bus101'], 'Cap': [1000], 'MinCap': [200], 'CandCap': [0], 'PlannedYr': [2020], 'RetYr': [2060], 'CapCred': [0.9], 'LeadTime': [10], 'YearAvail': [2020], 'HR': [10], 'FOM': [2], 'VOM': [1], 'PTC': [0], 'ITC': [0], 'Lifetime': [40], 'Ramp': [0.1], 'FOR': [0.05], 'CO2': [0], 'SO2': [0], 'NO2': [0], 'SystCap': [1000], 'RetCap': [0], 'TransAdder': [0], 'Tech_Num': [1]}).to_csv(data_dir / "gen.csv", index=False)
    pd.DataFrame({'Line_Number': [1, 2], 'From_Bus_Number': [101, 101], 'To_Bus_Number': [102, 102], 'From_Bus_Name': ['Bus101', 'Bus101'], 'To_Bus_Name': ['Bus102', 'Bus102'], 'Capacity': [1000, 1000], 'X': [0.1, 0.1], 'Rating_F': [1000, 1000], 'Rating_B': [1000, 1000], 'Tx_cost': [100, 100], 'Tx_limit': [1000, 1000], 'Lead_Time': [2, 2]}).to_csv(data_dir / "branch.csv", index=False)
    pd.DataFrame({'Bus_num': [101, 102], 'Bus_number': [101, 102], 'Bus_name': ['Bus101', 'Bus102'], 'LAT': [30, 31], 'LON': [-90, -91], 'Load_share': [0.6, 0.4], 'Region': [1, 1]}).to_csv(data_dir / "bus.csv", index=False)

    # Policy CSV needs 'Years' column
    pd.DataFrame({'Years': [2020], 'RPS': [0.1], 'CO2': [50], 'CO2_intensity': [0.5]}).to_csv(data_dir / "policy.csv", index=False)

    load_df = pd.DataFrame({
        'datetime': pd.date_range(start='2020-01-01', periods=8760, freq='h'),
        'year': [2020]*8760,
        'day': pd.date_range(start='2020-01-01', periods=8760, freq='h').date,
        'load_forecast': np.random.rand(8760) * 1000
    })
    load_df.to_csv(data_dir / "load.csv", index=False)

    # Renewable profile CSVs need 'datetime' column
    ren_cols = {'datetime': pd.date_range(start='2020-01-01', periods=8760, freq='h'), 'val': np.random.rand(8760)}
    for key in ['solar_cand', 'solar', 'wind_cand', 'wind']:
        pd.DataFrame(ren_cols).to_csv(data_dir / f"{key}.csv", index=False)

    # Storage CSV with proper columns
    pd.DataFrame({
        'Gen_num': [1],
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
    # Add missing attributes used by instantiate_model
    # The model expects line_bus_num to be a list of tuples, not a dict
    handler.line_bus_num = [(1, 101, 102), (2, 101, 102)]
    handler.large_load_option = False
    handler.tx_model = 'dc'
    # Mock load_blocks for load_par_adjust
    handler.load_blocks = pd.DataFrame(np.random.rand(24, 1), columns=['2020'])
    # Mock load_forecast column name
    handler.load_forecast = 'load_forecast'
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
        'renewables': [],
        'storage': [],
        'storage_cand': [],
        'storage_cand_year': [],
        'candidates': [],
        'upv_ex': [],
        'upv_can': [],
        'wind_ex': [],
        'wind_can': [],
        'dr': [],
        'exist': [1],
        'thermal': [1],
        'nuclear': [1],
        'coal': [],
        'oil': [],
        'ng': [],
        'ldes': [],
        'large_load_gen': [],
        'large_load_sto': []
    }

    return handler

def test_explan_optimizer_instantiation(mock_data_handler):
    # Instantiate ExplanOptimizer
    # We use a dummy solver name as we only test model construction
    optimizer = ExplanOptimizer(mock_data_handler, solver={'solver': 'cbc'})

    # Test instantiation of the model structure
    optimizer.instantiate_model()

    # Check if key Pyomo components were created on the optimizer's model
    model = optimizer.model
    assert hasattr(model, 'B')
    assert hasattr(model, 'G')
    assert hasattr(model, 'Y')
    assert hasattr(model, 'S_I')
    assert hasattr(model, 'L')

    # Verify dimensions (based on mock data)
    assert len(model.B) == 2
    assert len(model.G) == 1
    assert len(model.Y) == 1
    assert len(model.L) == 2

def test_explan_optimizer_populate_model(mock_data_handler):
    """Test that instantiate_model creates a valid Pyomo model with all expected sets and parameters."""
    optimizer = ExplanOptimizer(mock_data_handler, solver={'solver': 'cbc'})

    optimizer.instantiate_model()

    model = optimizer.model
    # Check if key sets were created
    assert hasattr(model, 'B')
    assert hasattr(model, 'G')
    assert hasattr(model, 'Y')
    assert hasattr(model, 'S_I')
    assert hasattr(model, 'L')

    # Check bus-gen pair sets
    assert hasattr(model, 'B_G')
    assert hasattr(model, 'B_G_thermal')
    assert hasattr(model, 'B_G_sto')
    assert hasattr(model, 'B_G_ren')
    assert hasattr(model, 'B_G_ldes')
    assert hasattr(model, 'B_G_ng')

    # Check that model parameters were initialized
    assert hasattr(model, 'm')  # timestep parameter
    assert hasattr(model, 's')  # season parameter
    assert hasattr(model, 'I')  # timestep range set
    assert hasattr(model, 'S')  # season range set

    # Verify dimensions (based on mock data)
    assert len(model.B) == 2  # 2 buses
    assert len(model.G) == 1  # 1 generator
    assert len(model.Y) == 1  # 1 year
    assert len(model.L) == 2  # 2 branches

def test_explan_optimizer_params_mapping(mock_data_handler):
    """Test that model parameters map correctly to data handler values."""
    optimizer = ExplanOptimizer(mock_data_handler, solver={'solver': 'cbc'})

    optimizer.instantiate_model()

    model = optimizer.model

    # Check model timestep parameter matches data handler
    assert pm.value(model.m) == mock_data_handler.M
    assert pm.value(model.s) == mock_data_handler.S

    # Check set contents match data handler input
    bus_nums = list(model.B)
    assert 101 in bus_nums
    assert 102 in bus_nums

    gen_nums = list(model.G)
    assert 1 in gen_nums

    years = list(model.Y)
    assert 2020 in years

    # Verify line numbers in model
    line_nums = list(model.L)
    assert 1 in line_nums
    assert 2 in line_nums
