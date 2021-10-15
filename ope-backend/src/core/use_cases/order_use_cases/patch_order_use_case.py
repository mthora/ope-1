from src.core.validations import patch_order_validation as validate


class PatchOrder:

    def __init__(self, order_repository):
        self.order_repository = order_repository

    def patch_order(self, order_id: int, done: bool):
        invalid_inputs = validate(order_id=order_id,
                                  done=done)

        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.order_repository.patch_order(order_id=order_id,
                                  done=done)#verificar

            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}