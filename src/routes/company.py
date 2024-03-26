from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..configs.database import get_db
from ..usecases.company import CompanyUseCase
from ..schemas.company import Company

router = APIRouter(prefix='/companies')

@router.get('/', response_model=List[Company])
def list(db: Session = Depends(get_db)) -> List[Company]:
    return CompanyUseCase.list_companies(db)