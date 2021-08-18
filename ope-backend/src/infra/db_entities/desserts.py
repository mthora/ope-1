from sqlalchemy import Column, Integer, String, SmallInteger, Float
from src.infra.config import Base


class Desserts(Base):
    __tablename__ = 'desserts'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    description = Column(String(200))
    price = Column(Float)
    amount = Column(Integer)
    img = Column(String(400))


    def to_dict(self):
        return {"id":self.id, "name":self.name, "description":self.description, "price":self.price, "amount":self.amount, "img":self.img}

    def __repr__(self):
        return f"Dessert [id{self.id}]"