from ortools.sat.python import cp_model
model = cp_model.CpModel()
color = {}
color["Bel"] = model.NewIntVar(1, 3, 'Bel')
color["Dan"] = model.NewIntVar(1, 3, 'Dan')
color["Fr"] = model.NewIntVar(1, 3, 'Fr')
color["Ger"] = model.NewIntVar(1, 3, 'Ger')
color["Net"] = model.NewIntVar(1, 3, 'Net')
color["Lux"] = model.NewIntVar(1, 3, 'Lux')

model.Add(color["Bel"] != color["Fr"])
model.Add(color["Bel"] != color["Ger"])
model.Add(color["Bel"] != color["Net"])
model.Add(color["Bel"] != color["Lux"])
model.Add(color["Dan"] != color["Ger"])
model.Add(color["Fr"] != color["Lux"])
model.Add(color["Ger"] != color["Net"])
model.Add(color["Ger"] != color["Lux"])
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
	for x in ["Bel", "Dan", "Fr", "Ger", "Net", "Lux"]:
		print (x, "=", solver.Value(color[x]))