from fastapi_users import schemas
from typing import Optional

class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    nom: str
    departement_id: Optional[int] = None

class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    nom: str
    departement_id: Optional[int] = None

class UserUpdate(schemas.BaseUserUpdate):
    nom: Optional[str] = None
    departement_id: Optional[int] = None
