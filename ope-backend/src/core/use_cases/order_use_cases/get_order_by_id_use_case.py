from src.core.validations import get_order_validation as validate


class GetOrderById:

    def __init__(self, order_repository):
        self.order_repository = order_repository

    def get_by_id(self, order_id):
        invalid_inputs = validate(id=order_id)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.order_repository.get_order_by_id(order_id=order_id)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
    