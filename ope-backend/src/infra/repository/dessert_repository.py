from sqlalchemy.exc import IntegrityError
from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Desserts as Dessert

class DessertRepository:

    @classmethod
    def create_dessert(cls, name: str, description: str, price: float, amount: int, img: str):
        with DBConnectionHandler() as db:
            try:
                new_dessert = Dessert(name=name, description=description ,price=price, amount=amount, img=img)
                db.session.add(new_dessert)
                db.session.commit()
                return {"data": new_dessert.to_dict(), "status": 201, "errors": []}
            except IntegrityError:
                db.session.rollback()
                return {"data": None, "status": 409, "errors":["Erro na requisição"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()