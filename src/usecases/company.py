from sqlalchemy.orm import Session
from typing import List

from ..errors.company import CompanyNotFound
from ..repositories.company import CompanyRepository
from ..schemas.company import Company


class CompanyUseCase:
    @staticmethod
    def list_all(db: Session) -> List[Company]:
        return CompanyRepository.find_all(db)


    @staticmethod
    def find_one(db: Session, company_id: int) -> Company:
        company = CompanyRepository.find_by_id(db, company_id)

        if not company:
            raise CompanyNotFound

        return company