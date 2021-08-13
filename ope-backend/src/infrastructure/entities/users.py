from sqlalchemy import Column, String, Integer
from src.infrastructure.config import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"User [id={self.id}]"
