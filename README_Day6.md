# Python Day 6 --- Build Your First REST API Using FastAPI

## Learning objectives

By the end of this lesson, you will be able to:

-   Explain what FastAPI is.
-   Create and run a FastAPI application locally.
-   Build GET endpoints with path and query parameters.
-   Build a POST endpoint that accepts and validates JSON.
-   Test endpoints using FastAPI's automatic Swagger documentation.

## 1. What is FastAPI?

FastAPI is a Python web framework for building APIs. It supports request
validation, asynchronous programming, and automatic API documentation.

Documentation: https://fastapi.tiangolo.com/

## 2. Set up the project

Open PowerShell:

``` powershell
cd D:\Python-Learning
```

Create a virtual environment if you have not already created one:

``` powershell
python -m venv .venv
```

Activate it:

``` powershell
.\.venv\Scripts\Activate.ps1
```

Install FastAPI:

``` powershell
python -m pip install "fastapi[standard]"
```

Check the installation:

``` powershell
python -m pip show fastapi
```

`fastapi[standard]` installs FastAPI and its standard optional
dependencies, including the development server tooling.

## 3. Project structure

Create `main.py` in your project directory:

``` text
Python-Learning/
├── .venv/
└── main.py
```

## 4. Create the first API endpoint

Add this to `main.py`:

``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Python FastAPI",
        "developer": "Milind"
    }
```

### Explanation

-   `FastAPI()` creates the application.
-   `@app.get("/")` registers a GET endpoint at `/`.
-   `home()` runs when that endpoint is requested.
-   Returning a dictionary produces a JSON response.

## 5. Run the API

With the virtual environment activated, run:

``` powershell
fastapi dev main.py
```

The development server normally runs at:

``` text
http://127.0.0.1:8000
```

Open that address in a browser. Expected response:

``` json
{
  "message": "Welcome to Python FastAPI",
  "developer": "Milind"
}
```

To stop the server, press `Ctrl+C` in the terminal.

## 6. GET API with a path parameter

Add this endpoint:

``` python
@app.get("/employee/{employee_id}")
def get_employee(employee_id: int):
    return {
        "employee_id": employee_id,
        "name": "Milind",
        "role": "PHP Developer"
    }
```

Test:

``` text
http://127.0.0.1:8000/employee/101
```

Expected response:

``` json
{
  "employee_id": 101,
  "name": "Milind",
  "role": "PHP Developer"
}
```

The `employee_id: int` type annotation tells FastAPI to validate the
path parameter as an integer. An invalid value, such as `/employee/abc`,
produces a validation error.

## 7. GET API with a query parameter

Add:

``` python
@app.get("/search")
def search_employee(name: str):
    return {
        "search_name": name,
        "message": "Employee search successful"
    }
```

Test:

``` text
http://127.0.0.1:8000/search?name=Milind
```

Expected response:

``` json
{
  "search_name": "Milind",
  "message": "Employee search successful"
}
```

## 8. POST API with Pydantic validation

Add a Pydantic model and POST endpoint:

``` python
from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    email: str
    role: str
    salary: float


@app.post("/employees")
def create_employee(employee: Employee):
    return {
        "message": "Employee created successfully",
        "data": employee
    }
```

Example request body:

``` json
{
  "name": "Milind",
  "email": "milind@example.com",
  "role": "PHP Developer",
  "salary": 54757
}
```

FastAPI validates the incoming JSON against the `Employee` model. For
example, a non-numeric salary value will cause a validation error.

**Important:** This example only returns the submitted data. It does not
save an employee to a database yet.

## 9. Test APIs using Swagger UI

FastAPI generates interactive API documentation automatically.

Open:

``` text
http://127.0.0.1:8000/docs
```

Steps:

1.  Find an endpoint.
2.  Expand it.
3.  Click **Try it out**.
4.  Enter any required parameters or JSON body.
5.  Click **Execute**.
6.  Review the response and status code.

Alternative documentation is available at:

``` text
http://127.0.0.1:8000/redoc
```

## 10. Complete `main.py`

The complete file should look like this:

``` python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Employee(BaseModel):
    name: str
    email: str
    role: str
    salary: float


@app.get("/")
def home():
    return {
        "message": "Welcome to Python FastAPI",
        "developer": "Milind"
    }


@app.get("/employee/{employee_id}")
def get_employee(employee_id: int):
    return {
        "employee_id": employee_id,
        "name": "Milind",
        "role": "PHP Developer"
    }


@app.get("/search")
def search_employee(name: str):
    return {
        "search_name": name,
        "message": "Employee search successful"
    }


@app.post("/employees")
def create_employee(employee: Employee):
    return {
        "message": "Employee created successfully",
        "data": employee
    }
```

Run the application:

``` powershell
fastapi dev main.py
```

## 11. Day 6 practice exercise --- Product API

Build these two endpoints yourself.

### GET `/products`

Return a list of products:

``` json
[
  {
    "id": 1,
    "name": "Gold Ring",
    "price": 25000
  },
  {
    "id": 2,
    "name": "Gold Chain",
    "price": 50000
  }
]
```

### POST `/products`

Create a Pydantic model that accepts:

-   `name`
-   `price`
-   `quantity`

Return a success message and the submitted product details.

Test both endpoints using Swagger UI at `http://127.0.0.1:8000/docs`.

## 12. Key concepts learned

-   FastAPI application creation.
-   GET and POST endpoints.
-   Path parameters and query parameters.
-   Pydantic request models and automatic validation.
-   JSON responses.
-   Running an API with the FastAPI development server.
-   Testing APIs through Swagger UI.