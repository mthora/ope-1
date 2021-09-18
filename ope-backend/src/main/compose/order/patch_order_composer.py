from src.infra.repository import OrderRepository
from src.core.controllers import PatchOrderController
from src.core.use_cases import PatchProduct


def patch_order_composer():
    repository = OrderRepository()
    use_case = PatchProduct(repository)
    controller = PatchOrderController(use_case)
    return controller