from src.infra.repository import ProductRepository
from src.core.controllers import CreateProductController
from src.core.use_cases import CreateProduct


def create_product_composer():
    repository = ProductRepository()
    use_case = CreateProduct(repository)
    controller = CreateProductController(use_case)
    return controller
