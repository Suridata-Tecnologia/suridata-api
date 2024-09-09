from sqlalchemy.orm import Session
from typing import List

from ..errors.company import CompanyNotFound
from ..errors.credential import DuplicatedCredential
from ..repositories.company import CompanyRepository
from ..schemas.company import Company

from ..repositories.credential import CredentialRepository
from ..schemas.credential import CredentialOut, CredentialIn


class CredentialUseCase:
    @staticmethod
    def list_all(db: Session) -> List[CredentialOut]:
        return CredentialRepository.find_all(db)
    

    @staticmethod
    def create(db: Session, credential: CredentialIn, user_id: int) -> CredentialOut:
        company = CompanyRepository.find_by_id(db, company_id=credential.company_id)

        if not company:
            raise CompanyNotFound
        
        credential_in_db = CredentialRepository.exists(
            db, 
            credential.company_id, 
            credential.username, 
            credential.password, 
            credential.complement
        )

        if credential_in_db:
            raise DuplicatedCredential
        
        new_credential = {**credential.model_dump(), "user_id":user_id}
        new_credential = CredentialRepository.create_or_update(db, new_credential)

        return new_credential
    

    @staticmethod
    def delete(db: Session, user_id: int, id: int) -> None:
        credential = CredentialRepository.delete(db, id)

        
