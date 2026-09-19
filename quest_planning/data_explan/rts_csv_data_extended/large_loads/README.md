# Large Loads Directory

This directory contains profile data for large loads (e.g., data centers, industrial facilities) that can be modeled in QuESt Planning.

## What are Large Loads?

Large loads can be modeled with:
- **Behind-the-meter (BTM) generation**: Natural gas generators and battery storage
- **Flexible demand**: Optional curtailment capability
- **Custom load profiles**: Hourly load data for the entire year

## How to Use This Feature

### 1. Enable in Configuration File

Edit your YAML configuration file (e.g., `quest_planning/config/input_rts_nodal_base.yaml`):

```yaml
# Enable large load modeling
large_load_option: True
large_load_flex: True  # Allow demand curtailment
ll_self_sufficiency: 0.0  # Minimum fraction of energy from onsite resources (0.0-1.0)
large_load_growth: 0  # Annual load growth rate

# Define large loads
large_loads:
  - id: LL_1
    bus: 111  # Bus number where load connects
    capacity_mw: 500  # Peak capacity in MW
    deploy_year: 2040  # Year the load comes online
    profile_file: my_load_profile.csv  # CSV file in this directory
    profile_type: normalized  # "normalized" (0-1 scale) or "absolute" (MW values)
    
    onsite_resources:
      ng:
        candidate: true
        max_capacity_mw: 200  # Maximum natural gas capacity
      
      bess:
        candidate: true
        max_energy_mwh: 800  # Maximum battery energy
        max_power_mw: 200    # Maximum battery power
```

### 2. Create Load Profile CSV File

Place your profile CSV file in this directory. The file must contain:

**Required Structure:**
- **Exactly 8760 rows** (one per hour of the year)
- **Required column**: `normalized` (for normalized profiles) or `load_mw` (for absolute profiles)

**Example Format** (for `profile_type: normalized`):

```csv
datetime,year,month,day,hour,normalized
1/1/2020 0:00,2020,1,1,1,0.578199
1/1/2020 1:00,2020,1,1,2,0.578187
1/1/2020 2:00,2020,1,1,3,0.578176
...
(8760 total rows)
```

**Normalized Profile Requirements:**
- Values in `normalized` column must be between 0.0 and 1.0
- The profile is scaled by `capacity_mw` to get actual MW values
- Peak value should be 1.0 (or close to it)

**Absolute Profile Format:**
Use `profile_type: absolute` and include `load_mw` column with actual MW values.

### 3. Run the Model

```bash
python -m quest_planning.explan_simulation quest_planning/config/your_config.yaml
```

## Example Data

For a working example, see:
- **Config**: `quest_planning/config/input_rts_nodal_base_DC_cjn.yaml`
- **Data**: `quest_planning/data_explan/rts_csv_data_cjn/large_loads/`

This directory contains example data center profiles with:
- Normalized hourly load profiles
- Multiple large load scenarios
- Behind-the-meter generation configurations

## Model Behavior

When large loads are enabled:
- **Net load calculation**: Large load demand minus onsite generation equals net grid load
- **Curtailment**: If `large_load_flex: True`, loads can be curtailed up to 25% (configurable)
- **Self-sufficiency**: The `ll_self_sufficiency` parameter enforces minimum onsite energy fraction
- **Investment optimization**: Model determines optimal onsite generation and storage capacity

## Troubleshooting

**Error: "profile must have 8760 rows"**
- Ensure your CSV has exactly 8760 data rows (one per hour)
- Header row is not counted

**Error: "profile_normalized appears >1.0"**
- Check that all values in the `normalized` column are ≤ 1.0
- Common issue: using absolute MW values instead of normalized (0-1) scale

**Error: "Large load configuration missing required fields"**
- Verify all required fields are present: `id`, `bus`, `profile_file`, `deploy_year`, `capacity_mw`

**FileNotFoundError**
- Ensure the `profile_file` name matches exactly (case-sensitive)
- Profile CSV must be in this `large_loads/` directory

## Additional Resources

- **Main README**: `/projects/README.md`
- **Configuration Guide**: See example config files in `quest_planning/config/`
- **Code Documentation**: `quest_planning/explan/explan_data_handler.py` (see `read_large_loads_config()` method)
