===================
Optimizer Class
===================

The `Optimizer` class serves as an abstract base class for implementing optimization models in the QuESt Planning tool. It leverages the Pyomo optimization framework to define, instantiate, and solve models. Subclasses must implement the abstract methods to define problem-specific parameters, variables, and constraints.

**Authors:** Sandia National Laboratories

-------------------
Class Overview
-------------------

.. class:: Optimizer

   Abstract base class for Pyomo ConcreteModel optimization framework.

   **Attributes:**
      - `_model`: A Pyomo ConcreteModel instance.
      - `_solver`: The solver to use for optimization (default: "glpk").
      - `_results`: The optimization results.

-------------------
Public Methods
-------------------

.. method:: __init__(solver="glpk")

   Initializes the `Optimizer` class.

   **Parameters:**
      - `solver` (str): The solver to use for optimization. Default is "glpk".

.. method:: solve_model()

   Solves the optimization model using the specified solver.

   **Dependencies:**
      - SolverFactory for solvers such as "glpk", "cbc", and "gurobi".
      - Highs solver for HiGHs optimization.

   **Example Usage:**
      >>> optimizer.solve_model()

.. method:: log_infeasible_constraints()

   Logs infeasible constraints in the optimization model.

   **Example Usage:**
      >>> optimizer.log_infeasible_constraints()

.. method:: run()

   Runs the optimizer by instantiating, populating, and solving the model.

   **Example Usage:**
      >>> optimizer.run()

.. method:: set_model_parameters(**kwargs)

   Sets model parameters using keyword arguments.

   **Parameters:**
      - `**kwargs`: Dictionary of parameter names and values to set.

   **Example Usage:**
      >>> optimizer.set_model_parameters(param1=value1, param2=value2)

-------------------
Abstract Methods
-------------------

The following methods must be implemented by subclasses:

.. method:: _set_model_param()

   Assigns model parameters and their default values.

.. method:: _set_model_var()

   Initializes model decision variables.

.. method:: instantiate_model()

   Instantiates the model and assigns optimizer attributes.

.. method:: populate_model()

   Sets model parameters, variables, and expressions.

.. method:: _process_results()

   Computes derived quantities of interest and prepares the results DataFrame.

.. method:: get_results()

   Returns the results DataFrame and any additional outputs.

-------------------
Properties
-------------------

.. attribute:: model

   **Type:** Pyomo ConcreteModel

   **Description:** The Pyomo model used for optimization.

   **Example Usage:**
      >>> model = optimizer.model

.. attribute:: solver

   **Type:** str

   **Description:** The solver name.

   **Example Usage:**
      >>> solver = optimizer.solver

.. attribute:: results

   **Type:** DataFrame

   **Description:** Results of the optimization process.

   **Example Usage:**
      >>> results = optimizer.results

-------------------
Error Handling
-------------------

.. method:: log_infeasible_constraints()
   :noindex:

   Logs infeasible constraints and generates an IIS (Irreducible Inconsistent Subsystem) analysis.

   **Example Usage:**
      >>> optimizer.log_infeasible_constraints()

------------------------
API Reference
------------------------

For a detailed reference of all methods, attributes, and inherited properties, refer to the autodoc-generated content below.

.. automodule:: quest_planning.explan.optimizer
   :noindex:
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

