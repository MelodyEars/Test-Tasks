
from collections import deque


def cipher_msg(encrypted_msg: dict, key_list: list):
	chiphered_msg = ""
	key_list.sort()
	while len(msg) > 0:
		for key in key_list:
			chiphered_msg += encrypted_msg[key]
			print(chiphered_msg)

	return chiphered_msg

def shuffle_msg(key_list: list, msg: deque) -> dict:
	encrypted_msg = {}
	while len(msg) > 0:
		for key in key_list:
			encrypted_msg[key] = msg.popleft()

	return encrypted_msg


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
	return deque(msg_list)


if __name__ == '__main__':
	key_list = [2, 3, 1]
	msg = "LLOHE"
	# keys = input('Enter the key via space: ').split()
	# msg = input('Enter the message: ')
	# key_list = list(map(int, keys))

	list_with_digraph = create_list_with_digraph(msg)
	encrypted_msg = shuffle_msg(key_list=key_list, msg=list_with_digraph)
	chiphered_msg = cipher_msg(encrypted_msg=encrypted_msg, key_list=key_list)

	print(chiphered_msg)
