from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    UniqueConstraint,
)
from .. import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    __table_args__ = (
        UniqueConstraint(
            "name", "description", "price", name="uq_product_name_description_price"
        ),
    )
