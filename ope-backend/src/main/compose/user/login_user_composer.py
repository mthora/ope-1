from src.infra.repository import UserRepository
from src.core.controllers import LoginUserController
from src.core.use_cases import LoginUser


def login_user_composer():
    repository = UserRepository()
    use_case = LoginUser(repository)
    controller = LoginUserController(use_case)
    return controller