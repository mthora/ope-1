class ListDessertsController:

    def __init__(self,list_desserts_use_case):
        self.list_desserts_use_case = list_desserts_use_case

    def route(self, body):
        response = self.list_desserts_use_case.list()
        return response