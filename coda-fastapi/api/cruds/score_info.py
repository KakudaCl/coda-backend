import datetime

from sqlalchemy.orm import Session

import api.schemas.score_info as score_info_schema
from api.models.score_info import ScoreInfo


def create_score_info(db: Session, score_info: score_info_schema.ScoreInfo) -> int:
    info = ScoreInfo(score_name=score_info.score_name,
                     user_id=score_info.user_id,
                     score_url='/sample',
                     thumbnail_url='/sample',
                     created_at=datetime.datetime.now(),
                     delete_flg=0)
    db.add(info)
    db.commit()
    db.refresh(info)
    return info.id


def list_score_info(db: Session, user_id: int) -> list[score_info_schema.ScoreInfo]:
    query = db.query(ScoreInfo).filter(ScoreInfo.user_id ==
                                       user_id).filter(ScoreInfo.delete_flg != 1)
    return query.all()


def delete_score_info(db: Session, score_info: score_info_schema.ScoreInfo):
    query = db.query(ScoreInfo).filter(ScoreInfo.user_id == score_info.user_id).filter(ScoreInfo.score_name == score_info.score_name).first()

    query.delete_flg = 1
    db.commit()
