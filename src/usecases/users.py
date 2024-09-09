from sqlalchemy.orm import Session
from typing import List

from ..repositories.users import UsersRepository
from ..schemas.users import Users


class UsersUseCase:
    @staticmethod
    def list_all(db: Session) -> List[Users]:
        return UsersRepository.find_all(db)
