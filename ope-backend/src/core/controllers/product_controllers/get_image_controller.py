class GetImageController:

    def __init__(self, get_image_use_case):
        self.get_image_use_case = get_image_use_case

    def route(self, arg):
        if arg is not None:
            product_id = arg
            response = self.get_image_use_case.get_image(product_id=product_id)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}