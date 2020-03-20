from ortools.sat.python import cp_model

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
	"""Print intermediate solutions."""

	def __init__(self, variables, countries):
		cp_model.CpSolverSolutionCallback.__init__(self)
		self.__variables = variables
		self.__solution_count = 0
		self.__countries = countries
		self.__colors = ['black', 'yellow', 'red', 'blue']

	def OnSolutionCallback(self, custom_variables = None):
		if custom_variables == None:
			self.__solution_count += 1
			custom_variables = self.__variables
		if type(custom_variables) == list:
			for v in custom_variables:
				self.OnSolutionCallback(v)
			print()
		else:
			print('%s = %s' % (custom_variables, self.__colors[self.Value(custom_variables)]), end = ' ')

	def SolutionCount(self):
		return self.__solution_count

	def GetValue(self, v):
		return self.Value(v)
