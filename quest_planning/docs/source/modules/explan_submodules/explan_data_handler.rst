=========================
ExplanDataHandler Class
=========================
The `ExplanDataHandler` class processes input data for the optimization model used in QuESt Planning. This class provides functionality to load, manipulate, and prepare datasets required for simulation and optimization.

**Authors:** C. Newlun and W. Olis

---------------------
Class Initialization
---------------------

.. class:: ExplanDataHandler

   Initializes the `ExplanDataHandler` class with default attributes.

   **Attributes:**
      - `block_selection`: Selected block type for load profile segmentation.
      - `tx_model`: Transmission model type.
      - `trans_expansion`: Determines whether transmission expansion is enabled.
      - `load_growth` (default: 1.5): Annual load growth rate.
      - `load_forecast`: Selected load forecast.
      - `es_cost`: Energy storage cost type (e.g., Base, Low, High).
      - `ldes_switch`: Enables/disables long-duration energy storage options.
      - `solver`: Optimization solver used.
      - `years`: Simulation years.
      - `season_time_duration`: Seasonal time weights.

---------------------
Public Methods
---------------------

.. method:: set_data_ls_index(data_ls)

   Sets or initializes the data list index.

   **Parameters:**
      - `data_ls` (list): List of data categories. If None, defaults to predefined categories.

   **Example Usage:**
      >>> handler.set_data_ls_index(['branch', 'bus', 'load'])

----------------------
Simulation Parameters
----------------------

.. method:: set_start_year(year)

   Sets the start year of the simulation.

   **Parameters:**
      - `year` (int): Start year.

   **Example Usage:**
      >>> handler.set_start_year(2025)

.. method:: set_end_year(year)

   Sets the end year of the simulation.

   **Parameters:**
      - `year` (int): End year.

   **Example Usage:**
      >>> handler.set_end_year(2030)

.. method:: set_year_gap(value)

   Sets the interval between simulation years.

   **Parameters:**
      - `value` (int): Year gap.

   **Example Usage:**
      >>> handler.set_year_gap(5)

.. method:: set_years_hours(years)

   Defines the simulation years and calculates year gaps.

   **Parameters:**
      - `years` (list): List of simulation years.

   **Example Usage:**
      >>> handler.set_years_hours([2025, 2030, 2035])

------------------------
Modeling Configuration
------------------------

.. method:: set_tx_model(value)

   Sets the transmission model type.

   **Parameters:**
      - `value` (str): Transmission model type. Options include "Transportation" or "Copper Sheet".

   **Example Usage:**
      >>> handler.set_tx_model("Copper Sheet")

.. method:: set_block_selection(value)

   Defines the block selection for load profiles.

   **Parameters:**
      - `value` (str): Block selection type (e.g., 'Full_year', 'Peak_Day').

   **Example Usage:**
      >>> handler.set_block_selection("Peak_Day")

.. method:: set_discount_rate(value)

   Sets the discount rate used in modeling.

   **Parameters:**
      - `value` (float): Discount rate (e.g., 0.05 for 5%).

   **Example Usage:**
      >>> handler.set_discount_rate(0.05)

.. method:: set_scenario(value)

   Sets the scenario name for the simulation.

   **Parameters:**
      - `value` (str): Scenario name.

   **Example Usage:**
      >>> handler.set_scenario("High Load Growth")

---------------------
Data Management
---------------------

.. method:: get_data()

   Loads all data from CSV files into the `load_data` attribute.

   **Dependencies:**
      - Requires `data_ls` and `data_dir` to be properly initialized.

   **Example Usage:**
      >>> handler.get_data()

.. method:: get_tech_nums()

   Defines generator technology categories and assigns tech numbers for each category.

   **Example Usage:**
      >>> handler.get_tech_nums()

.. method:: define_bus_nums()

   Defines bus numbers for different technology categories and creates mappings for network edges.

   **Example Usage:**
      >>> handler.define_bus_nums()

---------------------
Visualization
---------------------

.. method:: plot_load_profile(fig, ax, load_forecast)

   Plots the system-wide load profile using Matplotlib.

   **Parameters:**
      - `fig` (matplotlib.figure.Figure): Figure object.
      - `ax` (matplotlib.axes.Axes): Axes object.
      - `load_forecast` (str): Column name for load forecast data.

   **Example Usage:**
      >>> fig, ax = plt.subplots()
      >>> handler.plot_load_profile(fig, ax, 'Base Forecast')

.. method:: create_network_diagram(fig, ax, use_map)

   Creates a network diagram of the system.

   **Parameters:**
      - `fig` (matplotlib.figure.Figure): Figure object.
      - `ax` (matplotlib.axes.Axes): Axes object.
      - `use_map` (bool): Whether to overlay on a geographic map.

   **Example Usage:**
      >>> fig, ax = plt.subplots()
      >>> handler.create_network_diagram(fig, ax, False)

---------------------------
Advanced Functionality
---------------------------

.. method:: add_candidate_tech(tech, storage)

   Adds candidate technology characteristics to the database.

   **Parameters:**
      - `tech` (dict): Candidate technology characteristics.
      - `storage` (bool): Indicates whether the technology is energy storage.

   **Example Usage:**
      >>> tech = {
      ...     'Name': 'Solar_Cand',
      ...     'Candidate Capacity': 500,
      ...     'Capacity Credit': 0.8,
      ...     'Lead Time': 3,
      ...     'Deployable Year': 2026,
      ...     'PTC Credit': 0.02,
      ...     'ITC Credit': 0.1,
      ...     'Lifetime': 25,
      ...     'Ramp Rate': 1.0
      ... }
      >>> handler.add_candidate_tech(tech, storage=True)

------------------------
API Reference
------------------------

For a detailed reference of all methods, attributes, and inherited properties, refer to the autodoc-generated content below.

.. automodule:: quest_planning.explan.explan_data_handler
   :noindex:
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

