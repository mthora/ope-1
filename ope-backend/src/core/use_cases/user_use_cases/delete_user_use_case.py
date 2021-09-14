from src.core.validations import delete_user_validation as validate


class DeleteUser:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def delete_user(self, user_id):
        invalid_inputs = validate(user_id=user_id)
        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.user_repository.delete_user(user_id=user_id)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}