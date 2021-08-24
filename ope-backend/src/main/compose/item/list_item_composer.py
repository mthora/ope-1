from src.infra.repository import ItemRepository
from src.core.controllers import ListItemsController
from src.core.use_cases import ListItems


def list_item_composer():
    repository = ItemRepository()
    use_case = ListItems(repository)
    controller = ListItemsController(use_case)
    return controller
