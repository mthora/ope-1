from src.core.validations import get_product_order_validation as validate


class GetProduct_OrderById:

    def __init__(self, product_order_repository):
        self.product_order_repository = product_order_repository

    def get_by_id(self, product_order_id):
        invalid_inputs = validate(id=product_order_id)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.product_order_repository.get_product_order_by_id(product_order_id=product_order_id)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
