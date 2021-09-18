def patch_order_validation(
        order_id: int,
        done: bool):
    message: list[str] = []
    if not isinstance(order_id, int) or order_id is None or order_id == 0:
        message.append("Produto inválido")
    if not isinstance(done, bool) or done is None or done == "":
        message.append("Status inválido")

    return message