class DeleteProductController:

    def __init__(self, delete_product_use_case):
        self.delete_product_use_case = delete_product_use_case

    def route(self, arg):
        if arg is not None:
            product_id = arg
            response = self.delete_product_use_case.delete_product(product_id=product_id)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}