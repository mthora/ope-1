from src.infra.config import *
from src.infra.db_entities import *
from src.main.utils import hash_password

db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)
