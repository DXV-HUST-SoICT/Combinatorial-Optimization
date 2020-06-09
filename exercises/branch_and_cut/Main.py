import numpy as np
from fractions import Fraction as frac
from Utils import *

file = './data/mip_01'

def main():
	a, b, c, ic = read_milp_data(file)
	print(a)
	print(b)
	print(c)
	print(ic)
	# solve(a, b, c, ic)

if __name__ == '__main__':
	print('Main')
	main()