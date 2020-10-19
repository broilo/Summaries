# Linear Programming (LP)

> Also known as *linear optmization*, is a method to achieve the best outcome, e.g. maximum profit or lowest cost, in a mathematical model whose requirements are represented by linear relationships. 

Given a transformation between input and output values, described by a mathematical function f, optimization deals with generating and selecting the best solution from some set of available alternatives. This is performed by systematically choosing input values from an allowed set, computing the output of the function and then recording the best output values found during the process. 

* It's a special case of mathematical programming, a.k.a mathematical optimization.

Linear programs are problems that can be expressed in a canonical form as:

``` 
Maximize    c^{T}x 
subject to  Ax \leq b
and         x \geq 0
```

where x represents the vector of variables to be determined, c and b are vectores of known coefficients, A is a known matrix of coefficients. The expression to be maximized or minimized is called the objective function (in this case, c^{T}x). The inequalities Ax \leq b and x \geq 0 are the constrainsts which specify a convex polytope over which the objective function is to be optimized.

> The use of optimization software requires that the function f is defined in a suitable programming language and connected to a compile or run time to the optimization software. The optimization software will deliver input values in A, the software module realizing f will deliver the computed value f(x) and, in some cases, additional information about the function like derivatives.

## GEKKO Optimization Suite

* It's a Python package for ML and optimization of mixed-integer and differential algebraic equation. 
* It's couple with large-scale solvers for linear, quadratic, nolinear and mixed integer programming (LP, QP, NLP, MILP, MINLP).
* Modes of operation include parameter regression, data reconciliation, real-time optimization, dynamic simulation and nonlinear predictive control.

### What does GEKKO do?

* It's a high-level abstraction of mathematical optimization problems.
* Values in the models are defined by Contrainst, Parameter and Variables.
* The values are related to each other by Intermidiates or Equations.
* Objective functions are defined to maximize or minimize certain values.
* Objects are built-in collections of values (constants, parameters and variables) and relationships (intermidiates, equations and objective functions).
* Objects can build upon other objects with object-oriented relationships.

The APMonitor executable on the back-end compiles a model to byte-code and performs model reduction based on analysis of the sparsity structure (incidence of variables in equations or objective function) of the model. 

For differential and algebraic equation systems, orthogonal collocation on finite elements is used to transcribe the problem into a purely algebraic system of equations. APMonitor has several modes of operation, adjustable with the imode parameter. 

The core of all modes is the nonlinear model. Each mode interacts with the nonlinear model to receive or provide information. The 9 modes of operation are:

1. Steady-state simulation (SS)
1. Model parameter update (MPU)
1. Real-time optimization (RTO)
1. Dynamic simulation (SIM)
1. Moving horizon estimation (EST)
1. Nonlinear control / dynamic optimization (CTL)
1. Sequential dynamic simulation (SQS)
1. Sequential dynamic estimation (SQE)
1. Sequential dynamic optimization (SQO)

Modes 1-3 are steady state modes with all derivatives set equal to zero. 

Modes 4-6 are dynamic modes where the differential equations define how the variables change with time. 

Modes 7-9 are the same as 4-6 except the solution is performed with a sequential versus a simultaneous approach. Each mode for simulation, estimation, and optimization has a steady state and dynamic option.

APMonitor provides the following to a Nonlinear Programming Solver (APOPT, BPOPT, IPOPT, MINOS, SNOPT) in sparse form:

* Variables with default values and constraints
* Objective function
* Equations
* Evaluation of equation residuals
* Sparsity structure
* Gradients (1st derivatives)
* Gradient of the equations
* Gradient of the objective function
* Hessian of the Lagrangian (2nd derivatives)
* 2nd Derivative of the equations
* 2nd Derivative of the objective function

Once the solution is complete, APMonitor writes the results in results.json that is loaded back into the python variables by GEKKO

When the system of equations does not converge, APMonitor produces a convergence report in ‘infeasibilities.txt’. There are other levels of debugging that help expose the steps that APMonitor is taking to analyze or solve the problem. Setting DIAGLEVEL to higher levels (0-10) gives more output to the user. Setting COLDSTART to 2 decomposes the problem into irreducible sets of variables and equations to identify infeasible equations or properly initialize a model.

## References

[Linear Programming](https://en.wikipedia.org/wiki/Linear_programming)

[List of Optimization Software](https://en.wikipedia.org/wiki/List_of_optimization_software)

[GEKKO Optimization Suite](https://gekko.readthedocs.io/en/latest/)

[GEKKO Python Tutorials](https://apmonitor.com/wiki/index.php/Main/GekkoPythonOptimization)
