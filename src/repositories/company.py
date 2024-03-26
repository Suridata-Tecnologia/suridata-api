from sqlalchemy.orm import Session

from src.models.company import Company


class CompanyRepository:
    @staticmethod
    def find_all(db: Session) -> list[Company]:
        return db.query(Company).all()