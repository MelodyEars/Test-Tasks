def reducer(sequence: list) -> list:
	"""
	Calculate the difference between consecutive elements in a sequence.

	Args:
		sequence (list): The input sequence.

	Returns:
		list: A list of differences between consecutive elements.
	"""
	# Initialize an empty list to store the differences
	differences = []

	# Iterate over the sequence up to the second-to-last element
	for i in range(len(sequence) - 1):
		# Calculate the difference between the current element and the next element
		difference = sequence[i + 1] - sequence[i]
		# Add the difference to the list
		differences.append(difference)

	# Return the list of differences
	return differences


def adder():
	"""
	Adds the last element of each dictionary in DICT_SEQUENCE to the next dictionary
	"""

	# Sort the keys of DICT_SEQUENCE in reverse order
	sorted_keys = sorted(DICT_SEQUENCE.keys(), reverse=True)

	# Iterate over the sorted keys
	for key in sorted_keys:
		# Skip the first dictionary in DICT_SEQUENCE
		if key != 1:
			# Get the next dictionary element
			next_dict_elem = DICT_SEQUENCE[key - 1]

			# Get the last number from the current dictionary
			last_num = DICT_SEQUENCE[key][-1]

			# Calculate the step by adding the last number of the current dictionary
			# to the last number of the next dictionary
			step = last_num + next_dict_elem[-1]

			# Append the step to the next dictionary
			next_dict_elem.append(step)


def calculator(sequence: list, resent_key: int = 1) -> list:
	"""
	Calculate the difference between elements in the sequence and,
	based on the difference, either add new elements or reduce the sequence.

	Parameters:
	- sequence (list): The input sequence of numbers.
	- resent_key (int): The key used to store the sequence in the dictionary.

	Returns:
	- list: The last three elements of the resulting sequence.
	"""
	global DICT_SEQUENCE

	# Increment the resent_key by 1
	resent_key += 1

	# Calculate the differences between elements in the sequence
	result_1, result_2 = sequence[1] - sequence[0], sequence[2] - sequence[1]

	# If the differences are equal, add new elements to the sequence
	if result_2 == result_1:
		DICT_SEQUENCE[resent_key] = [result_1]
		[adder() for _ in range(NEW_ELEMENTS)]

	# If the differences are not equal, reduce the sequence
	else:
		DICT_SEQUENCE[resent_key] = reducer(sequence)
		return calculator(DICT_SEQUENCE[resent_key], resent_key)

	# Return the last three elements of the resulting sequence
	return DICT_SEQUENCE[1][-3:]


if __name__ == '__main__':
	# input_sequence = [15, 32, 57, 90, 131, 180]
	NEW_ELEMENTS = 3

	input_sequence = input('Enter the sequence via space: ').split()
	DICT_SEQUENCE = {1: list(map(int, input_sequence))}
	print(calculator(sequence=DICT_SEQUENCE[1]))
