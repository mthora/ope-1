from src.infra.repository import DrinkRepository
from src.core.controllers import ListDrinksController
from src.core.use_cases import ListDrinks


def list_drinks_composer():
    repository = DrinkRepository()
    use_case = ListDrinks(repository)
    controller = ListDrinksController(use_case)
    return controller
