# f = open('test_file.txt', 'r')

# print(f.read())

# f.close()

# with open('test_file.txt', 'r') as f:
# 	for i in f:
# 		print(i, end='')

	# f_cont = f.readline()
	# print(f_cont, end='')

	# f_cont = f.readline()
	# print(f_cont, end='')

	# f_cont = f.readline()
	# print(f_cont,  end='')

	# f_cont = f.readline()
	# print(f_cont,  end='')


# with open('test_copy.txt', 'w') as f:
# 	f.write('New Line')
# 	f.seek(0)
# 	f.write('Demo Line')


# with open('test_file.txt', 'a') as rf:
# 	with open('test_file_copy.txt', 'w') as wf:
# 		for line in rf:
# 			wf.write(line)


with open('img.jpg', 'rb') as rf:
	with open('img_copy.jpg', 'wb') as wf:
		for line in rf:
			wf.write(line)