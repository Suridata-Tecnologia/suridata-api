from sqlalchemy.orm import Session

from src.models.credential import Credential
from src.schemas.credential import CredentialIn, CredentialOut


class CredentialRepository:
    @staticmethod
    def find_all(db: Session) -> list[Credential]:
        return db.query(Credential).all()
    

    @staticmethod
    def exists(
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
        credential = Credential(**credential)

        if credential.id:
            db.merge(credential)
        else:
            db.add(credential)
        
        db.commit()
        return credential
    

    @staticmethod
    def delete(db: Session, id: int) -> None:
        credential = db.query(Credential).filter(Credential.id == id)
        import ipdb; ipdb.set_trace()
        # if credential.id:
        #     db.merge(credential)
        # else:
        #     db.add(credential)
        
        # db.commit()
        return credential
