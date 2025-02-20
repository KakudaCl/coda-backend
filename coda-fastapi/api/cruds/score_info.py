import datetime

from sqlalchemy.orm import Session

import api.schemas.score_info as score_info_schema
from api.models.score_info import ScoreInfo


def create_score_info(db: Session, score_info: score_info_schema.ScoreInfo) -> int:
    info = ScoreInfo(score_name=score_info.score_name,
                     user_id=score_info.user_id,
                     score_url='/sample',
                     thumbnail_url='/sample',
                     created_at=datetime.datetime.now())
    db.add(info)
    db.commit()
    db.refresh(info)
    return info.id
