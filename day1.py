# Variables and Data Types in Python
name = "Milind"
age = 38
salary = 100000.00
is_employed = True

# 1. Data types
print("Data Types:")
print(type(name))
print(type(age))
print(type(salary))
print(type(is_employed))

# 2. String concatenation and f-strings
full_message = "Hello, " + name + "!"
print("String Example:")
print(full_message)
print(f"My name is {name}, I am {age} years old, and I earn ${salary:,.2f}.")
print()

# 3. Arithmetic operators
print("Arithmetic Operators:")
a = 10
b = 5

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")
print()

# 4. Conditional statements
print("Age Check:")
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
print()

# 5. Comparison operators
print("Comparison Operators:")
x = 10
y = 5

print(f"Equal: {x == y}")
print(f"Not Equal: {x != y}")
print(f"Less Than: {x < y}")
print(f"Greater Than: {x > y}")
print(f"Less Than or Equal: {x <= y}")
print(f"Greater Than or Equal: {x >= y}")
print()

# 6. Smart practice: using functions for reusable logic

def check_adult(person_age):
    if person_age >= 18:
        return "Adult"
    return "Minor"

print("Function Example:")
print(f"Milind is an {check_adult(age)}.")