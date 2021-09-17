import jwt


def check_valid_token(token):
    if token is None or token == '':
        raise Exception("Token inválido")
    try:
        decoded_token = jwt.decode(token, key='123456', algorithms=["HS256"])
        return decoded_token
    except:
        raise Exception("Token inválido ou expirado")


def admin_route(request):
    token = request.headers.get("Authorization")
    try:
        decoded_token = check_valid_token(token)
        if decoded_token['role'] != 1:
            raise Exception("Token inválido ou expirado")
    except:
        raise Exception("Token inválido ou expirado")


def authorized_route(request):
    token = request.headers.get("Authorization")
    try:
        decoded_token = check_valid_token(token)
    except:
        raise Exception("Token inválido ou expirado")
