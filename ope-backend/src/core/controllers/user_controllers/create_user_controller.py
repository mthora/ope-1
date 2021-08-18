class CreateUserController:

    def __init__(self, create_user_use_case):
        self.create_user_use_case = create_user_use_case

    def route(self, body):

        if body is not None:
            print("controller", body)
            name = body["name"]
            role = body["role"]
            email = body["email"]
            password = body["password"]
            response = self.create_user_use_case.create(name=name, role=role, email=email, password=password)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}


    # rotas -> adapter (request, composer) -> composer -> controller(use_case) -> use_case(parametros_http) -> validation -> repository