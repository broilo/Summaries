# Variable and Equation Arrays
# x1=x0+p, p=1.2
# x2-1=x1+x0
# x2=x1**2

from gekko import GEKKO

# Initialize model
m = GEKKO()

# Define parameter
p = m.Param(1.2)

# Define array
x = m.Array(m.Var, 3)

# Equations
eq0 = x[1] == x[0]+p
eq1 = x[2]-1 == x[1]+x[0]
eq2 = x[2] == x[1]**2
m.Equation([eq0, eq1, eq2])

# Solve simulation
m.solve()
#m.solve(disp=False)

# Results
for i in range(3):
    print(f"x[{i}]={x[i].value}")
