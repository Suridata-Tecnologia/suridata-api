from sqlalchemy.orm import Session

from src.models.credential import Credential
from src.schemas.credential import CredentialIn, CredentialOut


class CredentialRepository:
    @staticmethod
    def find_all(db: Session) -> list[Credential]:
        return db.query(Credential).all()
    
    @staticmethod
    def is_duplicated(
        db: Session, 
        company_id: int, 
        username: str, 
        password: str, 
        complement: str
    ) -> bool:
        credential = db.query(Credential).filter(
            Credential.company_id == company_id, 
            Credential.username == username, 
            Credential.password == password, 
            Credential.complement == complement
        ).first()

        return credential is not None
    
    @staticmethod
    def create_or_update(db: Session, credential: dict) -> CredentialOut:
        credential_unit = Credential(**credential)
        import ipdb; ipdb.set_trace()
        db.add(credential_unit)
        
        db.commit()
    