from sqlalchemy.exc import IntegrityError, NoResultFound, MultipleResultsFound
from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Orders as Order


class OrderRepository:

    @classmethod
    def list_orders(cls):
        with DBConnectionHandler() as db:
            try:
                orders = []
                raw_orders: list[Order] = db.session.query(Order).all()
                for order in raw_orders:
                    orders.append(order.to_dict())
                return {"data": orders, "status": 200, "errors": []}
            except IntegrityError:
                db.session.rollback()
                return {"data": [], "status": 409, "errors": ["IntegrityError"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": [], "status": 500, "errors": ["Database connection error"]}
            finally:
                db.session.close()

    @classmethod
    def get_order_by_id(cls, order_id: int):
        with DBConnectionHandler() as db:
            try:
                order = db.session.query(Order).filter_by(id=order_id).one()
                return {"data": order.to_dict(), "status": 200, "errors": []}
            except NoResultFound:
                return {"data": None, "status": 404, "errors": [f"Order id {order_id} does not exist"]}
            except MultipleResultsFound:
                return {"data": None, "status": 409, "errors": [f"Order conflict with id {order_id}"]}
            except Exception as ex:
                return {"data": None, "status": 500, "errors": ["Database connection error"]}
