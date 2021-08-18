def validate_user(name: str, role: str, email: str, password: str):
    message: list[str] = []
    if not isinstance(name, str) or name is None or name == "":
        message.append("Nome inválido")
    if not isinstance(email, str) or email is None or email == "":
        message.append("Email inválido")
    if not isinstance(role, int) or role is None or role == "":
        message.append("Cargo inválido")
    if not isinstance(password, str) or password is None or password == "":
        message.append("Senha inválida")
    return message
