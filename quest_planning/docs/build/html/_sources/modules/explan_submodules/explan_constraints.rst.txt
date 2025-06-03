========================
ExplanConstraints Class
========================

The `ExplanConstraints` class defines constraints to be considered in the QuESt Planning optimization model. It contains methods for various constraints, including energy storage, thermal and renewable generation, policy constraints, transmission constraints, power balance, and investment constraints.

**Authors:** C. Newlun and W. Olis

------------------------
Class Initialization
------------------------

.. class:: ExplanConstraints

   Initializes the `ExplanConstraints` class.

   **Parameters:**
      - `data_handler`: An instance of the `ExplanDataHandler` class to provide data and configurations for the constraints.

   **Attributes:**
      - `_scenario`: The scenario defined in the `data_handler`.
      - `data_handler`: Reference to the data handler instance.
      - `index`: Index of the data loaded by the data handler.
      - `start_hr`, `end_hr`: Start and end hours for constraints.
      - `ini_level`: Initial energy storage state of charge.
      - `year_gap`, `year_gap_array`: Defines year gaps for weighting.
      - `tax_credit_end_year`, `total_itc`, `total_ptc`: Tax credit details.
      - `system`: System name from the data handler.
      - Tuples for various generator types (e.g., `storage_tuple`, `thermal_tuple`, etc.).

------------------------
Public Methods
------------------------

.. method:: set_expressions(model)

   Sets expressions for the optimization model, grouping constraints by category.

   **Parameters:**
      - `model`: Pyomo optimization model instance.

   **Example Usage:**
      >>> constraints.set_expressions(model)

.. method:: energy_storage_constraints(model)

   Defines energy storage-related constraints for the optimization model.

.. method:: thermal_generator_constraints(model)

   Defines thermal generation-related constraints for the optimization model.

.. method:: renewable_generator_constraints(model)

   Defines renewable generation-related constraints for the optimization model.

.. method:: policy_constraints(model)

   Defines policy-related constraints such as CO2 emissions and renewable portfolio standards.

.. method:: transmission_constraints(model)

   Defines transmission-related constraints for the optimization model.

.. method:: power_balance_constraints(model)

   Ensures power balance across the system in the optimization model.

.. method:: investment_constraints(model)

   Enforces constraints on investments in generation and transmission capacity.

.. method:: reliability_and_resilience_constraints(model)

   Defines reliability and resilience-related constraints.

.. method:: dr_and_ee_constraints(model)

   Defines demand response and energy efficiency constraints.

.. method:: obj_and_cost_breakdown(model)

   Defines the objective function and cost breakdown for the optimization model.

------------------------
Constraint Rules
------------------------

The `ExplanConstraints` class includes numerous constraint rules, such as:

- **Energy Storage:** `cSOC_old`, `cChDsch`, `cSOCmax`, `cSOCmin`, `cStoremax`, `cStoremin`, etc.
- **Thermal Generators:** `cThermMax`, `cThermMin`, `cThermRup`, `cThermRdwn`, etc.
- **Renewables:** `cPVExist`, `cPVCand`, `cWindExist`, `cWindCan`, `cCurtMax`, etc.
- **Policy Constraints:** `cRPS`, `cCO2emm`, `cCO2emmLimit`, etc.
- **Transmission:** `cTxFlwFw`, `cTxFlwBw`, `cDCPF`, etc.
- **Power Balance:** `cPwrBal`, `cPwrBal_CopperSheet`, etc.
- **Investment:** `cPCapTotal`, `cStoreCapTotal`, `cRetirements`, etc.
- **Objective Function:** `cOBJ`.

------------------------
API Reference
------------------------

For a detailed reference of all methods, attributes, and inherited properties, refer to the content below.

.. automodule:: quest_planning.explan.explan_constraints
   :noindex:
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

