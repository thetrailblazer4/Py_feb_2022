'''

if it treats functions as first-class citizens. 
This means the language supports passing functions as arguments to other functions, 
returning them as the values from other functions, and 
assigning them to variables or storing them in data structures.


is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable.[1]

'''

def square(x):
	return x * x


result = square
print(result.__name__)

# def cube(x):
# 	return x * x * x


# def my_lst(func, arg_lst):
# 	result = []
# 	for i in lst:
# 		result.append(func(i))
# 	return result

# lst = [1,2,3,4]


# print(my_lst(cube, lst))


# print(result)


# result = square(8)
# print(result)





# def outer_func(message):
# 	def inner_fun():
# 		print(message)
# 	return inner_fun


# new_var = outer_func('hello')
# new_var()


# def decorater_func(func):
# 	def wrapper_func():
# 		print('Hello')
# 		return func()
# 	return wrapper_func

# @decorater_func
# def display():
# 	print('executed display function')



# dec_disp = decorater_func(display)
# dec_disp()

# display()