from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#Temporary in memory storage
products = []
next_id = 1

#Product model
class Product(BaseModel):
    name: str
    price: float
    quantity: int

#Create
@app.post("/products")
def create_product(product: Product):
    global next_id

    new_product = {
        "id": next_id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity
    }

    products.append(new_product)
    next_id += 1

    return {
        "message": "Product created successfully",
        "product": new_product
    }

#Read All
@app.get("/products")
def get_products():
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    
    return products

#Read Single
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")

#Update
@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for product in products:
        if product["id"] == product_id:
            product["name"] = updated_product.name
            product["price"] = updated_product.price
            product["quantity"] = updated_product.quantity
            return {
                "message": "Product updated successfully",
                "product": product
            }

    raise HTTPException(status_code=404, detail="Product not found")

#Delete
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted_product = products.pop(index)

            return {
                "message": "Product deleted successfully",
                "data": deleted_product    
            }
        raise HTTPException(status_code=404, detail="Product not found")