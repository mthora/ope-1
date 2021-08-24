from src.core.validations import create_item_validation as validade


class CreateItem:

    def __init__(self, item_repository):
        self.item_repository = item_repository

    def create(self, name: str,
               description: str,
               price: float,
               amount: int,
               promotion: bool,
               img: str):
        invalid_inputs = validade(
            name=name,
            description=description,
            price=price,
            amount=amount,
            promotion=promotion,
            img=img)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.item_repository.create_item(name=name, description=description, price=price, amount=amount,
                                                        promotion=promotion, img=img)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
