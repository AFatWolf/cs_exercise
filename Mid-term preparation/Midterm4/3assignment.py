import pulp
pr = pulp.LpProblem("Farm_mgnt.problem", pulp.LpMaximize)
x = pulp.LpVariable("x", lowBound = 0) # x >= 0
y = pulp.LpVariable("y", lowBound = 0) # y >= 0
pr += x + y <= 50 # condition 1.
pr += 8*x + y <= 190 # condition 2.
pr += 2*x + y # goal
pr.solve()
print("The maximum value can be achieved at x=" + str(x.value()) + " y=", str(y.value()))