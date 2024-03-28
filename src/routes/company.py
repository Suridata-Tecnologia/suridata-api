from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..configs.database import get_db
from ..usecases.company import CompanyUseCase
from ..schemas.company import Company
from ..errors.company import CompanyNotFound


router = APIRouter(prefix='/companies')

@router.get('/', response_model=List[Company])
def list(db: Session = Depends(get_db)) -> List[Company]:
    return CompanyUseCase.list_all(db)


@router.get('/{company_id}', response_model=Company)
def find_one(company_id: int, db: Session = Depends(get_db)) -> Company:
    try:
        return CompanyUseCase.find_one(db, company_id)
    except CompanyNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")