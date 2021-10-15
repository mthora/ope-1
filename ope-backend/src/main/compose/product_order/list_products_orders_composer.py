from src.infra.repository import Product_OrderRepository
from src.core.controllers import ListProducts_OrdersController
from src.core.use_cases import ListProducts_Orders


def list_products_orders_composer():
    repository = Product_OrderRepository()
    use_case = ListProducts_Orders(repository)
    controller = ListProducts_OrdersController(use_case)
    return controller
