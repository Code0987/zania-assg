from pydantic import BaseModel, Field, PositiveInt
from typing import List


class OrderProduct(BaseModel):
    product_id: int = Field(..., description="The unique ID of the product")
    quantity: PositiveInt = Field(
        ...,
        description="The quantity of the product to order, must be a positive integer",
    )

    class Config:
        from_attributes = True
        orm_mode = True


class OrderBase(BaseModel):
    products: List[OrderProduct] = Field(
        ..., min_length=1, description="List of products with their quantities"
    )


class OrderCreate(OrderBase):
    """Order data needed for creation, same as OrderBase."""

    pass


class Order(OrderBase):
    id: int = Field(..., description="Unique identifier for the order")
    total_price: float = Field(min=0.01, description="The total price of the order")
    status: str = Field(
        ...,
        description="The current status of the order (e.g., 'pending', 'completed')",
    )

    class Config:
        from_attributes = True
        orm_mode = True
