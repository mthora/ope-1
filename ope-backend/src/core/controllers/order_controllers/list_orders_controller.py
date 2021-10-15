class ListOrdersController:

    def __init__(self, list_orders_use_case):
        self.list_orders_use_case = list_orders_use_case

    def route(self, body):
        response = self.list_orders_use_case.list()
        return response
