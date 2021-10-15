class UpdateProductController:

    def __init__(self, update_product_use_case):
        self.update_product_use_case = update_product_use_case

    def route(self, body):

        if body is not None:
            product_id = body["id"] if "id" in body else None
            name = body["name"] if "name" in body else None
            category = body["category"] if "category" in body else None
            description = body["description"] if "description" in body else None
            price = body["price"] if "price" in body else None
            amount = body["amount"] if "amount" in body else None
            promotion = body["promotion"] if "promotion" in body else None
            img = body["img"] if "img" in body else None

            response = self.update_product_use_case.update(product_id=product_id, name=name, category=category, description=description, price=price, amount=amount, promotion=promotion, img=img)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}