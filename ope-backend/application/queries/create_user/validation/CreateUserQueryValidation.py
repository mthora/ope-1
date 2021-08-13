class CreateUserQueryValidation:
    def __init__(self, input):
        self.input = input

    @staticmethod
    def validate(self):
        errors = []
        if len(self.input.email) <= 0 or isinstance(input.email, None):
            errors.append("O campo email é obrigatório")
        return errors
