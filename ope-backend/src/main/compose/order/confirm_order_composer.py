from src.infra.repository import OrderRepository
from src.core.controllers import ConfirmOrderController
from src.core.use_cases import ConfirmOrder


def confirm_order_composer():
    repository = OrderRepository()
    use_case = ConfirmOrder(repository)
    controller = ConfirmOrderController(use_case)
    return controller