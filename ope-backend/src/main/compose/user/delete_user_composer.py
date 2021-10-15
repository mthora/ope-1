from src.infra.repository import UserRepository
from src.core.use_cases import DeleteUser
from src.core.controllers import DeleteUserController


def delete_user_composer():
    repository = UserRepository()
    use_case = DeleteUser(repository)
    controller = DeleteUserController(use_case)
    return controller
