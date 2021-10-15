from src.infra.repository import UserRepository
from src.core.controllers import UpdateUserController
from src.core.use_cases import UpdateUser


def update_user_composer():
    repository = UserRepository()
    use_case = UpdateUser(repository)
    controller = UpdateUserController(use_case)
    return controller
