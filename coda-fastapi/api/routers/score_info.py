from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import api.cruds.score_info as score_info_crud
from api.db import get_db
from api.schemas.score_info import ScoreInfo

router = APIRouter()


@router.post(
    "/scores",
    tags=["譜面"]
)
async def create_score(score_info: ScoreInfo, db: Session = Depends(get_db)):
    return score_info_crud.create_score_info(db, score_info)


@router.get(
    "/scores/{user_account_id}",
    tags=["譜面"]
)
async def list_score_with_user_id(user_account_id: int, db: Session = Depends(get_db)):
    return score_info_crud.list_score_info(db, user_account_id)


@router.delete(
    "/scores",
    tags=["譜面"]
)
async def delete_score(score_info: ScoreInfo, db: Session = Depends(get_db)):
    return score_info_crud.delete_score_info(db, score_info)
