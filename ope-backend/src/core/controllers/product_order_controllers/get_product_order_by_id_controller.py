class GetProduct_OrderController:

    def __init__(self, get_product_order_by_id_use_case):
        self.get_product_order_by_id_use_case = get_product_order_by_id_use_case

    def route(self, arg):

        if arg is not None:
            product_order_id = arg
            response = self.get_product_order_by_id_use_case.get_by_id(product_order_id=product_order_id)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}
