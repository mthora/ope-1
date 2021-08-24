from src.core.validations import create_dessert_validation as validade


class CreateDessert:

    def __init__(self, dessert_repository):
        self.dessert_repository = dessert_repository

    def create(self, name: str, description: str, price: float, amount: int, img: str):
        invalid_inputs = validade(name=name, description=description, price=price, amount=amount, img=img)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.dessert_repository.create_dessert(name=name, description=description, price=price,
                                                              amount=amount, img=img)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
