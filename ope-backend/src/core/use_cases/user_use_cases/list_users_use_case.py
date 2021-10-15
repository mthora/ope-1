class ListUsers:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def list(self):
        try:
            response = self.user_repository.list_users()
            return response
        except:
            return {"data": None, "status": 400, "errors": ["Erro na requisição"]}
