import pytest
import pandas as pd
import numpy as np
import os
import shutil
from quest_planning.explan.explan_data_handler import ExplanDataHandler

@pytest.fixture
def data_handler():
    return ExplanDataHandler()

@pytest.fixture
def mock_data_dir(tmp_path):
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    # Create minimal CSV files required for basic functionality
    # Scalars
    scalars_df = pd.DataFrame({
        'Scalar': ['load_growth', 'voll', 'prm'],
        'Value': [1.5, 100000, 0.2]
    })
    scalars_df.to_csv(data_dir / "scalars.csv", index=False)

    # Tech
    tech_df = pd.DataFrame({
        'Tech_Num': [1, 2],
        'Tech': ['Nuclear', 'Solar'],
        'Lead_Time': [10, 2],
        'CandCap': [1000, 500],
        'RampRate': [0.1, 1.0],
        'FOM': [10, 5],
        'VOM': [2, 1],
        'PTC': [0, 0.02],
        'ITC': [0, 0.3],
        'CapCred': [0.9, 0.2],
        'Lifetime': [40, 25]
    })
    tech_df.to_csv(data_dir / "tech.csv", index=False)

    # Gen
    gen_df = pd.DataFrame({
        'Gen_num': [1, 2],
        'Gen_name': ['Gen1', 'Gen2'],
        'Tech': ['Nuclear', 'Solar'],
        'Bus_num': [101, 102],
        'Cap': [1000, 500],
        'MinCap': [200, 0],
        'CandCap': [0, 0],
        'PlannedYr': [2020, 2021],
        'RetYr': [2060, 2046],
        'CapCred': [0.9, 0.2],
        'LeadTime': [10, 2],
        'YearAvail': [2020, 2021],
        'HR': [10, 5],
        'FOM': [2, 1],
        'VOM': [1, 0.5],
        'PTC': [0, 0.02],
        'ITC': [0, 0.3],
        'Lifetime': [40, 25],
        'Ramp': [0.1, 1.0],
        'FOR': [0.05, 0.01],
        'CO2': [0, 0],
        'SO2': [0, 0],
        'NO2': [0, 0]
    })
    gen_df.to_csv(data_dir / "gen.csv", index=False)

    # Branch
    branch_df = pd.DataFrame({
        'Line_Number': [1],
        'From_Bus_Number': [101],
        'To_Bus_Number': [102],
        'From_Bus_Name': ['Bus101'],
        'To_Bus_Name': ['Bus102'],
        'Capacity': [1000]
    })
    branch_df.to_csv(data_dir / "branch.csv", index=False)

    # Bus
    bus_df = pd.DataFrame({
        'Bus_num': [101, 102],
        'Bus_name': ['Bus101', 'Bus102'],
        'LAT': [30.0, 31.0],
        'LON': [-90.0, -91.0],
        'Load_share': [0.6, 0.4]
    })
    bus_df.to_csv(data_dir / "bus.csv", index=False)

    # Load
    load_df = pd.DataFrame({
        'datetime': pd.date_range(start='2020-01-01', periods=8760, freq='h'),
        'year': [2020]*8760,
        'day': [pd.Timestamp('2020-01-01').date()] * 8760,
        'load_forecast': np.random.rand(8760) * 1000
    })
    load_df['day'] = load_df['datetime'].dt.date
    load_df.to_csv(data_dir / "load.csv", index=False)

    # Policy, storage, solar, wind, etc.
    for key in ['policy', 'prm', 'solar_cand', 'solar', 'storage', 'wind_cand', 'wind', 'gen_viz', 'capex_es', 'capex_h_es', 'capex_l_es', 'capex_tech', 'fuel', 'cap_cred']:
        pd.DataFrame({'Column1': [0]}).to_csv(data_dir / f"{key}.csv", index=False)

    return str(data_dir)

def test_set_basic_params(data_handler):
    data_handler.set_start_year(2020)
    assert data_handler.start_year == 2020

    data_handler.set_end_year(2040)
    assert data_handler.end_year == 2040

    data_handler.set_year_gap(5)
    assert data_handler.year_gap == 5

def test_set_block_selection(data_handler):
    data_handler.set_block_selection('Full_year')
    assert data_handler.M == 8760

    data_handler.set_block_selection('Peak_Day')
    assert data_handler.M == 24

    data_handler.set_block_selection('Seasonal_blocks')
    assert data_handler.M == 5

def test_set_load_growth(data_handler):
    # System-wide
    data_handler.set_load_growth(1.5)
    assert data_handler.load_growth == 0.015

    # Regional
    regional_growth = [{"region": "1", "growth": 2.0}, {"region": "2", "growth": 1.0}]
    data_handler.set_load_growth(0, regional_load_growth_option=True, regional_growth_list=regional_growth)
    assert data_handler.regional_load_growth == {1: 0.02, 2: 0.01}
    assert data_handler.load_growth is None

def test_get_data(data_handler, mock_data_dir):
    data_handler.data_dir = mock_data_dir
    data_handler.set_data_ls_index(None) # Use defaults
    data_handler.get_data()

    assert data_handler.load_data is not None
    # The index mapping in ExplanDataHandler makes it tricky to check by string
    # We check if any data was actually loaded into the load_data dictionary
    assert len(data_handler.load_data) > 0

def test_tech_and_bus_nums(data_handler, mock_data_dir):
    data_handler.data_dir = mock_data_dir
    data_handler.set_data_ls_index(None)
    data_handler.get_data()

    # Check tech_nums
    # Nuclear is in 'thermal' and 'nuclear'
    assert 1 in data_handler.tech_nums['thermal']
    assert 1 in data_handler.tech_nums['nuclear']
    # Solar is in 'renewables'
    assert 2 in data_handler.tech_nums['renewables']

    # Check bus_nums
    assert 101 in data_handler.bus_therm_num
    assert 102 in data_handler.bus_ren_num
