from solver import solve_it
import json
from datetime import datetime

files = open('_coursera').read().split('\n')[7:8]

test = []
for f in files:
	tmp = f.split(', ')
	test.append((tmp[0], tmp[1]))

result_file = open('all_result.txt', 'a')
result_file.write('Time: ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')

result = dict()

for t in test:
	output = solve_it(open(t[1]).read())
	result[t[0]] = {'output': output}

result_file.write(json.dumps(result, sort_keys=True, indent=4, separators=(',', ':')) + "\n\n")