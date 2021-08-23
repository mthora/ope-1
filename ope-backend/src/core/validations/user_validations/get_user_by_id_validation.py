def get_user_validation(id: int):
    message: list[str] = []
    if not isinstance(id, int) or id is None or id == "" or id <= 0:
        message.append("Id inválido")
    return message
