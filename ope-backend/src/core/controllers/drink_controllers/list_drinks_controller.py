class ListDrinksController:

    def __init__(self, list_drinks_use_case):
        self.list_drinks_use_case = list_drinks_use_case

    def route(self, body):
        response = self.list_drinks_use_case.list()
        return response
