class ListDrinks:

    def __init__(self, drink_repository):
        self.drink_repository = drink_repository

    def list(self):
        try:
            response = self.drink_repository.list_drinks()
            return response
        except:
            return {"data": None, "status": 400, "errors": ["Erro na requisição"]}