#!/usr/bin/python3
#created by Kirill Shvedov

class Client:
	max_credit = 35000
	
	def __init__(self, passport_id):  
		self.count = 0
		self.passport_id = passport_id
			
	def pay(self, salary, age):
		min_salary = 3000
		max_age = 40
		print("How much money do you wish?")
		x = input()

		if salary < min_salary:
			return "Sorry, you'd been denied credit."
		elif age <= max_age:
			return '''Credit approved! {}$ is now yours'''.format(x)
		else:
			return "Credit denied"

client = Client(1)
print(client.pay(9999, 20))




