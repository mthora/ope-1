def update_product_validation(
        product_id: int,
        name: str,
        description: str,
        price: float,
        amount: int,
        promotion: bool,
        img: str):
    message: list[str] = []
    if not isinstance(product_id, int) or product_id is None or product_id == 0:
        message.append("Produto inválido")
    if not isinstance(name, str) or name is None or name == "":
        message.append("Nome inválido")
    if not isinstance(description, str) or description is None or description == "":
        message.append("Descição inválida")
    if not isinstance(price, float) or price is None or price == 0.0:
        message.append("Preço inválido")
    if not isinstance(amount, int) or amount is None:
        message.append("Quantidade inválida")
    if not isinstance(promotion, bool) or promotion is None or promotion == "":
        message.append("Promoção inválida")
    if not isinstance(img, str) or img is None or img == "":
        message.append("Imagem inválida")
    return message