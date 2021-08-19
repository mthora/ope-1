from sqlalchemy.exc import IntegrityError
from src.infra.config import DBConnectionHandler
from src.infra.db_entities import Roles as Role


class RoleRepository:

    @classmethod
    def create_role(cls, role: str):
        with DBConnectionHandler() as db:
            try:
                new_role = Role(role=role)
                db.session.add(new_role)
                db.session.commit()
                return {"data": new_role.to_dict(), "status": 201, "errors": []}
            except IntegrityError:
                db.session.rollback()
                return {"data": None, "status": 409, "errors": ["Erro na requisição"]}
            except Exception as ex:
                print(ex)
                db.session.rollback()
                return {"data": None, "status": 500, "errors": ["Algo deu errado como o banco de dados"]}
            finally:
                db.session.close()