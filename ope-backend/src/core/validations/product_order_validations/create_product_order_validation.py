def create_product_order_validation(price: float, amount: int):
    message: list[str] = []
    if not isinstance(price, float) or price is None or price <= 0:
        message.append("Preço inválido")
    if not isinstance(amount, int) or amount is None or amount < 0:
        message.append("Quantidade inválida")
    return message