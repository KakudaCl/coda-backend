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
