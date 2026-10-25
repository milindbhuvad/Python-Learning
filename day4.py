#Object-Oriented Programming (OOP)

#Class and object
from sys import prefix


class Employee:
    def display_details(self):
        print(f"{self.name} - {self.role}")

employee = Employee()
employee.name = "Milind"
employee.role = "Software Engineer"
employee.display_details()

#Constructor
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.salary}")

employee = Employee("Milind", 50000)
employee.display_details()

#Instance methods
class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def display_details(self):
        annual_salary = self.calculate_annual_salary()

        print(f"Employee Name: {self.name}")
        print(f"Monthly Salary: ₹{self.monthly_salary}")
        print(f"Annual Salary: ₹{annual_salary}")

employee = Employee("Milind", 50000)
employee.display_details()

#Encapsulation
    #Python conventionally uses:
    #Without any prefix (e.g., attribute) to indicate that an attribute is public and can be accessed from outside the class.
    #A single underscore prefix (e.g., _attribute) to indicate that an attribute is intended for internal use (protected).
    #A double underscore prefix (e.g., __attribute) to indicate that an attribute is private and should not be accessed directly from outside the class.

class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

employee = Employee("Milind", 50000)
print(f"Name: {employee.get_name()}")
print(f"Salary: ₹{employee.get_salary()}")

#Inheritance
# Inheritance lets a child class reuse or extend a parent class.

class Developer:
    def work(self):
        print("Writing code...")

class PHPDeveloper(Developer):
    def language(self):
        print("PHP")

developer = PHPDeveloper()
developer.work()  # Inherited method
developer.language()  # Child class method

#Method overriding
class Developer:
    def write_code(self):
        print("Writing code in a generic way...")

class PythonDeveloper(Developer):
    def write_code(self):
        print("Writing code in Python...")

python_dev = PythonDeveloper()
python_dev.write_code()  # Calls the overridden method in PythonDeveloper

#Abstract classes and interfaces
#Python supports abstract classes and interfaces through the abc module. 
# An abstract class can have abstract methods that must be implemented by subclasses.
#Python supports abstract classes through the abc module. 

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class PayPalGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing payment of ₹{amount} through PayPal.")

paypal = PayPalGateway()
paypal.process_payment(1000)  # Calls the implemented method in PayPalGateway

# Static methods and class methods
# Python provides two useful method types in addition to instance methods.
# @staticmethod defines a method that doesn't automatically receive self or cls.
# @classmethod receives the class as cls, which is useful for accessing class-level data or implementing alternative constructors.
class Employee:
    company = "TechCorp"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

    @staticmethod
    def company_policy():
        print("Company policy: Work hard, stay humble.")

    @classmethod
    def get_company(cls):
        return cls.company

print(Employee.company_policy())  # Calling static method  
print(Employee.get_company())  # Accessing class method
