from typing import List

from src.infrastructure.config import DBConnectionHandler
from src.infrastructure.entities import Users
from src.domain.dtos.users import Users as UserDto
from .user_repository_interface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):

    @classmethod
    def create_user(cls, name: str, password: str) -> Users:
        with DBConnectionHandler as db_conn:
            try:
                new_user = Users(name, password)
                db_conn.session.add(new_user)
                db_conn.session.commit()

                return UserDto(id=new_user.id, name=new_user.name, password=new_user.password)
            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()
        return None

    @classmethod
    def get_user_by_id(cls, user_id: int) -> List[Users]:
        try:
            query_data = None
            with DBConnectionHandler() as db_conn:
                data = db_conn.session.query(Users).filter_by(id=user_id).one()
                query_data = [data]
            return query_data
        except:
            db_conn.session.rollback()
            raise
        finally:
            db_conn.session.close()
        return None
