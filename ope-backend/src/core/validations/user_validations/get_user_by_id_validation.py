def get_user_validation(user_id: int):
    message: list[str] = []
    if not isinstance(user_id, int) or user_id is None or user_id <= 0:
        message.append("Id inválido")
    return message
