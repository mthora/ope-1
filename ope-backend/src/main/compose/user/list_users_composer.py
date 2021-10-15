from src.infra.repository import UserRepository
from src.core.controllers import ListUsersController
from src.core.use_cases import ListUsers


def list_users_composer():
    repository = UserRepository()
    use_case = ListUsers(repository)
    controller = ListUsersController(use_case)
    return controller
