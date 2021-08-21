from sqlalchemy import Column, Integer, String, SmallInteger, Float
from src.infra.config import Base


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    description = Column(String(200))
    price = Column(Float)
    amount = Column(Integer)
    promotion = Column(Float)
    img = Column(String(400))

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description, "price": self.price, "amount": self.amount, "promotion": self.promotion, "img": self.img}

    def __repr__(self):
        return f"Item [id{self.id}]"



