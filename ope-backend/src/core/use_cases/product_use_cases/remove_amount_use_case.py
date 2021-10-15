from src.core.validations import remove_amount_validation as validate

class RemoveAmount:

    def __init__(self, product_repository):
        self.product_repository = product_repository

    def remove_amount(self, product_id: int, amount_to_remove: int):
        invalid_inputs = validate(product_id=product_id,
                                  amount_to_remove=amount_to_remove)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.product_repository.remove_product_amount(product_id=product_id,
                                                                     amount_to_remove=amount_to_remove)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}