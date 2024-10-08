from sqlalchemy.orm import Session

from src.models.company import Company


class CompanyRepository:
    @staticmethod
    def find_all(db: Session) -> list[Company]:
        return db.query(Company).all()


    @staticmethod
    def find_by_id(db: Session, company_id: int) -> list[Company]:
        return db.query(Company).filter(company_id == Company.id).first()