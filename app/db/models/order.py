from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
)
from sqlalchemy.orm import relationship
from .. import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    total_price = Column(Float, nullable=False)
    status = Column(String, default="pending")

    products = relationship("OrderProduct", back_populates="order")
