from src.core.validations import login_user_validation as validate

class LoginUser:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def login_user(self, email: str, password: str):
        invalid_inputs = validate(email=email, password=password)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.user_repository.login_user(email=email, password=password)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}