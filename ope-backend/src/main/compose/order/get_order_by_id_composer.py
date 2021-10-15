from src.infra.repository import OrderRepository
from src.core.use_cases import GetOrderById
from src.core.controllers import GetOrderController


def get_order_composer():
    repository = OrderRepository()
    use_case = GetOrderById(repository)
    controller = GetOrderController(use_case)
    return controller
