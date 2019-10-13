# Import PuLP modeler functions
from pulp import *

# A new problem
prob = LpProblem("example", LpMinimize)

# Variables
x = LpVariable("x", 0, 2)
y = LpVariable("y", -1, 5)
z = LpVariable("z", 3)

# Objective
prob += x + 4*y + 3*z, "objective"

# Constraints
prob += x+y <= 9, "c1"
prob += x+z >= 3, "c2"
prob += -y+z == 5, "c3"

# Solve the problem using the default solver
prob.solve()

# Print the status of the problem
print("Status:", LpStatus[prob.status])

# Print the value of the variables
for v in prob.variables():
	print(v.name, " = ", v.varValue)

# Print the value of the objective
print("objective = ", value(prob.objective))