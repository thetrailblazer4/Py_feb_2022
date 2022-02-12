lst = ['hello', 'hey', 'Hi', 'Bye']


def find_index(to_search, target):
	for index, value in enumerate(to_search):
		if value == target:
			return index
	return -1

print(find_index(lst, 'Bye'))

	# print(index, value)
