from src.core.validations import create_product_validation as validade


class CreateProduct:

    def __init__(self, item_repository):
        self.item_repository = item_repository

    def create(self, name: str,
               description: str,
               category: str,
               price: float,
               amount: int,
               promotion: bool,
               img: type):
        invalid_inputs = validade(
            name=name,
            description=description,
            category=category,
            price=price,
            amount=amount,
            promotion=promotion,
            img=img)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.item_repository.create_product(name=name, category=category, description=description, price=price, amount=amount,
                                                        promotion=promotion, img=img)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
