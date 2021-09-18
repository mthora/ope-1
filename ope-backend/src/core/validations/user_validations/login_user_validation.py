def login_user_validation(email: str, password: str):
    message: list[str] = []
    if not isinstance(email, str) or email is None or email == "":
        message.append("Email inválido")
    if not isinstance(password, str) or password is None or password == "":
        message.append("Senha inválida")
    return message