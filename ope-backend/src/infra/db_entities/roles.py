from sqlalchemy import Column, Integer, String
from src.infra.config import Base

class Roles(Base):
    __tablename__="role"

    id = Column(Integer, primary_key=True)
    role = Column(String(20), nullable=False)

    def to_dict(self):
        return {"id":self.id, "role":self.role}

    def __repr__(self):
        return f"Role [id:{self.id} role: {self.role}]"


