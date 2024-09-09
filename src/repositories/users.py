from sqlalchemy.orm import Session

from src.models.users import Users

class UsersRepository:
    @staticmethod
    def find_all(db: Session) -> list[Users]:
        return db.query(Users).all()
    

    @staticmethod
    def find_by_email(db: Session, email: str) -> Users:
        return db.query(Users).filter(Users.email == email).first()
    

    @staticmethod
    def create_or_update(db: Session, user: dict) -> Users:
        user = Users(**user)

        if user.id:
            db.merge(user)
        else:
            db.add(user)

        db.commit()

        return user


    @staticmethod
    def find_by_id(db: Session, id: int) -> Users:
        return db.query(Users).filter(Users.id == id).first()


    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Users).filter(Users.id == id).first() is not None


    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        user = db.query(Users).filter(Users.id == id).first()

        if user is not None:
            db.delete(user)
            db.commit()
