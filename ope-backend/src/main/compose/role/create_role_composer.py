from src.infra.repository import RoleRepository
from src.core.controllers import CreateRoleController
from src.core.use_cases import CreateRole

def create_role_composer():
    repository = RoleRepository()
    use_case = CreateRole(repository)
    controller = CreateRoleController(use_case)
    return controller