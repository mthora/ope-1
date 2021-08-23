class GetUserController:

    def __init__(self, get_user_by_id_use_case):
        self.get_user_by_id_use_case = get_user_by_id_use_case

    def route(self, arg):

        if arg is not None:
            user_id = arg
            response = self.get_user_by_id_use_case.get_by_id(user_id=user_id)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}
