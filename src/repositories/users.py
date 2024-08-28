from sqlalchemy.orm import Session

from src.models.users import Users

class UsersRepository:
    @staticmethod
    def find_all(db: Session) -> list[Users]:
        return db.query(Users).all()
