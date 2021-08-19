class CreateRoleController:

    def __init__(self, create_role_use_case):
        self.create_role_use_case = create_role_use_case

    def route(self, body):
        if body is not None:
            print("controller", body)
            role = body["role"] if "role" in body else None
            response = self.create_role_use_case.create(role=role)
            return response
        return {"data": None, "status": 400, "errors":["Requisição invalida"]}