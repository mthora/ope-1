class GetDessertController:

    def __init__(self, get_dessert_by_id_use_case):
        self.get_dessert_by_id_use_case = get_dessert_by_id_use_case

    def route(self, arg):

        if arg is not None:
            dessert_id = arg
            response = self.get_dessert_by_id_use_case.get_by_id(dessert_id=dessert_id)
            return response
        return {
            "data": None,
            "status": 400,
            "errors": ["Requisição inválida"]
        }