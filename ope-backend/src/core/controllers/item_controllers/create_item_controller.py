class CreateItemController:

    def __init__(self, create_item_use_case):
        self.create_item_use_case = create_item_use_case

    def route(self, body):

        if body is not None:
            print("controller", body)
            name = body["name"] if "name" in body else None
            description = body["description"] if "description" in body else None
            price = body["price"] if "price" in body else None
            amount = body["amount"] if "amount" in body else None
            promotion = body["promotion"] if "promotion" in body else None
            img = body["img"] if "img" in body else None
            response = self.create_item_use_case.create(
                name=name,
                description=description,
                price=price,
                amount=amount,
                promotion=promotion,
                img=img)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}
