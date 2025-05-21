from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Formation
from app.schemas.schemas import FormationCreate, FormationRead
from typing import List

router = APIRouter(prefix="/formations", tags=["formations"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=FormationRead)
def create_formation(formation: FormationCreate, db: Session = Depends(get_db)):
    db_formation = Formation(**formation.dict())
    db.add(db_formation)
    db.commit()
    db.refresh(db_formation)
    return db_formation

@router.get("/", response_model=List[FormationRead])
def list_formations(db: Session = Depends(get_db)):
    return db.query(Formation).all()

@router.get("/{formation_id}", response_model=FormationRead)
def get_formation(formation_id: int, db: Session = Depends(get_db)):
    formation = db.query(Formation).filter(Formation.id == formation_id).first()
    if not formation:
        raise HTTPException(status_code=404, detail="Formation non trouvée")
    return formation

@router.put("/{formation_id}", response_model=FormationRead)
def update_formation(formation_id: int, formation: FormationCreate, db: Session = Depends(get_db)):
    db_formation = db.query(Formation).filter(Formation.id == formation_id).first()
    if not db_formation:
        raise HTTPException(status_code=404, detail="Formation non trouvée")
    for key, value in formation.dict().items():
        setattr(db_formation, key, value)
    db.commit()
    db.refresh(db_formation)
    return db_formation

@router.delete("/{formation_id}")
def delete_formation(formation_id: int, db: Session = Depends(get_db)):
    db_formation = db.query(Formation).filter(Formation.id == formation_id).first()
    if not db_formation:
        raise HTTPException(status_code=404, detail="Formation non trouvée")
    db.delete(db_formation)
    db.commit()
    return {"ok": True}
