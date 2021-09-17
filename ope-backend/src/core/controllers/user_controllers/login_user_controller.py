class LoginUserController:

    def __init__(self, login_user_use_case):
        self.login_user_use_case = login_user_use_case

    def route(self, body):

        if body is not None:
            print("controller", body)
            email = body["email"] if "email" in body else None
            password = body["password"] if "password" in body else None
            response = self.login_user_use_case.login_user(email=email, password=password)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}
