from src.core.validations import create_product_order_validation as validate

class CreateProduct_Order:

    def __init__(self, product_order_repository):
        self.product_order_repository = product_order_repository

    def create(self, product_id: int, order_id: int, price: float, amount: int):
        invalid_inputs = validate(product_id=product_id, order_id=order_id,price=price, amount=amount)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.product_order_repository.create_product_order(product_id=product_id, order_id=order_id, price=price, amount=amount)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
