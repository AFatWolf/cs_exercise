import pulp
pr = pulp.LpProblem("Farm_mgnt.problem", pulp.LpMaximize)
x = pulp.LpVariable("x", lowBound = 0)
y = pulp.LpVariable("y", lowBound = 0)
pr += x + y <= 30
pr += 0.5*x + 0.*y <= 5
pr += 100*x + 50*y
pr.solve()
print("The maximum value can be achieved at x=" + str(x.value()) + " y=", str(y.value()))
