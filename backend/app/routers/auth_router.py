# Authentification FastAPI Users (squelette)
from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, CookieTransport
from fastapi_users.db import SQLAlchemyUserDatabase
from app.models.models import User
from app.schemas.user_schemas import UserRead, UserCreate, UserUpdate
from app.database import SessionLocal
from sqlalchemy.orm import sessionmaker
import uuid
from fastapi import Depends, Request
from fastapi_users.manager import BaseUserManager, UserAlreadyExists
from fastapi_users.password import get_password_hash
import os

SECRET = os.getenv("SECRET_KEY", "SECRET")

class UserManager(BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Request | None = None):
        print(f"User {user.id} has registered.")

async def get_user_db():
    db = SessionLocal()
    try:
        yield SQLAlchemyUserDatabase(db, User)
    finally:
        db.close()

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

cookie_transport = CookieTransport(cookie_name="auth", cookie_max_age=3600)
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_db,
    [auth_backend],
    UserRead,
    UserCreate,
    UserUpdate,
    UserManager,
)

router = APIRouter(prefix="/auth", tags=["auth"])

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/register",
    tags=["auth"]
)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"]
)
