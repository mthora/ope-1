from src.core.validations import create_order_validation as validate
import datetime

class CreateOrder:

    def __init__(self, order_repository):
        self.order_repository = order_repository

    def create_order(self, done: bool,
               initial_date: str,
               end_date: str,
               consumed_in: str,
               table: int,
               payment_method: str,
               obs: str,
               confirmed: bool):

        invalid_inputs = validate(done=done,
                                  initial_date=initial_date,
                                  end_date=end_date,
                                  consumed_in=consumed_in,
                                  table=table,
                                  payment_method=payment_method,
                                  obs=obs, confirmed=confirmed)

        input_is_valid = len(invalid_inputs) == 0
        if input_is_valid:
            response = self.order_repository.create_order(done=done, initial_date=initial_date,
                                                          end_date=end_date, consumed_in=consumed_in,
                                                          table=table, payment_method=payment_method,
                                                          obs=obs, confirmed=confirmed)
            return response
        return {"data": None, "status": 400, "errors": invalid_inputs}
