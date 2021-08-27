class ListProducts_Orders:

    def __init__(self, product_order_repository):
        self.product_order_repository = product_order_repository

    def list(self):
        try:
            response = self.product_order_repository.list_products_orders()
            return response
        except:
            return {"data": None, "status": 400, "errors": ["Erro na requisição"]}
