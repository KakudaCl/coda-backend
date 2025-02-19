from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import api.cruds.user_account as user_account_crud
from api.db import get_db
from api.schemas.user_account import UserAccountInfo

router = APIRouter()


@router.post(
    "/user_accounts",
    tags=["ユーザー"]
)
async def create_user(account_info: UserAccountInfo, db: Session = Depends(get_db)):
    return user_account_crud.create_user_account(db, account_info)


@router.post(
    "user_accounts/check",
    tags=["ユーザー"]
)
async def check_user(account_info: UserAccountInfo, db: Session = Depends(get_db)):
    return
