# -*- coding: utf-8 -*-
"""
Optimizer class for the QuESt Planning tool - extracted from the QuESt Analytics platform
Authors: Sandia National Laboratories
"""

from abc import ABCMeta, abstractmethod
import logging
import pyutilib
from six import with_metaclass
from pyomo.environ import *
from pyomo.opt import TerminationCondition
from pyomo.contrib.appsi.solvers.highs import Highs

from pyomo.util.infeasible import log_infeasible_constraints
from pyomo.contrib.iis import write_iis
from pyomo.core.expr import identify_variables

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.WARNING)

class Optimizer(with_metaclass(ABCMeta)):
    """Abstract base class for Pyomo ConcreteModel optimization framework."""

    def __init__(self, solver="glpk"):
        self._model = ConcreteModel()
        self._solver = solver

        self._results = None

    @property
    def model(self):
        """Pyomo ConcreteModel."""
        return self._model

    @property
    def solver(self):
        """The name of the solver for Pyomo to use."""
        return self._solver

    @property
    def results(self):
        """A results DataFrame containing series of indices, decision variables, and/or model parameters or derived quantities."""
        return self._results

    @abstractmethod
    def _set_model_param(self):
        """A method for assigning model parameters and their default values to the model."""
        pass

    @abstractmethod
    def _set_model_var(self):
        """A method for initializing model decision variables for the model."""
        pass

    @abstractmethod
    def instantiate_model(self):
        """A method for instantiating the model and assigning Optimizer attributes to model attributes."""
        pass

    @abstractmethod
    def populate_model(self):
        """A method for setting model parameters, variables, and an ExpressionsBlock object for defining objectives and constraints."""
        pass

    def solve_model(self):
        """Solves the model using the specified solver."""
        if self.solver == "neos":
            opt = SolverFactory("cbc")
            solver_manager = SolverManagerFactory("neos")
            results = solver_manager.solve(
                self.model, opt=opt)
        elif self.solver == "HiGHs":
            #Solver Factory does not work with HiGHs
            solver = Highs()
            results = solver.solve(
                self.model)
            print(results)
        else:
            solver = SolverFactory(self.solver)
            results = solver.solve(
                self.model, tee=True, keepfiles=False)
            print(results)
        assert results.solver.termination_condition == TerminationCondition.optimal

        self._process_results()

    @abstractmethod
    def _process_results(self):
        """A method for computing derived quantities of interest and creating the results DataFrame."""
        pass

    @abstractmethod
    def get_results(self):
        """A method for returning the results DataFrame plus any other quantities of interest."""
        pass
    
    def log_infeasible_constraints(self):
        """Logs infeasible constraints from the model."""
        logging.error("Optimizer: Logging infeasible constraints.")
        log_infeasible_constraints(self.model, log_expression=True, log_variables=True)
    
    def quick_feasibility_scan(self,model, log_file="feas_scan.log"):
        """
        Light-weight check for infeasible constraints and suspicious variable bounds.
        """
        
        logging.basicConfig(filename=log_file, level=logging.INFO)
        
        logging.info("=== Quick Feasibility Scan ===")
        
        # Check constraints that are infeasible under current variable values (if initialized)
        logging.info("Checking infeasible constraints...")
        log_infeasible_constraints(model, log_expression=True, log_variables=True)
        
        # Check variable bounds for suspicious ranges (e.g., lb > ub)
        logging.info("Checking variable bounds...")
        for v in model.component_objects(Var, active=True):
            for idx in v:
                var = v[idx]
                if var.lb is not None and var.ub is not None and var.lb > var.ub:
                    logging.warning(f"Variable {var.name} has lb > ub ({var.lb} > {var.ub})")
        
        logging.info("Feasibility scan complete.")

    def log_large_coefficients(self, threshold=1e6, log_file="large_coeffs.log"):
        """
        Logs all constraint coefficients with magnitude above threshold.
        """
        print(f"Logging coefficients or RHS > {threshold} to {log_file}")
        import logging
        logging.basicConfig(filename=log_file, level=logging.INFO)
        logging.info("=== Checking Large Coefficients/RHS ===")

        for c in self.model.component_objects(Constraint, active=True):
            constr = getattr(self.model, c.name)
            for idx in constr:
                con = constr[idx]
                expr = con.body
                if expr is None:
                    continue
                # Check variable values (linear coefficients may not exist)
                for v in identify_variables(expr):
                    # Evaluate the coefficient numerically if possible
                    try:
                        coef_val = value(expr.coeff(v))
                        if abs(coef_val) > threshold:
                            logging.info(f"Constraint {c.name}[{idx}] variable {v} coefficient = {coef_val}")
                            print(f"Constraint {c.name}[{idx}] variable {v} coefficient = {coef_val}")
                    except Exception:
                        pass  # skip if non-linear or can't extract coefficient

                # Check bounds (RHS)
                if con.has_lb() and abs(con.lb) > threshold:
                    logging.info(f"Constraint {c.name}[{idx}] lower bound = {con.lb}")
                    print(f"Constraint {c.name}[{idx}] lower bound = {con.lb}")
                if con.has_ub() and abs(con.ub) > threshold:
                    logging.info(f"Constraint {c.name}[{idx}] upper bound = {con.ub}")
                    print(f"Constraint {c.name}[{idx}] upper bound = {con.ub}")

    def run(self):
        """Instantiates, creates, and solves the optimizer model based on supplied information. Use if no steps are needed between constructing the model and solving it."""

        self.instantiate_model()
        self.populate_model()
        
        #self.log_large_coefficients(threshold=1e4, log_file="large_coeffs.log")

        # 🔹 Write the LP file before solving
        #self.model.write("model_dump.lp", io_options={"symbolic_solver_labels": True})
        #print("Model written to model_dump.lp")
        #input("⏸ Press Enter to continue solving after inspecting LP...")

        # Run a quick feasibility scan before full solve
        #self.quick_feasibility_scan(self.model)
        
        if self.solver == "neos":
            opt = SolverFactory("cbc")
            solver_manager = SolverManagerFactory("neos")
            results = solver_manager.solve(
                self.model, opt=opt)
        elif self.solver == "gurobi":
            solver = SolverFactory(self.solver)

            try:
                solver.available()
                
            except pyutilib.common._exceptions.ApplicationError as e:
                logging.error(
                    "Optimizer: {error}".format(error=e))
            else:
                #pass
                solver.options["NumericFocus"]= 3#cjn add
                solver.options["BarHomogeneous"]= 1#cjn add
                solver.options["ScaleFlag"]= 2#cjn add
                solver.options['Threads'] = 8
                #solver.options['ThreadLimit'] = 8
                
                results = solver.solve(
                    self.model, tee=True, keepfiles=True)
        elif self.solver == "HiGHs":
            #Solver Factory does not work with HiGHs
            solver = Highs()
            try:
                solver.available()
            except pyutilib.common._exceptions.ApplicationError as e:
                logging.error(
                    "Optimizer: {error}".format(error=e))
            else:
                
                results = solver.solve(
                    self.model)
            
        else:
            solver = SolverFactory(self.solver)

            try:
                solver.available()
            except pyutilib.common._exceptions.ApplicationError as e:
                logging.error(
                    "Optimizer: {error}".format(error=e))
            else:
                
                results = solver.solve(
                    self.model, tee=True, keepfiles=True)
                
                #logger = logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
                #log_infeasible_constraints(self.model, log_expression=True, log_variables=True,logger = logger)
                
        try:
            assert results.solver.termination_condition == TerminationCondition.optimal
        except AssertionError:
            logging.error(
                "Optimizer: An optimal solution could not be obtained. (solver termination condition: {0})".format(
                    results.solver.termination_condition
                )
            )
            self.log_pyomo_infeasible_constraints(self.model)
            
            log_infeasible_constraints(self.model, log_expression=True, log_variables=True)
            self.log_infeasible_constraints()
            write_iis(self.model, iis_file_name="IIS_Analysis", solver='gurobi')

            raise (
                AssertionError(
                    "An optimal solution could not be obtained. (solver termination condition: {0})".format(
                        results.solver.termination_condition
                    )
                )
            )
            
        else:
            self._process_results()

        self.print_model_stats()
        
        return self.get_results()

    def set_model_parameters(self, **kwargs):
        """Sets model parameters in kwargs to their respective values."""
        for kw_key, kw_value in kwargs.items():
            logging.info(
                "Optimizer: Setting {param} to {value}".format(
                    param=kw_key, value=kw_value
                )
            )
            setattr(self.model, kw_key, kw_value)

    