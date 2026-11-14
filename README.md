# Python Learning

This repository contains beginner-friendly Python examples and exercises covering core programming concepts.

# Python Installation
- Download it from the official Python website
- To check python version run below command
    - python --version


## Files

- `day1.py` 
    - Variables and Data Types in Python
        - Check Data Types of variables
        - String concatenation and f-strings
    - Arithmetic operators
    - Conditional statements
    - Using functions for reusable logic

- `day2.py` 
    - String operations
        - Checking text in a string
    - List operations
        - Looping through a list  
    - Range function
    - Dictionary example
        - List of dictionaries 
    - if-elif-else conditions
    - Practical example — skill checker
    - Practical employee example

- `day3.py`
    - Functions in Python
        - Function with parameters
        - Function with return value
        - Default arguments
        - Keyword arguments
    
    - Exception handling — try and except

- `day4.py`
    - Object-Oriented Programming (OOP)
        - Class and object basics
        - Constructors and instance methods
        - Encapsulation with private attributes
        - Inheritance and method overriding
        - Abstract classes and interfaces
        - Static methods and class methods

- `day 7/main.py`
    - FastAPI REST API basics
        - CRUD operations for products
        - In-memory storage using a Python list
        - Request validation with Pydantic models
        - HTTPException for error responses

- `day_8_database.py`
    - Run below command to install MySQL connector
        python -m pip install mysql-connector-python

    - Database connectivity with MySQL
        - Using `mysql.connector` to connect to a database
        - Configuring host, username, password, and database name
        - Verifying the connection with `is_connected()`
        - Preparing for future CRUD operations using Python and SQL

- `day_8_database_test.py`
    - Testing the database connection
        - Prints a success message when the DB connection is established
        - Helps verify MySQL is available before running database logic

- `day_9_crud_api.py`
    - FastAPI CRUD API with MySQL
        - Create product: `POST /products`
        - Read all products: `GET /products`
        - Read one product: `GET /products/{product_id}`
        - Update product: `PUT /products/{product_id}`
        - Delete product: `DELETE /products/{product_id}`
        - Uses `mysql.connector` to connect to the database and perform SQL operations

Note:
- The project continues with hands-on Python practice and backend API development.
- Day 7 introduces FastAPI, which is used to build simple REST endpoints for create, read, update, and delete operations.
- Day 8 focuses on connecting Python to a MySQL database and validating that the database server is reachable.
- Day 9 builds a complete CRUD API using FastAPI and MySQL to manage product records in a database.



