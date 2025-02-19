from sqlalchemy import BigInteger, Column, String

from api.db import Base


class UserAccount(Base):
    __tablename__ = "user_account"

    id = Column(BigInteger, primary_key=True, nullable=False)
    user_name = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
