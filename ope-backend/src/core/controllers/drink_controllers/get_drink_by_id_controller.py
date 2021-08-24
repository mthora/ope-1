class GetDrinkController:

    def __init__(self, get_drink_by_id_use_case):
        self.get_drink_by_id_use_case = get_drink_by_id_use_case

    def route(self, arg):

        if arg is not None:
            drink_id = arg
            response = self.get_drink_by_id_use_case.get_by_id(drink_id=drink_id)
            return response
        return {"data": None, "status": 400, "errors": ["Requisição inválida"]}
