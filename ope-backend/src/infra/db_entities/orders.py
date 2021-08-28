from sqlalchemy import Column, Integer, String, Boolean
from src.infra.config import Base


class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    done = Column(Boolean)
    initial_date = Column(String(20))
    end_date = Column(String(20))
    consumed_in = Column(String(20))
    table = Column(Integer)
    payment_method = Column(String(20))
    obs = Column(String(200))
    confirmed = Column(Boolean)

    def to_dict(self):
        return {"id": self.id,
                "done": self.done,
                "initial_date": self.initial_date,
                "end_date": self.end_date,
                "consumed_in": self.consumed_in,
                "table": self.table,
                "payment_method": self.payment_method,
                "obs": self.obs,
                "confirmed": self.confirmed}

    def __repr__(self):
        return f'Order [id{self.id}]'
