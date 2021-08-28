from sqlalchemy import Column, Integer, Float
from src.infra.config import Base

#FALTA ADICIONAR CHAVE ESTRANGEIRA DAS TABELAS ORDERS E PRODUCTS

class Products_Orders(Base):
    __tablename__ = "products_orders"

    id = Column(Integer, primary_key=True)
    id_product = Column(Integer)
    id_order = Column(Integer)
    price = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)


    def to_dict(self):
        return {"id": self.id,"id_product": self.id_product, "id_order": self.id_order, "price": self.price, "amount": self.amount}

    def __repr__(self):
        return f"Products Orders [id={self.id}]"
