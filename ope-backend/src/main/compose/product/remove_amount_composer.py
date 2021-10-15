from src.infra.repository import ProductRepository
from src.core.controllers import RemoveAmountController
from src.core.use_cases import RemoveAmount


def remove_amount_composer():
    repository = ProductRepository()
    use_case = RemoveAmount(repository)
    controller = RemoveAmountController(use_case)
    return controller