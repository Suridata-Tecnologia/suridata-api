from sqlalchemy.orm import Session
from typing import List

from ..repositories.credential import CredentialRepository
from ..schemas.credential import Credential


class CredentialUseCase:
    @staticmethod
    def list_all(db: Session) -> List[Credential]:
        return CredentialRepository.find_all(db)
