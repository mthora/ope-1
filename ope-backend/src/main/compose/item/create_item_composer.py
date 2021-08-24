from src.infra.repository import ItemRepository
from src.core.controllers import CreateItemController
from src.core.use_cases import CreateItem


def create_item_composer():
    repository = ItemRepository()
    use_case = CreateItem(repository)
    controller = CreateItemController(use_case)
    return controller
