from src.core.validations import update_product_order_validation as validate


class UpdateProduct_Order:

    def __init__(self, product_order_repository):
        self.product_order_repository = product_order_repository

    def update(self, product_order_id: int, price: float, amount: int):
        invalid_inputs = validate(product_order_id=product_order_id, price=price, amount=amount)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.product_order_repository.update_product_order(product_order_id=product_order_id, price=price, amount=amount)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
