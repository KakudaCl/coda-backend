from sqlalchemy import create_engine

from api.models.score_info import Base as score_info_base
from api.models.user_account import Base as user_account_base

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    user_account_base.metadata.drop_all(bind=engine)
    user_account_base.metadata.create_all(bind=engine)
    score_info_base.metadata.drop_all(bind=engine)
    score_info_base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
