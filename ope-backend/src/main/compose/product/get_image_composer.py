from src.infra.repository import ProductRepository
from src.core.controllers import GetImageController
from src.core.use_cases import GetImage


def get_image_composer():
    repository = ProductRepository()
    use_case = GetImage(repository)
    controller = GetImageController(use_case)
    return controller