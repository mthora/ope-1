from src.core.validations import upload_image_validation as validate

class UploadImage:

    def __init__(self, item_repository):
        self.item_repository = item_repository

    def upload(self, product_id, image):
        invalid_inputs = validate(product_id=product_id, image = image)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.item_repository.upload_image(product_id=product_id, img_file=image)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
