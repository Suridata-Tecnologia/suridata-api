import bcrypt
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Union, Annotated
from jose import JWTError, jwt
from src.schemas.token import Token
from os import environ

SECRET_KEY = 'Sur1d4t4@'
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signin")


class Auth:
    @staticmethod
    def create_token(data: dict, expires_delta: Union[timedelta, None] = None):
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=30)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return Token(token=encoded_jwt, token_type="bearer", expiration=expire.isoformat())


    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        password_as_bytes = plain_password.encode('utf-8')
        hashed_password_as_bytes = hashed_password.encode('utf-8')

        return bcrypt.checkpw(password=password_as_bytes, hashed_password=hashed_password_as_bytes)


    @staticmethod
    def get_password_hash(password: str) -> str:
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)

        return hashed_password.decode('utf-8')


    @staticmethod
    def is_authenticated(token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("user_id")

            if user_id is None:
                raise credentials_exception

        except JWTError:
            raise credentials_exception

        return user_id