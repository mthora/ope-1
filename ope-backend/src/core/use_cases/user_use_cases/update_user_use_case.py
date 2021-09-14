from src.core.validations import update_user_validation as validate


class UpdateUser:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def update(self, user_id: int, name: str, role: str, email: str):
        invalid_inputs = validate(user_id=user_id, name=name, role=role, email=email)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.user_repository.update_user(user_id=user_id, name=name, role=role, email=email)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
