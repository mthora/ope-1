def upload_image_validation(
        product_id, image):
    message: list[str] = []
    if not isinstance(product_id, int) or product_id is None or product_id < 1:
        message.append("Id inválido")
    if image is None:
       message.append("Imagem inválida")
    return message