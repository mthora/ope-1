from src.core.validations import update_product_validation as validate


class UpdateProduct:

    def __init__(self, product_repository):
        self.product_repository = product_repository

    def update(self, product_id: int, name: str, category: str, description: str, price: float, amount: int, promotion: bool, img: str):
        invalid_inputs = validate(product_id=product_id,
                                  name=name,
                                  category=category,
                                  description=description,
                                  price=price,
                                  amount=amount,
                                  promotion=promotion,
                                  img=img)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.product_repository.update_product(product_id=product_id,
                                  name=name,
                                  description=description,
                                category=category,
                                  price=price,
                                  amount=amount,
                                  promotion=promotion,
                                  img=img)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}