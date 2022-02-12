def decorator_function(func):
	def wrapper_function(*args, **kwargs):
		print('Hello')
		return func(*args, **kwargs)
	return wrapper_function

@decorator_function
def disp():
	print('Disp Function')

@decorator_function
def disp_info(name, age):
	print(f"disp_info ran with args ({name}, {age})")

disp_info('John', 27)