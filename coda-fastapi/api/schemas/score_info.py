from pydantic import BaseModel, Field


class ScoreInfo(BaseModel):
    score_name: str = Field(None, example="etude.pdf")
    user_id: int = Field(None, example=1)
