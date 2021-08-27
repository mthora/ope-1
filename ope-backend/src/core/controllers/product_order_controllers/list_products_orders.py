class ListProducts_OrdersController:

    def __init__(self, list_products_orders_use_case):
        self.list_products_orders_use_case = list_products_orders_use_case

    def route(self, body):
        response = self.list_products_orders_use_case.list()
        return response
