def create_role_validation(role:str):
    message:list[str] = []
    if not isinstance(role, str) or role is None or role == '' or len(role)>20:
        message.append("Cargo inválido")
    return message