import pulp
pr = pulp.LpProblem("Farm_mgnt.problem", pulp.LpMaximize)
x = pulp.LpVariable("x", lowBound = 0) # x >= 0
y = pulp.LpVariable("y", lowBound = 0) # y >= 0
pr += 4*x + y <= 36 # condition 1.
pr += 0.2*x + 0.1*y <= 2 # condition 2.
pr += 30*x + 10*y # goal
pr.solve()
P = 30*x.value() + 10*y.value()
print("The maximum value can be achieved at x=" + str(x.value()) + " y=", str(y.value()), "P =", P) 