from sqlalchemy.exc import IntegrityError
from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Drinks as Drink

class DrinkRepository:

    @classmethod
    def create_drink(cls, name: str, price: float, amount: int, img: str):
        with DBConnectionHandler() as db:
            try:
                new_drink = Drink(name=name, price=price, amount=amount, img=img)
                db.session.add(new_drink)
                db.session.commit()
                return {"data": new_drink.to_dict(), "status": 201, "errors": []}
            except IntegrityError:
                db.session.rollback()
                return {"data": None, "status": 409, "errors":["Erro na requisição"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()

