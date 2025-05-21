from pydantic import BaseModel, EmailStr
from typing import List, Optional

class DepartementBase(BaseModel):
    nom: str
    description: Optional[str] = None

class DepartementCreate(DepartementBase):
    pass

class DepartementRead(DepartementBase):
    id: int
    class Config:
        orm_mode = True

class FormationBase(BaseModel):
    titre: str
    description: Optional[str] = None
    theme: Optional[str] = None
    duree: Optional[int] = None

class FormationCreate(FormationBase):
    pass

class FormationRead(FormationBase):
    id: int
    class Config:
        orm_mode = True

class EtudiantBase(BaseModel):
    nom: str
    email: EmailStr
    departement_id: Optional[int] = None

class EtudiantCreate(EtudiantBase):
    mot_de_passe: str

class EtudiantRead(EtudiantBase):
    id: int
    departement: Optional[DepartementRead]
    formations: List[FormationRead] = []
    class Config:
        orm_mode = True
