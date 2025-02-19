from sqlalchemy.orm import Session

import api.schemas.user_account as user_account_schema
from api.models.user_account import UserAccount


def create_user_account(db: Session, user_account_info: user_account_schema.UserAccountInfo) -> int:
    info = UserAccount(**user_account_info.dict())
    db.add(info)
    db.commit()
    db.refresh(info)
    return info.id


def check_user_account(db: Session, user_account_info: user_account_schema.UserAccountInfo) -> bool:
    query = db.query(UserAccount).filter(
        UserAccount.user_name == user_account_info.user_name
    ).filter(UserAccount.password == user_account_info.password).first()
    if query:
        return True
    else:
        return False
