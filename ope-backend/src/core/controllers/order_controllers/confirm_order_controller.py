class ConfirmOrderController:

    def __init__(self, confirm_order_use_case):
        self.confirm_order_use_case = confirm_order_use_case

    def route(self, body):
        if body is not None:
            order_id = body["id"] if "id" in body else None
            confirmed = body["confirmed"] if "confirmed" in body else None
            response = self.confirm_order_use_case.confirm_order(order_id=order_id, confirmed=confirmed)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}