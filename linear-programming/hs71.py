# Example of an optimization problem from a benchmark test set: The Hock Schittkowski problem 71
# For more information: https://esa.github.io/pagmo2/docs/cpp/problems/hock_schittkowsky_71.html

from gekko import gekko
import numpy as np

# Initialize Model
m = GEKKO()

# Define parameter
eq = m.Param(value=40)

# Initialize variables
