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


class Developer(Emp):
	raise_amt = 1.09

	def __init__(self, first, last,pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang


class Manager(Emp):

	def __init__(self, first, last,pay, employees=None):
		super().__init__(first, last, pay)

		if employees is None:
			self.employees = []
		else:
			self.employees = employees


	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def display_emp(self):
		for i in self.employees:
			print(i.fullname())



emp_1 = Emp('Tom', 'K', 60000)
emp_2 = Developer('Jane', 'M', 70000, 'python')
mgr = Manager('John', 'H', 90000, [emp_1])


# print(mgr.first)

# mgr.add_emp(emp_2)
# mgr.remove_emp(emp_1)

# mgr.display_emp()

# print(isinstance(mgr, Emp))
print(issubclass(Manager, Emp))