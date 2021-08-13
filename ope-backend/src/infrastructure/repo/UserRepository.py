from src.infrastructure.config import DBConnectionHandler
from src.infrastructure.entities import Users


class UserRepository:
    @classmethod
    def create_user(cls, name: str, password: str):
        with DBConnectionHandler() as db_conn:
            try:
                new_user = Users(name, password)
                db_conn.session.add(new_user)
                db_conn.session.commit()
            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()
