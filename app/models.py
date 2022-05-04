from sqlalchemy import Column, Integer, String
from .database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, unique=True)
    question = Column(String, unique=True)
    answer = Column(String)
    created_at = Column(String)
