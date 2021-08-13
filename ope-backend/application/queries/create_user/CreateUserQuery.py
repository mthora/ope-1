from application.queries.create_user.validation.CreateUserQueryValidation import CreateUserQueryValidation


class CreateUserCommand:
    def __init__(self, input):
        self.input = input
        self.errors = []

    def is_valid(self):
        self.errors = CreateUserQueryValidation(self.input)
        return len(self.errors) == 0
