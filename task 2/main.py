
NEW_ELEMENTS = 3
DICT_SEQUENCE = {}


def reducer(sequence1):
	sequence2 = []

	for i in range(len(sequence1) - 1):
		sequence2.append(sequence1[i + 1] - sequence1[i])

	return sequence2


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
	result_1 = sequence[1] - sequence[0]
	result_2 = sequence[2] - sequence[1]

	if result_2 == result_1:
		DICT_SEQUENCE[resent_key] = [result_1]
		[adder() for _ in range(NEW_ELEMENTS)]

	else:
		DICT_SEQUENCE[resent_key] = reducer(sequence)
		return calculator(DICT_SEQUENCE[resent_key], resent_key)

	print(DICT_SEQUENCE)
	return DICT_SEQUENCE[1][-3:]


if __name__ == '__main__':
	# input_sequence = [15, 32, 57, 90, 131, 180]
	input_sequence = input('Enter the sequence via space: ').split()
	DICT_SEQUENCE = {1: list(map(int, input_sequence))}
	print(calculator(sequence=DICT_SEQUENCE[1]))
