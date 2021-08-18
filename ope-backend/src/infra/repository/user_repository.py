from sqlalchemy.exc import IntegrityError
from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Users as User


class UserRepository:

    @classmethod
    def create_user(cls, name: str, role: str, email: str, password: str):
        print("repo")
        with DBConnectionHandler() as db:
            try:
                new_user = User(name=name, role=role, email=email, password=password)
                print("repo", new_user)
                db.session.add(new_user)
                db.session.commit()

                return {"data": new_user.to_dict(), "status": 201, "errors": []}
            except IntegrityError:
                db.session.rollback()
                return {"data": None, "status": 409, "errors": ["E-mail e/ou nome de usuário já existe"]}
            except:
                db.session.rollback()
                return {"data": None, "status": 500, "errors": ["Algo deu errado na conexão com o banco de dados"]}
            finally:
                db.session.close()
