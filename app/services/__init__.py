from sqlalchemy import insert
from sqlalchemy.orm import Session
from ..db import models
from .. import schemas
from ..utils.exceptions import *


def get_all_products(db: Session):
    products = db.query(models.Product).all()
    if not products:
        raise ProductNotFoundException()
    return products


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        total_price=0,
        status="pending",
    )
    db.add(db_order)
    db.flush()

    total_price = 0
    for item in order.products:
        product = (
            db.query(models.Product)
            .filter(models.Product.id == item.product_id)
            .first()
        )
        if not product:
            raise ProductNotFoundException()
        if product.stock < item.quantity:
            raise InsufficientStockException(product_id=item.product_id)
        product.stock -= item.quantity
        total_price += product.price * item.quantity

        db.add(product)
        db.execute(
            insert(models.OrderProduct).values(
                order_id=db_order.id,
                product_id=item.product_id,
                quantity=item.quantity
            )
        )

    db_order.total_price = total_price
    db_order.status = "completed"

    db.commit()
    db.refresh(db_order)
    return db_order
