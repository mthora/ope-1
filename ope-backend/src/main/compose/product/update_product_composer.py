from src.infra.repository import ProductRepository
from src.core.controllers import UpdateProductController
from src.core.use_cases import UpdateProduct


def update_product_composer():
    repository = ProductRepository()
    use_case = UpdateProduct(repository)
    controller = UpdateProductController(use_case)
    return controller