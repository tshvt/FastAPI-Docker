from fastapi import FastAPI, Depends, status
from . import schemas, models
from .database import engine, SessionLocal
import requests
from sqlalchemy.orm import Session
from sqlalchemy import exists

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def is_same(q, db):
    if db.query(exists().where(models.Question.question_id == q['id'])).scalar():
        while db.query(exists().where(models.Question.question_id == q['id'])).scalar():
            q = requests.get("https://jservice.io/api/random?count=1").json()
        return q
    else:
        return q


@app.post("/add", status_code=status.HTTP_201_CREATED, response_model=schemas.QuestionResponse)
def add(num: schemas.IntRequest, db: Session = Depends(get_db)):

    response_question = db.query(models.Question).order_by(models.Question.id.desc()).first()

    callback_url = f"https://jservice.io/api/random?count={num.questions_num}"
    response = requests.get(callback_url).json()
    for q in response:
        q = is_same(q, db)
        new_question = models.Question(
            question_id=q['id'],
            question=q['question'],
            answer=q['answer'],
            created_at=q['created_at']
        )
        db.add(new_question)
        db.commit()
        db.refresh(new_question)

    return {} if response_question is None else response_question


@app.get('/all')
def show_all(db: Session = Depends(get_db)):
    all_questions = db.query(models.Question).all()
    return all_questions
