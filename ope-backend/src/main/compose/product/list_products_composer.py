from src.infra.repository import ProductRepository
from src.core.controllers import ListProductsController
from src.core.use_cases import ListProducts


def list_products_composer():
    repository = ProductRepository()
    use_case = ListProducts(repository)
    controller = ListProductsController(use_case)
    return controller
