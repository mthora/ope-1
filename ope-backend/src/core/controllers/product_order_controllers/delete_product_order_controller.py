class DeleteProduct_OrderController:

    def __init__(self, delete_product_order_use_case):
        self.delete_product_order_use_case = delete_product_order_use_case

    def route(self, arg):
        if arg is not None:
            product_order_id = arg
            response = self.delete_product_order_use_case.delete_product_order(product_order_id=product_order_id)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}
