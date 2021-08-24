from sqlalchemy.exc import IntegrityError, NoResultFound, MultipleResultsFound
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

    @classmethod
    def list_drinks(cls):
        with DBConnectionHandler() as db:
            try:
                drinks = []
                raw_drinks: list[Drink] = db.session.query(Drink).all()
                for drink in raw_drinks:
                    drinks.append(drink.to_dict())
                return {"data": drinks, "status": 200, "errors": []}
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
    def get_drink_by_id(cls, drink_id:int):
        with DBConnectionHandler() as db:
            try:
                drink = db.session.query(Drink).filter_by(id=drink_id).one()
                return {"data": drink.to_dict(), "status": 200, "errors": []}
            except NoResultFound:
                return {"data": None, "status": 404, "errors": [f"Bebida de id {drink_id} não existe"]}
            except MultipleResultsFound:
                return {"data": None, "status": 409, "errors": [f"Conflito de bebidas com id {drink_id}"]}
            except Exception as ex:
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}