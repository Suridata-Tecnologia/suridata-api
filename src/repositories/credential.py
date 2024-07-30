from sqlalchemy.orm import Session

from src.models.credential import Credential


class CredentialRepository:
    @staticmethod
    def find_all(db: Session) -> list[Credential]:
        return db.query(Credential).all()