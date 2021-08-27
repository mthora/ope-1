from sqlalchemy.exc import IntegrityError, NoResultFound, MultipleResultsFound
from src.main.utils import hash_password
from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Users as User


class UserRepository:

    @classmethod
    def list_users(cls):
        with DBConnectionHandler() as db:
            try:
                users = []
                raw_users: list[User] = db.session.query(User).all()
                for user in raw_users:
                    users.append(user.to_dict())
                return {"data": users, "status": 200, "errors": []}
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
    def create_user(cls, name: str, role: str, email: str, password: str):
        with DBConnectionHandler() as db:
            try:
                new_user = User(name=name, role=role, email=email, password=hash_password(password))
                print("repo", new_user)
                db.session.add(new_user)
                db.session.commit()
                return {"data": new_user.to_dict(), "status": 201, "errors": []}
            except IntegrityError:
                db.session.rollback()
                return {"data": None, "status": 409, "errors": ["E-mail e/ou nome de usuário já existe"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()

    @classmethod
    def get_user_by_id(cls, user_id:int):
        with DBConnectionHandler() as db:
            try:
                user = db.session.query(User).filter_by(id=user_id).one()
                return {"data": user.to_dict(), "status": 200, "errors": []}
            except NoResultFound:
                return {"data": None, "status": 404, "errors": [f"Usuário de id {user_id} não existe"]}
            except MultipleResultsFound:
                return {"data": None, "status": 409, "errors": [f"Conflito de usuário com id {user_id}"]}
            except Exception as ex:
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}