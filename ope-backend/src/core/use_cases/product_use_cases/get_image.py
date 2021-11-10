from src.core.validations import get_image_validation as validate

class GetImage:

    def __init__(self, product_repository):
        self.product_repository = product_repository

    def get_image(self, product_id):
        invalid_inputs = validate(product_id)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.product_repository.get_image(product_id=product_id)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
