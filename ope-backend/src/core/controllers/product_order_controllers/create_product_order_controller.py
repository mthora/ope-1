class CreateProduct_OrderController:

    def __init__(self, create_product_order_use_case):
        self.create_product_order_use_case = create_product_order_use_case

    def route(self, body):

        if body is not None:
            print("controller", body)
            product_id = body["product_id"] if "product_id" in body else None
            order_id = body["order_id"] if "order_id" in body else None
            price = body["price"] if "price" in body else None
            amount = body["amount"] if "amount" in body else None
            response = self.create_product_order_use_case.create(
                product_id=product_id,
                order_id=order_id,
                price=price,
                amount=amount,

            )
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}