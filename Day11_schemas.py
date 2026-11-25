from pydantic import BaseModel, ConfigDict, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)

class ProductResponse(ProductCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)