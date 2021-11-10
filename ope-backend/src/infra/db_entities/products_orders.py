from sqlalchemy import Column, Integer, Float, ForeignKey, String
from src.infra.config import Base
from sqlalchemy.orm import relationship

class Products_Orders(Base):
    __tablename__ = "products_orders"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    products = relationship("Products", back_populates="products_orders")

    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    orders = relationship("Orders", back_populates="products_orders")

    price = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)

    name = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "product_id": self.product_id,
            "order_id": self.order_id,
            "price": self.price,
            "amount": self.amount}

    def __repr__(self):
        return f"Products Orders [id={self.id}]"
