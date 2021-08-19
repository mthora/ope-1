from src.core.validations import create_role_validation as validade

class CreateRole:

    def __init__(self, role_repository):
        self.role_repository = role_repository

    def create(self, role:str):
        invalid_inputs = validade(role=role)
        input_is_valid = len(invalid_inputs)==0
        if input_is_valid:
            response = self.role_repository.create_role(role=role)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
