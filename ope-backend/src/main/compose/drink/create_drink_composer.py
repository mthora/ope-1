from src.infra.repository import DrinkRepository
from src.core.controllers import CreateDrinkController
from src.core.use_cases import CreateDrink

def create_drink_composer():
    repository = DrinkRepository()
    use_case = CreateDrink(repository)
    controller = CreateDrinkController(use_case)
    return controller