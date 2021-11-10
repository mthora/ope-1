from sqlalchemy.exc import IntegrityError, NoResultFound, MultipleResultsFound
from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Products as Product
from flask import current_app as app
import base64
import os

class ProductRepository:
    @classmethod
    def create_product(cls, name: str, category: int, description: str, price: float, amount: int, promotion: bool):
        with DBConnectionHandler() as db:
            try:
                new_product = Product(name=name, category=category, description=description, price=price, amount=amount,
                                      promotion=promotion, img=None)
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

    def delete_product(self, product_id: int):
        with DBConnectionHandler() as db:
            try:
                product = db.session.query(Product).filter_by(id=product_id).first()
                if product:
                    db.session.delete(product)
                    db.session.commit()
                    return {"data": None, "status": 200, "errors": []}
                return {"data": None, "status": 404, "errors": [f"Product de id {product_id} não existe"]}
            except MultipleResultsFound:
                return {"data": None, "status": 409, "errors": [f"Conflito de usuários com id {product_id}"]}
            except Exception as ex:
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()

    def update_product(self,
                        product_id: int,
                        name: str,
                        category: str,
                        description: str,
                        price: float,
                        amount: int,
                        promotion: bool,
                        img: str):
        with DBConnectionHandler() as db:
            try:
                product = db.session.query(Product).filter_by(id=product_id).first()
                if product:
                    product.name = name
                    product.description = description
                    product.category = category
                    product.price = price
                    product.amount = amount
                    product.promotion = promotion
                    product.img = img
                    db.session.commit()
                    return {"data": None, "status": 200, "errors": []}
                return {"data": None, "status": 404, "errors": [f"Product de id {product_id} não existe"]}
            except IntegrityError:
                return {"data": None, "status": 409, "errors": [f"Nome de produto já existe."]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()

    def upload_image(self, product_id: int, img_file):
        with DBConnectionHandler() as db:
            try:
                product = db.session.query(Product).filter_by(id=product_id).first()
                path = app.config['UPLOAD_FOLDER']
                name = f"{img_file.filename}"
                img_file.save(os.path.join(path, name))
                image_path = os.path.join(path, name)
                if product:
                    with open(image_path, 'rb') as img_file:
                        image = base64.b64encode(img_file.read())
                    product.img = image.decode('utf-8')
                    db.session.commit()
                    return {"data": None, "status": 200, "errors": []}
                return {"data": None, "status": 404, "errors": [f"Product de id {product_id} não existe"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()

    def get_image(self, product_id: int):
        with DBConnectionHandler() as db:
            try:
                product = db.session.query(Product).filter_by(id=product_id).first()
                if product:
                    image_name = product.img.split('\\')[2]
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
                    print(image_path)
                    with open(image_path, 'rb') as img_file:
                        image = base64.b64encode(img_file.read())
                    return {"data": image.decode("utf-8"), "status": 200, "errors": []}
                return {"data": None, "status": 404, "errors": [f"Product de id {product_id} não existe"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()

    def remove_product_amount(self,
                        product_id: int,
                        amount_to_remove: int):
        with DBConnectionHandler() as db:
            try:
                product = db.session.query(Product).filter_by(id=product_id).first()
                if product:
                    product.amount-=amount_to_remove
                    if product.amount < 0:
                        return {"data": None, "status": 400, "errors": ["A quantidade comprada é maior do que a disponível"]}
                    db.session.commit()
                    return {"data": None, "status": 200, "errors": []}
                return {"data": None, "status": 404, "errors": [f"Product de id {product_id} não existe"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()