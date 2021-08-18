from src.core.validations import create_drink_validation as validade

class CreateDrink:

    def __init__(self, drink_repository):
        self.drink_repository = drink_repository

    def create(self, name: str, price: float, amount: int, img: str):
        invalid_inputs = validade(name=name, price=price, amount=amount, img=img)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.drink_repository.create_drink(name=name, price=price, amount=amount, img=img)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}