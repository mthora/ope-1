class UpdateUserController:

    def __init__(self, update_user_use_case):
        self.update_user_use_case = update_user_use_case

    def route(self, body):

        if body is not None:
            name = body["name"] if "name" in body else None
            role = body["role"] if "role" in body else None
            email = body["email"] if "email" in body else None
            user_id = body["id"] if "id" in body else None
            response = self.update_user_use_case.update(user_id=user_id, name=name, role=role, email=email)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}
