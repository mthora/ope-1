from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Users as User


class UserRepository:

    @classmethod
    def create_user(cls, name: str, role: str, email: str, password: str):
        print("repo")
        with DBConnectionHandler as db:
            try:
                new_user = User(name=name, role=role, email=email, password=password)
                print("repo", new_user)
                db.session.add(new_user)
                db.session.commit()

                return {"data": new_user, "status": 201, "errors": []}
            except:
                db.session.rollback()
                return {"data": None, "status": 500, "errors": ["Não foi possível criar o usuário"]}
            finally:
                db.session.close()
