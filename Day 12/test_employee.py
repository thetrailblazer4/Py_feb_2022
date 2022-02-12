import unittest
from employee import Emp



class TestEmp(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('Hello World')

	@classmethod
	def tearDownClass(cls):
		print('Bye')

	def setUp(self):
		print('SetUp')
		self.emp_1 = Emp('John', 'M', 50000)
		self.emp_2 = Emp('Tom', 'K', 60000)

	def tearDown(self):
		print('tearDown')


	def test_fullname(self):

		self.assertEqual(self.emp_1.fullname, 'John M')
		self.assertEqual(self.emp_2.fullname, 'Tom K')

		self.emp_1.first = 'Jane'
		self.emp_2.first = 'Kate'

		self.assertEqual(self.emp_1.fullname, 'Jane M')
		self.assertEqual(self.emp_2.fullname, 'Kate K')
		print('Test')


	def test_email(self):

		self.assertEqual(self.emp_1.email, 'John.M@company.com')
		self.assertEqual(self.emp_2.email, 'Tom.K@company.com')

		self.emp_1.first = 'Jane'
		self.emp_2.first = 'Kate'

		self.assertEqual(self.emp_1.email, 'Jane.M@company.com')
		self.assertEqual(self.emp_2.email, 'Kate.K@company.com')

		print('Test')


	def test_apply_raise(self):

		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 52500)
		self.assertEqual(self.emp_2.pay, 63000)

		print('Test')










if __name__ == '__main__':
	unittest.main()