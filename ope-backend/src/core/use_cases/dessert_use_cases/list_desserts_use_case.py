class ListDesserts:

    def __init__(self, dessert_repository):
        self.dessert_repository = dessert_repository

    def list(self):
        try:
            response = self.dessert_repository.list_desserts()
            return response
        except:
            return {"data": None, "status": 400, "errors": ["Erro na requisição"]}