from sqlalchemy import Column, Integer, String, SmallInteger
from src.infra.config import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    role = Column(SmallInteger, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "role": self.role, "email": self.email, "password": self.password}

    def __repr__(self):
        return f"User [email={self.email}]"
