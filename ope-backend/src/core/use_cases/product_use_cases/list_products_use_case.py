class ListProducts:

    def __init__(self, item_repository):
        self.item_repository = item_repository

    def list(self):
        try:
            response = self.item_repository.list_products()
            return response
        except:
            return {"data": None, "status": 400, "errors": ["Erro na requisição"]}
