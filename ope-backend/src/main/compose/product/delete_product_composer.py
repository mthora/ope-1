from src.infra.repository import ProductRepository
from src.core.use_cases import DeleteProduct
from src.core.controllers import DeleteProductController


def delete_product_composer():
    repository = ProductRepository()
    use_case = DeleteProduct(repository)
    controller = DeleteProductController(use_case)
    return controller