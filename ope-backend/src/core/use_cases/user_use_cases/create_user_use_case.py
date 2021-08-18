from src.core.validations import create_user_validation as validate

class CreateUser:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create(self, name: str, role: str, email: str, password: str):
        invalid_inputs = validate(name=name, role=role, email=email, password=password)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.user_repository.create_user(name=name, role=role, email=email, password=password)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}