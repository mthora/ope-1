from sqlalchemy.exc import IntegrityError, NoResultFound, MultipleResultsFound
from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Products_Orders as Product_Order


class Product_OrderRepository:

    @classmethod
    def list_products_orders(cls):
        with DBConnectionHandler() as db:
            try:
                products_orders = []
                raw_products_orders: list[Product_Order] = db.session.query(Product_Order).all()
                for product_order in raw_products_orders:
                    products_orders.append(product_order.to_dict())
                return {"data": products_orders, "status": 200, "errors": []}
            except IntegrityError:
                db.session.rollback()
                return {"data": [], "status": 409, "errors": ["Integrity Error"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": [], "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()


    @classmethod
    def get_product_order_by_id(cls, product_order_id:int):
        with DBConnectionHandler() as db:
            try:
                product_order = db.session.query(Product_Order).filter_by(id=product_order_id).one()
                return {"data": product_order.to_dict(), "status": 200, "errors": []}
            except NoResultFound:
                return {"data": None, "status": 404, "errors": [f"Pedido de produto de id {product_order_id} não existe"]}
            except MultipleResultsFound:
                return {"data": None, "status": 409, "errors": [f"Conflito de pedido de produto com id {product_order_id}"]}
            except Exception as ex:
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}