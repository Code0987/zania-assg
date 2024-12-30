from pydantic import BaseModel, Field, PositiveInt


class OrderItem(BaseModel):
    id: int = Field(..., description="The unique ID of the product")
    quantity: PositiveInt = Field(
        ...,
        description="The quantity of the product to order, must be a positive integer",
    )

    class Config:
        from_attributes = True


class Order(BaseModel):
    id: int = Field(..., description="Unique identifier for the order")
    price: float = Field(min=0.01, description="The total price of the order")

    class Config:
        from_attributes = True
