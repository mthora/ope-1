from src.infra.repository import OrderRepository
from src.core.controllers import CreateOrderController
from src.core.use_cases import CreateOrder


def create_order_composer():
    repository = OrderRepository()
    use_case = CreateOrder(repository)
    controller = CreateOrderController(use_case)
    return controller
