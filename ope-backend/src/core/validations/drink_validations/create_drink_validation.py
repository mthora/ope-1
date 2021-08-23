def create_drink_validation(name: str, price: float, amount: int, img: str):
    message: list[str] = []
    if not isinstance(name, str) or name is None or len(name) > 40 or name == "":
        message.append("Nome inválido")
    if not isinstance(price, float) or price is None or price <= 0:
        message.append("Preço inválido")
    if not isinstance(amount, int) or amount is None or amount < 0:
        message.append("Quantidade inválida")
    if not isinstance(img, str) or img is None:
        message.append("Imagem obrigatória")
    return message