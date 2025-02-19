from sqlalchemy.orm import Session

import api.models.user_account as user_account_model
import api.schemas.user_account as user_account_schema


def create_user_account(db: Session, user_account_info: user_account_schema.UserAccountInfo) -> int:
    info = user_account_model.UserAccount(**user_account_info.dict())
    db.add(info)
    db.commit()
    db.refresh(info)
    return info.id


def check_user_account(db: Session, user_account_info: user_account_schema.UserAccountInfo) -> bool:
    
