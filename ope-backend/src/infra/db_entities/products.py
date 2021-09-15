
from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.config import Base


class Products(Base):

    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    description = Column(String(200))
    price = Column(Float)
    amount = Column(Integer)
    promotion = Column(Boolean)
    img = Column(String(400))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "amount": self.amount,
            "promotion": self.promotion,
            "img": self.img
        }


    def __repr__(self):
        return f"Item [id={self.id}]"
