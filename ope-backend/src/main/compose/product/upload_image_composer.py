from src.infra.repository import ProductRepository
from src.core.controllers import UploadImageController
from src.core.use_cases import UploadImage


def upload_image_composer():
    repository = ProductRepository()
    use_case = UploadImage(repository)
    controller = UploadImageController(use_case)
    return controller
