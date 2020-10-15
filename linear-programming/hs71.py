# Example of an optimization problem from a benchmark test set: The Hock Schittkowski problem 71
# For more information: https://esa.github.io/pagmo2/docs/cpp/problems/hock_schittkowsky_71.html
# To show the result in terminal run: python hs71.py
# To create a .min file run: pyton hs71.py | cat > hs71.min

from gekko import GEKKO
import numpy as np

# Initialize Model
m = GEKKO()

# Define parameter
eq = m.Param(value=40)

# Initialize variables
x1, x2, x3, x4 = [m.Var(lb=1, ub=5) for i in range(4)]

# Initial values
x1.value = 1
x2.value = 5
x3.value = 5
x4.value = 1

# Equations
m.Equation(x1*x2*x3*x4 >= 24)
m.Equation(x1**2+x2**2+x3**2+x4**2 == eq)

# Objective function
m.Obj(x1*x4*(x1+x2+x3)+x3)

# Set gloobal options
m.options.IMODE = 3  # Steady state optimization

# Solve simulation
m.solve()

# Results
print('')
print('Results')
print(f"x1: {x1.value},\nx2: {x2.value},\nx3: {x3.value},\nx4: {x4.value}")
print('')
