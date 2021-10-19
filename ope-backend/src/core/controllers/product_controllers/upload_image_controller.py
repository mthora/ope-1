class UploadImageController:

    def __init__(self, upload_image_use_case):
        self.upload_image_use_case = upload_image_use_case

    def route(self, arg, files):
        if arg is not None:
            product_id = arg
            image = files[0]
            response = self.upload_image_use_case.upload(
               product_id=product_id, image=image)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}
