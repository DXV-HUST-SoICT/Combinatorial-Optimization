
def main(test_id = '00', L = 50):
	if L <= 0:
		return
	try:
		input_file = 'input/input-' + test_id + '.txt'
		output_file = 'output/output-' + test_id + '_' + str(L).zfill(3) + '.txt'
		input_data = open(input_file, encoding="utf-8").read().split('\n\n')
		output_stream = open(output_file, 'w', encoding="utf-8")
	except:
		print(input_file, output_file)
		return
	for p in input_data:
		tmp_words = p.split(' ')
		words = []
		for w in tmp_words:
			prefix = ''
			i = 0
			while True:
				j = min(i + L - len(prefix), len(w))
				words.append(prefix + w[i:j])
				prefix = '-'
				if (j == len(w)):
					break
				i = j
		sum_len = [0]
		res = [0]
		pre = [-1]
		for i in range(len(words)):
			w = words[i]
			sum_len.append(sum_len[i] + len(w))
			res.append(float("inf"))
			pre.append(0)
			j = i
			while j >= 0:
				ll = line_len(sum_len, j, i)
				if ll > L:
					break
				sl = slack(ll, L)
				if res[-1] > res[j] + sl:
					res[-1] = res[j] + sl
					pre[-1] = j
				j -= 1
		lw = [len(words)]
		while pre[lw[-1]] >= 0:
			lw.append(pre[lw[-1]])
		for i in range(len(lw), 1, -1):
			f = lw[i - 1]
			l = lw[i - 2]
			output_stream.write(' '.join(words[f:l]) + '\n')
		output_stream.write('\n')

def line_len(sum_len, j, i):
	return sum_len[i + 1] - sum_len[j] + (i - j)

def slack(line_len, L):
	return pow(L - line_len, 2)

if __name__ == "__main__":
	num_input = 5
	for i in range(num_input):
		test_id = str(i).zfill(2)
		for L in range(5, 101, 5):
			main(test_id = test_id, L = L)