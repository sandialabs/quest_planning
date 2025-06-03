===========================
ExplanResultsViewer Class
===========================

The `ExplanResultsViewer` class processes and visualizes the results from the QuESt Planning optimization model. It provides tools for creating result folders, visualizing data through plots and maps, and exporting results for further analysis.

**Authors:** C. Newlun and W. Olis

------------------------
Class Initialization
------------------------

.. class:: ExplanResultsViewer

   Initializes the `ExplanResultsViewer` class.

   **Parameters:**
      - `data_handler`: An instance of the `ExplanDataHandler` class to access simulation data.

   **Attributes:**
      - `system`: Placeholder for system name.
      - `rd`: Results data.
      - `stacked_bar_by_bus_option`: Boolean flag for plotting options.
      - `policy_plot_option`: Boolean flag for policy plots.

------------------------
Public Methods
------------------------

.. method:: create_lookup_info()

   Creates lookup information for generator, technology, and bus mappings from the data handler.

   **Example Usage:**
      >>> viewer.create_lookup_info()

.. method:: create_results_folder(filepath)

   Creates directories for storing results.

   **Parameters:**
      - `filepath` (str): Base path for results folder. Defaults to current working directory if None.

   **Example Usage:**
      >>> viewer.create_results_folder(filepath='/path/to/results')

.. method:: process_results_gui(rd, pd, timestamp, report, filepath)

   Processes optimization results in GUI mode.

   **Parameters:**
      - `rd`: Results data.
      - `pd`: Parameter data.
      - `timestamp` (str): Timestamp of the results.
      - `report` (str): Report summary.
      - `filepath` (str): Path for results storage.

   **Example Usage:**
      >>> viewer.process_results_gui(rd, pd, '20250113', 'Report', '/path/to/results')

.. method:: plot_results()

   Generates and saves various result plots.

   **Example Usage:**
      >>> viewer.plot_results()

.. method:: create_map()

   Generates geographic maps visualizing generation and transmission.

   **Example Usage:**
      >>> viewer.create_map()

.. method:: export_results()

   Exports results to an Excel file.

   **Example Usage:**
      >>> viewer.export_results()

.. method:: stacked_resource_bar(fig, ax, figsize)

   Creates a stacked bar chart of installed capacity by year.

   **Parameters:**
      - `fig` (matplotlib.figure.Figure): Figure object.
      - `ax` (matplotlib.axes.Axes): Axes object.
      - `figsize` (tuple): Size of the figure.

   **Example Usage:**
      >>> fig, ax = plt.subplots()
      >>> viewer.stacked_resource_bar(fig, ax, figsize=(8, 6))

------------------------
Visualization
------------------------

.. method:: plot_cost_bar()

   Plots operational and investment costs.

   **Example Usage:**
      >>> viewer.plot_cost_bar()

.. method:: map_results()

   Generates maps of system results.

   **Example Usage:**
      >>> viewer.map_results()

.. method:: policy_plot()

   Creates plots related to policy constraints, such as emissions.

   **Example Usage:**
      >>> viewer.policy_plot()

------------------------
API Reference
------------------------

For a detailed reference of all methods, attributes, and inherited properties, refer to the content below.

.. automodule:: quest_planning.explan.explan_results_viewer
   :noindex:
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

