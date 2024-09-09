from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List, Union

from ..configs.database import get_db
from ..usecases.credential import CredentialUseCase
from ..schemas.credential import CredentialOut, CredentialIn
from ..utils.auth import Auth 


router = APIRouter(prefix='/credentials', dependencies=[Depends(Auth.is_authenticated)])

@router.get('/', response_model=List[CredentialOut])
async def list(
    db: Session = Depends(get_db),
    
) -> List[CredentialOut]:
    return CredentialUseCase.list_all(db)


@router.get('/items')
async def read_item(q: Union[str, None] = None):
    return {'q': q}


@router.post('/', response_model=CredentialOut, status_code=status.HTTP_201_CREATED)
async def create_credential(
    credential: CredentialIn, 
    db: Session = Depends(get_db),
    user_id = Depends(Auth.is_authenticated)
):
    new_credential = CredentialUseCase.create(db, credential, user_id)
   
    return new_credential


@router.delete('/{credential_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_credential(
    credential_id: int, 
    db: Session = Depends(get_db),
    user_id = Depends(Auth.is_authenticated)
):
    delete = CredentialUseCase.delete(db, credential_id, user_id)
   
    return 
    
    
