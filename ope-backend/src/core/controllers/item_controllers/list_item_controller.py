class ListItemsController:

    def __init__(self, list_items_use_case):
        self.list_items_use_case = list_items_use_case

    def route(self, body):
        response = self.list_items_use_case.list()
        return response
