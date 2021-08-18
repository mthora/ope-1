from src.infra.repository import UserRepository
from src.core.controllers import CreateUserController
from src.core.use_cases import CreateUser


def create_user_composer():
    repository = UserRepository()
    use_case = CreateUser(repository)
    controller = CreateUserController(use_case)
    return controller
