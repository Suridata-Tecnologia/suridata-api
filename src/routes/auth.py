from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from src.schemas.token import Token
from src.configs.database import get_db
from src.utils.auth import Auth
from ..usecases.auth import AuthUseCase

router = APIRouter(prefix='/auth')

@router.post('/signin', response_model=Token)
def signin(
    response: Response, 
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], 
    db: Session = Depends(get_db)
) -> Token:
    try:
        token = AuthUseCase.signin(db, form_data)

        response.headers["Authorization"] = f"Bearer {token.token}"
        
        return token
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username or password."
        )


@router.post('/validate')
def validate_token(response: Response, token = Depends(Auth.is_authenticated)) -> None:
    response.headers["Authorization"] = f"Bearer {token}"

    return Response(status_code=status.HTTP_200_OK)