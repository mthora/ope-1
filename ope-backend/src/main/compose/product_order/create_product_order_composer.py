from src.infra.repository import Product_OrderRepository
from src.core.controllers import CreateProduct_OrderController
from src.core.use_cases import CreateProduct_Order


def create_product_order_composer():
    repository = Product_OrderRepository()
    use_case = CreateProduct_Order(repository)
    controller = CreateProduct_OrderController(use_case)
    return controller
