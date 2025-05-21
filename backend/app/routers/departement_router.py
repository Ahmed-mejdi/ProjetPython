from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Departement
from app.schemas.schemas import DepartementCreate, DepartementRead
from typing import List

router = APIRouter(prefix="/departements", tags=["departements"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DepartementRead)
def create_departement(departement: DepartementCreate, db: Session = Depends(get_db)):
    db_dept = Departement(**departement.dict())
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

@router.get("/", response_model=List[DepartementRead])
def list_departements(db: Session = Depends(get_db)):
    return db.query(Departement).all()

@router.get("/{departement_id}", response_model=DepartementRead)
def get_departement(departement_id: int, db: Session = Depends(get_db)):
    dept = db.query(Departement).filter(Departement.id == departement_id).first()
    if not dept:
        raise HTTPException(status_code=404, detail="Département non trouvé")
    return dept

@router.put("/{departement_id}", response_model=DepartementRead)
def update_departement(departement_id: int, departement: DepartementCreate, db: Session = Depends(get_db)):
    db_dept = db.query(Departement).filter(Departement.id == departement_id).first()
    if not db_dept:
        raise HTTPException(status_code=404, detail="Département non trouvé")
    for key, value in departement.dict().items():
        setattr(db_dept, key, value)
    db.commit()
    db.refresh(db_dept)
    return db_dept

@router.delete("/{departement_id}")
def delete_departement(departement_id: int, db: Session = Depends(get_db)):
    db_dept = db.query(Departement).filter(Departement.id == departement_id).first()
    if not db_dept:
        raise HTTPException(status_code=404, detail="Département non trouvé")
    db.delete(db_dept)
    db.commit()
    return {"ok": True}
