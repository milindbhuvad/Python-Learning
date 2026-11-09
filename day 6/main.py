from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return{
        "message": "Welcome to Python FastAPI",
        "developer": "Milind"
    }

@app.get("/employee/{employee_id}")
def get_employee(employee_id: int):
    return{
        "employee_id": employee_id,
        "name": "John Doe",
        "department": "Engineering"
    }

@app.get("/search")
def search_employee(name: str = None, department: str = None):
    return{
        "name": name,
        "department": department
    }

class Employee(BaseModel):
    name: str
    email: str
    role: str
    salary: float

@app.post("/employee")
def create_employee(employee: Employee):
    return{
        "message": "Employee created successfully",
        "employee": employee
    }

#Day 6 Exercise
@app.get("/products")
def get_products():
    return {
        "products": [
            {"id": 1, "name": "Gold Ring", "price": 25000},
            {"id": 2, "name": "Gold Chain", "price": 50000}
        ]
    }

class Product(BaseModel):
    name: str
    price: float
    quantity: int

@app.post("/products")
def create_product(product: Product):
    return {
        "message": "Product created successfully",
        "product": product
    }