class ListUsersController:

    def __init__(self, list_users_use_case):
        self.list_users_use_case = list_users_use_case

    def route(self, body):
        response = self.list_users_use_case.list()
        return response
