from src.infra.repository import Product_OrderRepository
from src.core.use_cases import GetProduct_OrderById
from src.core.controllers import GetProduct_OrderController


def get_product_order_composer():
    repository = Product_OrderRepository()
    use_case = GetProduct_OrderById(repository)
    controller = GetProduct_OrderController(use_case)
    return controller
