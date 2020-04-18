from solver import solve_it
import json
from datetime import datetime
import time

files = open('_coursera').read().split('\n')[3:6]

test = []
for f in files:
	tmp = f.split(', ')
	test.append((tmp[0], tmp[1]))

result_file = open('all_result.txt', 'a')

result = dict()

for t in test:
	start = time.clock()
	output = solve_it(open(t[1]).read())
	end = time.clock()
	result[t[0]] = {'output': output + '\n' + str(end - start)}

result_file.write('Time: ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
result_file.write(json.dumps(result, sort_keys=True, indent=4, separators=(',', ':')) + "\n\n")