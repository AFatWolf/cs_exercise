import pulp
pr = pulp.LpProblem("Farm_mgnt.problem", pulp.LpMaximize)
x = pulp.LpVariable("x", lowBound = 0) # x >= 0
y = pulp.LpVariable("y", lowBound = 0) # y >= 0
pr += 3*x + y <= 480 # condition 1.
pr += 0.8*x + 0.1*y <= 50 # condition 2.
pr += 20*x + 6*y # goal
pr.solve()
P = 20*x.value() + 6*y.value()
print("The maximum value can be achieved at x=" + str(x.value()) + " y=", str(y.value()), "P =", P) 