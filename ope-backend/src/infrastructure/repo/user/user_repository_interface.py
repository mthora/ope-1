from abc import ABC, abstractmethod
from typing import List
from src.domain.dtos import Users


class UserRepositoryInterface(ABC):

    @abstractmethod
    def create_user(self, name: str, password: str) -> Users:
        raise Exception("Método create_user não implementado")

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> List[Users]:
        raise Exception("Método get_user_by_id não implementado")
