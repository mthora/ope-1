def remove_amount_validation(
        product_id: int,
        amount_to_remove: int):
    message: list[str] = []
    if not isinstance(product_id, int) or product_id is None or product_id == 0:
        message.append("Produto inválido")
    if not isinstance(amount_to_remove, int) or amount_to_remove is None:
        message.append("Quantidade inválida")
    return message