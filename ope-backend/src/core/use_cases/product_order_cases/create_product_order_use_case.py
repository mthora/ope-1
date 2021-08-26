from src.core.validations import create_product_order_validation as validate

class CreateProduct_Order:

    def __init__(self, product_order_repository):
        self.product_order_repository = product_order_repository

    def create(self, id_product: int, id_order: int, price: float, amount: int):
        invalid_inputs = validate(id_product=id_product, id_order=id_order, price=price, amount=amount)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.product_order_repository.create_product_order(id_product=id_product, id_order=id_order, price=price, amount=amount)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
