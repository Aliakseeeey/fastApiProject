from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException
from pydantic import EmailStr
from app.users.dao import UserDao
from jose import jwt
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plan_password, hashed_password) -> bool:
    return pwd_context.verify(plan_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encode_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UserDao.find_one_or_none(email=email)
    if not user and not verify_password(password, user.password):
        return None
    return user
