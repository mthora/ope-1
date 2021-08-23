from src.infra.repository import DessertRepository
from src.core.controllers import ListDessertsController
from src.core.use_cases import ListDesserts

def list_desserts_composer():
    repository = DessertRepository()
    use_case = ListDesserts(repository)
    controller = ListDessertsController(use_case)
    return controller