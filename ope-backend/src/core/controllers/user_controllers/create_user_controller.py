class CreateUserController:

    def __init__(self, create_user_use_case):
        self.create_user_use_case = create_user_use_case

    def route(self, body):

        if body is not None:
            print("controller", body)
            name = body["name"] if "name" in body else None
            role = body["role"] if "role" in body else None
            email = body["email"] if "email" in body else None
            password = body["password"] if "password" in body else None
            response = self.create_user_use_case.create(name=name, role=role, email=email, password=password)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}
