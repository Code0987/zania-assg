from fastapi import HTTPException


class ProductNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="Product not found.")


class InsufficientStockException(HTTPException):
    def __init__(self, product_id: int):
        super().__init__(
            status_code=400,
            detail=f"Insufficient stock for product with ID {product_id}.",
        )


class OrderValidationException(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=400, detail=message)
