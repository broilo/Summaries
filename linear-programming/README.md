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



## References

[Linear Programming](https://en.wikipedia.org/wiki/Linear_programming#:~:text=Linear%20programming%20(LP%2C%20also%20called, are%20represented%20by%20linear%20relationships.)

[List of Optimization Software](https://en.wikipedia.org/wiki/List_of_optimization_software)

[GEKKO Optimization Suite](https://gekko.readthedocs.io/en/latest/)
