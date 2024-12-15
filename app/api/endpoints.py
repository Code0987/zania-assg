from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..schemas import Product, ProductCreate, Order, OrderCreate
from ..services import *
from ..utils.exceptions import *
from ..utils.auth_utils import TokenBearer
from logging import getLogger


logger = getLogger(__name__)

router = APIRouter(dependencies=[Depends(TokenBearer(auto_error=False))])


@router.get("/products")
def list_products(db: Session = Depends(get_db)):
    try:
        products = get_all_products(db)
        products = [schemas.Product.model_validate(p) for p in products]
        return products
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Error retrieving products.")


@router.post("/products")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        new_product = create_product(db, product)
        new_product = schemas.Product.model_validate(new_product)
        return new_product
    except Exception as e:
        logger.error(e)
        if "uq_product_name_description_price" in str(e):
            raise HTTPException(
                status_code=400,
                detail="Product with the same name, description and price already exists.",
            )
        raise HTTPException(status_code=500, detail="Error adding product.")


@router.post("/orders")
def place_order(order: OrderCreate, db: Session = Depends(get_db)):
    try:
        new_order = create_order(db, order)
        new_order = schemas.Order.model_validate(new_order)
        return new_order
    except InsufficientStockException as e:
        raise e
    except OrderValidationException as e:
        raise e
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Error placing order.")
