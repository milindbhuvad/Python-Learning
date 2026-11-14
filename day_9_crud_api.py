from fastapi import FastAPI
from pydantic import BaseModel
from day_8_database import get_db_connection

app = FastAPI()

#Product request model
class Product(BaseModel):
    name: str
    price: float
    quantity: int

#Create a new product
@app.post("/products")
def create_product(product: Product):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (product.name, product.price, product.quantity))
        connection.commit()

        return {"message": "Product created successfully."}
    except Exception as error:
        return {"error": str(error)}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#Read all products
@app.get("/products")
def read_products():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM products"
        cursor.execute(select_query)
        products = cursor.fetchall()

        return {"products": products}
    except Exception as error:
        return {"error": str(error)}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#Read a single product by ID
@app.get("/products/{product_id}")
def read_product(product_id: int):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM products WHERE id = %s"
        cursor.execute(select_query, (product_id,))
        product = cursor.fetchone()

        if product:
            return {"product": product}
        else:
            return {"error": "Product not found"}
    except Exception as error:
        return {"error": str(error)}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#Update a product by ID
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        update_query = "UPDATE products SET name = %s, price = %s, quantity = %s WHERE id = %s"
        cursor.execute(update_query, (product.name, product.price, product.quantity, product_id))
        connection.commit()

        if cursor.rowcount > 0:
            return {"message": "Product updated successfully."}
        else:
            return {"error": "Product not found"}
    except Exception as error:
        return {"error": str(error)}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#Delete a product by ID
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        delete_query = "DELETE FROM products WHERE id = %s"
        cursor.execute(delete_query, (product_id,))
        connection.commit()

        if cursor.rowcount > 0:
            return {"message": "Product deleted successfully."}
        else:
            return {"error": "Product not found"}
    except Exception as error:
        return {"error": str(error)}
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()