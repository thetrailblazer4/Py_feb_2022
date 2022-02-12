import logging

logging.basicConfig(filename='calc.log', level=logging.INFO)

def logger(func):
	def log_func(*args):
		logging.info(f"Running '{func.__name__}' with arguments {args}")
		print(func(*args))
	return log_func

@logger
def square(x):
	return x * x


def cube(x):
	return x * x * x

@logger
def add(a, b):
	return a + b


def sub(a, b):
	return a - b

# square(6)


add(2,3)