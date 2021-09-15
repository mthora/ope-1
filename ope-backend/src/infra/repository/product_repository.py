from sqlalchemy.exc import IntegrityError
from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Products as Product


class ProductRepository:

    @classmethod
    def create_product(
            cls,
            name: str,
            description: str,
            price: float,
            amount: int,
            promotion: bool,
            img: str):
        with DBConnectionHandler() as db:
            try:
                new_product = Product(name=name,
                                description=description,
                                price=price,
                                amount=amount,
                                promotion=promotion,
                                img=img)
                db.session.add(new_product)
                db.session.commit()
                return {
                    "data": new_product.to_dict(),
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
    def list_products(cls):
        with DBConnectionHandler() as db:
            try:
                products = []
                raw_products: list[Product] = db.session.query(Product).all()
                for product in raw_products:
                    products.append(product.to_dict())
                return {
                    "data": products,
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
