class Emp:

	def __init__(self, first, last,pay):
		self.first = first
		self.last = last
		self.pay = pay

	@property
	def fullname(self):
		return f"{self.first} {self.last}"

	@property
	def email(self):
		return f"{self.first}.{self.last}@company.com"


emp_1 = Emp('John', 'M', 60000)

emp_1.first = 'Tom'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print(emp_1.email)
print(emp_1.email)
print(emp_1.email)
print(emp_1.email)
print(emp_1.email)
print(emp_1.email)
print(emp_1.email)
print(emp_1.email)
print(emp_1.email)
print(emp_1.email)