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
    def create_credential(db: Session, credential: CredentialIn) -> CredentialOut:
        company = CompanyRepository.find_by_id(db, company_id=credential.company_id)

        if not company:
            raise CompanyNotFound
        
        is_duplicate_credential = CredentialRepository.is_duplicated(
            db, 
            credential.company_id, 
            credential.username, 
            credential.password, 
            credential.complement
        )

        if is_duplicate_credential:
            raise DuplicatedCredential
        
        teste = CredentialRepository.create_or_update(db, credential.model_dump())

        
        return teste
