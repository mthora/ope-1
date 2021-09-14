def update_user_validation(user_id: int, name: str, role: str, email: str):
    message: list[str] = []
    if not isinstance(name, str) or name is None or name == "":
        message.append("Nome inválido")
    if not isinstance(email, str) or email is None or email == "":
        message.append("Email inválido")
    if not isinstance(role, int) or role is None or role == 0:
        message.append("Cargo inválido")
    if not isinstance(user_id, int) or user_id is None or user_id == 0:
        message.append("Usuário inválido")
    return message
