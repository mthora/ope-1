class GetOrderController:

    def __init__(self, get_order_by_id_use_case):
        self.get_order_by_id_use_case = get_order_by_id_use_case

    def route(self, arg):

        if arg is not None:
            order_id = arg
            response = self.get_order_by_id_use_case.get_by_id(order_id=order_id)
            return response
        return {"data": None, "status": 400, "errors": ["Invalid request"]}
