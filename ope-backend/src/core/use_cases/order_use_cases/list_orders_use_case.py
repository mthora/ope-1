class ListOrders:

    def __init__(self, order_repository):
        self.order_repository = order_repository

    def list(self):
        try:
            response = self.order_repository.list_orders()
            return response
        except:
            return {"data": None, "status": 400, "errors": ["Request error"]}
