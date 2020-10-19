# Solve linear equation
# 3x+2y=1
# x+2y=0

from gekko import GEKKO

# Initialize model
m = GEKKO()

# Define variables
x = m.Var()
y = m.Var()

# Equations
m.Equation(3*x+2*y == 1)
m.Equation(x+2*y == 0)

# Solve simulation
m.solve()
#m.solve(disp=False)

# Results
print("")
print(f"x: {x.value} and y: {y.value}")
