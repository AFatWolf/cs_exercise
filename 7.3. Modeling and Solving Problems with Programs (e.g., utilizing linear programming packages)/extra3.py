import pulp
pr = pulp.LpProblem("Farm_ngnt.problem", pulp.LpMaximize)
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)
z = pulp.LpVariable("z", lowBound=0)
pr += x + y + z <= 30
pr += 0.1*x + 0.1*y + 0.1*z <= 5
pr += 0.1*x + 0.3*y <= 5
pr += 0.5*x <= 5
pr += 100*x + 20*y + 10*z
pr.solve()
print("x=", x.value(), "y=", y.value(), "z=", z.value())
print("Maximum Profits=",100*x.value() + 20*y.value() + 10*z.value())
