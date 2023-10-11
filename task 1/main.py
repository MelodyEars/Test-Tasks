from loguru import logger


def shuffle_msg(key_list: list, msg: list) -> list:
	key_to_list = {key: [] for key in sorted(key_list)}

	steep_count = len(key_list)
	num = steep_count
	step_msg = msg[:num]  # ['HE', 'L', 'LO', 'W', 'OR', 'L', 'D']

	while step_msg:
		for i, key in enumerate(key_list):
			if i < len(step_msg):
				key_to_list[key].append(step_msg[i])

		resent_num = num
		num += steep_count
		step_msg = msg[resent_num:num]

		print(key_to_list)

	chiphered_msg = ''.join([''.join(value) for key, value in sorted(key_to_list.items())])
	print(chiphered_msg)
	return chiphered_msg


def create_list_with_digraph(msg):
	msg_list = []
	step_count = 3
	num = 3
	step_msg = msg[:num]

	while step_msg:
		msg_list.append(step_msg[0:2])
		if len(step_msg) == 3:
			msg_list.append(step_msg[2])

		resent_num = num
		num += step_count
		step_msg = msg[resent_num:num]

	print(msg_list)
	return msg_list


if __name__ == '__main__':
	keys = input('Enter the key via space: ').split()
	msg = input('Enter the message: ')
	key_list = list(map(int, keys))

	list_with_digraph = create_list_with_digraph(msg)
	chiphered_msg = shuffle_msg(key_list=key_list, msg=list_with_digraph)

	logger.warning("".join(chiphered_msg))


