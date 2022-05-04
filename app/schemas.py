from pydantic import BaseModel
from typing import Optional


class IntRequest(BaseModel):
    questions_num: int


class QuestionResponse(BaseModel):
    # id: int
    # question_id: int
    question: Optional[str] = None
    # answer: str
    # created_at: str

    class Config:
        orm_mode = True
