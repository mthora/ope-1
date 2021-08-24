from sqlalchemy.exc import IntegrityError
from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Items as Item


class ItemRepository:

    @classmethod
    def create_item(
            cls,
            name: str,
            description: str,
            price: float,
            amount: int,
            promotion: bool,
            img: str):
        with DBConnectionHandler() as db:
            try:
                new_item = Item(name=name,
                                description=description,
                                price=price,
                                amount=amount,
                                promotion=promotion,
                                img=img)
                db.session.add(new_item)
                db.session.commit()
                return {
                    "data": new_item.to_dict(),
                    "status": 201,
                    "errors": []}
            except IntegrityError:
                db.session.rollback()
                return {
                    "data": None,
                    "status": 409,
                    "errors": ["Erro na requisição"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {
                    "data": None,
                    "status": 500,
                    "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()

    @classmethod
    def list_items(cls):
        with DBConnectionHandler() as db:
            try:
                items = []
                raw_item: list[Item] = db.session.query(Item).all()
                for item in raw_item:
                    items.append(item.to_dict())
                return {
                    "data": items,
                    "status": 200,
                    "errors": []}
            except IntegrityError:
                db.session.rollback()
                return {
                    "data": [],
                    "status": 409,
                    "errors": ["Integrity Error"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {
                    "data": [],
                    "status": 500,
                    "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()
