def validate_user(name: str, role: str, email: str, password: str):
    message = []
    if not isinstance(name, str) or name is None:
        message.append("Nome inválido")
    if not isinstance(email, str) or email is None:
        message.append("Email inválido")
    if not isinstance(role, str) or role is None:
        message.append("Cargo inválido")
    if not isinstance(password, str) or password is None:
        message.append("Senha inválida")
    return message
