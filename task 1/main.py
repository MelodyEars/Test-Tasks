

def solve(key: list, msg: list):
	# список, куди буде записано дешифроване повідомлення. Спочатку він ініціалізується таким самим, як msg.
	decrypted = msg

	# Проходимо циклом по всіх символах повідомлення msg.
	for i, char in enumerate(msg):
		# беремо номер символу ключа key_index за модулем довжини ключа
		key_index = i % len(key)

		# беремо загальний індекс за формулою:
		# index = (кількість повних циклів по ключу) * (довжина ключа) + (номер символу ключа)
		index = (round(i / len(key)) * len(key)) + key[key_index]

		# Записуємо символ у decrypted за обчисленим індексом.
		decrypted[index - 1] = char

		# Виводимо для зручності, куди потрапив символ.
		print(f'{char}, at index {i}, goes in destination index {index - 1} (letter number {index})')

	# з'єднуємо символи і отримуємо дешифроване повідомлення.
	print(''.join(decrypted))


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
	key_list = [2, 3, 1]
	msg = "LLOHE"
	# keys = input('Enter the key via space: ').split()
	# msg = input('Enter the message: ')
	# key_list = list(map(int, keys))

	list_with_digraph = create_list_with_digraph(msg)
	solve(key=key_list, msg=list_with_digraph)
