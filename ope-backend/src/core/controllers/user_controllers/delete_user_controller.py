class DeleteUserController:

    def __init__(self, delete_user_use_case):
        self.delete_user_use_case = delete_user_use_case

    def route(self, arg):
        if arg is not None:
            user_id = arg
            response = self.delete_user_use_case.delete_user(user_id=user_id)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}
