#Functions in Python
def greet():
    print("Hello, Milind!")

greet()

#Function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Milind")

#Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

#Default arguments
def greet(name="Milind"):
    print(f"Hello, {name}!")
greet()
greet("John")

#Keyword arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
greet(name="Milind", age=25)
greet(age=30, name="John")

#Exception handling — try and except
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
finally:
    print("Execution completed.")