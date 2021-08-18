from sqlalchemy import Column, Integer, String, SmallInteger, Float
from src.infra.config import Base

class Drinks(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    price = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)
    img = Column(String(400), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price, "amount": self.amount, "img": self.img }

    def __repr__(self):
        return f"Drinks [id={self.id}]"