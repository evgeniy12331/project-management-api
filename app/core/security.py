import bcrypt
from datetime import datetime, timedelta, timezone
from jose import jwt,JWTError
from app.core.config import settings

def hash_password(password: str):
    password_bytes = password.encode('utf-8')
    sait = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes,sait)
    return hashed.decode('utf-8')

def verify_password(
        plain_password: str,
        hashed_password: str
):
    password_bytes = plain_password.encode('utf-8')
    hashed_bytes =  hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes,hashed_bytes)

def create_access_token(
        user_id: int,
        role: str
):
    payload = {
        'sub': str(user_id),
        'role': role,
        'type': 'access',
        'exp': datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    }
    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm = settings.ALGORITHM
    )
    return token

def create_refresh_token(user_id: int):
    payload = {
        'sub': str(user_id),
        'type': 'refresh',
        'exp': datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    }
    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return token

def decode_token(token: str):
    payload = jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms= [settings.ALGORITHM]
    )
    return payload

def verify_token(payload: dict, expected_type: str):
    if payload.get('type') != expected_type:
        raise JWTError('invalid token')
    return True