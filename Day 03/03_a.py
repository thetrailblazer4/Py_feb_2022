# # Mutable
# list_1 = ['Hello', 'Hi', 'Bye']
# list_2 = list_1


# print(list_1)
# print(list_2)

# list_1[0] = 'Hey'

# print(list_1)
# print(list_2)

# Immutable
# tuples_1 = ('Hello', 'Hi', 'Bye')

# tuples_2 = tuples_1


# print(tuples_1)
# print(tuples_2)

# tuples_1[0] = 'Hey'

# print(tuples_1)
# print(tuples_2)

# sets = {'Hello', 'Hi', 'Bye', 'Hi'}
# print(sets)
# print('Hi' in sets)

# # Empty lists
# empty_lists = []
# empty_lists = list()

# # Empty tuples
# empty_tuples = ()
# empty_tuples = tuple()

# # Empty sets
# empty_sets = {}   # This used for creating dict
# empty_sets = set()

# dict {key: value}

emp = ['John','john@company.com','800000']

# nums = [0,1,2,3,4,5,6]

for emp_info in emp:
	print(emp_info)
# print(list(range(100)))

# for i in range(100):
# 	print('Hello')

# print('John' in emp)

# for index, item in enumerate(emp):
# 	print(index, item)

emp = {'name':'John', 'pay':800000, 'prog_lang':['Python','java']}

# print(emp.keys())
# print(emp.values())
# print(emp.items())

# for key, value in emp.items():
# 	print(f"{key} - {value}")

# emp['email'] = 'john@company.com'
# emp['phone'] = '666-33333-44'

# emp.update({'email':'john@company.com', 'Phone':'666-33333-44' })

# print(emp['email'])

# # del emp['email']
# removed = emp.pop('email')
# print(removed)


# print(emp)
# # print(emp.get('email', 'Error'))