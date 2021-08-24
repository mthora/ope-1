from src.infra.repository import DrinkRepository
from src.core.use_cases import GetDrinkById
from src.core.controllers import GetDrinkController


def get_drink_composer():
    repository = DrinkRepository()
    use_case = GetDrinkById(repository)
    controller = GetDrinkController(use_case)
    return controller
