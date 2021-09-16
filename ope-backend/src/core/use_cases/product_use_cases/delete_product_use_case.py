from src.core.validations import delete_product_validation as validate


class DeleteProduct:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def delete_product(self, product_id):
        invalid_inputs = validate(product_id=product_id)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.product_repository.delete_product(product_id=product_id)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}