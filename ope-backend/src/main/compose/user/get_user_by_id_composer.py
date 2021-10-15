from src.infra.repository import UserRepository
from src.core.use_cases import GetUserById
from src.core.controllers import GetUserController


def get_user_composer():
    repository = UserRepository()
    use_case = GetUserById(repository)
    controller = GetUserController(use_case)
    return controller
