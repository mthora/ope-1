def update_product_order_validation(product_order_id: int, price: float, amount: int):
    message: list[str] = []
    if not isinstance(product_id, int) or product_id is None or price <= 0:
        message.append("ID inválido")
    if not isinstance(order_id, int) or product_id is None or price <= 0:
        message.append("ID inválido")
    if not isinstance(price, float) or price is None or price <= 0:
        message.append("Preço inválido")
    if not isinstance(amount, int) or amount is None or amount < 0:
        message.append("Quantidade inválida")
    return message