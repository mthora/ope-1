from sqlalchemy import Column, Integer, Float, ForeignKey
from src.infra.config import Base
from sqlalchemy.orm import relationship

class Products_Orders(Base):
    __tablename__ = "products_orders"

    id = Column(Integer, primary_key=True)

    id_product = Column(Integer, ForeignKey('products.id'), nullable=False)
    products = relationship("Products", foreign_keys=[id_product])

    id_order = Column(Integer, ForeignKey('orders.id'), nullable=False)
    order = relationship("Orders", foreign_keys=[id_order])

    price = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "id_product": self.id_product,
            "id_order": self.id_order,
            "price": self.price,
            "amount": self.amount}

    def __repr__(self):
        return f"Products Orders [id={self.id}]"
