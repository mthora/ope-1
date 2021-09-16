from src.infra.repository import Product_OrderRepository
from src.core.use_cases import DeleteProduct_Order
from src.core.controllers import DeleteProduct_OrderController


def delete_product_order_composer():
    repository = Product_OrderRepository()
    use_case = DeleteProduct_Order(repository)
    controller = DeleteProduct_OrderController(use_case)
    return controller