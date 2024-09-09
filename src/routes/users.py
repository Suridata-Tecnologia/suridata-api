from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..configs.database import get_db
from ..usecases.users import UsersUseCase
from ..schemas.users import Users


router = APIRouter(prefix='/users')

@router.get('/', response_model=List[Users])
def list_all(db: Session = Depends(get_db)) -> List[Users]:
    return UsersUseCase.list_all(db)

