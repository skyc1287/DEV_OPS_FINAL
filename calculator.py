"""Module docstring."""

# define function for addition
def add(x, y):
    """ docstring for add function"""
    return x + y

# define function for subtraction
def subtract(x, y):
    """ docstring for subtract function"""
    return x - y

# define function for multiplication
def multiply(x, y):
    """ docstring for multiply function"""
    return x * y

# define function for division
def divide(x, y):
    """ docstring for divide function"""
    return x / y

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter first number:  "))
num2 = float(input("Enter second number:  "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")
