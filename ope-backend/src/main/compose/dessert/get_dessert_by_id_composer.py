from src.infra.repository import DessertRepository
from src.core.use_cases import GetDessertById
from src.core.controllers import GetDessertController

def get_dessert_composer():
    repository = DessertRepository()
    use_case = GetDessertById(repository)
    controller = GetDessertController(use_case)
    return controller


