class UpdateProduct_OrderController:

    def __init__(self, update_product_order_use_case):
        self.update_product_order_use_case = update_product_order_use_case

    def route(self, body):

        if body is not None:
            print("controller", body)
            product_order_id = body["product_order_id"] if "product_order_id" in body else None
            price = body["price"] if "price" in body else None
            amount = body["amount"] if "amount" in body else None
            response = self.update_product_order_use_case.update(
                product_order_id=product_order_id,
                price=price,
                amount=amount,

            )
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}