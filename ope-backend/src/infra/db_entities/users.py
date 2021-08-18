from sqlalchemy import Column, Integer, String
from src.infra.config import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return f"User [name={self.email}]"
