from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Etudiant, Formation
from app.schemas.schemas import EtudiantCreate, EtudiantRead
from typing import List

router = APIRouter(prefix="/etudiants", tags=["etudiants"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=EtudiantRead)
def create_etudiant(etudiant: EtudiantCreate, db: Session = Depends(get_db)):
    db_etudiant = Etudiant(
        nom=etudiant.nom,
        email=etudiant.email,
        mot_de_passe=etudiant.mot_de_passe,  # À hasher en prod !
        departement_id=etudiant.departement_id
    )
    db.add(db_etudiant)
    db.commit()
    db.refresh(db_etudiant)
    return db_etudiant

@router.get("/", response_model=List[EtudiantRead])
def list_etudiants(db: Session = Depends(get_db)):
    return db.query(Etudiant).all()

@router.get("/{etudiant_id}", response_model=EtudiantRead)
def get_etudiant(etudiant_id: int, db: Session = Depends(get_db)):
    etu = db.query(Etudiant).filter(Etudiant.id == etudiant_id).first()
    if not etu:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé")
    return etu

@router.put("/{etudiant_id}", response_model=EtudiantRead)
def update_etudiant(etudiant_id: int, etudiant: EtudiantCreate, db: Session = Depends(get_db)):
    db_etu = db.query(Etudiant).filter(Etudiant.id == etudiant_id).first()
    if not db_etu:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé")
    for key, value in etudiant.dict().items():
        setattr(db_etu, key, value)
    db.commit()
    db.refresh(db_etu)
    return db_etu

@router.delete("/{etudiant_id}")
def delete_etudiant(etudiant_id: int, db: Session = Depends(get_db)):
    db_etu = db.query(Etudiant).filter(Etudiant.id == etudiant_id).first()
    if not db_etu:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé")
    db.delete(db_etu)
    db.commit()
    return {"ok": True}

@router.post("/{etudiant_id}/inscription/{formation_id}")
def inscrire_etudiant_formation(etudiant_id: int, formation_id: int, db: Session = Depends(get_db)):
    etu = db.query(Etudiant).filter(Etudiant.id == etudiant_id).first()
    formation = db.query(Formation).filter(Formation.id == formation_id).first()
    if not etu or not formation:
        raise HTTPException(status_code=404, detail="Étudiant ou formation non trouvé")
    etu.formations.append(formation)
    db.commit()
    return {"ok": True}
