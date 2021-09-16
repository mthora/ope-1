from src.infra.repository import Product_OrderRepository
from src.core.controllers import UpdateProduct_OrderController
from src.core.use_cases import UpdateProduct_Order


def update_product_order_composer():
    repository = Product_OrderRepository()
    use_case = UpdateProduct_Order(repository)
    controller = UpdateProduct_OrderController(use_case)
    return controller
