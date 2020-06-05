from solver import solve_it
import json
from datetime import datetime
import time

files = open('_coursera').read().split('\n')[9:10]

test = []
for f in files:
	tmp = f.split(', ')
	test.append((tmp[0], tmp[1]))

for t in test:
	print(t[0])
	result = dict()
	start = time.clock()
	output = solve_it(open(t[1]).read())
	end = time.clock()
	result[t[0]] = {'output': output + '\n' + str(end - start)}
	result_file = open('all_result.txt', 'a')
	result_file.write('Time: ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
	result_file.write(json.dumps(result, sort_keys=True, indent=4, separators=(',', ':')) + "\n\n")
	result_file.close()