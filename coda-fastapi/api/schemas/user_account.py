from pydantic import BaseModel, Field


class UserAccountInfo(BaseModel):
    user_name: str = Field(None, example="hanako")
    password: str = Field(None, example="qwerty")
