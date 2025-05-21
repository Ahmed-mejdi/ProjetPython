from fastapi import FastAPI
from app.routers.departement_router import router as departement_router
from app.routers.formation_router import router as formation_router
from app.routers.etudiant_router import router as etudiant_router
from app.routers.auth_router import router as auth_router

app = FastAPI()

app.include_router(departement_router)
app.include_router(formation_router)
app.include_router(etudiant_router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur la plateforme de gestion de formations !"}
