# -*- coding: utf-8 -*-
"""Help text for the page help popups.

Keys must match the topic strings passed by each page's help buttons.
Bodies support the Qt rich text subset used by QuESt (b, i, br).
"""

from PySide6.QtWidgets import QMessageBox

HELP_TOPICS = {
    # -- planning_model_page
    "Select Simulation Years": (
        "Select the simulation years to be modeled within the QuESt Planning optimization model. Use caution when selecting simulation years, "
        "as choosing too many years can lead to increased computational complexity. Select the start and end year of the planning horizon. Once chosen, press the "
        "<b><i>Select Simulation Years</i></b> button to navigate to select the intermediate simulation years."
    ),
    "Transmission Model": (
        "Use the drop down menu to select the transmission model to be modeled within the QuESt Planning optimization model. Currently, QuESt Planning supports the copperplate and transportation model. D.C. power flow constraints are under development."
    ),
    "Temporal Selection": (
        "Use the drop down menu to select the temporal resolution to be modeled within the QuESt Planning optimization model. Currently, QuESt Planning supports load blocks and representative weeks. A full year 8760 hourly analysis is under development."
    ),
    "Annual Discount Rate": (
        "Select an annual discount rate to be used to make the net-present value calculation in the optimization model.<br><br>"
        "The discount factor can be calculated using the formula:<br>"
        "<b>Discount Factor = 1 / (1 + r)^n</b><br>"
        "where:<br>"
        "<b>r</b> = annual discount rate (as a decimal)<br>"
        "<b>n</b> = number of years<br><br>"
        "For example, if the discount rate is 5% (0.05) and the number of years is 10, the discount factor would be:<br>"
        "<b>Discount Factor = 1 / (1 + 0.05)^10 ≈ 0.6139</b>"
    ),
    "Base Currency Year": (
        "Select the base currency year where the discount factor calculation is based."
    ),
    # -- scenario_builder_page
    "Scenario Builder": (
        "The Scenario Builder page collects the inputs that define a planning scenario: a unique scenario name, capital cost trajectories, load forecasts and annual load growth, renewable portfolio standard goals, transmission expansion options, candidate storage technologies, and generation retirements. "
        "Once configured, select <b><i>View Scenario</i></b> to review the summary before building and solving the optimization model."
    ),
    "Select Scenario Name": (
        "Select a <b><i>Scenario Name</i></b>. This scenario should be unique as it will be used to save print results."
    ),
    "Select Capital Costs": (
        "Select the capital cost trajectory for energy storage technologies. The cost trajectories are low, mid, and high. These trajectories are defined in the input csv data."
    ),
    "Select Load Forecasts": (
        "Select the load forecasts for the scenario. The load forecasts are defined in the csv data."
    ),
    "Select Annual Load Growth": (
        "Select the annual load growth for the scenario. The annual load growth is defines a percentage (%). NOTE: the annual load growth parameter is only defined when only one year of load data is provided."
    ),
    "Select Renewable Portfolio Standard Goals": (
        "Select the Future Generation Mix to be used in the scenario. The Future Generation Mix schedule can be defined in the csv data. Alternatively, you can select <b><i>Custom</i></b> option to define custom RPS targets.<br>"
        "You can also select to enforce CO2 emisison reduction and CO2 intensity reduction targets. These targets must be defined in the csv data."
    ),
    "Select Transmission Expansion Option": (
        "Transmission expansion is a feature that will be added in a later release of QuESt Planning."
    ),
    "Candidate Technologies Selection": (
        "Click the <b><i>Candidate Technologies</i></b> button to select the candidate technologies to be considered in the QuESt Planning optimization."
    ),
    "Generation Retirements Selection": (
        "Click the <b><i>Retirement Schedule</i></b> to select the retirement schedule to be enforced in the QuESt Planning optimization.The <b><i>Default</i></b> option is the retirement schedule detailed in the csv data."
    ),
    "Large Load Model Selection": (
        "Click the <b><i>Large Load Model</i></b> button to select the large load model to be considered in the QuESt Planning optimization."
    ),
    # -- build_run_page
    "Build & Solve Optimization Model": (
        "Click the <b><i>Browse</i></b> button to select a Results folder to save the results. By default, a results folder will be created after an optimal solve.<br><br>"
        "Select a <b><i>Solver</i></b> to be used in the optimization. Note, the solver and accompanying licenses, if required, must be installed and accessible.<br><br>"
        "Next, click the <b><i>Build</i></b> button to build the optimization model. The status of the build will appear within the QuESt Planning window.<br><br>"
        "Once, the model has been successfully built. Click the <b><i>Solve</i></b> button to solve the optimization model."
    ),
    # -- power_system_data_page
    "Upload Power System Data": (
        "Use the <b><i>Browse</i></b> button to navigate to the folder of the input data. "
        "Next, use the <b><i>Open</i></b> button to open the folder and pre-process the input data."
    ),
}


def show_help(parent, topic):
    """Show the help text for the given topic in a message box.

    Raises KeyError if the topic is not in HELP_TOPICS, so a mistyped
    topic string fails loudly during development.
    """
    QMessageBox.information(parent, topic, HELP_TOPICS[topic])


def show_error(parent, title, text):
    """Show an error message in a message box."""
    QMessageBox.critical(parent, title, text)

