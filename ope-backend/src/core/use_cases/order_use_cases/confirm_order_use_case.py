from src.core.validations import patch_order_validation as validate

class ConfirmOrder:

    def __init__(self, order_repository):
        self.order_repository = order_repository

    def confirm_order(self, order_id: int, confirmed: bool):
        invalid_inputs = validate(order_id=order_id,
                                  done=confirmed)

        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.order_repository.confirm_order(order_id=order_id,
                                  confirmed=confirmed)

            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}