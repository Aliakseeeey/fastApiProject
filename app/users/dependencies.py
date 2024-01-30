from fastapi import Request, HTTPException, Depends, status
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime
from app.users.dao import UserDao
from app.config import settings


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
        print(payload)
    except InvalidTokenError:
        print(111)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        print(222)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id = payload.get("sub")
    if not user_id:
        print(333)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await UserDao.find_by_id(int(user_id))
    if not user:
        print(444)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user
