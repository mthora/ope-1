class RemoveAmountController:

    def __init__(self, remove_amount_use_case):
        self.remove_amount_use_case = remove_amount_use_case

    def route(self, body):
        if body is not None:
            product_id = body["id"] if "id" in body else None
            amount_to_remove = body["amount_to_remove"] if "amount_to_remove" in body else None
            response = self.remove_amount_use_case.remove_amount(product_id=product_id, amount_to_remove=amount_to_remove)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}