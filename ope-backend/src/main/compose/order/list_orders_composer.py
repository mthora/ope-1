from src.infra.repository import OrderRepository
from src.core.controllers import ListOrdersController
from src.core.use_cases import ListOrders


def list_orders_composer():
    repository = OrderRepository()
    use_case = ListOrders(repository)
    controller = ListOrdersController(use_case)
    return controller


