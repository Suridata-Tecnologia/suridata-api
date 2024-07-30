from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List

from ..configs.database import get_db
from ..usecases.credential import CredentialUseCase
from ..schemas.credential import Credential


router = APIRouter(prefix='/credentials')

@router.get('/', response_model=List[Credential])
def list(db: Session = Depends(get_db)) -> List[Credential]:
    return CredentialUseCase.list_all(db)
