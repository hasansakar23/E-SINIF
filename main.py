from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
evaluations = relationship("Evaluation", back_populates="assignment")


@app.post("/teacher", response_model=schemas.TeacherOut)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud.create_teacher(db, teacher)

@app.post("/class", response_model=schemas.ClassOut)
def create_class(cls: schemas.ClassCreate, db: Session = Depends(get_db)):
    return crud.create_class(db, cls)

@app.post("/student", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.post("/assignment", response_model=schemas.AssignmentOut)
def upload_assignment(assignment: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    return crud.upload_assignment(db, assignment)

@app.post("/evaluation", response_model=schemas.EvaluationOut)
def evaluate_assignment(evaluation: schemas.EvaluationCreate, db: Session = Depends(get_db)):
    return crud.evaluate_assignment(db, evaluation)

@app.get("/teacher/{teacher_id}/assignments", response_model=list[schemas.AssignmentOut])
def get_teacher_assignments(teacher_id: str, db: Session = Depends(get_db)):
    return crud.get_assignments_by_teacher(db, teacher_id)

@app.get("/report/class/{class_id}", response_model=list[schemas.EvaluationOut])
def get_evaluation_report(class_id: str, db: Session = Depends(get_db)):
    return crud.get_evaluations_by_class(db, class_id)
from fastapi import File, UploadFile
from auto_evaluate import extract_text_from_pdf, evaluate_homework_with_gemini

@app.post("/auto-evaluate")
def auto_evaluate(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)
    result = evaluate_homework_with_gemini(text)
    return result

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")  # 👈 burada açıkça dosya adı belirtildi

print("API KEY:", os.getenv("GEMINI_API_KEY"))


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    assignment_id = Column(Integer, ForeignKey("assignments.id"))
    coherence = Column(Integer)
    sources = Column(Integer)
    reasoning = Column(Integer)
    language = Column(Integer)
    feedback = Column(String)
    total_score = Column(Float)

    assignment = relationship("Assignment", back_populates="evaluations")
