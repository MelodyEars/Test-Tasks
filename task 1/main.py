from collections import deque

from loguru import logger


def shuffle_msg(key_list: list, msg: list) -> list:
	len_key = len(key_list)
	chiphered_msg = []

	steep_count = len_key
	num = len_key

	step_msg = msg[:num]  # ['LL', 'O', 'HE']

	while step_msg:
		for count, key in enumerate(key_list):  # key_list = [2, 3, 1]
			chiphered_msg.insert(key - 1, step_msg[count])

		resent_num = num
		num += steep_count
		step_msg = msg[resent_num:num]

	print(chiphered_msg)
	return chiphered_msg


def create_list_with_digraph(msg):
	msg_list = []

	steep_count = 3
	num = 3

	step_msg = msg[:num]

	while step_msg:
		msg_list.append(step_msg[0: 2])
		if len(step_msg) == 3:
			msg_list.append(step_msg[2])

		resent_num = num
		num += steep_count
		step_msg = msg[resent_num:num]

	print(msg_list)
	return msg_list


if __name__ == '__main__':
	# key_list = [2, 3, 1]
	# msg = "LLOHE"
	keys = input('Enter the key via space: ').split()
	msg = input('Enter the message: ')
	key_list = list(map(int, keys))

	list_with_digraph = create_list_with_digraph(msg)
	chiphered_msg = shuffle_msg(key_list=key_list, msg=list_with_digraph)

	logger.warning("".join(chiphered_msg))
