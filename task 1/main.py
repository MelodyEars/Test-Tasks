def shuffle_msg(key_list, msg):
	"""
    Shuffle the characters in the message based on a given key list.
    Args:
        key_list (list): A list of keys used for shuffling the characters.
        msg (str): The message to be shuffled.
    Returns:
        str: The shuffled message.
    """

	# Create a dictionary with empty lists for each key in the key list
	key_to_list = {key: [] for key in key_list}
	# Iterate over each character in the message
	for i, char in enumerate(msg):
		# Get the key for the current character based on its position in the key list
		key = key_list[i % len(key_list)]
		# Append the character to the list associated with the key
		key_to_list[key].append(char)
	# Join the characters in each list, sort the lists based on their keys,
	# and join the resulting strings to form the shuffled message
	chiphered_msg = ''.join(''.join(value) for key, value in sorted(key_to_list.items()))
	return chiphered_msg


def create_list_with_digraph(msg):
	"""
	 Create a list of digraphs from a given message.
	 Args:
	     msg (str): The input message.
	 Returns:
	     list: A list of digraphs extracted from the message.
	 """

	msg_list = []  # Initialize an empty list to store the digraphs
	step_count = 3  # Number of characters to step forward in each iteration
	num = 3  # Initial value of the number of characters to extract
	step_msg = msg[:num]  # Extract the first `num` characters from the message

	while step_msg:
		msg_list.append(step_msg[0:2])  # Extract the first two characters and add them to the list
		if len(step_msg) == 3:
			msg_list.append(step_msg[2])  # If there is a third character, add it to the list

		resent_num = num  # Store the current value of `num` for future reference
		num += step_count  # Increment `num` by `step_count`
		step_msg = msg[resent_num:num]  # Extract the next `num` characters from the message

	return msg_list  # Return the list of digraphs


if __name__ == '__main__':
	# keys = [3, 4, 1, 2]
	# msg = "THISISJUSTATEST"
	keys = input('Enter the key via space: ').split()
	msg = input('Enter the message: ')
	key_list = list(map(int, keys))

	list_with_digraph = create_list_with_digraph(msg)
	chiphered_msg = shuffle_msg(key_list=key_list, msg=list_with_digraph)

	print(chiphered_msg)
