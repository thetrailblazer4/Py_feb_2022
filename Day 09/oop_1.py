# Class and instances, objects, instance variables

class Emp:

	raise_amt = 1.05
	num_of_emps = 0

	def __init__(self, first, last,pay):
		self.first = first
		self.last = last
		self.email = f'{first.lower()}.{last.lower()}@company.com'
		self.pay = pay

		Emp.num_of_emps += 1

	def fullname(self):
		return f"{self.first} {self.last}"


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_str(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday()==6:
			return False
		return True




emp_1 = Emp('Tom', 'K', 60000)
emp_2 = Emp('Jane', 'M', 70000)


import datetime

my_date = datetime.date(2022,2,5)

print(my_date)

print(Emp.is_workday(my_date))

# emp_1_str  = 'Tom-K-60000'

# new_emp_1 = Emp.from_str(emp_1_str)

# first, last, pay = emp_1_str.split('-')

# new_emp_1 = Emp(first, last, pay)

# print(new_emp_1.first)



# import datetime

# print(datetime.__file__)