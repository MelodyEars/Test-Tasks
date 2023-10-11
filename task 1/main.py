

def shuffle_msg(key_list: list, msg: list):
	"""
	Shuffles the characters in a message according to a given key list.
	Args:
	    key_list (list): The list of keys to shuffle the message.
	    msg (list): The message to be shuffled.
	Returns:
	    list: The shuffled message.
	"""
	# Create a dictionary with keys from key_list and empty lists as values
	key_to_list = {key: [] for key in sorted(key_list)}
	# Determine the number of iterations needed to shuffle the message
	steep_count = len(key_list)
	num = steep_count
	# Extract the initial portion of the message to be shuffled
	step_msg = msg[:num]

	# Shuffle the message by assigning characters to the appropriate key
	while step_msg:
		for i, key in enumerate(key_list):
			if i < len(step_msg):  # If there are characters left in the message
				key_to_list[key].append(step_msg[i])  # Add the character to the list

		# Update the indexes for the next portion of the message
		resent_num = num
		num += steep_count
		step_msg = msg[resent_num:num]

	# Join the characters in the shuffled lists and sort them by key
	chiphered_msg = ''.join([''.join(value) for key, value in sorted(key_to_list.items())])

	# Return the shuffled message
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
	keys = input('Enter the key via space: ').split()
	msg = input('Enter the message: ')
	key_list = list(map(int, keys))

	list_with_digraph = create_list_with_digraph(msg)
	chiphered_msg = shuffle_msg(key_list=key_list, msg=list_with_digraph)

	print(chiphered_msg)

