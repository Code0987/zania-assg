from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(..., description="The name of the product")
    description: str = Field(..., description="A detailed description of the product")
    price: float = Field(
        min=0.01, description="Price of the product, must be greater than zero"
    )
    stock: int = Field(..., description="Number of items in stock")

    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True


class ProductCreate(ProductBase):
    """Product data needed for creation, same as ProductBase."""

    pass


class Product(ProductBase):
    id: int = Field(..., description="Unique identifier for the product")

    class Config:
        from_attributes = True
        orm_mode = True
