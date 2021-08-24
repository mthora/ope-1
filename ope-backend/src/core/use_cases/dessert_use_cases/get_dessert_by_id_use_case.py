from src.core.validations import get_dessert_validation as validate

class GetDessertById:

    def __init__(self, dessert_repository):
        self.dessert_repository = dessert_repository

    def get_by_id(self, dessert_id):
        invalid_inputs = validate(id=dessert_id)
        input_id_valid = len(invalid_inputs) == 0
        if input_id_valid:
            response = self.dessert_repository.get_dessert_by_id(dessert_id=dessert_id)
            return response
        return {
            "data": None,
            "status": 400,
            "errors": invalid_inputs
        }