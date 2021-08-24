from src.core.validations import get_drink_validation as validate


class GetDrinkById:

    def __init__(self, drink_repository):
        self.drink_repository = drink_repository

    def get_by_id(self, drink_id):
        invalid_inputs = validate(id=drink_id)
        input_id_valid = len(invalid_inputs) == 0
        if input_id_valid:
            response = self.drink_repository.get_drink_by_id(drink_id=drink_id)
            return response
        return {
            "data": None,
            "status": 400,
            "errors": invalid_inputs
        }