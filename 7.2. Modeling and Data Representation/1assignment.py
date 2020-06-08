import pulp
pr = pulp.LpProblem("Farm_ngnt.problem", pulp.LpMaximize)
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)
pr += x + y <= 30
pr += 0.5*x + 0.1*y <= 6
pr += 100*x + 50*y
pr.solve()
print("x=", str(x.value()), "y=", str(y.value()))  

