# LEGB --> Local, Enclosing, Global and Builtins

# x = 'global x'

# def demo(z):
# 	# global x
# 	x = 'local y'
# 	print(z)


# demo('local z')
# # print(z)


# import builtins

# print(dir(builtins))

# def max():
# 	pass

# nums = [0,3,1,2,5,4]

# print(max(nums))



x = 'global x'

def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print(x)
	inner()
	print(x)

outer()
print(x)