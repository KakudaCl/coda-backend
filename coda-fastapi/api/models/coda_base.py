from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from api.db import Base


class UserAccount(Base):
    __tablename__ = "user_account"

    id = Column(BigInteger, primary_key=True, nullable=False)
    user_name = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)

    score_info = relationship("ScoreInfo", back_populates="user_account")


class ScoreInfo(Base):
    __tablename__ = "score_info"

    id = Column(BigInteger, primary_key=True, nullable=False)
    score_name = Column(String(30), nullable=False)
    user_id = Column(BigInteger, ForeignKey("user_account.id"), nullable=False)
    score_url = Column(String(30), nullable=False)
    thumbnail_url = Column(String(30), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    delete_flg = Column(Boolean)

    user_account = relationship("UserAccount", back_populates="score_info")
