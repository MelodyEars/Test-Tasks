
NEW_ELEMENTS = 3

def reducer(sequence1):
	sequence2 = []

	for i in range(len(sequence1) - 1):
		sequence2.append(sequence1[i + 1] - sequence1[i])

	return sequence2


def adder(sequence, step):
	for i in range(NEW_ELEMENTS):
		sequence.append(sequence[-1] + step)

	return sequence

def calculator(msg):
	dict_sequence = {"1": msg}

	for key, sequence in dict_sequence.items():
		result_1 = sequence[1] - sequence[0]
		result_2 = sequence[2] - sequence[1]

		if result_2 == result_1:
			for i in dict_sequence.keys():
				dict_sequence[i] = dict_sequence[i] + adder(sequence, result_1)

		else:
			dict_sequence[int(key) + 1] = reducer(sequence)

	return dict_sequence["1"][-3:]

			# решить рекурсией, глобальная преремен для словаря и рекурсивно функцией вьісщитьівать разницу


if __name__ == '__main__':
	msg = [15, 32, 57, 90, 131, 180]
	# msg = [12, 14, 16, 18, 20]
	print(calculator(msg))
