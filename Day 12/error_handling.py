'''
FileNotFoundError
NameError

'''

# new_var = old_var

try:
	f = open('testfile.txt', 'r')

except FileNotFoundError as e:
	print(e)

except NameError as e:
	print(e)

except Exception as e:
	print(e)

else:
	print(f.read())
	f.close()

finally:
	print('hello')