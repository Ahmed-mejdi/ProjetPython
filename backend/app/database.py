from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

if __name__ == "__main__":
    # Test de connexion à la base
    try:
        with engine.connect() as conn:
            print("Connexion à la base de données réussie !")
    except Exception as e:
        print(f"Erreur de connexion à la base de données : {e}")
