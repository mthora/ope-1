from src.core.validations import delete_product_order_validation as validate


class DeleteProduct_Order:

    def __init__(self, product_order_repository):
        self.product_order_repository = product_order_repository

    def delete_product_order(self, product_order_id):
        invalid_inputs = validate(product_order_id=product_order_id)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.product_order_repository.delete_product_order(product_order_id=product_order_id)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}