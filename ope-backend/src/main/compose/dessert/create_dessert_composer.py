from src.infra.repository import DessertRepository
from src.core.controllers import CreateDessertController
from src.core.use_cases import CreateDessert


def create_dessert_composer():
    repository = DessertRepository()
    use_case = CreateDessert(repository)
    controller = CreateDessertController(use_case)
    return controller
