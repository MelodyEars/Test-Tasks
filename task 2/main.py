def reducer(sequence):
	return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]


def adder():
	for key in sorted(DICT_SEQUENCE.keys(), reverse=True):
		if key != 1:
			next_dict_elem = DICT_SEQUENCE[key - 1]
			last_num = DICT_SEQUENCE[key][-1]
			step = last_num + next_dict_elem[-1]
			next_dict_elem.append(step)


def calculator(sequence: list, resent_key=1):
	global DICT_SEQUENCE
	resent_key += 1
	result_1, result_2 = sequence[1] - sequence[0], sequence[2] - sequence[1]

	if result_2 == result_1:
		DICT_SEQUENCE[resent_key] = [result_1]
		[adder() for _ in range(NEW_ELEMENTS)]
	else:
		DICT_SEQUENCE[resent_key] = reducer(sequence)
		return calculator(DICT_SEQUENCE[resent_key], resent_key)

	return DICT_SEQUENCE[1][-3:]


if __name__ == '__main__':
	# input_sequence = [15, 32, 57, 90, 131, 180]
	NEW_ELEMENTS = 3

	input_sequence = input('Enter the sequence via space: ').split()
	DICT_SEQUENCE = {1: list(map(int, input_sequence))}
	print(calculator(sequence=DICT_SEQUENCE[1]))
