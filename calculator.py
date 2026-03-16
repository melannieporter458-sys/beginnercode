def add (n1, n2):
	"""Adds two numbers"""
	return n1 + n2

def subtract(n1, n2):
	"""Subtracts two numbers"""
	return n1 - n2

def multiply(n1, n2):
	"""Multiplies two numbers"""
	return n1 * n2

def divide(n1, n2):
	"""Divides tow numbers, handles division by zero error"""
	if n2 == 0:
		return "Error: Cannot divide by zero!"
	return n1 / n2

print("Select an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
	# Take input from the user
	choice = input("Enter choice (1/2/3/4): ")

	# Check if the choice is valid
	if choice in ['1', '2', '3', '4' ]:
		try:
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number"))
		except ValueError:
			print("Invalid input. Please enter a number.")
			continue

		if choice == '1':
			print(f"{num1} + {num2} = {add(num1, num2)}")
		elif choice == '2':
			print(f"{num1} - {num2} = {subtract(num1, num2)}")
		elif choice == '3':
			print(f"{num1} * {num2} = {multiply(num1, num2)}")
		elif choice == '4':
			result = divide(num1, num2)
			print(f"{num1} / {num2} = {result}")

		# Ask if the user wants anoter calculation
		calc_again = input("Do you want another calculation? (yes/no): ")
		if calc_again.lower() != 'yes':
			break

	else:
		print("Invalid Input! Plese enter a valid operation choice (1/2/3/4).")
