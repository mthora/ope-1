def update_product_order_validation(product_order_id: int, price: float, amount: int):
    message: list[str] = []
    if not isinstance(price, float) or price is None or price <= 0:
        message.append("Preço inválido")
    if not isinstance(amount, int) or amount is None or amount < 0:
        message.append("Quantidade inválida")
    if not isinstance(product_order_id, int) or product_order_id is None or product_order_id == 0:
        message.append("Pedido de produto inválido")
    return message