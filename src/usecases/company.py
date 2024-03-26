from sqlalchemy.orm import Session
from typing import List

from ..repositories.company import CompanyRepository
from ..schemas.company import Company


class CompanyUseCase:
    @staticmethod
    def list_companies(db: Session) -> List[Company]:
        return CompanyRepository.find_all(db)