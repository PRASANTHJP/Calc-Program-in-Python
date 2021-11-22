# Hi Guys ,Welcome to Pyhton Programming :)
# Python program for simple calculator   # Note: # operator is single line comment in python so its not runing when program run,its just understanding purpose only 

# Function to add two numbers

def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers

def subtract(num1, num2):
	return num1 - num2

# Function to multiply two numbers

def multiply(num1, num2):
	return num1 * num2

# Function to divide two numbers

def divide(num1, num2):
	return num1 / num2

print("Please select operation -\n" 

		"1. Addition\n" 
		"2. Subtraction\n" 
		"3. Multiply\n" 
		"4. Dividion\n")
print("thanks for Coming")


# Take input from the user

select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Hi Guys Please Enter first number: "))
number_2 = int(input("Hi Guys Please Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=", multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=", divide(number_1, number_2))

else:
	print("Invalid input please enter the valid operator")
