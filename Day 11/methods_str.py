class Emp:

	raise_amt = 1.05

	def __init__(self, first, last,pay):
		self.first = first
		self.last = last
		self.email = f'{first.lower()}.{last.lower()}@company.com'
		self.pay = pay

	def fullname(self):
		return f"{self.first} {self.last}"


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	def __repr__(self):
		return f"Emp('{self.first}', '{self.last}', {self.pay})"

	def __str__(self):
		return f"{self.fullname()} - {self.email}"

emp_1 = Emp('Tom', 'K', 60000)

# print(repr(emp_1))

print(emp_1)