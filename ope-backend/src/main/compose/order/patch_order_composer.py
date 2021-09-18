from src.infra.repository import OrderRepository
from src.core.controllers import PatchOrderController
from src.core.use_cases import PatchOrder


def patch_order_composer():
    repository = OrderRepository()
    use_case = PatchOrder(repository)
    controller = PatchOrderController(use_case)
    return controller