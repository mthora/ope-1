def delete_product_order_validation(product_order_id: int):
    message: list[str] = []
    if not isinstance(product_order_id, int) or product_order_id is None or product_order_id <= 0:
        message.append("Id inválido")
    return message