from datetime import timedelta
from sqlalchemy.orm import Session

from ..errors.auth import UserNotFound, WrongPassword
from ..utils.auth import Auth
from ..repositories.users import UsersRepository
from ..schemas.token import Token


class AuthUseCase:
   @staticmethod
   def signin(db: Session, user_data: dict) -> Token:
        user = UsersRepository.find_by_email(db, user_data.username)
    
        if not user:
            raise UserNotFound

        pass_is_correct = Auth.verify_password(user_data.password, user.password)

        if not pass_is_correct:
            raise WrongPassword

        token = Auth.create_token(data={'user_id': user.id}, expires_delta=timedelta(days=365))

        return token