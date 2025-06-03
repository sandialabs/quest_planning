=====================
ExplanOptimizer
=====================

.. module:: quest_planning.explan.optimizer
   :synopsis: Optimizer for setting up and solving Pyomo models in QuESt Planning.

The `ExplanOptimizer` class sets up the Pyomo optimization model for the QuESt Planning framework, including parameter definitions, variable initialization, constraint population, and solver configuration.

**Authors**: C. Newlun and W. 

------------------------
Class Reference
------------------------
.. autoclass:: quest_planning.explan.explan_optimizer.ExplanOptimizer
   :members:
   :special-members: __init__, __doc__
   :exclude-members: _process_results

------------------------
Attributes
------------------------
.. py:attribute:: data_handler
   :type: object
   :value: None

   A data handler object that provides data and configuration settings for the optimizer.

.. py:attribute:: var_index_labels
   :type: dict
   :value: None

   Dictionary mapping variable names to their index labels.

.. py:attribute:: par_index_labels
   :type: dict
   :value: None

   Dictionary mapping parameter names to their index labels.

.. py:attribute:: index
   :type: callable
   :value: None

   Function that resolves index names to data references.

.. py:attribute:: solver
   :type: str
   :value: 'cbc'

   The solver to be used for optimization (e.g., `cbc`, `gurobi`, `HiGHs`).

------------------------
Methods
------------------------

.. py:method:: __init__(data_handler, **kwargs)

   Initializes the `ExplanOptimizer` with the given data handler and optional solver configuration.

   :param data_handler: The data handler object for the optimizer.
   :param kwargs: Additional keyword arguments, including `solver`.

.. py:method:: _set_model_param()

   Sets up parameters for the Pyomo optimization model, including definitions for loads, renewable profiles, RPS policies, and generator-specific attributes.

.. py:method:: _set_model_var()

   Initializes Pyomo variables for the model, such as generation dispatch, state of charge, renewable curtailments, and power flow.

.. py:method:: instantiate_model()

   Instantiates the Pyomo model, defining its sets, parameters, and constraints.

.. py:method:: populate_model()

   Fully defines the model by setting parameters, variables, and constraints using the `ExplanConstraints` class.

.. py:method:: solve_model()

   Solves the optimization model using the specified solver. If successful, processes and returns the results.

   **Raises:**
      - `AssertionError`: If the solver fails to find an optimal solution.

.. py:method:: print_model_stats()

   Prints the model size and statistics for diagnostic purposes.

.. py:method:: _process_results()

   Processes and organizes model results, including derived quantities of interest and creating results DataFrames.

.. py:method:: get_results()

   Returns model variables, parameters, and the timestamp as results of the optimization.

   :returns: A tuple containing model variables, parameters, and the timestamp.

.. py:method:: get_timestamp()

   Generates a timestamp for when the model results are retrieved.

   :returns: A string representing the timestamp.

------------------------
Detailed Description
------------------------

The `ExplanOptimizer` class provides a specialized implementation for setting up and solving Pyomo models in the QuESt Planning framework. It interfaces with a data handler to ingest configuration settings and data, then defines the optimization problem based on these inputs. The class includes methods for processing results, generating reports, and providing diagnostics.

------------------------
API Reference
------------------------

For a detailed reference of all methods, attributes, and inherited properties, refer to the content below.

.. automodule:: quest_planning.explan.explan_optimizer
   :noindex:
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

