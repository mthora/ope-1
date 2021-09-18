class PatchOrderController:

    def __init__(self, patch_order_use_case):
        self.patch_order_use_case = patch_order_use_case

    def route(self, body):

        if body is not None:
            order_id = body["id"] if "id" in body else None
            done = body["done"] if "done" in body else None


            response = self.patch_order_use_case.patch_order(order_id=order_id, done=done) # verificar
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}