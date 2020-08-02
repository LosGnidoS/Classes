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
		min_age = 25
		print("How much do you wish?")
		x = input(); x = int(x)
		while x > self.max_credit:
			print("How much do you wish?")
			x = input(); x = int(x)

		if salary < min_salary:
			return "Sorry, you'd been\
 denied credit.You're too bomzh..."
		elif age <= max_age and age >= min_age:
			return "Credit approved!\
{}$ is now yours".format(x)
		else:
			return "Credit denied,you're\
too young..."

client = Client(1)
print(client.pay(20000,31))




